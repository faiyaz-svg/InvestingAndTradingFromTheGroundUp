"""Number checks for part 15, Options. Lessons 1 to 8 (the second writer appends lessons 9 to 15)."""
import datetime
import math
import sys

import numpy as np
import pandas as pd

from _lib import ROOT, lesson, has, usd

F = "15-options"
sys.path.insert(0, str(ROOT / "tools" / "figures" / F))
import bs  # noqa: E402
import chain  # noqa: E402


def close(a, b, tol=1e-9):
    assert abs(a - b) <= tol, (a, b)


def r4(x):
    return f"{x:.4f}"


def r2(x):
    return f"{x:.2f}"


# Base case used in lessons 4 to 8
S0, K0, T0, R0, V0 = 50.0, 50.0, 0.25, 0.04, 0.30
C0 = bs.price(S0, K0, T0, R0, V0)
P0 = bs.price(S0, K0, T0, R0, V0, kind="put")

# ---------------------------------------------------------------- lesson 1
t = lesson(F, 1)
assert datetime.date(2027, 1, 15).weekday() == 4 and 15 <= 15 <= 21  # a Friday, a third Friday
assert 3.25 * 100 == 325
cost3 = 1.40 * 100 * 3
assert cost3 == 420
shares_cost = 50 * 100
close((58 - 50) * 100, 800)
close(800 - 325, 475)
assert f"{800 / 5000 * 100:.1f}" == "16.0" and f"{475 / 325 * 100:.1f}" == "146.2"
close(50 + 3.25, 53.25)
close((50 - 44) * 100 - 275, 325)
close((55 - 50) * 100 - 325, 175)
has(t, usd(325, 0), usd(5000, 0), usd(800, 0), usd(475, 0), "16.0%", "146.2%", usd(53.25),
    usd(420, 0), usd(600, 0), usd(275, 0), usd(325, 0), usd(500, 0), usd(175, 0), "January 15, 2027")

# ---------------------------------------------------------------- lesson 2
t = lesson(F, 2)


def prof(S, K, p, kind, side):
    pay = max(S - K, 0) if kind == "call" else max(K - S, 0)
    return (pay - p if side == "long" else p - pay) * 100


rows = {40: (-325, 325, 725, -725), 45: (-325, 325, 225, -225), 47.25: (-325, 325, 0, 0), 50: (-325, 325, -275, 275),
        53.25: (0, 0, -275, 275), 55: (175, -175, -275, 275), 60: (675, -675, -275, 275)}
for s, (lc, sc, lp, sp) in rows.items():
    close(prof(s, 50, 3.25, "call", "long"), lc)
    close(prof(s, 50, 3.25, "call", "short"), sc)
    close(prof(s, 50, 2.75, "put", "long"), lp)
    close(prof(s, 50, 2.75, "put", "short"), sp)
close(50 + 3.25, 53.25)
close(50 - 2.75, 47.25)
close((50 - 0) * 100 - 275, 4725)
close(prof(40, 50, 2.75, "put", "short"), -725)
has(t, usd(325, 0), usd(275, 0), usd(725, 0), usd(225, 0), usd(675, 0), usd(175, 0), usd(500, 0), usd(1000, 0),
    usd(53.25), usd(47.25), usd(4725, 0))
# exercises
close(60 - 4.10, 55.90)
close((60 - 52) * 100 - 410, 390)
close(130 - 200, -70)
close(2 * 100 + 0 * 1, 200)
close(325 + 325, 650)
close(50 + 6.50, 56.50)
close((50 - 46) * 100 - 275, 125)
has(t, usd(55.90), usd(800, 0), usd(390, 0), usd(130, 0), usd(200, 0), "-US$70", usd(650, 0), usd(56.50), usd(125, 0), usd(400, 0))
# the In code snippet agrees
assert prof(55, 50, 3.25, "call", "long") == 175

# ---------------------------------------------------------------- lesson 3
t = lesson(F, 3)
calls, puts = chain.rows("call"), chain.rows("put")
ivs_c = [f"{r['iv'] * 100:.1f}%" for r in calls]
ivs_p = [f"{r['iv'] * 100:.1f}%" for r in puts]
assert ivs_c == ["36.1%", "33.0%", "30.6%", "29.0%", "28.6%"], ivs_c
assert ivs_p == ["36.1%", "32.9%", "30.6%", "29.0%", "28.6%"], ivs_p
assert [f"{r['delta']:.2f}" for r in calls] == ["0.77", "0.68", "0.57", "0.43", "0.31"]
assert [f"{r['delta']:.2f}" for r in puts] == ["-0.23", "-0.32", "-0.43", "-0.57", "-0.69"]
for r in calls + puts:
    assert r["bid"] < r["ask"]
for r_ in calls:
    has(t, f"| {r_['K']:.2f} | {r_['bid']:.2f} | {r_['ask']:.2f} | {r_['last']:.2f} | {r_['vol']:,} | {r_['oi']:,} | {r_['iv'] * 100:.1f}% | {r_['delta']:.2f} |")
