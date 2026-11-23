"""Calibration plot of the made-up forecast log (lesson 7)."""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview, ROOT

ROWS = list(csv.DictReader((ROOT / "docs" / "assets" / "data" / "forecast-log.csv").open(encoding="utf-8")))
BUCKETS = [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 1.01)]


def points():
    out = []
    for lo, hi in BUCKETS:
        sel = [r for r in ROWS if lo <= float(r["forecast"]) < hi]
        out.append((sum(float(r["forecast"]) for r in sel) / len(sel), sum(int(r["outcome"]) for r in sel) / len(sel), len(sel)))
    return out


def draw(fig, ax, c):
    pts = points()
    ax.plot([0, 1], [0, 1], color=c["muted"], linestyle="--", linewidth=1)
    ax.text(0.03, 0.92, "Dashed line: perfect calibration", color=c["muted"], fontsize=9)
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=c["accent"], marker="o", markersize=7)
    for x, y, n in pts:
        ax.annotate(f"{y:.2f} ({n} forecasts)", (x, y), textcoords="offset points", xytext=(6, -14), fontsize=9, color=c["fg"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Average forecast in the bucket")
    ax.set_ylabel("Share that happened")


if __name__ == "__main__":
    for q in save_pair(draw, "19-data-flows-and-forecasting", "calibration"):
        preview(q)
