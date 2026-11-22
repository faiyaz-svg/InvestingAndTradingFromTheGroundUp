"""Number checks for part 13, ETFs, portfolios and factors.

Everything is made up: funds, assets, prices and returns. The model section above
the marker line is shared with the figure scripts in tools/figures/13-etfs-portfolios-and-factors/.
"""
import numpy as np

# ---- Model (shared with the figures) ----
def fee_value(start, gross, fee, years):
    return start * (1 + gross - fee) ** years

# Volatility decay simulation: zero-drift index, daily sigma 1.8%, 250 days
def leverage_sim(seed=8, days=250, sigma=0.018):
    r = np.random.default_rng(seed).normal(0.0, sigma, days)
    idx = np.concatenate([[100.0], 100 * np.cumprod(1 + r)])
    lev = np.concatenate([[100.0], 100 * np.cumprod(1 + 2 * r)])
    naive = 100 * (1 + 2 * (idx / 100 - 1))
    return r, idx, lev, naive

# Two-asset portfolio volatility
def port_sd(w1, s1, s2, rho):
    w2 = 1 - w1
    return (w1**2 * s1**2 + w2**2 * s2**2 + 2 * w1 * w2 * rho * s1 * s2) ** 0.5

# Three made-up assets for the frontier
MU = np.array([0.08, 0.03, 0.065])
SD = np.array([0.16, 0.05, 0.15])
CORR = np.array([[1, 0.1, 0.6], [0.1, 1, 0.1], [0.6, 0.1, 1]])
COV = np.outer(SD, SD) * CORR
RF = 0.02

def tangency():
    x = np.linalg.solve(COV, MU - RF)
    return x / x.sum()

def min_var():
    y = np.linalg.solve(COV, np.ones(3))
    return y / y.sum()

# ==== LESSON CHECKS
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _lib import lesson, has, usd, cad, pct, num

F = "13-etfs-portfolios-and-factors"
close = lambda a, b, t=1e-9: abs(a - b) < t

# ---- Lesson 1: how ETFs work
t = lesson(F, 1)
nav = 250_000_000 / 5_000_000
assert nav == 50.0
prem = (50.12 - nav) / nav
assert round(100 * prem, 2) == 0.24 and round(100 * (49.88 - nav) / nav, 2) == -0.24
basket = 50_000 * nav
sale = 50_000 * 50.12
assert round(sale - basket) == 6000 and round(50_000 * 49.88) == 2_494_000
has(t, usd(nav), "0.24%", "-0.24%", usd(basket, 0), usd(sale, 0), usd(6000, 0), usd(2_494_000, 0))
assert 1000 * (40 - 10) == 30000 and 0.01 * 30000 == 300
has(t, usd(30000, 0), usd(300, 0))
n2 = (180_000_000 - 600_000) / 3_000_000
assert round(n2, 2) == 59.80
assert round(100 * (59.95 - n2) / n2, 2) == 0.25
has(t, usd(n2), "0.25% premium")
assert 2000 * 6 == 12000 and 0.005 * 12000 == 60
has(t, usd(12000, 0), usd(60, 0))

