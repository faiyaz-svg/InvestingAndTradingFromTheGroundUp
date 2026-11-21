"""The prospect theory value function with the 1992 median estimates (lesson 1)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

ALPHA = 0.88
LAMBDA = 2.25


def value(x):
    x = np.asarray(x, dtype=float)
    return np.where(x >= 0, np.abs(x) ** ALPHA, -LAMBDA * np.abs(x) ** ALPHA)


def draw(fig, ax, c):
    x = np.linspace(-100, 100, 401)
    ax.plot(x, value(x), color=c["accent"])
    ax.axhline(0, color=c["muted"], lw=1)
    ax.axvline(0, color=c["muted"], lw=1)
    ax.plot([100], [float(value(100))], "o", color=c["up"])
    ax.plot([-100], [float(value(-100))], "o", color=c["down"])
    ax.annotate("Gain of 100: felt value 57.5", xy=(100, 57.5), xytext=(10, 95), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.annotate("Loss of 100: felt value -129.5", xy=(-100, -129.5), xytext=(-98, -80), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.set_xlabel("Gain or loss versus your reference point (US$)")
    ax.set_ylabel("How it feels (value)")


if __name__ == "__main__":
    for q in save_pair(draw, "04-psychology-journal-and-paper-trading", "value-function"):
        preview(q)
