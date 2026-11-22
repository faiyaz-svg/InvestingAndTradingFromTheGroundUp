"""Northwind: from market cap to enterprise value (lesson 2)."""
from _model import ns, save_pair, preview

STEPS = [
    ("Shares\noutstanding", ns["MCAP"], "total"),
    ("Options and\nstock units", ns["EQ_DIL"] - ns["MCAP"], "delta"),
    ("Diluted\nequity value", ns["EQ_DIL"], "total"),
    ("Debt", ns["DEBT"], "delta"),
    ("Cash", -ns["CASH"], "delta"),
    ("Enterprise\nvalue", ns["EV"], "total"),
]


def draw(fig, ax, c):
    run = 0
    for k, (name, v, kind) in enumerate(STEPS):
        if kind == "total":
            ax.bar(k, v, color=c["blue"], width=0.62)
            run = v
            ax.text(k, v + 40, f"{v:,.0f}", ha="center", va="bottom", fontsize=8.5)
        else:
            col = c["up"] if v >= 0 else c["down"]
            ax.bar(k, v, bottom=run, color=col, width=0.62)
            ax.text(k, max(run, run + v) + 40, f"{v:+,.0f}", ha="center", va="bottom", fontsize=8.5)
            run += v
    ax.set_xticks(range(len(STEPS)))
    ax.set_xticklabels([s[0] for s in STEPS], fontsize=8.2)
    ax.set_ylabel("US$ millions (axis starts at 4,500)")
    ax.set_ylim(4500, 5500)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "ev-bridge", width=6.6, height=3.8):
        preview(p)
