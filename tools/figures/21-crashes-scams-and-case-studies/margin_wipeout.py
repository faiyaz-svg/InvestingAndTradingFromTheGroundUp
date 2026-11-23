"""Equity left after a price fall, for different loan shares (lesson 1). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

LOANS = [(0.0, "No loan", "muted"), (0.5, "Loan is 50% of the price", "blue"), (0.9, "Loan is 90% of the price", "down")]


def draw(fig, ax, c):
    x = np.linspace(0, 15, 151)
    for loan, label, col in LOANS:
        eq = np.maximum(0, 1 - loan - x / 100) / (1 - loan) * 100
        ax.plot(x, eq, color=c[col], linewidth=2, label=label)
    ax.set_xlabel("Fall in the stock price (%)")
    ax.set_ylabel("Your money left (% of what you put in)")
    ax.set_ylim(-3, 105)
    ax.set_xlim(0, 15)
    ax.legend(loc="lower left", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "21-crashes-scams-and-case-studies", "margin-wipeout", width=6.0, height=3.6):
        preview(p)
