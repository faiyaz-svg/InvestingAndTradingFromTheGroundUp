"""Make the book's synthetic price data for ```chart fences and chart drills.

Real stock and index prices are licensed, so every price chart in the book is
drawn from made-up data. Each chart is described in tools/charts_src/<folder>.yml
as a list of segments (a trend, a range, a gap, a hand-shaped bar ...), and this
script turns the description into bars with a fixed random seed, so the output
never changes unless the description does.

    - name: uptrend-pullback
      seed: 11
      tf: D                  # D (daily), W (weekly), 1m, 5m, 15m or 60m
      start: 2026-01-05      # intraday: "2026-03-02 09:30" (New York time)
      price: 100             # first open
      volume: 2000000        # typical volume per bar
      decimals: 2            # optional: price decimals (4 for a currency pair such as USD/CAD)
      segments:
        - {kind: trend, bars: 40, drift: 0.004, vol: 0.012}
        - {kind: to, bars: 8, price: 104, vol: 0.01, volume: 0.7}
        - {kind: range, bars: 20, low: 101, high: 106, vol: 0.01}
        - {kind: gap, pct: 0.03}
        - {kind: bar, open: 0.0, high: 0.031, low: -0.004, close: 0.028, volume: 2.5}
        - {kind: trend, bars: 20, drift: 0.003, vol: 0.012, volume: 1.5}

Segment kinds:
  trend  bars, drift (mean return per bar), vol (stdev of return per bar)
  to     bars, price: move to this close by the last bar (a bridge), with vol noise
  range  bars, low, high: closes stay inside the band, bouncing off the edges
  gap    pct: the next bar opens this far from the last close (no bar of its own)
  bar    one bar shaped by hand: open, high, low, close as returns from the last close
A chart can also set csv: <name> to write docs/assets/data/<name>.csv
(date,open,high,low,close,volume) for the In code snippets.
Any segment can set volume (a multiplier of the typical volume) and wick (the
typical wick size as a fraction of price; default half of vol).

Writes docs/assets/charts/<folder>/<name>.json as
  {"tf": ..., "synthetic": true, "bars": [[time, open, high, low, close, volume], ...]}
Daily and weekly times are "YYYY-MM-DD". Intraday times are Unix seconds that
encode the New York wall clock as UTC (charts.js shows them as ET).

It prints a summary of every segment (bar numbers, dates, closes, lowest low and
highest high), which is what lessons and drills quote. With --preview it also
saves a PNG of each chart to tools/charts_src/_preview/ for checking by eye.

Run from the repo root:
    .venv/Scripts/python tools/make_charts.py                       every file
    .venv/Scripts/python tools/make_charts.py 05-reading-charts     one folder
    .venv/Scripts/python tools/make_charts.py 05-reading-charts --preview
"""

from __future__ import annotations

import json
import math
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "charts_src"
OUT = ROOT / "docs" / "assets" / "charts"
DATA = ROOT / "docs" / "assets" / "data"
PREVIEW = SRC / "_preview"

INTRADAY_MINUTES = {"1m": 1, "5m": 5, "15m": 15, "60m": 60}
SESSION_OPEN = (9, 30)
SESSION_CLOSE = (16, 0)


def trading_days(start: date):
    d = start
    while True:
        if d.weekday() < 5:
            yield d
        d += timedelta(days=1)


def weeks(start: date):
    d = start - timedelta(days=start.weekday())
    while True:
        yield d
        d += timedelta(days=7)


def intraday_times(start: str, minutes: int):
    """Bar start times, session by session, as naive datetimes (New York clock)."""
    t = datetime.strptime(start, "%Y-%m-%d %H:%M")
    while True:
        open_t = t.replace(hour=SESSION_OPEN[0], minute=SESSION_OPEN[1])
        close_t = t.replace(hour=SESSION_CLOSE[0], minute=SESSION_CLOSE[1])
        if t.weekday() < 5 and open_t <= t < close_t:
            yield t
            t += timedelta(minutes=minutes)
        else:
            day = t.date() + timedelta(days=1) if t >= close_t else t.date()
            while day.weekday() >= 5:
                day += timedelta(days=1)
            t = datetime(day.year, day.month, day.day, *SESSION_OPEN)


