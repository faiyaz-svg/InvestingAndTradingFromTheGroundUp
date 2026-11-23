"""Lesson 7: average next-month return by momentum group, made-up universe."""
import numpy as np
import pandas as pd
from _common import FOLDER, load
from figstyle import preview, save_pair


def draw(fig, ax, c):
    prices = pd.DataFrame({f"s{k:02d}": load(f"stock-{k:02d}") for k in range(1, 11)})
    month = prices.resample("ME").last()
    nxt = month.pct_change().shift(-1)
    mom = month.shift(1) / month.shift(12) - 1
    ok = mom.notna().all(axis=1) & nxt.notna().all(axis=1)
    g = np.ceil(mom[ok].rank(axis=1, method="first") / 2)
    vals = [nxt[ok][g == q].stack().mean() * 100 for q in (1, 2, 3, 4, 5)]
    ax.bar(range(1, 6), vals, color=[c["down"] if v < 0 else c["up"] for v in vals])
    ax.axhline(0, color=c["muted"], lw=0.8)
    ax.set_xticks(range(1, 6))
    ax.set_xticklabels(["1 (losers)", "2", "3", "4", "5 (winners)"])
    ax.set_xlabel("Group by 12-1 month return")
    ax.set_ylabel("Average next-month return (%)")
    ax.grid(False)


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "momentum-groups"):
        preview(p)
