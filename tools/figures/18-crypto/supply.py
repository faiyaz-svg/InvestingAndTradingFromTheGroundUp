"""Bitcoin issuance by halving period (lesson 1). Protocol rules, no market data."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview


def supply_after(epochs):
    sub = 50 * 10**8
    total = 0
    out = []
    for _ in range(epochs):
        total += 210_000 * sub
        out.append(total / 10**8 / 1e6)
        sub //= 2
    return out


def draw(fig, ax, c):
    sup = supply_after(6)
    x = list(range(1, 7))
    ax.bar(x, sup, color=c["accent"], width=0.65)
    ax.axhline(21, color=c["muted"], linestyle="--", linewidth=1)
    ax.text(0.45, 21.3, "21 million cap", color=c["muted"], fontsize=9, ha="left", va="bottom")
    subs = [50, 25, 12.5, 6.25, 3.125, 1.5625]
    for xi, s, v in zip(x, subs, sup):
        ax.text(xi, v + 0.3, f"{v:.2f}M", ha="center", fontsize=8, color=c["fg"])
        ax.text(xi, 1.0, f"{s:g}\nBTC", ha="center", fontsize=8, color=c["bg"])
    ax.set_xticks(x)
    ax.set_xticklabels([f"After\nperiod {i}" for i in x], fontsize=8)
    ax.set_ylabel("Bitcoin issued (millions)")
    ax.set_ylim(0, 23.5)


if __name__ == "__main__":
    for q in save_pair(draw, "18-crypto", "supply"):
        preview(q)
