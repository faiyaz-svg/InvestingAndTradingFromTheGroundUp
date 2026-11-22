"""Present value of the forecast cash flows and of the terminal value (lesson 5)."""
from _model import ns, save_pair, preview

CASES = [
    ("Gordon growth\n(9.1%, 3.0%)", ns["dcf"]()),
    ("Exit multiple\n(13x EBITDA)", ns["dcf"](exit_mult=ns["EXIT_MULT"])),
    ("Gordon growth\n(10.1%, 2.0%)", ns["dcf"](wacc=0.101, tg=0.02)),
]


def draw(fig, ax, c):
    for k, (name, d) in enumerate(CASES):
        ax.bar(k, d["pv_fcf"], color=c["blue"], width=0.55, label="Years 1 to 5" if k == 0 else None)
        ax.bar(k, d["pv_tv"], bottom=d["pv_fcf"], color=c["accent"], width=0.55, label="Terminal value" if k == 0 else None)
        ax.text(k, d["pv_fcf"] / 2, f"{d['pv_fcf']:,.0f}", ha="center", va="center", fontsize=8.5, color="#ffffff")
        ax.text(k, d["pv_fcf"] + d["pv_tv"] / 2, f"{100 * d['tv_share']:.0f}%", ha="center", va="center", fontsize=9, color="#000000")
        ax.text(k, d["ev"] + 80, f"EV {d['ev']:,.0f}", ha="center", va="bottom", fontsize=8.5)
    ax.set_xticks(range(len(CASES)))
    ax.set_xticklabels([n for n, _ in CASES], fontsize=8.5)
    ax.set_ylabel("Present value, US$ millions")
    ax.set_ylim(0, 6600)
    ax.legend(loc="upper left", fontsize=8.5)
    ax.set_axisbelow(True)
    ax.grid(axis="x", visible=False)


if __name__ == "__main__":
    for p in save_pair(draw, "10-valuation-and-research", "tv-share", width=6.4, height=3.8):
        preview(p)
