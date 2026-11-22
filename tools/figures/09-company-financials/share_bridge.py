"""Northwind FY2025 share count: start, issued, bought back, end, and the diluted count (lesson 9)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import save_pair, preview
from _model import ns

g = ns


def draw(fig, ax, c):
    vals = [("Start of\nFY2025", g["SH_START"], "total"), ("Issued", g["SH_ISSUED"], "delta"),
            ("Bought\nback", -g["SH_BOUGHT"], "delta"), ("End of\nFY2025", g["SH_END"], "total"),
            ("Weighted\nbasic", g["W_BASIC"], "total"), ("Option\nshares (net)", g["OPT_NET"], "delta"),
            ("RSUs", g["RSU"], "delta"), ("Weighted\ndiluted", g["W_DIL"], "total")]
    run = 0
    for k, (name, v, kind) in enumerate(vals):
        if kind == "total":
            ax.bar(k, v, color=c["blue"], width=0.6)
            run = v
            ax.text(k, v + 0.15, f"{v:.1f}", ha="center", fontsize=8.5)
        else:
            ax.bar(k, v, bottom=run, color=c["up"] if v > 0 else c["down"], width=0.6)
            ax.text(k, max(run, run + v) + 0.15, f"{v:+.1f}", ha="center", fontsize=8.5)
            run += v
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels([v[0] for v in vals], fontsize=7.8)
    ax.set_ylim(94, 104.5)
    ax.set_ylabel("Shares (millions)")
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)
    ax.text(0.02, 0.96, "Vertical axis starts at 94", transform=ax.transAxes, fontsize=8, color=c["muted"], va="top")


if __name__ == "__main__":
    for p in save_pair(draw, "09-company-financials", "share-bridge", width=6.6, height=3.6):
        preview(p)
