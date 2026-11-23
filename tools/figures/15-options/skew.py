"""Implied volatility against strike for the made-up Stock A chain (lesson 8)."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
import chain


def draw(fig, ax, c):
    cr, pr = chain.rows("call"), chain.rows("put")
    ax.plot([r["K"] for r in cr], [r["iv"] * 100 for r in cr], "o-", color=c["accent"], label="Calls")
    ax.plot([r["K"] for r in pr], [r["iv"] * 100 for r in pr], "s--", color=c["blue"], label="Puts")
    ax.axvline(chain.S, color=c["muted"], lw=1, ls="--")
    ax.annotate("Stock at 50.20", (chain.S, 35), (50.6, 35), color=c["fg"], fontsize=9)
    ax.set_xlabel("Strike (US$)")
    ax.set_ylabel("Implied volatility (% per year)")
    ax.legend(loc="upper right")


if __name__ == "__main__":
    for q in save_pair(draw, "15-options", "iv-skew"):
        preview(q)
