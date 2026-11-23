"""Lesson 2: 20-day volatility, annualised, for one made-up stock and the made-up index."""
import numpy as np
from _common import FOLDER, load, fmt_dates
from figstyle import preview, save_pair


def draw(fig, ax, c):
    for name, label, col in (("stock-01", "stock-01", c["accent"]), ("index-x-3y", "index-x", c["blue"])):
        v = load(name).pct_change().rolling(20).std() * np.sqrt(252)
        ax.plot(v.index, v * 100, color=col, label=label)
    ax.set_ylabel("20-day volatility, annualised (%)")
    fmt_dates(ax)
    ax.legend(loc="upper right")


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "rolling-volatility"):
        preview(p)
