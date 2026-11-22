"""Value per share against discount rate and terminal growth (lesson 5)."""
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from _model import ns, save_pair, preview

WACCS = [0.081, 0.086, 0.091, 0.096, 0.101]
TGS = [0.02, 0.025, 0.03, 0.035, 0.04]


def draw(fig, ax, c):
    grid = np.array([[ns["dcf"](wacc=w, tg=g)["ps"] for g in TGS] for w in WACCS])
    price = ns["PRICE"]
    cmap = LinearSegmentedColormap.from_list("v", [c["down"], c["bg"], c["up"]])
    span = max(abs(grid - price).max(), 1)
    ax.imshow(grid, cmap=cmap, vmin=price - span, vmax=price + span, aspect="auto")
    for i in range(len(WACCS)):
        for j in range(len(TGS)):
            ax.text(j, i, f"{grid[i, j]:.2f}", ha="center", va="center", fontsize=9, color=c["fg"])
    ax.set_xticks(range(len(TGS)))
    ax.set_xticklabels([f"{100 * g:.1f}%" for g in TGS])
    ax.set_yticks(range(len(WACCS)))
    ax.set_yticklabels([f"{100 * w:.1f}%" for w in WACCS])
    ax.set_xlabel("Terminal growth rate")
    ax.set_ylabel("Discount rate (WACC)")
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "sensitivity", width=6.0, height=3.8):
        preview(p)
