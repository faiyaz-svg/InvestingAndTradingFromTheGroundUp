"""Year-over-year CPI-U, all items and core, 2017 to 2025 (lessons 4).

Data: BLS Public Data API v1, series CUUR0000SA0 (all items, not seasonally
adjusted) and CUUR0000SA0L1E (all items less food and energy), downloaded
2026-11-21 into bls_cpi.csv next to this file. Public domain (BLS).
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

HERE = Path(__file__).resolve().parent


def load():
    idx = {}
    for r in csv.DictReader(open(HERE / "bls_cpi.csv")):
        if r["cpi_all"] not in ("-", ""):
            idx[(int(r["year"]), int(r["month"]))] = (float(r["cpi_all"]), float(r["cpi_core"]))
    return idx


def yoy():
    idx = load()
    out = []
    for (y, m), (a, c) in sorted(idx.items()):
        if y >= 2017 and (y - 1, m) in idx:
            pa, pc = idx[(y - 1, m)]
            out.append((y + (m - 1) / 12, y, m, 100 * (a / pa - 1), 100 * (c / pc - 1)))
    return out


def draw(fig, ax, c):
    d = yoy()
    x = np.array([r[0] for r in d])
    # break the line where a month is missing
    gap = np.where(np.diff(x) > 1.5 / 12)[0]
    for name, col, k in (("All items (headline)", c["accent"], 3), ("Core (less food and energy)", c["blue"], 4)):
        y = np.array([r[k] for r in d])
        xs, ys = x.copy(), y.copy()
        for g in gap[::-1]:
            xs = np.insert(xs, g + 1, np.nan)
            ys = np.insert(ys, g + 1, np.nan)
        ax.plot(xs, ys, color=col, label=name)
    ax.axhline(2, color=c["muted"], lw=1, ls="--")
    ax.text(2025.3, 1.6, "2%", color=c["muted"], fontsize=9)
    ax.set_ylabel("Change from a year earlier (%)")
    ax.set_xlim(2017, 2026)
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for p in save_pair(draw, "11-macro-and-economic-data", "cpi-headline-core"):
        preview(p)
