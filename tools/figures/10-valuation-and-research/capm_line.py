"""Cost of equity against beta (lesson 4)."""
import numpy as np
from _model import ns, save_pair, preview

rf, erp = ns["RF"], ns["ERP"]


def draw(fig, ax, c):
    b = np.linspace(0, 2, 50)
    ax.plot(b, 100 * (rf + b * erp), color=c["accent"])
    for beta, label in [(0.8, "Beta 0.8"), (1.0, "Northwind, beta 1.0"), (1.4, "Beta 1.4")]:
        y = 100 * (rf + beta * erp)
        ax.plot([beta], [y], "o", color=c["blue"])
        ax.annotate(f"{label}: {y:.2f}%", (beta, y), textcoords="offset points", xytext=(6, -14), fontsize=8.5)
    ax.axhline(100 * rf, color=c["muted"], linewidth=1, linestyle="--")
    ax.text(1.98, 100 * rf + 0.12, f"Risk-free rate {100 * rf:.2f}%", ha="right", fontsize=8.5, color=c["muted"])
    ax.set_xlabel("Beta")
    ax.set_ylabel("Cost of equity (%)")
    ax.set_xlim(0, 2)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "capm-line", width=6.0, height=3.6):
        preview(p)
