"""Three funding payments paid by a long perpetual position (lesson 6). Made-up rates."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

NOTIONAL = 22_000
RATES = [0.0001, 0.0003, 0.0010]
LABELS = ["00:00 UTC\nrate 0.01%", "08:00 UTC\nrate 0.03%", "16:00 UTC\nrate 0.10%"]


def draw(fig, ax, c):
    pay = [NOTIONAL * r for r in RATES]
    ax.bar(range(3), pay, color=c["down"], width=0.55)
    for i, p in enumerate(pay):
        ax.text(i, p + 0.6, f"US${p:.2f}", ha="center", fontsize=9, color=c["fg"])
    ax.set_xticks(range(3))
    ax.set_xticklabels(LABELS, fontsize=9)
    ax.set_ylabel("Funding paid by the long (US$)")
    ax.set_ylim(0, 27)
    ax.text(2.45, 25, f"Total for the day: US${sum(pay):.2f}", ha="right", fontsize=9, color=c["muted"])


if __name__ == "__main__":
    for q in save_pair(draw, "18-crypto", "funding"):
        preview(q)
