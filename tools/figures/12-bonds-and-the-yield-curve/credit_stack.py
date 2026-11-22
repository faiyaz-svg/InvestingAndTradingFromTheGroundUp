"""What a corporate yield is made of: Treasury yield, expected loss, risk premium (lesson 5). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

TSY = 4.00
BARS = [("Investment grade\n(Bond B)", 0.12, 0.88), ("High yield\n(Bond C)", 1.20, 2.80)]  # expected loss, premium (pp)


def draw(fig, ax, c):
    for i, (name, el, prem) in enumerate(BARS):
        ax.bar(i, TSY, color=c["blue"], width=0.5, label="Treasury yield" if i == 0 else None)
        ax.bar(i, el, bottom=TSY, color=c["down"], width=0.5, label="Expected loss" if i == 0 else None)
        ax.bar(i, prem, bottom=TSY + el, color=c["accent"], width=0.5, label="Risk premium" if i == 0 else None)
        ax.text(i, TSY + el + prem + 0.12, f"{TSY + el + prem:.2f}%", ha="center", fontsize=10)
    ax.set_xticks(range(len(BARS)))
    ax.set_xticklabels([b[0] for b in BARS])
    ax.set_ylabel("Yield (%)")
    ax.set_ylim(0, 9.5)
    ax.set_xlim(-0.6, 1.9)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "12-bonds-and-the-yield-curve", "credit-stack", width=6.0, height=3.6):
        preview(p)
