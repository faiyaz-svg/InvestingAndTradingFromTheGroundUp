"""Three stylised yield curve shapes (lesson 3). Made-up numbers, for illustration."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

MAT = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30])
NORMAL = [3.4, 3.5, 3.6, 3.8, 3.9, 4.1, 4.2, 4.4, 4.8, 4.9]
FLAT = [4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5]
INV = [5.4, 5.3, 5.1, 4.8, 4.6, 4.4, 4.3, 4.2, 4.3, 4.3]


def draw(fig, ax, c):
    x = np.arange(len(MAT))
    ax.plot(x, NORMAL, color=c["up"], label="Normal (upward)")
    ax.plot(x, FLAT, color=c["muted"], label="Flat")
    ax.plot(x, INV, color=c["down"], label="Inverted")
    ax.set_xticks(x)
    ax.set_xticklabels(["3m", "6m", "1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"])
    ax.set_xlabel("Time to maturity")
    ax.set_ylabel("Yield (%), made up")
    ax.set_ylim(3, 6)
    ax.legend(loc="upper center", ncol=3, fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "12-bonds-and-the-yield-curve", "curve-shapes", width=6.0, height=3.4):
        preview(p)
