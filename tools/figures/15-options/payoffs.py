"""Profit at expiry of long and short calls and puts (lesson 2). Strike 50, call premium 3.25, put premium 2.75."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
K, CP, PP = 50.0, 3.25, 2.75
S = np.linspace(35, 65, 301)


def _setup(ax, c, title):
    ax.axhline(0, color=c["muted"], lw=1)
    ax.set_title(title, color=c["fg"], fontsize=10)
    ax.set_xlabel("Stock A price at expiry (US$)")
    ax.axvline(K, color=c["grid"], lw=1, ls="--")


def draw_calls(fig, axs, c):
    lc = (np.maximum(S - K, 0) - CP) * 100
    axs[0].plot(S, lc, color=c["up"]); _setup(axs[0], c, "Long call, strike 50, premium 3.25")
    axs[1].plot(S, -lc, color=c["down"]); _setup(axs[1], c, "Short call, strike 50, premium 3.25")
    axs[0].set_ylabel("Profit or loss per contract (US$)")
    axs[0].plot([K + CP], [0], "o", color=c["accent"]); axs[0].annotate("Breakeven 53.25", (K + CP, 0), (54.5, -250), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    axs[0].annotate("Max loss US$325", (36, -325), (36, -150), color=c["fg"], fontsize=9)
    axs[1].plot([K + CP], [0], "o", color=c["accent"]); axs[1].annotate("Max gain US$325", (36, 325), (36, 150), color=c["fg"], fontsize=9)
    axs[1].annotate("Loss has no limit", (64, -1100), (36, -600), color=c["fg"], fontsize=9)


def draw_puts(fig, axs, c):
    lp = (np.maximum(K - S, 0) - PP) * 100
    axs[0].plot(S, lp, color=c["up"]); _setup(axs[0], c, "Long put, strike 50, premium 2.75")
    axs[1].plot(S, -lp, color=c["down"]); _setup(axs[1], c, "Short put, strike 50, premium 2.75")
    axs[0].set_ylabel("Profit or loss per contract (US$)")
    axs[0].plot([K - PP], [0], "o", color=c["accent"]); axs[0].annotate("Breakeven 47.25", (K - PP, 0), (51, 700), color=c["fg"], fontsize=9, arrowprops=dict(arrowstyle="->", color=c["muted"]))
    axs[0].annotate("Max loss US$275", (56, -275), (55, -120), color=c["fg"], fontsize=9)
    axs[1].plot([K - PP], [0], "o", color=c["accent"]); axs[1].annotate("Max gain US$275", (56, 275), (55, 100), color=c["fg"], fontsize=9)
    axs[1].annotate("Loss up to US$4,725", (36, -1200), (50.5, -1000), color=c["fg"], fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw_calls, "15-options", "calls-payoff", width=9.0, height=3.6, axes=2):
        preview(q)
    for q in save_pair(draw_puts, "15-options", "puts-payoff", width=9.0, height=3.6, axes=2):
        preview(q)
