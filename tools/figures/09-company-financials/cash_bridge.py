"""Northwind FY2025: from net income to free cash flow (lesson 4)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import save_pair, preview
from _model import ns

cf = ns["CF"]
STEPS = [
    ("Net income", cf["ni"], "total"),
    ("Depreciation and amortization", cf["da"], "delta"),
    ("Stock-based pay", cf["sbc"], "delta"),
    ("Working capital", cf["d_wc"], "delta"),
    ("Operating cash flow", cf["cfo"], "total"),
    ("Capital spending", cf["capex"], "delta"),
    ("Free cash flow", cf["fcf"], "total"),
]


def draw(fig, ax, c):
    run = 0
    for k, (name, v, kind) in enumerate(STEPS):
        if kind == "total":
            ax.bar(k, v, color=c["blue"], width=0.62)
            run = v
            ax.text(k, v + 6, f"{v:,.0f}", ha="center", va="bottom", fontsize=8.5)
        else:
            col = c["up"] if v >= 0 else c["down"]
            ax.bar(k, v, bottom=run, color=col, width=0.62)
            top = max(run, run + v)
            ax.text(k, top + 6, f"{v:+,.0f}", ha="center", va="bottom", fontsize=8.5)
            run += v
    labels = ["Net\nincome", "Depreciation,\namortization", "Stock-based\npay", "Working\ncapital",
              "Operating\ncash flow", "Capital\nspending", "Free cash\nflow"]
    ax.set_xticks(range(len(STEPS)))
    ax.set_xticklabels(labels, fontsize=8.2)
    ax.set_ylabel("US$ millions, FY2025")
    ax.set_ylim(0, 270)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "09-company-financials", "cash-bridge", width=6.6, height=3.8):
        preview(p)
