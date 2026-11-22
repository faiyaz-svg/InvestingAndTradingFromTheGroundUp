"""Round-trip cost in R against the stop distance (lesson 8)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def draw(fig, ax, c):
    stop = np.linspace(0.05, 1.0, 200)
    for cost, col in ((0.02, c["accent"]), (0.05, c["fg"]), (0.10, c["down"])):
        ax.plot(stop, cost / stop, color=col, label=f"US${cost:.2f} per share")
    ax.axhline(0.5, color=c["muted"], linestyle="--", linewidth=1)
    ax.text(0.62, 0.53, "0.5R", color=c["muted"], fontsize=9)
    ax.set_ylim(0, 1.6)
    ax.set_xlabel("Stop distance (US$ per share)")
    ax.set_ylabel("Round-trip cost (R)")
    ax.legend(frameon=False, loc="upper right", title="All-in cost")


if __name__ == "__main__":
    for q in save_pair(draw, "08-day-trading", "cost-vs-stop"):
        preview(q)
