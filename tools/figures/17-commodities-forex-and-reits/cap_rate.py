"""Property value and equity value at three cap rates for REIT A (lesson 9). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

NOI = 108.0
DEBT = 720.0
RATES = [0.065, 0.075, 0.085]


def draw(fig, ax, c):
    base_v = NOI / 0.075
    base_e = base_v - DEBT
    w = 0.35
    for i, r in enumerate(RATES):
        v = NOI / r
        e = v - DEBT
        dv = v / base_v - 1
        de = e / base_e - 1
        ax.bar(i - w / 2, 100 * dv, width=w, color=c["blue"], label="Property value" if i == 0 else None)
        ax.bar(i + w / 2, 100 * de, width=w, color=c["accent"], label="Equity (NAV)" if i == 0 else None)
        ax.text(i - w / 2, 100 * dv + (1.5 if dv >= 0 else -4), f"{100 * dv:+.1f}%", ha="center", fontsize=8, color=c["fg"])
        ax.text(i + w / 2, 100 * de + (1.5 if de >= 0 else -4), f"{100 * de:+.1f}%", ha="center", fontsize=8, color=c["fg"])
    ax.axhline(0, color=c["muted"], linewidth=1)
    ax.set_xticks(range(3))
    ax.set_xticklabels([f"{100 * r:.1f}%" for r in RATES])
    ax.set_xlabel("Cap rate")
    ax.set_ylabel("Change from the 7.5% case (%)")
    ax.set_ylim(-32, 42)
    ax.legend(loc="upper right", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "17-commodities-forex-and-reits", "cap-rate-leverage"):
        preview(q)
