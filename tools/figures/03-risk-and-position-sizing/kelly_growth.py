"""Growth rate per trade against the fraction risked (lesson 9)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def g(p, b, f):
    return p * np.log(1 + b * f) + (1 - p) * np.log(1 - f)


def draw(fig, ax, c):
    f = np.linspace(0, 0.3, 300)
    ax.plot(f * 100, g(0.55, 1, f) * 100, color=c["accent"])
    ax.axhline(0, color=c["muted"], lw=1)
    for x, lab, dy in ((0.05, "Half Kelly (5%)", 0.09), (0.10, "Full Kelly (10%)", 0.07), (0.20, "Twice Kelly (20%)", 0.12)):
        ax.plot([x * 100], [g(0.55, 1, x) * 100], "o", color=c["fg"])
        ax.annotate(lab, xy=(x * 100, g(0.55, 1, x) * 100), xytext=(x * 100 - 4.5, g(0.55, 1, x) * 100 + dy), color=c["fg"], fontsize=9)
    ax.set_xlabel("Fraction of the account risked per trade (%)")
    ax.set_ylabel("Growth per trade (log %)")
    ax.set_ylim(-0.4, 0.8)


if __name__ == "__main__":
    for q in save_pair(draw, "03-risk-and-position-sizing", "kelly-growth"):
        preview(q)
