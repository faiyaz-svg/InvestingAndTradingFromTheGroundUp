"""Expectancy in R against win rate for three payoff ratios (lesson 3)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def draw(fig, ax, c):
    p = np.linspace(0.1, 0.9, 200)
    for b, col in ((1, c["blue"]), (2, c["accent"]), (3, c["teal"])):
        ax.plot(p * 100, p * b - (1 - p), color=col, label=f"Payoff ratio {b}")
        be = 1 / (1 + b)
        ax.plot([be * 100], [0], "o", color=col)
    ax.axhline(0, color=c["muted"], lw=1)
    ax.set_xlabel("Win rate (%)")
    ax.set_ylabel("Expectancy (R per trade)")
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for q in save_pair(draw, "03-risk-and-position-sizing", "expectancy"):
        preview(q)
