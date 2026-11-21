"""Equity ratio as a position falls, for four loan sizes, against a 30% requirement (lesson 10)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

REQ = 0.30
# Loan as a share of the starting position value, with the label.
LOANS = [(0.0, "No loan"), (1 / 3, "Loan = 1/3"), (0.5, "Loan = 1/2"), (2 / 3, "Loan = 2/3")]


def draw(fig, ax, c):
    fall = np.linspace(0, 0.5, 200)
    cols = [c["blue"], c["teal"], c["accent"], c["orange"]]
    for (loan, name), col in zip(LOANS, cols):
        v = 1 - fall
        ratio = (v - loan) / v * 100
        ax.plot(fall * 100, ratio, color=col, linewidth=2, label=name)
        if loan > 0:
            call = 100 * (1 - loan / (1 - REQ))
            if 0 < call < 50:
                ax.plot([call], [REQ * 100], marker="o", color=col)
    ax.axhline(REQ * 100, color=c["muted"], linestyle="--", linewidth=1)
    ax.text(49, REQ * 100 + 2, "30% requirement (made up)", ha="right", fontsize=8, color=c["muted"])
    ax.set_xlabel("Fall in the position's value (%)")
    ax.set_ylabel("Equity as a share of the position (%)")
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 50)
    ax.legend(loc="lower left", fontsize=8)


if __name__ == "__main__":
    for p in save_pair(draw, "02-accounts-currency-and-taxes", "margin-call"):
        preview(p)