for r_ in puts:
    has(t, f"| {r_['K']:.2f} | {r_['bid']:.2f} | {r_['ask']:.2f} | {r_['last']:.2f} | {r_['vol']:,} | {r_['oi']:,} | {r_['iv'] * 100:.1f}% | {r_['delta']:.2f} |")
close(3.45 * 100, 345)
close((3.35 + 3.45) / 2, 3.40)
assert f"{0.10 / 3.40 * 100:.1f}" == "2.9" and f"{0.05 / 1.325 * 100:.1f}" == "3.8"
mid = {"c47.5": 5.025, "c50": 3.40, "c52.5": 2.15, "p52.5": 3.925}
for got, want in zip([r_["mid"] for r_ in calls][1:4] + [puts[3]["mid"]], [5.025, 3.40, 2.15, 3.925]):
    close(got, want, 1e-9)
close(50.20 - 47.50, 2.70)
close(5.025 - 2.70, 2.325)
close(50.20 - 50, 0.20)
close(3.40 - 0.20, 3.20)
close(52.50 - 50.20, 2.30)
close(3.925 - 2.30, 1.625)
has(t, "2.325", "3.20", "1.625", "5.025", "3.925", usd(345, 0), "2.9%", "3.8%", "1.325")
close((3.45 - 3.35) * 100 * 5, 50)
has(t, usd(50, 0), "STKA 270219C00050000", "STKA 270219P00047500", "US$47.50", "US$1.63")
assert datetime.date(2027, 2, 19).weekday() == 4 and 15 <= 19 <= 21
assert 47500 / 1000 == 47.5 and 50000 / 1000 == 50
# time-value figure uses the 30% model; the chain splits above come from midpoints

# ---------------------------------------------------------------- lesson 4
t = lesson(F, 4)
close(C0, 3.2297415888278955, 1e-12)
assert r2(C0) == "3.23" and r2(P0) == "2.73"
rows4 = [
    ((51, 50, .25, .04, .30, 0), "3.81", "2.31"),
    ((50, 51, .25, .04, .30, 0), "2.76", "3.26"),
    ((50, 50, .30, .04, .30, 0), "3.56", "2.96"),
    ((50, 50, .25, .04, .35, 0), "3.72", "3.23"),
    ((50, 50, .25, .05, .30, 0), "3.29", "2.67"),
    ((50, 50, .25, .04, .30, .02), "3.09", "2.84"),
]
for a, c_, p_ in rows4:
    assert r2(bs.price(*a)) == c_, (a, bs.price(*a))
    assert r2(bs.price(*a, kind="put")) == p_, (a, bs.price(*a, kind="put"))
    has(t, f"| {c_} | {p_} |")
has(t, "| Base case | 3.23 | 2.73 |")
# one-step tree
v, p, d = bs.one_step_tree(50, 50, 1.1, 0.9, 0.04, 0.25)
assert r2(v) == "2.72" and f"{p:.4f}" == "0.5503" and abs(d - 0.5) < 1e-9
loan_pv = 22.50 * math.exp(-0.04 * 0.25)
assert r2(loan_pv) == "22.28" and r2(25 - loan_pv) == "2.72"
close(50 * 1.1, 55)
assert r2(0.5 * 55 - 22.50) == "5.00" and 0.5 * 45 - 22.50 == 0
assert f"{math.exp(-0.01):.4f}" == "0.9900"
has(t, "US$22.28", "US$2.72", "0.5503", "0.9900", "US$22.50")
# Black-Scholes by hand
d1, d2 = bs.d1_d2(50, 50, .25, .04, .30)
assert f"{d1:.4f}" == "0.1417" and f"{d2:.4f}" == "-0.0083"
assert f"{bs.norm_cdf(d1):.4f}" == "0.5563" and f"{bs.norm_cdf(d2):.4f}" == "0.4967"
Ke = 50 * math.exp(-0.01)
assert r2(Ke) == "49.50" and f"{bs.norm_cdf(-d2):.4f}" == "0.5033" and f"{bs.norm_cdf(-d1):.4f}" == "0.4437"
assert r2(50 * bs.norm_cdf(d1)) == "27.82" and r2(Ke * bs.norm_cdf(d2)) == "24.59"
assert r2(Ke * bs.norm_cdf(-d2)) == "24.92" and r2(50 * bs.norm_cdf(-d1)) == "22.18"
assert f"{0.02125 / 0.15:.4f}" == "0.1417"
has(t, "0.1417", "-0.0083", "0.5563", "0.4967", "49.50", "27.82", "24.59", "24.92", "22.18", "3.2297", "2.7322", "0.0083")
close(bs.price(51, 50, .25, .04, .30) - C0, 0.5823, 5e-5)
has(t, "0.5823", "US$58.23", "3.81 - 3.23 = 0.58")
vp = bs.price(50, 50, .25, 0, .30, kind="call")
assert 0.5 * 10 == 5.0 and (1 - 0.8) / (1.2 - 0.8) == 0.5
has(t, "US$5.00", "p = (1 - 0.8) / (1.2 - 0.8) = 0.5", "0.5 x 40 = US$20", "3.72", "3.23", "3.09", "2.84")
for k in ("Black, F. and Scholes, M. (1973)", "Merton, R. C. (1973)", "Cox, J. C., Ross, S. A. and Rubinstein, M. (1979)"):
    has(t, k)

