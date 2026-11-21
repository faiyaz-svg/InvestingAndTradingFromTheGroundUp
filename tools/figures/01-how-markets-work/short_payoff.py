"""Profit and loss of 100 shares bought at US$50 and 100 shares sold short at US$50 (lesson 8)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def draw(fig, ax, c):
    p = np.linspace(0, 100, 201)
    ax.plot(p, (p - 50) * 100, color=c["up"], label="Long 100 shares")
    ax.plot(p, (50 - p) * 100, color=c["down"], label="Short 100 shares")
    ax.axhline(0, color=c["muted"], lw=1)
    ax.set_xlabel("Stock A price (US$)")
    ax.set_ylabel("Profit or loss (US$)")
    ax.annotate("Short gain capped at US$5,000\n(price cannot go below 0)", xy=(0, 5000), xytext=(12, 4300), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.annotate("Short loss has no limit", xy=(100, -5000), xytext=(58, -4500), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.legend(loc="center left")


if __name__ == "__main__":
    for q in save_pair(draw, "01-how-markets-work", "short-vs-long"):
        preview(q)
