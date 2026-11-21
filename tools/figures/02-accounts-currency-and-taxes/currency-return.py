"""Stock return in USD, currency return and your return in CAD for four made-up cases (lesson 5)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

D = chr(92) + "$"  # an escaped dollar sign, so matplotlib does not read $ as math

# (label, stock return in USD, US dollar change against the Canadian dollar)
CASES = [
    (f"Stock +10%\nUS{D} -5%", 0.10, -0.05),
    (f"Stock +10%\nUS{D} +5%", 0.10, 0.05),
    (f"Stock -8%\nUS{D} +4%", -0.08, 0.04),
    (f"Stock 0%\nUS{D} -7%", 0.0, -0.07),
]


def draw(fig, ax, c):
    x = np.arange(len(CASES))
    w = 0.26
    usd = [100 * u for _, u, _ in CASES]
    fx = [100 * f for _, _, f in CASES]
    cad = [100 * ((1 + u) * (1 + f) - 1) for _, u, f in CASES]
    series = [
        (-w, usd, c["blue"], f"Stock return in US{D}"),
        (0, fx, c["teal"], f"US{D} against C{D}"),
        (w, cad, c["accent"], f"Your return in C{D}"),
    ]
    for off, vals, col, name in series:
        bars = ax.bar(x + off, vals, w, color=col, label=name)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v + (0.6 if v >= 0 else -1.6), f"{v:.1f}%", ha="center", fontsize=7)
    ax.axhline(0, color=c["muted"], linewidth=1)
    ax.set_xticks(x, [k for k, _, _ in CASES])
    ax.set_ylabel("Return (%)")
    ax.set_ylim(-12, 20)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper right", fontsize=8)


if __name__ == "__main__":
    for p in save_pair(draw, "02-accounts-currency-and-taxes", "currency-return"):
        preview(p)
