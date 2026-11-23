"""Equity of a 10x long perpetual against price, and its liquidation price (lesson 6)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

Q, ENTRY, COLL, M = 1000, 20.0, 2000.0, 0.005
LIQ = (Q * ENTRY - COLL) / (Q * (1 - M))


def draw(fig, ax, c):
    p = np.linspace(17.0, 22.0, 100)
    ax.plot(p, COLL + Q * (p - ENTRY), color=c["accent"], label="Equity")
    ax.plot(p, M * Q * p, color=c["down"], linestyle="--", label="Maintenance margin")
    ax.axvline(LIQ, color=c["muted"], linestyle=":", linewidth=1)
    ax.annotate(f"Liquidation price\nUS${LIQ:.2f}", (LIQ, M * Q * LIQ), (18.9, 1100), color=c["fg"], fontsize=9,
                arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.scatter([ENTRY], [COLL], color=c["blue"], zorder=3)
    ax.text(ENTRY + 0.05, COLL + 150, "Entry US$20.00", color=c["blue"], fontsize=9)
    ax.set_xlabel("Coin A price (US$)")
    ax.set_ylabel("Position equity (US$)")
    ax.set_ylim(-200, 4400)
    ax.legend(loc="upper left", frameon=False, fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "18-crypto", "liquidation"):
        preview(q)