def volume_shape(t: datetime, minutes: int) -> float:
    """Intraday volume is high at the open and the close and low at midday (a U shape)."""
    m = (t.hour * 60 + t.minute) - (SESSION_OPEN[0] * 60 + SESSION_OPEN[1])
    span = 390
    x = (m + minutes / 2) / span
    return 0.55 + 2.2 * (x - 0.5) ** 2 * 4 / 2


def make_closes(seg: dict, last: float, rng: np.random.Generator) -> list[float]:
    kind = seg["kind"]
    n = int(seg.get("bars", 1))
    vol = float(seg.get("vol", 0.01))
    if kind == "trend":
        rets = rng.normal(float(seg.get("drift", 0.0)), vol, n)
        out, p = [], last
        for r in rets:
            p *= math.exp(r)
            out.append(p)
        return out
    if kind == "to":
        target = float(seg["price"])
        # A Brownian bridge in log price from last to target.
        steps = rng.normal(0, vol, n)
        walk = np.cumsum(steps)
        line = np.linspace(0, 1, n + 1)[1:]
        bridge = walk - line * walk[-1]
        logs = math.log(last) + line * (math.log(target) - math.log(last)) + bridge
        return [math.exp(x) for x in logs]
    if kind == "range":
        lo, hi = float(seg["low"]), float(seg["high"])
        mid = (lo + hi) / 2
        out, p = [], min(max(last, lo), hi)
        for _ in range(n):
            p = p + 0.15 * (mid - p) + rng.normal(0, vol) * p
            # Bounce off the edges instead of leaving the band.
            if p > hi:
                p = hi - (p - hi) - abs(rng.normal(0, vol)) * p * 0.5
            if p < lo:
                p = lo + (lo - p) + abs(rng.normal(0, vol)) * p * 0.5
            p = min(max(p, lo), hi)
            out.append(p)
        return out
    raise SystemExit(f"unknown segment kind {kind!r}")


def build(chart: dict) -> tuple[dict, list[dict]]:
    rng = np.random.default_rng(int(chart["seed"]))
    tf = str(chart.get("tf", "D"))
    dec = int(chart.get("decimals", 2))
    base_vol = float(chart.get("volume", 1_000_000))
    price = float(chart["price"])
    if tf == "D":
        clock = trading_days(date.fromisoformat(str(chart["start"])))
    elif tf == "W":
        clock = weeks(date.fromisoformat(str(chart["start"])))
    elif tf in INTRADAY_MINUTES:
        clock = intraday_times(str(chart["start"]), INTRADAY_MINUTES[tf])
    else:
        raise SystemExit(f"{chart['name']}: unknown tf {tf!r}")

    bars: list[list] = []
    summary: list[dict] = []
    last_close = price
    next_open: float | None = price

    for seg in chart["segments"]:
        kind = seg["kind"]
        if kind == "gap":
            next_open = last_close * (1 + float(seg["pct"]))
            summary.append({"kind": "gap", "from": round(last_close, 2), "to": round(next_open, 2)})
            continue
        vmult = float(seg.get("volume", 1.0))
        first = len(bars)
        if kind == "bar":
            o = last_close * (1 + float(seg.get("open", 0.0))) if next_open is None else next_open
            ref = last_close
            c = ref * (1 + float(seg["close"]))
            h = max(ref * (1 + float(seg["high"])), o, c)
            lo = min(ref * (1 + float(seg["low"])), o, c)
            t = next(clock)
            v = base_vol * vmult * (volume_shape(t, INTRADAY_MINUTES[tf]) if tf in INTRADAY_MINUTES else 1)
            bars.append([t, o, h, lo, c, v])
            last_close, next_open = c, None
        else:
            vol = float(seg.get("vol", 0.01))
            wick = float(seg.get("wick", vol / 2))
            for c in make_closes(seg, last_close, rng):
                o = next_open if next_open is not None else last_close * (1 + rng.normal(0, vol / 4))
                h = max(o, c) * (1 + abs(rng.normal(0, wick)))
                lo = min(o, c) * (1 - abs(rng.normal(0, wick)))
                t = next(clock)
                shape = volume_shape(t, INTRADAY_MINUTES[tf]) if tf in INTRADAY_MINUTES else 1
                v = base_vol * vmult * shape * math.exp(rng.normal(0, 0.25))
                bars.append([t, o, h, lo, c, v])
                last_close, next_open = c, None
        seg_bars = bars[first:]
        summary.append(
            {
                "kind": kind,
                "bars": f"{first + 1}-{len(bars)}",
                "times": f"{fmt_time(seg_bars[0][0], tf)} to {fmt_time(seg_bars[-1][0], tf)}",
                "close": f"{seg_bars[0][4]:.{dec}f} -> {seg_bars[-1][4]:.{dec}f}",
                "low": round(min(b[3] for b in seg_bars), dec),
                "high": round(max(b[2] for b in seg_bars), dec),
            }
        )

    rows = []
    for t, o, h, lo, c, v in bars:
        o, h, lo, c = (round(x, dec) for x in (o, h, lo, c))
        h = max(h, o, c)
        lo = min(lo, o, c)
        rows.append([out_time(t, tf), o, h, lo, c, int(round(v, -2))])
    out = {"tf": tf, "synthetic": True, "bars": rows}
    if dec != 2:
        out["decimals"] = dec
    return out, summary


