"""Gain needed to recover a loss (lesson 1)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def draw(fig, ax, c):
    loss = np.linspace(0, 0.9, 200)
    ax.plot(loss * 100, loss / (1 - loss) * 100, color=c["accent"])
    spots = {0.1: (4, 330), 0.25: (12, 480), 0.5: (30, 640), 0.75: (48, 800)}
    for L, (tx, ty) in spots.items():
        g = L / (1 - L) * 100
        ax.plot([L * 100], [g], "o", color=c["down"])
        ax.annotate(f"{L*100:.0f}% loss needs +{g:.0f}%", xy=(L * 100, g), xytext=(tx, ty), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.set_xlabel("Loss from the peak (%)")
    ax.set_ylabel("Gain needed to get back (%)")
    ax.set_ylim(0, 950)


if __name__ == "__main__":
    for q in save_pair(draw, "03-risk-and-position-sizing", "loss-recovery"):
        preview(q)
