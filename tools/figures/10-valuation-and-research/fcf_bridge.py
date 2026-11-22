"""Northwind FY2025: unlevered free cash flow and levered free cash flow (lesson 3)."""
from _model import ns, save_pair, preview

t = ns["TAX"]
ebit, da, cx = ns["EBIT0"], ns["DA0"], ns["CF25"]["capex"]
dw = ns["CF25"]["d_wc"]
nopat = ebit * (1 - t)
ufcf = nopat + da + cx + dw
intr = ns["IS25"]["interest"] * (1 - t)
sbc = ns["IS25"]["sbc"]
STEPS = [
    ("EBIT", ebit, "total"),
    ("Tax on\nEBIT", -ebit * t, "delta"),
    ("D&A", da, "delta"),
    ("Capex", cx, "delta"),
    ("Working\ncapital", dw, "delta"),
    ("Unlevered\nFCF", ufcf, "total"),
    ("After-tax\ninterest", -intr, "delta"),
    ("Stock pay\nadded back", sbc, "delta"),
    ("Levered\nFCF", ufcf - intr + sbc, "total"),
]


def fmt(v, sign=False):
    s = f"{v:+,.2f}" if sign else f"{v:,.2f}"
    return s[:-3] if s.endswith(".00") else s


def draw(fig, ax, c):
    run = 0
    for k, (name, v, kind) in enumerate(STEPS):
        if kind == "total":
            ax.bar(k, v, color=c["blue"], width=0.62)
            run = v
            ax.text(k, v + 5, fmt(v), ha="center", va="bottom", fontsize=8)
        else:
            col = c["up"] if v >= 0 else c["down"]
            ax.bar(k, v, bottom=run, color=col, width=0.62)
            ax.text(k, max(run, run + v) + 5, fmt(v, True), ha="center", va="bottom", fontsize=8)
            run += v
    ax.set_xticks(range(len(STEPS)))
    ax.set_xticklabels([s[0] for s in STEPS], fontsize=7.8)
    ax.set_ylabel("US$ millions, FY2025")
    ax.set_ylim(0, 290)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "fcf-bridge", width=7.0, height=3.8):
        preview(p)
