"""Present value of Stock A (cash soon) and Stock B (cash late) at two discount rates (lesson 3). Made-up."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview


def pv_a(r):
    return sum(20 / (1 + r) ** t for t in range(1, 6))


def pv_b(r):
    return 100 / (1 + r) ** 10


def draw(fig, ax, c):
    x = np.arange(2)
    w = 0.36
    lo = [pv_a(0.03), pv_b(0.03)]
    hi = [pv_a(0.06), pv_b(0.06)]
    b1 = ax.bar(x - w / 2, lo, w, color=c["blue"], label="Discount rate 3%")
    b2 = ax.bar(x + w / 2, hi, w, color=c["accent"], label="Discount rate 6%")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"US${b.get_height():.2f}", ha="center", fontsize=9)
    ax.set_xticks(x, ["Stock A\nUS$20 a year, years 1 to 5", "Stock B\nUS$100 in year 10"])
    ax.set_ylabel("Present value (US$)")
    ax.set_ylim(0, 110)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper right")


if __name__ == "__main__":
    for p in save_pair(draw, "11-macro-and-economic-data", "pv-two-companies"):
        preview(p)
