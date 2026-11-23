"""Time decay of an at-the-money option and vega against the stock price (lesson 7)."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
def draw(fig, axs, c):
    days = np.linspace(90, 0.5, 200)
    axs[0].plot(days, [bs.price(50, 50, d / 365, 0.04, 0.30) * 100 for d in days], color=c["accent"], label="At-the-money call")
    axs[0].plot(days, [bs.price(50, 50, d / 365, 0.04, 0.30, kind="put") * 100 for d in days], color=c["blue"], label="At-the-money put")
    axs[0].invert_xaxis()
    axs[0].set_xlabel("Days left to expiry")
    axs[0].set_ylabel("Option value per contract (US$)")
    axs[0].set_title("Value, stock unchanged at 50", color=c["fg"], fontsize=10)
    axs[0].legend(loc="upper right", fontsize=9)
    S = np.linspace(38, 62, 241)
    for T, col, lab in ((0.25, c["accent"], "3 months left"), (0.08, c["blue"], "about 1 month left")):
        axs[1].plot(S, [bs.greeks(s, 50, T, 0.04, 0.30)["vega"] * 100 for s in S], color=col, label=lab)
    axs[1].set_xlabel("Stock A price (US$)")
    axs[1].set_ylabel("Vega per contract (US$ per vol point)")
    axs[1].set_title("Vega of a 50-strike option", color=c["fg"], fontsize=10)
    axs[1].legend(loc="upper left", fontsize=9)


if __name__ == "__main__":
    for q in save_pair(draw, "15-options", "theta-vega", width=9.0, height=3.6, axes=2):
        preview(q)
