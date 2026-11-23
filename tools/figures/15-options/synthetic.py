"""A long call plus a short put behaves like the stock (lesson 5). Strike 50, C = 3.23, P = 2.73."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
def draw(fig, ax, c):
    S = np.linspace(35, 65, 301)
    C, P = bs.price(50, 50, 0.25, 0.04, 0.30), bs.price(50, 50, 0.25, 0.04, 0.30, kind="put")
    lc = (np.maximum(S - 50, 0) - C) * 100
    sp = -(np.maximum(50 - S, 0) - P) * 100
    ax.plot(S, lc, color=c["up"], label="Long call")
    ax.plot(S, sp, color=c["down"], label="Short put")
    ax.plot(S, lc + sp, color=c["accent"], lw=3, ls="--", label="Sum (a straight line, slope 100)")
    ax.axhline(0, color=c["muted"], lw=1)
    ax.set_xlabel("Stock A price at expiry (US$)")
    ax.set_ylabel("Profit or loss per pair (US$)")
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "15-options", "synthetic-long"):
        preview(q)
