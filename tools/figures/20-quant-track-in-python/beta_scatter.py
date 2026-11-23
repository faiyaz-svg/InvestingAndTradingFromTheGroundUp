"""Lesson 6: daily returns of stock-04 against the index, with the fitted line."""
import numpy as np
from _common import FOLDER, load
from figstyle import preview, save_pair


def draw(fig, ax, c):
    y = load("stock-04").pct_change().dropna() * 100
    x = load("index-x-3y").pct_change().dropna() * 100
    beta, alpha = np.polyfit(x, y, 1)
    ax.scatter(x, y, s=8, color=c["blue"], alpha=0.5)
    xs = np.array([x.min(), x.max()])
    ax.plot(xs, alpha + beta * xs, color=c["accent"], label=f"Fitted line, slope (beta) {beta:.2f}")
    ax.set_xlabel("Index daily return (%)")
    ax.set_ylabel("stock-04 daily return (%)")
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for p in save_pair(draw, FOLDER, "beta-scatter"):
        preview(p)
