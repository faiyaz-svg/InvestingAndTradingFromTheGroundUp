"""Depth of a made-up order book for Stock A (lesson 4)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview

BIDS = [(49.98, 300), (49.97, 500), (49.96, 800), (49.95, 1200)]
ASKS = [(50.00, 400), (50.01, 600), (50.02, 700), (50.03, 1000)]


def draw(fig, ax, c):
    cum = 0
    xs, ys = [], []
    for p, s in BIDS:
        cum += s
        xs += [p + 0.005, p - 0.005]
        ys += [cum, cum]
    ax.fill_between(xs, ys, step=None, color=c["up"], alpha=0.35)
    ax.plot(xs, ys, color=c["up"])
    cum = 0
    xs, ys = [], []
    for p, s in ASKS:
        cum += s
        xs += [p - 0.005, p + 0.005]
        ys += [cum, cum]
    ax.fill_between(xs, ys, color=c["down"], alpha=0.35)
    ax.plot(xs, ys, color=c["down"])
    ax.set_xlabel("Price (US$)")
    ax.set_ylabel("Shares available up to this price")
    ax.text(49.965, 2500, "Bids (buyers)", color=c["up"], ha="center")
    ax.text(50.015, 2500, "Asks (sellers)", color=c["down"], ha="center")
    ax.annotate("Spread US$0.02", xy=(49.99, 900), ha="center", color=c["fg"], fontsize=9)
    ax.set_xlim(49.945, 50.035)
    ax.set_ylim(0, 3200)


if __name__ == "__main__":
    for p in save_pair(draw, "01-how-markets-work", "order-book-depth"):
        preview(p)
