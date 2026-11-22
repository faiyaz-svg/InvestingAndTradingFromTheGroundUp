"""Best of N random rules (lesson 6): the best of many no-edge rules looks skilled."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview


def simulate():
    rng = np.random.default_rng(66)
    days, trials = 250, 200
    out = {}
    for n in (1, 10, 100, 1000):
        best = []
        for _ in range(trials):
            r = rng.normal(0, 0.01, (n, days))
            sh = r.mean(axis=1) / r.std(axis=1, ddof=1) * np.sqrt(252)
            best.append(sh.max())
        out[n] = float(np.mean(best))
    return out


def draw(fig, ax, cc):
    res = simulate()
    ns = [str(n) for n in res]
    vals = list(res.values())
    ax.bar(ns, vals, color=cc["accent"], width=0.55)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.07, f"{v:.2f}", ha="center", color=cc["fg"], fontsize=10)
    ax.set_xlabel("Number of no-edge rules tried")
    ax.set_ylabel("Best Sharpe ratio (annualized)")
    ax.set_ylim(0, 3.9)
    ax.grid(False)


if __name__ == "__main__":
    for q in save_pair(draw, "06-ict-and-smart-money-tested", "best-of-n", width=6.0, height=3.4):
        preview(q)