# ---- Lesson 2: fees and tracking
t = lesson(F, 2)
v0 = fee_value(10000, 0.07, 0, 30)
vlow, vmid, vhigh = (fee_value(10000, 0.07, f, 30) for f in (0.001, 0.01, 0.0225))
has(t, usd(v0), usd(vlow), usd(vmid), usd(vhigh), usd(v0 - vlow), usd(v0 - vmid))
assert round(100 * (v0 - vmid) / v0, 1) == 24.5
has(t, "24.5%")
idx = np.array([1.2, -0.8, 2.1, 0.5, -1.5, 1.9, 0.7, -0.3, 1.1, 2.4, -2.0, 0.9])
fund = np.array([1.18, -0.81, 2.07, 0.5, -1.52, 1.89, 0.66, -0.31, 1.08, 2.4, -2.03, 0.89])
ann = lambda r: np.prod(1 + r / 100) - 1
ia, fa = ann(idx), ann(fund)
assert round(100 * ia, 2) == 6.26 and round(100 * fa, 2) == 6.05 and round(100 * (fa - ia), 2) == -0.21
sdd = np.std(fund - idx, ddof=1)
assert round(sdd, 4) == 0.0123 and round(sdd * 12 ** 0.5, 2) == 0.04
has(t, "6.26%", "6.05%", "-0.21%", "0.0123 percentage points", "0.04% a year")
assert round(0.04 / 40.02 * 100, 2) == 0.10 and round(10000 * 0.04 / 40.02, 2) == 10.00
has(t, "0.04 / 40.02 = 0.10%", usd(10.00))
assert round(12 * 0.10, 1) == 1.2
a = 20000 * 1.0575 ** 20
b = 20000 * 1.06 ** 20
assert round(a) == 61184 and round(b, 2) == 64142.71 and round(b) - round(a) == 2959 and round(b - a) == 2959
has(t, usd(61184, 0), usd(b), usd(2959, 0), "-0.25%")
assert round(0.04 / 25.12 * 100, 2) == 0.16 and round(5000 * 0.0016) == 8
has(t, "0.16%", "US$8")

# ---- Lesson 3: US vs Canadian listed
t = lesson(F, 3)
div = 50_000 * 0.015
assert div == 750 and div * 0.15 == 112.5 and close(112.5 / 50_000, 0.00225)
has(t, cad(750, 0), cad(112.5), "0.225%")
assert 20_000 * 0.015 * 0.15 == 45 and 20_000 * 0.015 == 300
assert round(300 / 45, 1) == 6.7 and round(600 / 45, 1) == 13.3
has(t, cad(45, 0), cad(300, 0), "6.7 years", "13.3 years")
assert round(0.15 * 0.02, 3) == 0.003
has(t, "0.30% a year")
assert 30_000 * 0.02 * 0.15 == 90 and 30_000 * 0.015 == 450 and 90 * 5 == 450
has(t, cad(600, 0), cad(90, 0), cad(450, 0))

# ---- Lesson 4: leveraged and inverse
t = lesson(F, 4)
f = 100 * (1 + 2 * -0.10) * (1 + 2 * 0.10)
assert round(f) == 96 and round(100 * 0.9 * 1.1) == 99
assert round(100 * 0.7 * 1.3) == 91
assert round(100 * 1.1 * 0.9) == 99
assert round(2 * (2 - 1) * (-0.1) * 0.1, 2) == -0.02
has(t, usd(80, 0), usd(96, 0), "-4%", "100 to 70 to 91", "a loss of 9%", "100 to 110", "to 99")
assert round(1.1 * 1.1 - 1, 2) == 0.21 and round(1.2 * 1.2 - 1, 2) == 0.44
has(t, "21%", "44%")
g = lambda L, mu, s: L * mu - L**2 * s**2 / 2
vals = {(L, s): round(100 * g(L, 0.08, s), 1) for L in (1, 2, 3, -1) for s in (0.2, 0.3)}
assert vals == {(1, .2): 6.0, (2, .2): 8.0, (3, .2): 6.0, (-1, .2): -10.0, (1, .3): 3.5, (2, .3): -2.0, (3, .3): -16.5, (-1, .3): -12.5}
has(t, "| 20% | 6.0% | 8.0% | 6.0% | -10.0% |", "| 30% | 3.5% | -2.0% | -16.5% | -12.5% |")
r, ix, lv, nv = leverage_sim()
assert (round(ix[-1], 1), round(lv[-1], 1), round(nv[-1], 1)) == (98.2, 87.8, 96.3)
assert round(0.95 * 1.05, 4) == 0.9975 and round(1.04 * 1.04, 4) == 1.0816 and round(1.08 * 1.08, 4) == 1.1664
assert round(2 * 8.16, 2) == 16.32
has(t, "8.16%", "16.64%", "16.32%", "0.32 points", "0.9975")
assert round(100 * g(2, 0.08, 0.25), 1) == 3.5 and round(100 * g(1, 0.08, 0.25), 3) == 4.875
has(t, "3.5% a year", "4.875%")

