"""The Brier penalty for one forecast, with the lesson 7 examples marked."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview


def draw(fig, ax, c):
    p = np.linspace(0, 1, 101)
    ax.plot(p, (p - 1) ** 2, color=c["up"], label="Event happens: penalty (p - 1)^2")
    ax.plot(p, p ** 2, color=c["down"], label="Event does not happen: penalty p^2")
    for x, y, lab, dy in [(0.8, 0.04, "0.8, happened: 0.04", 14), (0.3, 0.09, "0.3, did not: 0.09", 14), (0.9, 0.81, "0.9, did not: 0.81", -14)]:
        ax.plot([x], [y], marker="o", color=c["accent"], zorder=5)
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(-6, dy), fontsize=9, color=c["fg"], ha="right" if x > 0.5 else "left")
    ax.set_xlabel("Forecast probability that the event happens (p)")
    ax.set_ylabel("Penalty for one forecast")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    ax.legend(loc="upper center", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "19-data-flows-and-forecasting", "brier-penalty"):
        preview(q)