# ---------------------------------------------------------------- lesson 5
t = lesson(F, 5)
close(C0 - P0, 50 - 50 * math.exp(-0.01), 1e-12)
assert r4(C0 - P0) == "0.4975" and r4(50 - Ke) == "0.4975"
C2, P2 = bs.price(50, 50, .25, .04, .30, .02), bs.price(50, 50, .25, .04, .30, .02, "put")
assert r4(C2) == "3.0926" and r4(P2) == "2.8445" and r4(C2 - P2) == "0.2481"
assert r4(50 * math.exp(-0.02 * 0.25)) == "49.7506" and r4(Ke) == "49.5025"
close(C2 - P2, 50 * math.exp(-0.005) - Ke, 1e-12)
assert r2(3.60 - 2.70) == "0.90" and r2(50 + 2.70 - 3.60) == "49.10"
gain = Ke - 49.10
assert r4(gain) == "0.4025" and r2(gain * 100) == "40.25"
c50, p50 = 3.40, 2.70
assert r2(c50 - p50) == "0.70" and r4(50.20 - Ke) == "0.6975"
assert r2(50 + 0.4975) == "50.50"
# synthetic line crosses zero at strike + net cost
close(50 + (C0 - P0), 50.4975083125, 1e-9)
has(t, "0.4975", "0.4975", "3.0926", "2.8445", "0.2481", "49.7506", "49.5025", "0.90", "US$49.10", "0.4025", usd(40.25), "0.6975", "0.70", "US$50.50")
# exercises
par1 = 100 - 100 * math.exp(-0.5 * 0.04)
assert r4(par1) == "1.9801" and r2(7.50 - par1) == "5.52" and r4(100 * math.exp(-0.02)) == "98.0199"
close(3.45 - 2.65, 0.80)
close(50 + 0.80, 50.80)
assert r2(3.10 - 3.00) == "0.10" and r2(50 + 3.00 - 3.10) == "49.90"
g3 = 49.90 - Ke
assert r4(g3) == "0.3975" and r2(g3 * 100) == "39.75"
has(t, "1.9801", "98.0199", "US$5.52", "US$50.80", "49.90", "0.3975", usd(39.75), "0.80")
# the In code function
def parity_gap(call, put, S, K, T, r, q=0.0):
    return (call - put) - (S * math.exp(-q * T) - K * math.exp(-r * T))
assert r4(parity_gap(3.60, 2.70, 50, 50, .25, .04)) == "0.4025"
assert r4(parity_gap(3.40, 2.70, 50.20, 50, .25, .04)) == "0.0025"
# American bounds for Stock A: 0 <= C - P <= 0.4975
assert 0 <= C0 - P0 <= 50 - Ke + 1e-12
# chain follows parity at three strikes
for (K, c_, p_) in ((47.5, 5.025, 1.85), (50, 3.40, 2.70), (55, 1.325, 5.575)):
    assert abs((c_ - p_) - (50.20 - K * math.exp(-0.01))) < 0.01, K

# ---------------------------------------------------------------- lesson 6
t = lesson(F, 6)
g = bs.greeks(50, 50, .25, .04, .30)
gp = bs.greeks(50, 50, .25, .04, .30, kind="put")
assert r4(g["delta"]) == "0.5563" and r4(gp["delta"]) == "-0.4437" and r4(g["gamma"]) == "0.0527"
close(g["delta"] - 1, gp["delta"], 1e-12)
assert r2(g["delta"] * 100) == "55.63"
has(t, "0.5563", "-0.4437", "0.0527", "55.63", "0.5563 - 1 = -0.4437")
dl = {40: ("0.0892", "-0.9108"), 45: ("0.2875", "-0.7125"), 50: ("0.5563", "-0.4437"), 55: ("0.7814", "-0.2186"), 60: ("0.9126", "-0.0874")}
for s, (cd, pd_) in dl.items():
    assert r4(bs.greeks(s, 50, .25, .04, .30)["delta"]) == cd, s
    assert r4(bs.greeks(s, 50, .25, .04, .30, kind="put")["delta"]) == pd_, s
    has(t, f"| US${s} | {cd} | {pd_} |")
# 55 call from the chain
row55 = [x for x in calls if x["K"] == 55][0]
d1c, d2c = bs.d1_d2(50.20, 55, .25, .04, row55["iv"])
assert r2(row55["delta"]) == "0.31" and r2(bs.norm_cdf(d2c)) == "0.26"
has(t, "0.31", "0.26")
# gamma after a 1 dollar rise
d51 = bs.greeks(51, 50, .25, .04, .30)["delta"]
assert r4(d51) == "0.6078" and r4(g["delta"] + g["gamma"]) == "0.6090"
has(t, "0.6090", "0.6078")
for days, gm in ((91.25, "0.0527"), (30, "0.0925"), (10, "0.1605")):
    assert r4(bs.greeks(50, 50, days / 365, .04, .30)["gamma"]) == gm
