"""Archegos: value and swap exposure, March 2020 and March 2021 (lesson 6). Source: SEC press release 2022-70."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

DATA = [("March 2020", 1.5, 10), ("March 2021 (peak)", 36, 160)]  # value, exposure, US\\$ billions


def draw(fig, ax, c):
    w = 0.34
    for i, (name, val, exp) in enumerate(DATA):
        ax.bar(i - w / 2, val, width=w, color=c["blue"], label="Value of the fund" if i == 0 else None)
        ax.bar(i + w / 2, exp, width=w, color=c["accent"], label="Exposure through swaps and other positions" if i == 0 else None)
        ax.text(i - w / 2, val + 3, f"{val:g}", ha="center", fontsize=10)
        ax.text(i + w / 2, exp + 3, f"{exp:g}", ha="center", fontsize=10)
    ax.set_xticks(range(len(DATA)))
    ax.set_xticklabels([d[0] for d in DATA])
    ax.set_ylabel("US\\$ billions")
    ax.set_ylim(0, 185)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "21-crashes-scams-and-case-studies", "archegos-exposure", width=6.0, height=3.6):
        preview(p)