# ---- Lesson 5: asset allocation
t = lesson(F, 5)
rows = {}
for w in (0.8, 0.6, 0.4):
    e = w * 7 + (1 - w) * 3
    s = w * -40 + (1 - w) * 5
    rows[w] = (round(e, 1), round(s, 1), round(-s / 100 * 50_000))
assert rows == {0.8: (6.2, -31.0, 15500), 0.6: (5.4, -22.0, 11000), 0.4: (4.6, -13.0, 6500)}
has(t, "6.2%", "-31%", cad(15500, 0), "5.4%", "-22%", cad(11000, 0), "4.6%", "-13%", cad(6500, 0))
assert round(6.2 - 5.4, 1) == 0.8 and 31 - 22 == 9
has(t, "0.8 percentage points", "9 points")
assert round(0.7 * 7 + 0.3 * 3, 1) == 5.8
s7 = 0.7 * -40 + 0.3 * 5
assert s7 == -26.5 and round(0.265 * 80000) == 21200
has(t, "5.8%", "-26.5%", cad(21200, 0))

# ---- Lesson 6: diversification
t = lesson(F, 6)
sd = lambda rho, w=0.6: port_sd(w, 0.16, 0.06, rho)
assert round(100 * sd(0.2), 2) == 10.35 and round(100 * sd(0), 2) == 9.90 and round(100 * sd(-0.3), 2) == 9.17
assert round(100 * sd(0.8), 2) == 11.61 and round(100 * sd(1), 2) == 12.00
has(t, "0.009216", "0.000576", "0.0009216", "0.0107136", "10.35%", "1.65 points", "9.90%", "9.17%", "11.61%", "12.00%")
assert round(50_000 * sd(0.2)) == 5175
has(t, cad(5175, 0), cad(6000, 0))
Nv = {n: 0.3 * (1 / n + (1 - 1 / n) * 0.3) ** 0.5 for n in (1, 5, 10, 30, 100)}
assert [round(100 * v, 1) for v in Nv.values()] == [30.0, 19.9, 18.2, 17.1, 16.6]
assert round(100 * 0.3 * 0.3 ** 0.5, 1) == 16.4
has(t, "| Portfolio volatility | 30.0% | 19.9% | 18.2% | 17.1% | 16.6% | 16.4% |", "16.4%")
pp = lambda rho: 20 * (0.5 * (1 + rho)) ** 0.5
assert round(pp(0.5), 2) == 17.32 and round(pp(0.9), 2) == 19.49
has(t, "17.32%", "19.49%")
q1 = port_sd(0.5, 0.18, 0.05, 0.1)
assert round(100 * q1, 2) == 9.58 and round(0.5 * 18 + 0.5 * 5 - 100 * q1, 2) == 1.92
has(t, "0.009175", "9.58%", "11.5%", "1.92 points")
q3 = (0.0625 * (1 / 20 + 19 / 20 * 0.4)) ** 0.5
assert round(q3, 4) == 0.1639 and round(25 * 0.4 ** 0.5, 2) == 15.81
has(t, "0.026875", "16.39%", "15.81")

