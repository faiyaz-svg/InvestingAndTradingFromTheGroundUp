"""Conversion fee by amount converted, from a tiered schedule against a flat fee (lesson 3)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

# Wealthsimple tiers as of 2026: (lower bound in C$, fee in %).
TIERS = [(0, 1.5), (10_000, 1.0), (25_000, 0.5), (100_000, 0.0)]


def draw(fig, ax, c):
    edges = [t[0] for t in TIERS] + [150_000]
    for (lo, fee), hi in zip(TIERS, edges[1:]):
        ax.hlines(fee, lo / 1000, hi / 1000, color=c["accent"], linewidth=3)
        ax.text((lo + hi) / 2000, fee + 0.07, f"{fee:.1f}%", ha="center", fontsize=9)
    ax.hlines(1.5, 0, 150, color=c["blue"], linewidth=2, linestyle="--", label="Flat 1.5% (CAD account, per fill)")
    ax.plot([], [], color=c["accent"], linewidth=3, label="Tiered fee on a conversion")
    ax.set_xlabel("Amount converted (C$ thousands)")
    ax.set_ylabel("Fee (%)")
    ax.set_ylim(-0.1, 1.9)
    ax.set_xlim(0, 150)
    ax.legend(loc="lower left")


if __name__ == "__main__":
    for p in save_pair(draw, "02-accounts-currency-and-taxes", "conversion-tiers"):
        preview(p)
