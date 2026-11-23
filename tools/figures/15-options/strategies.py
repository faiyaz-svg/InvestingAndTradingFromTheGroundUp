"""Payoff figures for lessons 9 to 14 of part 15: profit at expiry and six weeks before expiry.

Each strategy panel draws two curves per contract (100 shares): the profit at expiry (sharp corners) and the
profit with T = 0.125 years left, from Black-Scholes at each leg's chain volatility.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import numpy as np
from figstyle import save_pair, preview
import bs
import positions as P

S = np.linspace(38, 62, 241)
T_MID = 0.125


def panel(ax, c, pos, title, notes, calendar=False):
    if calendar:
        exp = np.array([P.calendar_at_near_expiry(pos, s) for s in S]) * 100
        now = np.array([_now(pos, s) for s in S]) * 100
        l1, l2 = "At the near leg's expiry", "Today"
    else:
        exp = np.array([pos.expiry(s) for s in S]) * 100
        now = np.array([pos.before(s, T_MID) for s in S]) * 100
        l1, l2 = "At expiry", "6 weeks before expiry"
    ax.axhline(0, color=c["muted"], lw=1)
    ax.axvline(P.S0, color=c["grid"], lw=1, ls="--")
    ax.plot(S, now, color=c["blue"], lw=1.6, ls="--", label=l2)
    ax.plot(S, exp, color=c["accent"], lw=2, label=l1)
    ax.set_title(title, color=c["fg"], fontsize=10)
    ax.set_xlabel("Stock A price (US$)")
    ax.legend(loc="best", fontsize=8)
    lo, hi = min(exp.min(), now.min()), max(exp.max(), now.max())
    pad = (hi - lo) * 0.12
    ax.set_ylim(lo - pad, hi + pad)
    for (x, y, txt) in notes:
        ax.annotate(txt, (x, y), color=c["fg"], fontsize=8)


def _now(pos, s):
    return sum(l.qty * l.value(s, l.T) for l in pos.legs) - pos.net


def mk(name, left, right, ylabel="Profit or loss per contract (US$)"):
    def draw(fig, axs, c):
        panel(axs[0], c, *left[:3], **(left[3] if len(left) > 3 else {}))
        panel(axs[1], c, *right[:3], **(right[3] if len(right) > 3 else {}))
        axs[0].set_ylabel(ylabel)
    return draw


def run():
    figs = {
        "covered-call-and-put": mk("a", (P.COVERED_CALL, "Covered call: 100 shares, short 52.50 call",
                                         [(38.5, -520, "Breakeven 48.10"), (53.5, 120, "Max profit US$440")]),
                                   (P.CASH_PUT, "Cash-secured put: short 47.50 put",
                                    [(38.5, -700, "Breakeven 45.70"), (50.5, 130, "Max profit US$180")])),
        "vertical-spreads": mk("b", (P.BULL_CALL, "Bull call spread: long 50, short 55",
                                      [(38.5, -170, "Max loss US$215"), (51.5, 230, "Max profit US$285")]),
                               (P.BULL_PUT, "Bull put spread: short 50, long 45",
                                [(38.5, -300, "Max loss US$370"), (50.5, 140, "Max profit US$130")])),
        "straddle-strangle": mk("c", (P.STRADDLE, "Long straddle at 50", [(38.5, 300, "Breakevens 43.80 and 56.20")]),
                                (P.STRANGLE, "Long strangle, 47.50 put and 52.50 call", [(38.5, 300, "Breakevens 43.40 and 56.60")])),
        "condor-butterfly": mk("d", (P.CONDOR, "Iron condor: 45/47.50 puts, 52.50/55 calls", [(38.5, -125, "Max loss US$130 each side")]),
                               (P.BUTTERFLY, "Call butterfly 47.50 / 50 / 52.50", [(38.5, 120, "Max profit US$190 at 50")])),
        "calendar-diagonal": mk("e", (P.CALENDAR, "Call calendar at 50", [(38.5, -97, "Max loss about US$80")], dict(calendar=True)),
                                (P.DIAGONAL, "Call diagonal: long Feb 50, short Jan 52.50", [(38.5, -197, "Max loss US$186")], dict(calendar=True))),
    }
    for name, fn in figs.items():
        for q in save_pair(fn, "15-options", name, width=9.0, height=3.8, axes=2):
            preview(q)


def draw_zero_dte(fig, axs, c):
    hours = np.linspace(6.5, 0.05, 200)
    T = hours / (24 * 365)
    for S0_, col, lab in ((50.0, c["accent"], "Stock at 50.00"), (50.5, c["up"], "Stock at 50.50"), (49.5, c["blue"], "Stock at 49.50")):
        axs[0].plot(hours, [bs.price(S0_, 50.0, t, 0.04, 0.30) * 100 for t in T], color=col, label=lab)
    axs[0].invert_xaxis()
    axs[0].set_xlabel("Hours left before expiry")
    axs[0].set_ylabel("Call value per contract (US$)")
    axs[0].set_title("50-strike call value on the last day", color=c["fg"], fontsize=10)
    axs[0].legend(fontsize=8)
    Sx = np.linspace(47, 53, 241)
    for h, col, lab in ((6.5, c["blue"], "6.5 hours left"), (0.5, c["accent"], "30 minutes left")):
        axs[1].plot(Sx, [bs.greeks(s, 50, h / (24 * 365), 0.04, 0.30)["gamma"] for s in Sx], color=col, label=lab)
    axs[1].set_xlabel("Stock A price (US$)")
    axs[1].set_ylabel("Gamma (delta change per US$1)")
    axs[1].set_title("Gamma of the 50 call", color=c["fg"], fontsize=10)
    axs[1].legend(fontsize=8)


if __name__ == "__main__":
    run()
    for q in save_pair(draw_zero_dte, "15-options", "zero-dte", width=9.0, height=3.6, axes=2):
        preview(q)