# ---- Lesson 7: rebalancing
t = lesson(F, 7)
s_, b_ = 60_000 * 1.25, 40_000 * 1.02
V = s_ + b_
assert (s_, round(b_), round(V)) == (75000, 40800, 115800)
assert round(100 * s_ / V, 2) == 64.77 and round(100 * b_ / V, 2) == 35.23
assert round(0.6 * V) == 69480 and round(0.4 * V) == 46320 and round(69480 - s_) == -5520
has(t, usd(75000, 0), usd(40800, 0), usd(115800, 0), "64.77%", "35.23%", usd(69480, 0), usd(46320, 0), "-US$5,520")
assert round(100 * s_ / V - 60, 2) == 4.77
assert round(100 * 84000 / 124000, 2) == 67.74 and round(0.6 * 124000) == 74400 and 84000 - 74400 == 9600
has(t, "4.77 points", "67.74%", "7.74 points", usd(74400, 0), usd(9600, 0))
V2 = V + 5000
assert round(0.4 * V2) == 48320 and round(48320 - b_) == 7520
assert round(100 * s_ / V2, 1) == 62.1
has(t, usd(120800, 0), usd(48320, 0), usd(7520, 0), "62.1%", "37.9%")
tot = 125
x2 = tot / 2 * 0.5
y2 = tot / 2 * 2
assert x2 + y2 == 156.25
has(t, "US$156.25", "56.25%", "62.50")
s1, b1 = 35_000 * 1.2, 15_000 * 0.96
T1 = s1 + b1
assert (round(s1), round(b1), round(T1)) == (42000, 14400, 56400) and round(100 * s1 / T1, 2) == 74.47
has(t, "56,400", "74.47%", "25.53%")
assert round(0.7 * T1) == 39480 and round(s1 - 39480) == 2520 and round(0.3 * T1) == 16920
has(t, "39,480", "US$2,520", "16,920")
T2 = T1 + 3000
assert round(0.3 * T2) == 17820 and round(17820 - b1) == 3420
assert round(100 * (b1 + 3000) / T2, 2) == 29.29 and round(100 * s1 / T2, 2) == 70.71
has(t, "59,400", "17,820", "3,420", "29.29%", "70.71%")

# ---- Lesson 8: MPT
t = lesson(F, 8)
wA = (0.05**2 - 0.1 * 0.16 * 0.05) / (0.16**2 + 0.05**2 - 2 * 0.1 * 0.16 * 0.05)
assert round(wA, 3) == 0.064
has(t, "0.0017", "0.0265", "6.4%", "93.6%")
sh = lambda w: (w * 8 + (1 - w) * 3 - 2) / (100 * port_sd(w, 0.16, 0.05, 0.1))
assert [round(sh(w), 3) for w in (0, 0.2, 0.4, 0.6, 1)] == [0.200, 0.373, 0.409, 0.400, 0.375]
has(t, "| 0% | 3.0% | 5.00% | 0.200 |", "| 20% | 4.0% | 5.37% | 0.373 |", "| 40% | 5.0% | 7.33% | 0.409 |", "| 60% | 6.0% | 10.00% | 0.400 |", "| 100% | 8.0% | 16.00% | 0.375 |")
wt = tangency()
assert [round(100 * x, 1) for x in wt] == [32.0, 55.6, 12.4]
tm, ts = wt @ MU, float(np.sqrt(wt @ COV @ wt))
assert (round(100 * tm, 2), round(100 * ts, 2), round((tm - RF) / ts, 3)) == (5.04, 7.26, 0.418)
has(t, "32.0% A, 55.6% B and 12.4% C", "5.04%", "7.26%", "0.418")
assert round(0.5 * 5.04 + 0.5 * 2, 2) == 3.52 and round(0.5 * 7.26, 2) == 3.63
has(t, "3.52%", "3.63%")
assert round((9 - 2) / 18, 3) == 0.389
assert round(100 * port_sd(0.2, 0.16, 0.05, 0.1), 2) == 5.37
has(t, "0.00288", "0.389", "5.37%")
assert round(0.7 * 5.04 + 0.3 * 2, 2) == 4.13 and round(0.7 * 7.26, 2) == 5.08
has(t, "4.13%", "5.08%")
assert (min_var() > -0.05).all()

