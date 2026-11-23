"""Delta and gamma of a call against the stock price (lesson 6). Strike 50, 4%, volatility 30%."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
def draw(fig, axs, c):
    S = np.linspace(38, 62, 241)
    for T, col, lab in ((0.25, c["accent"], "3 months left"), (0.03, c["blue"], "11 days left")):
        axs[0].plot(S, [bs.greeks(s, 50, T, 0.04, 0.30)["delta"] for s in S], color=col, label=lab)
        axs[1].plot(S, [bs.greeks(s, 50, T, 0.04, 0.30)["gamma"] for s in S], color=col, label=lab)
    axs[0].set_title("Delta of a 50-strike call", color=c["fg"], fontsize=10)
    axs[1].set_title("Gamma of a 50-strike call", color=c["fg"], fontsize=10)
    axs[0].set_ylabel("Delta")
    axs[1].set_ylabel("Gamma (delta change per US$1)")
    for a in axs:
        a.set_xlabel("Stock A price (US$)")
        a.axvline(50, color=c["grid"], lw=1, ls="--")
    axs[0].legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "15-options", "delta-gamma", width=9.0, height=3.6, axes=2):
        preview(q)
