"""REIT A: from net income to FFO to AFFO (lesson 8). Made-up numbers, US$ millions."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

STEPS = [("Net income", 30.0, "total"), ("Real estate\ndepreciation", 42.0, "delta"), ("Gain on\nproperty sale", -12.0, "delta"),
         ("FFO", None, "total"), ("Recurring\ncapex", -14.0, "delta"), ("Straight-line\nrent", -4.0, "delta"), ("AFFO", None, "total")]


def draw(fig, ax, c):
    level = 0.0
    for i, (label, v, kind) in enumerate(STEPS):
        if kind == "total":
            if v is not None:
                level = v
            ax.bar(i, level, color=c["accent"], width=0.6)
            ax.text(i, level + 1.2, f"{level:.0f}", ha="center", fontsize=9, color=c["fg"])
        else:
            bottom = level if v > 0 else level + v
            ax.bar(i, abs(v), bottom=bottom, color=c["up"] if v > 0 else c["down"], width=0.6)
            ax.text(i, max(level, level + v) + 1.2, f"{v:+.0f}", ha="center", fontsize=9, color=c["fg"])
            level += v
    ax.set_xticks(range(len(STEPS)))
    ax.set_xticklabels([s[0] for s in STEPS], fontsize=8)
    ax.set_ylabel("US$ millions (made up)")
    ax.set_ylim(0, 82)


if __name__ == "__main__":
    for q in save_pair(draw, "17-commodities-forex-and-reits", "ffo-bridge", width=6.4):
        preview(q)
