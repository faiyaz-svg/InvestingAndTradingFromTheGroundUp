"""Same edge at 1%, 2% and 5% risk per trade, one seeded path (lesson 8)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
from figstyle import save_pair, preview
import sim


def draw(fig, ax, c):
    r = sim.outcomes(paths=1, seed=7)
    for f, col in ((0.01, c["blue"]), (0.02, c["accent"]), (0.05, c["down"])):
        eq = sim.curves(r, f)[0]
        ax.plot(range(len(eq)), eq, color=col, lw=1.6, label=f"{f*100:.0f}% risk per trade")
    ax.set_yscale("log")
    ax.set_yticks([5000, 10000, 20000, 50000, 100000])
    ax.set_yticklabels(["5k", "10k", "20k", "50k", "100k"])
    ax.axhline(10000, color=c["muted"], lw=1)
    ax.set_xlabel("Trade number")
    ax.set_ylabel("Account (US$, log scale)")
    ax.legend(loc="upper left")


if __name__ == "__main__":
    for q in save_pair(draw, "03-risk-and-position-sizing", "equity-curves"):
        preview(q)
