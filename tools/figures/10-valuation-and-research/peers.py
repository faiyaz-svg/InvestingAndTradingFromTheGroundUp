"""EV/EBITDA of Northwind and four made-up peers (lesson 7)."""
import statistics
from _model import ns, save_pair, preview

PEERS = [("Stock B", 14.5), ("Stock C", 17.0), ("Stock D", 21.0), ("Stock E", 12.0)]


def draw(fig, ax, c):
    med = statistics.median(v for _, v in PEERS)
    names = [n for n, _ in PEERS] + ["Northwind"]
    vals = [v for _, v in PEERS] + [ns["EV"] / ns["EBITDA0"]]
    ax.bar(names, vals, color=[c["blue"]] * len(PEERS) + [c["accent"]], width=0.55)
    for k, v in enumerate(vals):
        ax.text(k, v + 0.3, f"{v:.1f}x", ha="center", fontsize=8.5)
    ax.axhline(med, color=c["muted"], linestyle="--", linewidth=1.2)
    ax.text(4.45, med + 0.4, f"Peer median {med:.2f}x", ha="right", fontsize=8.5, color=c["muted"])
    ax.set_ylabel("EV / EBITDA (times)")
    ax.set_ylim(0, 25)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "peers", width=6.0, height=3.6):
        preview(p)
