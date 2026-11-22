"""Account equity over three days against the margin lines (lesson 2). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

LABELS = ["Day 0\nstart", "Day 1\nclose", "Day 2\nclose", "Day 2\nafter deposit", "Day 3\nclose"]
EQUITY = [5500, 5300, 4300, 4800, 5200]
INITIAL, MAINT = 4800, 4400


def draw(fig, ax, c):
    x = range(len(EQUITY))
    ax.plot(x, EQUITY, color=c["accent"], marker="o")
    ax.axhline(INITIAL, color=c["blue"], linestyle="--", linewidth=1)
    ax.axhline(MAINT, color=c["down"], linestyle="--", linewidth=1)
    ax.text(4.2, INITIAL + 25, "Initial margin US$4,800", color=c["blue"], fontsize=9, ha="right", va="bottom")
    ax.text(4.2, MAINT - 25, "Maintenance margin US$4,400", color=c["down"], fontsize=9, ha="right", va="top")
    ax.annotate("Margin call:\ndeposit US$500", (2, 4300), (1.35, 3950), color=c["fg"], fontsize=9,
                arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.set_xticks(list(x))
    ax.set_xticklabels(LABELS, fontsize=9)
    ax.set_ylabel("Account equity (US$)")
    ax.set_ylim(3700, 5800)


if __name__ == "__main__":
    for q in save_pair(draw, "14-futures", "margin-path"):
        preview(q)
