"""A 2x daily-reset fund against its index over 250 days (lesson 4)."""
import numpy as np
from _model import ns, save_pair, preview

F = "13-etfs-portfolios-and-factors"


def draw(fig, ax, c):
    r, idx, lev, naive = ns["leverage_sim"]()
    d = np.arange(len(idx))
    ax.plot(d, idx, color=c["muted"], label=f"Index: {idx[-1]:.1f}")
    ax.plot(d, naive, color=c["blue"], linestyle="--", label=f"Twice the index's total return: {naive[-1]:.1f}")
    ax.plot(d, lev, color=c["accent"], label=f"2x daily-reset fund: {lev[-1]:.1f}")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Value (start = 100)")
    ax.legend(loc="upper left", fontsize=8.5)
    ax.set_xlim(0, 250)
    ax.set_ylim(55, 145)


if __name__ == "__main__":
    for p in save_pair(draw, F, "leveraged-decay", width=6.0, height=3.6):
        preview(p)
