"""Price-yield curve of Bond A with the duration tangent (lesson 4)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

F, CPN, N = 1000.0, 0.04, 10


def price(y):
    i = y / 2
    k = np.arange(1, 2 * N + 1)
    return float(np.sum(F * CPN / 2 / (1 + i) ** k) + F / (1 + i) ** (2 * N))


def draw(fig, ax, c):
    y = np.linspace(0.01, 0.08, 120)
    p = np.array([price(v) for v in y])
    # modified duration at 4% by a small central difference
    h = 1e-5
    dpdy = (price(0.04 + h) - price(0.04 - h)) / (2 * h)
    tang = price(0.04) + dpdy * (y - 0.04)
    ax.plot(100 * y, p, color=c["accent"], label="Actual price")
    ax.plot(100 * y, tang, color=c["blue"], linestyle="--", label="Duration estimate (tangent at 4%)")
    ax.fill_between(100 * y, tang, p, where=p > tang, color=c["accent"], alpha=0.18)
    ax.plot([4], [price(0.04)], "o", color=c["fg"])
    ax.annotate("US$1,000 at 4%", (4, price(0.04)), textcoords="offset points", xytext=(8, 8), fontsize=9)
    ax.annotate("Gap = convexity", (5.6, 960), fontsize=9, color=c["accent"])
    ax.set_ylim(650, 1350)
    ax.set_xlabel("Yield to maturity (%)")
    ax.set_ylabel("Price of Bond A (US$)")
    ax.legend(loc="upper right", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "12-bonds-and-the-yield-curve", "price-yield", width=6.0, height=3.8):
        preview(p)