has(t, "0.0925", "0.1605")
# US$3 move
p53 = bs.price(53, 50, .25, .04, .30)
assert r4(C0) == "3.2297" and r4(p53) == "5.1241" and r4(p53 - C0) == "1.8943"
d_only = g["delta"] * 3
assert r4(d_only) == "1.6690" or r4(d_only) == "1.6690"
assert f"{3.2297 + 1.669:.3f}" == "4.899"
gam = 0.5 * g["gamma"] * 9
assert f"{gam:.3f}" == "0.237" and f"{d_only + gam:.3f}" == "1.906" and f"{3.2297 + d_only + gam:.3f}" == "5.136"
assert f"{(p53 - C0) - d_only:.2f}" == "0.23" and f"{abs(p53 - (C0 + d_only + gam)):.2f}" == "0.01"
p47 = bs.price(47, 50, .25, .04, .30)
assert r4(p47 - C0) == "-1.4258" and f"{-d_only + gam:.3f}" == "-1.432"
has(t, "1.669", "4.899", "0.237", "5.136", "+1.906", "5.1241", "+1.8943", "0.23 per share", "US$23", "-1.669", "-1.432", "-1.4258")
# exercises
close(0.31 * 100 * 5, 155)
close(0.44 * 2, 0.88)
assert r4(g["delta"] * 100 * 3) == "166.8985" and math.ceil(166.8985) == 167
has(t, "155 shares", usd(155, 0), "+0.88", usd(88, 0), "166.9", "167 shares")
assert f"{g['delta'] * 100 * 3:.1f}" == "166.9"

# ---------------------------------------------------------------- lesson 7
t = lesson(F, 7)
assert r4(g["theta"]) == "-0.0189" and r4(gp["theta"]) == "-0.0135"
assert r2(-g["theta"] * 100) == "1.89" and r2(-gp["theta"] * 100) == "1.35"
decay = {90: ("3.2060", "1.90"), 60: ("2.5842", "2.28"), 30: ("1.7956", "3.12"), 14: ("1.2096", "4.45"), 7: ("0.8476", "6.19"), 1: ("0.3160", "15.93")}
for dd, (val, th) in decay.items():
    assert r4(bs.price(50, 50, dd / 365, .04, .30)) == val, dd
    assert r2(-bs.greeks(50, 50, dd / 365, .04, .30)["theta"] * 100) == th, dd
    has(t, f"| {dd} | {val} | -US${th} |")
