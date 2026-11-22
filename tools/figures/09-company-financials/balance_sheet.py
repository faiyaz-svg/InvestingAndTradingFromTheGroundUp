"""Northwind balance sheets: assets equal liabilities plus equity (lesson 3)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from figstyle import save_pair, preview
from _model import ns

BS = ns["BS"]
YEARS = ["FY2024", "FY2025"]


def draw(fig, ax, c):
    left = {"Assets": [("Cash", "cash"), ("Receivables", "ar"), ("Inventory", "inv"), ("Prepaid", "prepaid"),
                       ("PP&E", "ppe"), ("Intangibles", "intang"), ("Goodwill", "goodwill")],
            "Liabilities and equity": [("Payables", None), ("Debt", "debt"), ("Equity", "equity")]}
    cols = [c["accent"], c["blue"], c["teal"], c["fg"], c["orange"], c["up"], c["muted"]]
    for xi, y in enumerate(YEARS):
        b = BS[y]
        for side, off in (("Assets", -0.2), ("Liabilities and equity", 0.2)):
            bottom = 0
            for k, (name, key) in enumerate(left[side]):
                if side == "Assets":
                    v = b[key]
                else:
                    v = {"Payables": b["ap"] + b["accrued"], "Debt": b["debt"], "Equity": b["equity"]}[name]
                col = cols[k] if side == "Assets" else [c["down"], c["orange"], c["blue"]][k]
                ax.bar(xi + off, v, bottom=bottom, width=0.34, color=col, edgecolor=c["bg"], linewidth=1.2)
                if v >= 55:
                    ax.text(xi + off, bottom + v / 2, f"{name} {v:,.0f}", ha="center", va="center", fontsize=7.2,
                            color="#0e1116")
                bottom += v
            ax.text(xi + off, bottom + 15, f"{bottom:,.0f}", ha="center", fontsize=8.5)
    ax.set_xticks([0, 1])
    ax.set_xticklabels([f"{y}\nassets | liabilities + equity" for y in YEARS], fontsize=8.5)
    ax.set_ylabel("US$ millions")
    ax.set_ylim(0, 1200)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "09-company-financials", "balance-sheet", width=6.6, height=4.0):
        preview(p)
