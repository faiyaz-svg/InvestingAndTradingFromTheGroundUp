"""Price weights against market-cap weights for three made-up stocks (lesson 10)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

PRICE = [200, 50, 10]
SHARES = [10, 100, 300]  # millions
NAMES = ["Stock A", "Stock B", "Stock C"]


def draw(fig, ax, c):
    pw = np.array(PRICE) / sum(PRICE) * 100
    cap = np.array([p * s for p, s in zip(PRICE, SHARES)], float)
    cw = cap / cap.sum() * 100
    x = np.arange(3)
    w = 0.36
    b1 = ax.bar(x - w / 2, pw, w, color=c["blue"], label="Price-weighted")
    b2 = ax.bar(x + w / 2, cw, w, color=c["accent"], label="Cap-weighted")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{b.get_height():.1f}%", ha="center", fontsize=9)
    ax.set_xticks(x, [f"{n}\nUS${p}" for n, p in zip(NAMES, PRICE)])
    ax.set_ylabel("Weight in the index (%)")
    ax.set_ylim(0, 90)
    ax.grid(axis="x", visible=False)
    ax.legend()


if __name__ == "__main__":
    for p in save_pair(draw, "01-how-markets-work", "index-weights"):
        preview(p)
