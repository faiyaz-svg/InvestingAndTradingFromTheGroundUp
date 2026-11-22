"""DCF value per share against the discount rate, with the market price (lesson 6)."""
import numpy as np
from _model import ns, save_pair, preview


def draw(fig, ax, c):
    w = np.linspace(0.065, 0.13, 60)
    ax.plot(100 * w, [ns["dcf"](wacc=x)["ps"] for x in w], color=c["accent"])
    ax.axhline(ns["PRICE"], color=c["blue"], linestyle="--", linewidth=1.3)
    ax.text(12.9, ns["PRICE"] + 1.2, f"Market price US${ns['PRICE']:.2f}", ha="right", fontsize=8.5, color=c["blue"])
    iw = ns["implied_wacc"]()
    ax.plot([100 * iw], [ns["PRICE"]], "o", color=c["blue"])
    ax.annotate(f"Implied rate {100 * iw:.1f}%", (100 * iw, ns["PRICE"]), textcoords="offset points", xytext=(8, 10), fontsize=8.5)
    base = ns["dcf"]()["ps"]
    ax.plot([9.1], [base], "o", color=c["up"])
    ax.annotate(f"Base case, 9.1%: US${base:.2f}", (9.1, base), textcoords="offset points", xytext=(8, -14), fontsize=8.5)
    ax.set_xlabel("Discount rate (%)")
    ax.set_ylabel("Value per share (US$)")


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "value-vs-rate", width=6.0, height=3.6):
        preview(p)
