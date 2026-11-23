"""Loss on a short sale as the price rises, against the margin posted (lesson 5). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

SOLD, SHARES, MARGIN = 20.0, 1000, 10_000


def draw(fig, ax, c):
    p = np.linspace(20, 120, 201)
    loss = (p - SOLD) * SHARES
    ax.plot(p, loss / 1000, color=c["down"], linewidth=2, label="Loss on 1,000 shares sold short at US\\$20")
    ax.axhline(MARGIN / 1000, color=c["accent"], linewidth=1.5, linestyle="--")
    ax.text(60, MARGIN / 1000 + 3, "Margin posted: US\\$10,000 (a 50% initial margin)", color=c["accent"], fontsize=9)
    ax.plot([30], [10], "o", color=c["accent"])
    ax.text(32, 4.5, "Price US\\$30: margin gone", color=c["accent"], fontsize=9)
    ax.set_xlabel("Stock A price (US\\$)")
    ax.set_ylabel("Loss (US\\$ thousands)")
    ax.set_xlim(20, 120)
    ax.set_ylim(0, 105)
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "21-crashes-scams-and-case-studies", "short-loss", width=6.0, height=3.6):
        preview(p)
