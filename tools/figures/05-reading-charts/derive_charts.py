"""Derive chart data files that make_charts.py cannot draw directly (part 5).

  stock-a-weekly.json  the weekly bars of stock-a-daily.json (same made-up stock)
  rs-ratio.json        rs-stock closes divided by rs-index closes, scaled to 100 at the start

Run after tools/make_charts.py 05-reading-charts, from the repo root:
    .venv/Scripts/python tools/figures/05-reading-charts/derive_charts.py
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CH = ROOT / "docs" / "assets" / "charts" / "05-reading-charts"


def load(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def save(name, tf, bars):
    (CH / f"{name}.json").write_text(json.dumps({"tf": tf, "synthetic": True, "bars": bars}, separators=(",", ":")) + "\n", encoding="utf-8", newline="\n")
    print(name, len(bars), "bars", bars[0][0], "to", bars[-1][0])


def weekly(bars):
    out, cur, key = [], None, None
    for t, o, h, lo, c, v in bars:
        d = date.fromisoformat(t)
        k = d.isocalendar()[:2]
        if k != key:
            if cur:
                out.append(cur)
            monday = date.fromordinal(d.toordinal() - d.weekday()).isoformat()
            cur, key = [monday, o, h, lo, c, v], k
        else:
            cur[2] = max(cur[2], h)
            cur[3] = min(cur[3], lo)
            cur[4] = c
            cur[5] += v
    out.append(cur)
    return out


def ratio(stock, index):
    base = stock[0][4] / index[0][4]
    out, prev = [], 100.0
    for s, i in zip(stock, index):
        r = round(s[4] / i[4] / base * 100, 2)
        out.append([s[0], prev, max(prev, r), min(prev, r), r, 0])
        prev = r
    return out


if __name__ == "__main__":
    save("stock-a-weekly", "W", weekly(load("stock-a-daily")))
    save("rs-ratio", "D", ratio(load("rs-stock"), load("rs-index")))
