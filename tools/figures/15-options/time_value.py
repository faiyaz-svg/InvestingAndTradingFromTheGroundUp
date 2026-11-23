"""Intrinsic value and time value of calls across strikes (lesson 3). Stock A at 50.20, volatility 30%, T = 0.25."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
S0 = 50.20
K = np.arange(40, 62.6, 2.5)


def draw(fig, ax, c):
    val = np.array([bs.price(S0, k, 0.25, 0.04, 0.30) for k in K])
    intr = np.maximum(S0 - K, 0)
    ax.bar(K, intr, width=1.8, color=c["blue"], label="Intrinsic value")
    ax.bar(K, val - intr, width=1.8, bottom=intr, color=c["accent"], label="Time value")
    ax.axvline(S0, color=c["muted"], lw=1, ls="--")
    ax.annotate("Stock at 50.20", (S0, 6.5), (50.8, 6.5), color=c["fg"], fontsize=9, va="center")
    ax.set_xlabel("Call strike (US$)")
    ax.set_ylabel("Call value per share (US$)")
    ax.legend(loc="upper right")


if __name__ == "__main__":
    for q in save_pair(draw, "15-options", "time-value-by-strike"):
        preview(q)
