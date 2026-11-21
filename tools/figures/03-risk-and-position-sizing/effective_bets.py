"""Effective number of independent bets against correlation (lesson 7)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def draw(fig, ax, c):
    rho = np.linspace(0, 1, 100)
    for n, col in ((4, c["accent"]), (8, c["blue"])):
        ax.plot(rho, n / (1 + (n - 1) * rho), color=col, label=f"{n} positions")
    ax.set_xlabel("Average correlation between the positions")
    ax.set_ylabel("Effective independent bets")
    ax.set_ylim(0, 8.5)
    ax.legend(loc="upper right")


if __name__ == "__main__":
    for q in save_pair(draw, "03-risk-and-position-sizing", "effective-bets"):
        preview(q)