def out_time(t, tf: str):
    if tf in INTRADAY_MINUTES:
        return int(datetime(t.year, t.month, t.day, t.hour, t.minute, tzinfo=timezone.utc).timestamp())
    return t.isoformat()


def fmt_time(t, tf: str) -> str:
    return t.strftime("%Y-%m-%d %H:%M") if tf in INTRADAY_MINUTES else t.isoformat()


def write_csv(name: str, data: dict) -> None:
    """The bars as a CSV for the In code snippets: date (or datetime, New York time), OHLCV."""
    DATA.mkdir(parents=True, exist_ok=True)
    head = "datetime" if data["tf"] in INTRADAY_MINUTES else "date"
    dec = int(data.get("decimals", 2))
    lines = [f"{head},open,high,low,close,volume"]
    for t, o, h, lo, c, v in data["bars"]:
        if data["tf"] in INTRADAY_MINUTES:
            t = datetime.fromtimestamp(t, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
        lines.append(f"{t},{o:.{dec}f},{h:.{dec}f},{lo:.{dec}f},{c:.{dec}f},{v}")
    out = DATA / f"{name}.csv"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("   csv", out.relative_to(ROOT).as_posix())


def preview(name: str, data: dict, folder: str) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import mplfinance as mpf
    import pandas as pd

    rows = data["bars"]
    if data["tf"] in INTRADAY_MINUTES:
        idx = pd.to_datetime([r[0] for r in rows], unit="s")
    else:
        idx = pd.to_datetime([r[0] for r in rows])
    df = pd.DataFrame([r[1:] for r in rows], index=idx, columns=["Open", "High", "Low", "Close", "Volume"])
    PREVIEW.mkdir(parents=True, exist_ok=True)
    out = PREVIEW / f"{folder}--{name}.png"
    mpf.plot(df, type="candle", volume=True, style="nightclouds", savefig=dict(fname=out, dpi=80))
    print("   preview", out.relative_to(ROOT).as_posix())


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    want_preview = "--preview" in sys.argv
    files = [SRC / f"{a}.yml" for a in args] if args else sorted(SRC.glob("*.yml"))
    for path in files:
        folder = path.stem
        charts = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        names = [c["name"] for c in charts]
        if len(names) != len(set(names)):
            raise SystemExit(f"{path.name}: duplicate chart names")
        for chart in charts:
            data, summary = build(chart)
            out = OUT / folder / f"{chart['name']}.json"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(data, separators=(",", ":")) + "\n", encoding="utf-8", newline="\n")
            rows = data["bars"]
            print(f"{folder}/{chart['name']}.json: {len(rows)} bars, {rows[0][0]} to {rows[-1][0]}")
            for i, s in enumerate(summary, 1):
                print("  ", i, " ".join(f"{k}={v}" for k, v in s.items()))
            if chart.get("csv"):
                write_csv(chart["csv"], data)
            if want_preview:
                preview(chart["name"], data, folder)


if __name__ == "__main__":
    main()
