"""Made-up forecast log (60 forecasts) written to docs/assets/data/forecast-log.csv.

Every row is invented for teaching. The forecaster is a little overconfident:
the true chance of "yes" is pulled 30% toward 50% from the stated forecast.
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs" / "assets" / "data" / "forecast-log.csv"

KINDS = [
    "Stock {s} closes the week above its Monday open",
    "Stock {s} reports revenue above the consensus figure",
    "Stock {s} gaps up at the open after earnings",
    "Stock {s} ends the month above its 50-day average",
]
FORECASTS = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]


def make():
    rng = random.Random(1901)
    rows = []
    d = date(2026, 1, 5)
    for i in range(60):
        f = rng.choice(FORECASTS)
        true_p = 0.5 + 0.7 * (f - 0.5)
        y = 1 if rng.random() < true_p else 0
        s = "AB"[i % 2]
        q = KINDS[i % 4].format(s=s)
        rows.append([d.isoformat(), q, f"{f:.1f}", y])
        d += timedelta(days=4 + (i % 3))
    return rows


def write():
    rows = make()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["date", "question", "forecast", "outcome"])
        w.writerows(rows)
    return rows


if __name__ == "__main__":
    rows = write()
    n = len(rows)
    brier = sum((float(r[2]) - r[3]) ** 2 for r in rows) / n
    base = sum(r[3] for r in rows) / n
    print("n", n, "yes rate", base, "brier", round(brier, 4), "always .5", 0.25,
          "base-rate forecast brier", round(base * (1 - base), 4))
    buckets = [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 1.01)]
    for lo, hi in buckets:
        sel = [r for r in rows if lo <= float(r[2]) < hi]
        print(lo, hi, len(sel), round(sum(float(r[2]) for r in sel) / len(sel), 3), round(sum(r[3] for r in sel) / len(sel), 3))
