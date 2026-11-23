"""A bond portfolio's loss from a rise in yields, against a bank's equity (lesson 6). Made-up balance sheet."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

DUR, SEC, EQUITY = 6.2, 60.0, 6.0  # years, securities per 100 of assets, equity per 100 of assets


def draw(fig, ax, c):
    dy = np.linspace(0, 4, 81)
    loss = SEC * DUR * dy / 100
    ax.plot(dy, loss, color=c["down"], linewidth=2, label="Loss on US\\$60 of securities, duration 6.2 years")
    ax.axhline(EQUITY, color=c["accent"], linewidth=1.5, linestyle="--")
    ax.text(0.05, EQUITY + 0.3, "Equity: US\\$6 per US\\$100 of assets", color=c["accent"], fontsize=9)
    x0 = EQUITY / (SEC * DUR / 100)
    ax.plot([x0], [EQUITY], "o", color=c["accent"])
    ax.text(x0 + 0.08, EQUITY - 1.0, f"Equity gone at +{x0:.2f} points", color=c["accent"], fontsize=9)
    ax.set_xlabel("Rise in yields (percentage points)")
    ax.set_ylabel("Loss (US\\$ per US\\$100 of assets)")
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 16)
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "21-crashes-scams-and-case-studies", "bank-duration", width=6.0, height=3.6):
        preview(p)