has(t, "-0.0189", "-0.0135", "US$1.89", "US$1.35")
assert r4(g["vega"]) == "0.0987" and r2(g["vega"] * 100) == "9.87"
assert r2(bs.price(50, 50, .25, .04, .35) - C0) == "0.49" and r2(bs.price(50, 50, .25, .04, .35)) == "3.72"
assert r2(bs.price(50, 50, .25, .04, .35, kind="put") - P0) == "0.49" and r2(bs.price(50, 50, .25, .04, .35, kind="put")) == "3.23" and r2(P0) == "2.73"
assert r2(bs.greeks(50, 50, .08, .04, .30)["vega"] * 100) == "5.62"
has(t, "0.0987", "US$9.87", "rises by 0.49 to 3.72", "from 2.73 to 3.23", "US$5.62")
b4 = bs.price(50, 50, 30 / 365, .04, .60)
a4 = bs.price(50, 50, 29 / 365, .04, .35)
assert r4(b4) == "3.5040" and r4(a4) == "2.0443" and r4(a4 - b4) == "-1.4597" and r2((a4 - b4) * 100) == "-145.97"
assert r2(b4 * 100) == "350.40"
has(t, "3.5040", "2.0443", "-1.4597", "US$145.97", "US$350.40")
assert r4(g["rho"]) == "0.0615" and r2(g["rho"] * 100) == "6.15" and r4(gp["rho"]) == "-0.0623"
rho2 = bs.greeks(50, 50, 2, .04, .30)["rho"]
assert r4(rho2) == "0.4529" and r2(rho2 * 100) == "45.29"
has(t, "0.0615", "US$6.15", "-0.0623", "0.4529", "US$45.29")
# exercises
close(0.0445 * 100 * 2, 8.90)
close(8.90 * 3, 26.70)
assert r4(g["vega"] * 4) == "0.3950" and r2(g["vega"] * 4 * 100) == "39.50"
has(t, "US$8.90", "US$26.70", "-0.0987 x 4" if False else "0.09874 x 4", "US$39.50", "US$9.87 against US$5.62")
# the In code function matches bs.py
def call_price_and_greeks(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    N = bs.norm_cdf
    pdf = bs.norm_pdf
    price = S * N(d1) - K * math.exp(-r * T) * N(d2)
    theta = (-S * pdf(d1) * sigma / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * N(d2)) / 365
    return price, theta
close(call_price_and_greeks(50, 50, .25, .04, .30)[0], C0, 1e-12)
close(call_price_and_greeks(50, 50, .25, .04, .30)[1], g["theta"], 1e-12)

# ---------------------------------------------------------------- lesson 8
t = lesson(F, 8)
iv = bs.implied_vol(3.40, 50.20, 50, .25, .04)
assert f"{iv * 100:.1f}" == "30.6" and f"{iv * 100:.2f}" == "30.59"
ivp = bs.implied_vol(2.70, 50.20, 50, .25, .04, kind="put")
assert f"{ivp * 100:.2f}" == "30.56" and abs(iv - ivp) < 0.0003
lo, hi = 0.10, 0.60
steps = [("35.000", "3.8358", "Too high"), ("22.500", "2.6022", "Too low"), ("28.750", "3.2187", "Too low"), ("31.875", "3.5272", "Too high"),
         ("30.312", "3.3729", "Too low"), ("31.094", "3.4500", "Too high"), ("30.703", "3.4115", "Too high"), ("30.508", "3.3922", "Too low")]
for i, (vol_s, price_s, verdict) in enumerate(steps, 1):
    m = (lo + hi) / 2
    pr = bs.price(50.20, 50, .25, .04, m)
    assert f"{m * 100:.3f}" == vol_s, (i, m)
    assert r4(pr) == price_s, (i, pr)
    assert (verdict == "Too high") == (pr > 3.40)
    has(t, f"| {i} | {vol_s}% | {price_s} | {verdict} |")
    if pr < 3.40:
        lo = m
    else:
        hi = m
em = 50.20 * iv * math.sqrt(0.25)
assert r2(em) == "7.68" and f"{iv * 0.5 * 100:.1f}" == "15.3"
assert f"{0.30 / math.sqrt(252) * 100:.1f}" == "1.9" and r2(0.30 / math.sqrt(252) * 100) == "1.89" and r2(0.30 / 15.875 * 100) == "1.89"
assert r2(50 * 0.30 / math.sqrt(252)) == "0.94"
has(t, "30.59%", "30.56%", "US$7.68", "15.3%", "0.30 / 15.87 = 1.9%", "US$0.94", "50.20 x 0.3059 x 0.5")
close(100 * 0.40 * 0.5, 20)
close(0.30 / 15.875 * 100, 1.89, 0.005)
close(36.1 - 28.6, 7.5)
has(t, usd(20, 0), "1.89%", "7.5 volatility points", "3.8358", "10% to 35%", "22.5%", "36.1%", "28.6%")
# realized volatility of the sample
bars = pd.read_csv(ROOT / "docs" / "assets" / "data" / "stock-a-daily.csv")
rets = np.log(bars["close"]).diff().dropna()
assert len(bars) == 83
assert f"{rets.std() * math.sqrt(252) * 100:.2f}" == "16.14"
has(t, "83-day sample")
# the In code solver agrees with bs.py
def call_(S, K, T, r, sigma):
    return bs.price(S, K, T, r, sigma)
def iv_code(price, S, K, T, r, lo=0.01, hi=3.0):
    for _ in range(100):
        mid_ = (lo + hi) / 2
        if call_(S, K, T, r, mid_) < price:
            lo = mid_
        else:
            hi = mid_
    return (lo + hi) / 2
close(iv_code(3.40, 50.20, 50, .25, .04), iv, 1e-8)


# ================================================================ lessons 9 to 15 (second writer)
import positions as P  # noqa: E402

ACCT, R1 = 25_000, 250.0
FEE = P.FEE


def d(x):
    return round(x, 2)


def pnl(pos, S):
    return d(pos.expiry(S) * 100)


def be(pos):
    return P.breakevens(pos.expiry)


def gr(pos):
    g = {k: round(v * 100, 2) for k, v in pos.greeks().items()}
    return g["delta"], g["gamma"], g["theta"], g["vega"]


# --- lesson 9
t = lesson(F, 9)
cc, csp = P.COVERED_CALL, P.CASH_PUT
close(cc.net, 48.10, 1e-9)
assert pnl(cc, 60) == 440 and pnl(cc, 0.0001) < -4809 and be(cc) == [48.1]
assert d(csp.net) == -1.80 and pnl(csp, 60) == 180 and be(csp) == [45.7]
close(47.5 * 100 - 180, 4570)
assert gr(cc) == (56.64, -5.40, 1.78, -9.87)
assert gr(csp) == (31.60, -4.30, 1.42, -8.93)
assert round(chain.rows("call")[3]["delta"] * 100, 1) == 43.4
risk_cc = (48.10 - 46.70) * 100 + 2 * FEE
close(risk_cc, 141.30)
assert r2(risk_cc / R1) == "0.57" and r2(4810 / ACCT * 100) == "19.24"
assert r2((440 - 1.30) / R1) == "1.75" and d(440 - 1.30) == 438.70
risk_put = (45.70 - 43.70) * 100 + 2 * FEE
close(risk_put, 201.30)
assert r2(risk_put / R1) == "0.81" and d(180 - 1.30) == 178.70 and r2(178.70 / R1) == "0.71"
assert d((51.00 - 50.20 + 2.10) * 100) == 290
assert d(csp.expiry(44.0)) == -1.70
has(t, "US$48.10", "US$4,810", "US$180", "US$440", "48.10", "45.70", "US$4,570", "+56.64", "-5.40", "+US$1.78", "-US$9.87",
    "+31.60", "-4.30", "+US$1.42", "-US$8.93", "US$141.30", "0.57R", "19.2%", "US$438.70", "1.75R", "US$201.30", "0.81R",
    "US$178.70", "0.71R", "US$290", "-US$170", "US$4,750", "US$1.30", "US$0.65", "43.4")

# --- lesson 10
t = lesson(F, 10)
bc, bp = P.BULL_CALL, P.BULL_PUT
assert d(bc.net) == 2.15 and d(bp.net) == -1.30
assert pnl(bc, 60) == 285 and pnl(bc, 40) == -215 and be(bc) == [52.15]
assert pnl(bp, 60) == 130 and pnl(bp, 40) == -370 and be(bp) == [48.7]
assert gr(bc) == (25.71, 0.21, -0.39, 1.02)
assert gr(bp) == (20.70, -1.81, 0.03, -2.32)
close(bc.fees(), 2.60)
ml = 215 + 2.60
assert d(ml) == 217.60 and r2(ml / R1) == "0.87" and r2(2 * ml / R1) == "1.74" and d(2 * ml) == 435.20
assert d(285 - 2.60) == 282.40 and r2(282.40 / R1) == "1.13" and r2(282.40 / ml) == "1.30"
assert d(370 + 2.60) == 372.60 and r2(372.60 / R1) == "1.49"
nar = P.Position([P.Leg(-1, "put", 47.5), P.Leg(1, "put", 45.0)])
assert d(nar.net) == -0.45 and pnl(nar, 40) == -205 and be(nar) == [47.05]
assert d(205 + 2.60) == 207.60 and r2(207.60 / R1) == "0.83"
assert d(2.20 - 1.30) == 0.90 and d((2.5 - 0.90) * 100) == 160 and d(52.50 + 0.90) == 53.40
assert d(1.30 - 3.00) == -1.70
assert int(300 // 217.60) == 1 and r2(300 / 217.60) == "1.38"
has(t, "US$215", "US$130", "US$285", "US$370", "52.15", "48.70", "+25.71", "+0.21", "-US$0.39", "+US$1.02", "+20.70", "-1.81",
    "+US$0.03", "-US$2.32", "US$217.60", "0.87R", "US$435.20", "1.74R", "US$282.40", "1.13R", "1.30", "US$372.60", "1.49R",
    "US$207.60", "0.83R", "47.05", "US$45", "US$205", "US$160", "53.40", "-US$170", "1.38", "US$2.60")

# --- lesson 11
t = lesson(F, 11)
sd, sg = P.STRADDLE, P.STRANGLE
assert d(sd.net) == 6.20 and d(sg.net) == 4.10
assert pnl(sd, 50) == -620 and pnl(sg, 50) == -410 and pnl(sg, 48) == -410 and pnl(sg, 52) == -410
assert be(sd) == [43.8, 56.2] and be(sg) == [43.4, 56.6]
close(43.80 * 100, 4380)
close(43.40 * 100, 4340)
assert gr(sd) == (13.34, 10.25, -3.31, 19.75)
assert gr(sg) == (11.75, 9.71, -3.20, 18.80)
assert f"{6.20 / 50.20 * 100:.1f}" == "12.4"
em2 = 50.20 * chain.rows("call")[2]["iv"] * 0.5
assert r2(em2) == "7.68" and r2(math.sqrt(2 / math.pi)) == "0.80"
assert d(14 * 3.31) == 46.34
assert d(5 * 19.75) == 98.75
assert d(chain.rows("call")[2]["bid"] + chain.rows("put")[2]["bid"]) == 6.00
assert r2(622.60 / R1) == "2.49" and r2(412.60 / R1) == "1.65" and d(622.60 / 0.01) == 62260
assert r2(622.60 / 650) == "0.96"
assert d((7 - 6.20) * 100 - 2.60) == 77.40 and r2(77.40 / 650) == "0.12"
assert d((10 - 6.20) * 100 - 2.60) == 377.40 and r2(377.40 / 650) == "0.58"
assert d(2.20 + 4.00) == 6.20 and d(52.5 + 6.2) == 58.70 and d(52.5 - 6.2) == 46.30
assert d(5.50 - 4.10) == 1.40 and d(4 * 19.75) == 79.00
has(t, "US$620", "US$410", "6.20", "4.10", "43.80", "56.20", "43.40", "56.60", "US$4,380", "US$4,340", "+13.34", "+10.25",
    "-US$3.31", "+US$19.75", "+11.75", "+9.71", "-US$3.20", "+US$18.80", "12.4%", "US$7.68", "US$46", "US$98.75",
    "US$600", "US$622.60", "2.49R", "US$412.60", "1.65R", "US$62,260", "0.96R", "US$77.40", "0.12R", "US$377.40", "0.58R",
    "58.70", "46.30", "US$140", "US$79.00", "3% a week")

# --- lesson 12
t = lesson(F, 12)
ic, bf = P.CONDOR, P.BUTTERFLY
assert d(ic.net) == -1.20 and d(bf.net) == 0.60
assert pnl(ic, 50) == 120 and pnl(ic, 40) == -130 and pnl(ic, 60) == -130 and be(ic) == [46.3, 53.7]
assert pnl(bf, 50) == 190 and pnl(bf, 40) == -60 and pnl(bf, 60) == -60 and be(bf) == [48.1, 51.9]
assert gr(ic) == (-3.42, -1.48, 0.30, -2.40)
assert gr(bf) == (-1.59, -0.54, 0.14, -0.94)
assert d(ic.fees()) == 5.20 and d(bf.fees()) == 5.20
assert d(130 + 5.20) == 135.20 and r2(135.20 / R1) == "0.54" and d(2 * 135.20) == 270.40 and r2(270.40 / R1) == "1.08"
assert d(120 - 5.20) == 114.80 and r2(114.80 / R1) == "0.46" and r2(114.80 / 135.20) == "0.85"
assert d(60 + 5.20) == 65.20 and r2(65.20 / R1) == "0.26" and d(3 * 65.20) == 195.60 and r2(195.60 / R1) == "0.78"
assert d(4 * 65.20) == 260.80 and r2(260.80 / R1) == "1.04"
assert d(3 * (190 - 5.20)) == 554.40 and r2(554.40 / R1) == "2.22"
assert d(120 - 50 - 5.20) == 64.80 and d(ic.expiry(53) * 100) == 70.0
assert f"{135.20 / (135.20 + 114.80) * 100:.0f}" == "54"
assert d(1.80 - 1.35 + 2.10 - 1.35) == 1.20 and d(5.10 + 2.20 - 6.70) == 0.60
assert r2(190 / 60) == "3.17" and d((5 - 1.50) * 100) == 350 and d(45 + 1.5) == 46.5 and d(55 - 1.5) == 53.5
assert d(1.20 - 1.50) == -0.30 and r2(250 / 135.20) == "1.85"
has(t, "US$120", "US$130", "US$190", "US$60", "46.30", "53.70", "48.10", "51.90", "-3.42", "-1.48", "+US$0.30", "-US$2.40",
    "-1.59", "-0.54", "+US$0.14", "-US$0.94", "US$135.20", "0.54R", "US$270.40", "1.08R", "US$114.80", "0.46R", "0.85",
    "US$65.20", "0.26R", "US$195.60", "0.78R", "US$260.80", "1.04R", "US$554.40", "2.22R", "US$64.80", "54%", "US$5.20",
    "US$350", "46.50", "53.50", "-US$30", "US$150", "US$100", "1.85", "3.80")

# --- lesson 13
t = lesson(F, 13)
cal, dia = P.CALENDAR, P.DIAGONAL
assert (P.NEAR50_BID, P.NEAR525_BID) == (2.65, 1.59)
assert d(cal.net) == 0.80 and d(dia.net) == 1.86
assert round(P.T_LEFT * 365) == 35 and round(P.T_NEAR * 365) == 56 and round(P.T0 * 365) == 91
assert datetime.date(2026, 11, 20) + datetime.timedelta(days=56) == datetime.date(2027, 1, 15)
assert datetime.date(2026, 11, 20) + datetime.timedelta(days=91) == datetime.date(2027, 2, 19)
cal_t = {S: round(P.calendar_at_near_expiry(cal, S) * 100) for S in (44, 46, 48, 50, 52, 54, 56)}
dia_t = {S: round(P.calendar_at_near_expiry(dia, S) * 100) for S in (44, 46, 48, 50, 52, 54, 56)}
assert cal_t == {44: -60, 46: -29, 48: 29, 50: 119, 52: 42, 54: -7, 56: -34}, cal_t
assert dia_t == {44: -166, 46: -135, 48: -77, 50: 13, 52: 136, 54: 137, 56: 110}, dia_t
assert P.breakevens(lambda S: P.calendar_at_near_expiry(cal, S)) == [47.13, 53.66]
assert P.breakevens(lambda S: P.calendar_at_near_expiry(dia, S)) == [49.75]
assert gr(cal) == (0.94, -1.35, 0.50, 2.11)
assert gr(dia) == (16.84, -1.21, 0.37, 2.28)
assert d(5 * 2.11) == 10.55
assert d(80 + 2.60) == 82.60 and r2(82.60 / R1) == "0.33" and d(3 * 82.60) == 247.80 and r2(247.80 / R1) == "0.99"
assert d(4 * 82.60) == 330.40 and r2(330.40 / R1) == "1.32"
assert d(3 * (119 - 2.60)) == 349.20 and r2(349.20 / R1) == "1.40"
assert d(3 * (34 + 2.60)) == 109.80 and r2(109.8 / R1) == "0.44" and d(3 * (60 + 2.60)) == 187.80 and r2(187.8 / R1) == "0.75"
assert d(186 + 2.60) == 188.60 and r2(188.60 / R1) == "0.75" and d(136 - 2.60) == 133.40 and r2(133.4 / R1) == "0.53"
assert d(166 + 2.60) == 168.60 and r2(168.6 / R1) == "0.67" and d(137 - 2.60) == 134.40
assert d(3.45 - 2.65) == 0.80 and d(3.45 - 1.59) == 1.86
has(t, "US$80", "US$186", "0.80", "1.86", "-US$60 | -US$29 | +US$29 | +US$119 | +US$42 | -US$7 | -US$34",
    "-US$166 | -US$135 | -US$77 | +US$13 | +US$136 | +US$137 | +US$110", "47.13", "53.66", "49.75",
    "+0.94", "-1.35", "+US$0.50", "+US$2.11", "+16.84", "-1.21", "+US$0.37", "+US$2.28", "US$10.55", "US$82.60", "0.33R",
    "US$247.80", "0.99R", "US$330.40", "1.32R", "US$349.20", "1.40R", "US$109.80", "0.44R", "US$187.80", "0.75R",
    "US$188.60", "US$133.40", "0.53R", "US$168.60", "0.67R", "US$134.40", "November 20, 2026", "January 15, 2027", "2.65", "1.59")

# --- lesson 14
t = lesson(F, 14)
assert d(6.90 - (50.20 - 45)) == 1.70
assert d(5.25 - (50.20 - 45)) == 0.05
intr = 45 * 0.04 / 365
assert f"{intr:.3f}" == "0.005"
assert d((50.20 - 45) + 0.50 - 5.25 - intr) == 0.45
vv = lambda S_, h: round(bs.price(S_, 50, h / 8760, 0.04, 0.30) * 100, 2)
assert [vv(50, h) for h in (6.5, 3, 1, 0.5, 0.25)] == [16.37, 11.11, 6.41, 4.53, 3.20]
gm = lambda h: bs.greeks(50, 50, h / 8760, 0.04, 0.30)["gamma"]
g3m = bs.greeks(50, 50, 0.25, 0.04, 0.30)["gamma"]
assert r4(g3m) == "0.0527" and r4(gm(6.5)) == "0.9763" and r2(gm(6.5) / g3m) == "18.54" and r2(gm(0.25)) == "4.98"
assert r2(50 * 0.30 * math.sqrt(6.5 / 8760)) == "0.41"
assert vv(50.5, 3) == 50.47 and vv(49.5, 3) == 0.39
c = 17 + 1.30
assert d(c) == 18.30 and int(R1 // c) == 13 and d(13 * c) == 237.90 and r2(13 * c / R1) == "0.95"
w = d(vv(50.5, 3) - 17 - 1.30)
assert w == 32.17 and d(13 * w) == 418.21 and r2(13 * w / R1) == "1.67"
l1 = d(17 - 0.39 + 1.30)
assert l1 == 17.91 and d(13 * l1) == 232.83 and r2(13 * l1 / R1) == "0.93"
l2 = d(17 - 11.11 + 1.30)
assert l2 == 7.19 and d(13 * l2) == 93.47 and r2(13 * l2 / R1) == "0.37"
assert r2(0.93 + 1.67) == "2.60" and int(500 // 18.30) == 27 and r2(500 / 18.30) == "27.32"
assert d((53 - 50) * 100) == 300 and d(0.03 * 100) == 3
has(t, "1.70", "0.05", "0.005", "5.70", "5.25", "US$45", "16.37", "11.11", "6.41", "4.53", "3.20", "0.0527", "0.9763", "18.5",
    "4.98", "US$0.41", "US$50.47", "US$0.39", "US$18.30", "13 contracts", "US$237.90", "0.95R", "US$32.17", "US$418.21",
    "1.67R", "US$17.91", "US$232.83", "0.93R", "US$7.19", "US$93.47", "0.37R", "2.6R", "27 contracts", "US$300", "June 4, 2026",
    "US$0.01", "50.02")

# --- lesson 15
t = lesson(F, 15)
ke = 50 * math.exp(-0.04 * 0.25)
assert r4(ke) == "49.5025" and r4(50 - ke) == "0.4975" and r4(C0 - P0) == "0.4975" and r4(P0) == "2.7322"
assert d(0.57 * 100) == 57 and r2(80 * 0.30 * 0.5) == "12.00"
assert d(2.65 - 1.90) == 0.75 and d((2.5 - 0.75) * 100) == 175 and d(50 - 0.75) == 49.25
assert r2(622.60 / R1) == "2.49"
has(t, usd(325, 0), "49.5025", "0.4975", "2.7322", usd(57, 0), usd(12, 0), usd(75, 0), usd(175, 0), "49.25", "2.49R",
    "C$0.04", "10 defined-risk option trades", "IT-479R", "23 to 32")
