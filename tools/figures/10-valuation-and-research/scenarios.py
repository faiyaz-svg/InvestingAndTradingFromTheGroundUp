"""Bear, base and bull value per share against the market price (lesson 9)."""
from _model import ns, save_pair, preview


def draw(fig, ax, c):
    vals = [ns["dcf"](s)["ps"] for s in (ns["BEAR"], ns["BASE"], ns["BULL"])]
    ax.bar(["Bear", "Base", "Bull"], vals, color=[c["down"], c["blue"], c["up"]], width=0.5)
    for k, v in enumerate(vals):
        ax.text(k, v + 0.8, f"US${v:.2f}", ha="center", fontsize=9)
    ax.axhline(ns["PRICE"], color=c["accent"], linestyle="--", linewidth=1.3)
    ax.text(2.45, ns["PRICE"] + 1, f"Market price US${ns['PRICE']:.2f}", ha="right", fontsize=8.5, color=c["accent"])
    ax.set_ylabel("DCF value per share (US$)")
    ax.set_ylim(0, 64)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "scenarios", width=6.0, height=3.6):
        preview(p)