# ---- Lesson 9: factors
t = lesson(F, 9)
m = np.array([2.0, -1.5, 3.0, 0.5, -2.5, 4.0, 1.0, -3.0, 2.5, 0.0, 1.5, -1.0])
sa = np.array([3.4, -1.9, 4.2, 1.1, -3.2, 5.4, 1.6, -4.0, 3.9, 0.4, 2.0, -1.7])
beta, alpha = np.polyfit(m, sa, 1)
cv = np.cov(m, sa, ddof=1)[0, 1]
assert round(cv, 3) == 6.762 and round(m.var(ddof=1), 3) == 4.884 and round(beta, 2) == 1.38 and round(alpha, 2) == 0.18
has(t, "6.762", "4.884", "1.38", "0.18%")
assert round((3.1 + 2.2 + 1.0) / 3, 2) == 2.10 and round((-1.2 - 0.8 - 2.4) / 3, 2) == -1.47
assert round(2.10 + 1.47, 2) == 3.57
has(t, "2.10%", "-1.47%", "3.57%")
assert round(0.2 * 2.0, 2) == 0.40 and round(2.0 * 0.42, 2) == 0.84 and round(0.2 * 0.84, 2) == 0.17 and round(0.2 * 6, 1) == 1.2
has(t, "0.40 percentage points", "0.84%", "0.17 points", "1.2 points")
assert round(8.4 / 6.0, 2) == 1.4 and round(2 + 1.4 * 5, 1) == 9.0
has(t, "8.4 / 6.0 = 1.4", "Expected return = 2 + 7 = 9%")
top = (3.1 + 2.2 - 1.0) / 3
assert round(top, 2) == 1.43 and round(top + (1.2 + 0.8 + 2.4) / 3, 2) == 2.90
has(t, "1.43%", "2.90%")
assert round(3.0 * 0.42, 2) == 1.26 and round(0.25 * 1.26, 3) == 0.315
has(t, "1.26%", "0.315")

# ---- Lesson 10: long-term portfolio
t = lesson(F, 10)
assert 30_000 + 15_000 + 15_000 + 30_000 + 10_000 == 100_000
assert 30_000 * 0.015 * 0.15 == 67.5 and round(450 / 67.5, 1) == 6.7
has(t, cad(67.50), cad(450, 0), "6.7 years")
e = 0.2 * 7 + 0.8 * 3
s = 0.2 * -40 + 0.8 * 5
assert round(e, 1) == 3.8 and s == -4.0 and round(0.04 * 16000) == 640 and round(0.22 * 16000) == 3520
has(t, "3.8%", "-4%", cad(640, 0), "22%", cad(3520, 0))
for g_, lump_e, dca_e, p_e in ((0.01, 13521.90, 12809.33, 112.68), (0.0, 12000.0, 12000.0, 100.0), (-0.01, 10636.62, 11247.90, 88.64)):
    P = [100 * (1 + g_) ** k for k in range(13)]
    lump = 12000 / P[0] * P[12]
    dca = sum(1000 / P[k] for k in range(12)) * P[12]
    assert (round(lump, 2), round(dca, 2), round(P[12], 2)) == (lump_e, dca_e, p_e)
    has(t, cad(lump_e), cad(dca_e), cad(p_e))
q2a, q2b = fee_value(10000, 0.07, 0.001, 30), fee_value(10000, 0.07, 0.005, 30)
assert (round(q2a, 2), round(q2b, 2), round(q2a - q2b, 2)) == (74016.95, 66143.66, 7873.28)
has(t, usd(q2a), usd(q2b), usd(q2a - q2b))
assert round(100 * (40.10 - 40) / 40, 2) == 0.25
q5 = port_sd(0.5, 0.2, 0.1, 0.5)
assert round(100 * q5, 2) == 13.23
has(t, "0.0175", "13.23%", "0.9975", "1.68%")
assert round(4 * 0.42, 2) == 1.68
print("part 13 checks ok")
