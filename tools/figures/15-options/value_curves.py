"""Call value before expiry against the stock price (lesson 4). Strike 50, 4%, volatility 30%."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
def draw(fig, ax, c):
    S = np.linspace(35, 65, 301)
    ax.plot(S, np.maximum(S - 50, 0), color=c["muted"], label="At expiry")
    ax.plot(S, [bs.price(s, 50, 0.05, 0.04, 0.30) for s in S], color=c["blue"], label="T = 0.05 years (about 18 days)")
    ax.plot(S, [bs.price(s, 50, 0.25, 0.04, 0.30) for s in S], color=c["accent"], label="T = 0.25 years (about 3 months)")
    ax.plot([50], [bs.price(50, 50, 0.25, 0.04, 0.30)], "o", color=c["accent"])
    ax.annotate("3.23 at the money,\n3 months left", (50, 3.23), (38, 8), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    ax.set_xlabel("Stock A price now (US$)")
    ax.set_ylabel("Call value per share (US$)")
    ax.legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "15-options", "value-before-expiry"):
        preview(q)
