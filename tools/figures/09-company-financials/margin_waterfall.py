"""Northwind FY2025: revenue down to net income (lesson 2)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import save_pair, preview
from _model import ns

i = ns["IS"]["FY2025"]
STEPS = [
    ("Revenue", i["rev"], "total"),
    ("Cost of goods sold", -i["cogs"], "delta"),
    ("Gross profit", i["gp"], "total"),
    ("Operating expenses", -i["opex"], "delta"),
    ("Operating income", i["ebit"], "total"),
    ("Interest", -i["interest"], "delta"),
    ("Income taxes", -i["tax"], "delta"),
    ("Net income", i["ni"], "total"),
]


def draw(fig, ax, c):
    run = 0
    for k, (name, v, kind) in enumerate(STEPS):
        if kind == "total":
            ax.bar(k, v, color=c["blue"], width=0.62)
            run = v
            ax.text(k, v + 18, f"{v:,.0f}\n{100 * v / i['rev']:.1f}%", ha="center", va="bottom", fontsize=8.5)
        else:
            ax.bar(k, v, bottom=run, color=c["down"], width=0.62)
            ax.text(k, run + 18, f"{v:,.0f}", ha="center", va="bottom", fontsize=8.5)
            run += v
    ax.set_xticks(range(len(STEPS)))
    ax.set_xticklabels([s[0].replace(" ", "\n", 1) if len(s[0]) > 10 else s[0] for s in STEPS], fontsize=8.5)
    ax.set_ylabel("US$ millions, FY2025")
    ax.set_ylim(0, 1400)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "09-company-financials", "margin-waterfall", width=6.6, height=3.8):
        preview(p)
