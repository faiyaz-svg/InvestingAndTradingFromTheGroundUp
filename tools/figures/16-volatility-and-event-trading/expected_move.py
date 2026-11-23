"""Profit of a long straddle at expiry with the expected move marked (lesson 4)."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import vol_data
from vol_data import bs

S, K, T, R, IV = 60.51, 60.50, 7 / 365, 0.04, 0.55
STRADDLE = bs.price(S, K, T, R, IV) + bs.price(S, K, T, R, IV, kind="put")


def draw(fig, ax, c):
    x = np.linspace(48, 73, 300)
    pnl = np.abs(x - K) - STRADDLE
    ax.plot(x, pnl, color=c["accent"])
    ax.axhline(0, color=c["muted"], lw=1)
    ax.axvspan(K - STRADDLE, K + STRADDLE, color=c["zone"])
    for xb in (K - STRADDLE, K + STRADDLE):
        ax.axvline(xb, color=c["muted"], lw=1, ls="--")
    ax.annotate("Breakeven\n%.2f" % (K - STRADDLE), (K - STRADDLE, 7), (K - STRADDLE - 6.5, 8), color=c["fg"], fontsize=9)
    ax.annotate("Breakeven\n%.2f" % (K + STRADDLE), (K + STRADDLE, 7), (K + STRADDLE + 0.6, 8), color=c["fg"], fontsize=9)
    ax.annotate("Straddle price = expected move\n(shaded band)", (K, -STRADDLE), (K - 5.8, -STRADDLE - 2.6), color=c["fg"], fontsize=9)
    ax.set_xlabel("Stock A price at expiry (US$)")
    ax.set_ylabel("Profit per share (US$)")
    ax.set_ylim(-STRADDLE - 4, 11)


if __name__ == "__main__":
    for q in save_pair(draw, "16-volatility-and-event-trading", "expected-move"):
        preview(q)
    print(round(STRADDLE, 4))
