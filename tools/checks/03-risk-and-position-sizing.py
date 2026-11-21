"""Number checks for part 3, Risk and position sizing."""
import json
import math
import sys

import numpy as np
import pandas as pd

from _lib import ROOT, lesson, has, usd, cad

F = "03-risk-and-position-sizing"
sys.path.insert(0, str(ROOT / "tools" / "figures" / F))
import sim  # noqa: E402

CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def close(a, b, tol=1e-9):
    assert abs(a - b) <= tol, (a, b)


def kelly(p, b):
    return p - (1 - p) / b


def growth(p, b, f):
    return p * math.log(1 + b * f) + (1 - p) * math.log(1 - f)


# ---- Lesson 1
t = lesson(F, 1)
for L, g in [(0.05, "5.3"), (0.10, "11.1"), (0.20, "25.0"), (0.25, "33.3"), (0.30, "42.9"), (0.40, "66.7"), (0.50, "100.0"), (0.60, "150.0"), (0.75, "300.0"), (0.90, "900.0")]:
    assert f"{100 * L / (1 - L):.1f}" == g
    has(t, f"| {g}% |")
acct = 10_000 * 0.9**4
close(acct, 6561)
has(t, "US$6,561", "34.39%")
assert f"{(10_000 - acct) / acct * 100:.1f}" == "52.4"
has(t, "52.4%")
x = 10_000 * 0.99**10
y = 10_000 * 0.90**10
has(t, usd(x), "9.56%", "0.9044", usd(y), "65.13%", "0.3487")
assert f"{(1 / 0.99**10 - 1) * 100:.1f}" == "10.6" and f"{(1 / 0.9**10 - 1) * 100:.1f}" == "186.8"
has(t, "10.6%", "186.8%")
has(t, "25%", "US$14,000", "42.9%", "50%")
a5 = 10_000 * 0.98**5
has(t, usd(a5), "9.61%", "10.6%")
assert f"{(1 / 0.98**5 - 1) * 100:.1f}" == "10.6" and f"{(1 - 0.98**5) * 100:.2f}" == "9.61"

# ---- Lesson 2
t = lesson(F, 2)
g = bars("stock-a-pullback")
by_date = {b[0]: b for b in g}
assert by_date["2026-02-25"][4] == 48.20
assert by_date["2026-03-05"][2] == 51.33 and by_date["2026-03-05"][2] >= 51.20
assert by_date["2026-02-19"][3] == 46.90
E, S, X, N = 48.20, 46.70, 51.20, 166
close(E - S, 1.5)
R = N * (E - S)
close(R, 249)
close((X - E) / (E - S), 2.0)
close(N * (X - E), 498)
has(t, "US$1.50", usd(R), "+2.0R", usd(498), "51.33")
trades = [(48.20, 46.70, 51.20), (20.00, 19.00, 19.00), (75.50, 73.50, 74.50), (31.00, 30.00, 31.30), (60.00, 58.00, 66.20), (40.00, 41.00, 38.60)]
rs = [round((x_ - e) / (e - s), 1) for e, s, x_ in trades]
assert rs == [2.0, -1.0, -0.5, 0.3, 3.1, 1.4], rs
has(t, "+2.0R", "-1.0R", "-0.5R", "+0.3R", "+3.1R", "+1.4R")
assert round(sum(rs), 1) == 5.3 and f"{sum(rs) / 6:.2f}" == "0.88"
assert round(5.3 * 250) == 1325
has(t, "+5.3R", "0.88R", "US$1,325")
close((35.20 - 32.00) / (32.00 - 30.40), 2.0)
close((31.20 - 32.00) / 1.60, -0.5)
close((50 - 46) / (52 - 50), 2.0)
close(465 / 300, 1.55)
close(-330 / 300, -1.1)
has(t, "1.60", "-0.5R", "+1.55R", "-1.1R", "-0.80")

# ---- Lesson 3
t = lesson(F, 3)
p, W, L = 18 / 40, 1.8, 0.9
b = W / L
exp = p * W - (1 - p) * L
close(exp, 0.315)
close(exp * 250, 78.75)
close(exp * 250 * 40, 3150)
close(1 / (1 + b), 1 / 3)
has(t, "0.45", "2.0", "+0.315R", usd(78.75), usd(3150, 0), "33.3%", "11.7 percentage points", "32.4R", "19.8R", "12.6R")
for bb, be in [(0.5, "66.7"), (1.0, "50.0"), (1.5, "40.0"), (2.0, "33.3"), (3.0, "25.0")]:
    assert f"{100 / (1 + bb):.1f}" == be
    has(t, f"| {be}% |")
close(0.7 * 0.3 - 0.3 * 1.0, -0.09)
has(t, "-0.09R")
se = math.sqrt(0.45 * 0.55 / 40)
assert f"{se:.4f}" == "0.0787"
lo, hi = 0.45 - 1.96 * se, 0.45 + 1.96 * se
assert f"{196 * se:.1f}" == "15.4" and f"{lo * 100:.1f}" == "29.6" and f"{hi * 100:.1f}" == "60.4"
has(t, "0.0787", "7.9 percentage points", "15.4 points", "29.6% to 60.4%")
r = np.array([2.0, -1.0, -0.5, 0.3, 3.1, 1.4, -1.0, -1.0])
wins, losses = r[r > 0], -r[r < 0]
pp = len(wins) / len(r)
e2 = pp * wins.mean() - (1 - pp) * losses.mean()
close(e2, r.mean())
assert round(float(e2), 4) == 0.4125
has(t, "0.4125R")
close(0.40 * 2.4 - 0.60 * 1.0, 0.36)
close(0.45 * 1.5 - 0.55, 0.125)
close(0.125 * 200 * 100, 2500)
assert f"{math.sqrt(0.62 * 0.38 / 25) * 100:.1f}" == "9.7"
has(t, "+0.36R", "40.0%", "+0.125R", usd(25.0), usd(2500, 0), "0.0971", "9.7 percentage points")

# ---- Lesson 4
t = lesson(F, 4)
risk = 0.01 * 25_000
shares = math.floor(risk / (48.20 - 46.70))
assert shares == 166
close(166 * 48.20, 8001.20)
assert f"{166 * 48.2 / 25000 * 100:.1f}" == "32.0"
close(166 * 1.5 / 25000 * 100, 0.996)
close(167 * 1.5, 250.5)
has(t, "166 shares", usd(risk), "US$1.50", "166.67", usd(8001.20), "32.0%", usd(249), "0.996%", "US$250.50", "US$1.00")
for sd, n, cost, loss in [(0.75, 333, 16050.60, 249.75), (1.50, 166, 8001.20, 249.00), (3.00, 83, 4000.60, 249.00), (5.00, 50, 2410.00, 250.00)]:
    assert math.floor(250 / sd) == n
    close(n * 48.20, cost)
    close(n * sd, loss)
    has(t, f"| {usd(sd)} | {n} | {usd(cost)} | {usd(loss)} |")
assert math.floor(250 / 0.30) == 833
close(518 * 1.5, 777)
has(t, "518 shares", usd(777, 0), "3.1%", usd(155.40))
ca = 0.01 * 30_000
usd_risk = ca / 1.37
assert f"{usd_risk:.2f}" == "218.98"
sh = math.floor(usd_risk / 1.5)
assert sh == 145 and f"{usd_risk / 1.5:.2f}" == "145.99"
close(145 * 48.2, 6989.0)
assert f"{145 * 48.2 * 1.37:.2f}" == "9574.93"
close(145 * 1.5, 217.5)
assert round(145 * 1.5 * 1.37) == 298
assert f"{146 * 1.5 * 1.37:.2f}" == "300.03"
has(t, cad(300), "US$218.98", "145.99", "145 shares", usd(6989), cad(9574.93), usd(217.5), "about C$298", "C$300.03")
assert math.floor(0.005 * 40_000 / 1.20) == 166
close(166 * 27.60, 4581.60)
close(25_000 / 48.20, 518.6721991701245)
close(518 * 0.30, 155.4)
assert f"{518 * 0.30 / 25000 * 100:.2f}" == "0.62"
close(833 * 48.20, 40150.6)
has(t, usd(4581.60), usd(40150.60), "518.67", "0.62%", "133 shares")
assert math.floor(200 / 1.5) == 133
assert math.floor(150 / 1.40 / 1.0) == 107
assert f"{150 / 1.4:.2f}" == "107.14" and f"{107 * 1.40:.2f}" == "149.80"
has(t, "US$107.14", "107 shares", cad(149.80))


def position_size(account, risk_pct, entry, stop, fx=1.0):
    return math.floor(account * risk_pct / 100 / fx / (entry - stop))


assert position_size(25_000, 1, 48.20, 46.70) == 166
assert position_size(30_000, 1, 48.20, 46.70, fx=1.37) == 145
has(t, "166 and then 145")

# ---- Lesson 5
t = lesson(F, 5)
bs = pd.DataFrame(bars("stock-a-pullback"), columns=["date", "open", "high", "low", "close", "volume"])
prev = bs["close"].shift()
tr = pd.concat([bs["high"] - bs["low"], (bs["high"] - prev).abs(), (bs["low"] - prev).abs()], axis=1).max(axis=1)
bs["atr"] = tr.rolling(14).mean()
row = bs[bs["date"] == "2026-02-25"].iloc[0]
assert round(row["atr"], 4) == 0.7971 and f"{row['atr']:.2f}" == "0.80"
stop_atr = row["close"] - 2 * row["atr"]
assert f"{stop_atr:.2f}" == "46.61" and f"{2 * row['atr']:.3f}" == "1.594"
close(0.25 * 0.80, 0.20)
close(46.90 - 0.20, 46.70)
assert by_date["2026-02-18"][3] == 47.19 and by_date["2026-02-20"][3] == 47.93
assert math.floor(250 / 1.5) == 166 and math.floor(250 / (2 * row["atr"])) == 156
assert f"{48.20 - stop_atr:.2f}" == "1.59"
assert abs((46.70 - 46.61) - 0.09) < 1e-9
has(t, "46.90", "47.19", "47.93", "46.70", "0.7971", "46.61", "US$1.59", "156 shares", "166 shares", "1.594", "nine cents")
close(31.10 - 0.15, 30.95)
close(32.50 - 30.95, 1.55)
close(max(52.40 - 51.50, abs(52.40 - 50.80), abs(51.50 - 50.80)), 1.6)
close(60 - 2 * 1.2, 57.6)
close(300 / 2.4, 125)
assert f"{2.10 / 1.80:.2f}" == "1.17"
has(t, "US$30.95", "US$1.55", "US$1.60", "US$57.60", "125", "1.17 ATRs")

# ---- Lesson 6
t = lesson(F, 6)
close((48.20 - 46.55) * 166, 273.90)
close(1.65 / 1.5, 1.10)
close((48.20 - 45.10) * 166, 514.60)
assert f"{3.10 / 1.5:.2f}" == "2.07" and f"{514.6 / 25000 * 100:.2f}" == "2.06"
gd = bars("stock-a-gap-down")
gd_by = {b[0]: b for b in gd}
assert gd_by["2026-04-15"][4] == 48.20 and gd_by["2026-04-16"][1] == 45.10
close(46.70 - 45.10, 1.60)
has(t, usd(249), usd(273.90), "-1.10R", usd(514.60), "-2.07R", "2.06%", "1.0%", "1.60 below the stop", "3.10 below")
close(0.04 * 166, 6.64)
assert f"{6.64 / 249:.2f}" == "0.03" and f"{2 / 249:.2f}" == "0.01"
close(166 * 0.005, 0.83)
fx_in, fx_out = 0.015 * 8001.20, 0.015 * 51.20 * 166
assert f"{fx_in:.2f}" == "120.02" and f"{fx_out:.2f}" == "127.49" and f"{fx_in + fx_out:.2f}" == "247.51"
assert f"{(fx_in + fx_out) / 249:.2f}" == "0.99"
assert f"{498 - (fx_in + fx_out):.2f}" == "250.49" and f"{(498 - fx_in - fx_out) / 249:.2f}" == "1.01"
has(t, usd(6.64), "0.83", usd(2.0), "120.02 + 127.49", usd(247.51), "498.00 - 247.51", usd(250.49), "+1.01R", "0.99R")
close(0.315 - 0.035, 0.28)
assert f"{(6.64 + 2.00) / 249:.3f}" == "0.035"
has(t, "0.28R", "0.035R")
close(2.00 * 166, 332)
close(2.00 / 1.5, 1.3333333333333333)
close((20 - 17.60) * 250, 600)
close(2.40 / 1.00, 2.4)
close(0.04 / 0.5, 0.08)
close(0.04 / 2.0, 0.02)
close(1.5 / 2.5, 0.6)
has(t, usd(332), "-1.33R", usd(600), usd(250), "-2.40R", "0.08R", "0.02R", "0.6%", "1.5%")

# ---- Lesson 7
t = lesson(F, 7)
pos = [(166, 49.10, 46.70, 398.40), (80, 61.40, 59.50, 152.00), (300, 12.80, 11.90, 270.00), (55, 93.00, 90.00, 165.00)]
tot = 0
for n, pr, st, want in pos:
    close(n * (pr - st), want)
    tot += n * (pr - st)
    has(t, usd(want))
close(tot, 985.40)
assert f"{tot / 25000 * 100:.2f}" == "3.94"
close(tot + 250, 1235.40)
assert f"{(tot + 250) / 25000 * 100:.2f}" == "4.94"
has(t, usd(985.40), "3.94%", usd(250), usd(1235.40), "4.94%")
n, rho = 4, 0.8
assert f"{n / (1 + (n - 1) * rho):.2f}" == "1.18" and f"{math.sqrt(n + n * (n - 1) * rho):.2f}" == "3.69"
assert f"{8 / (1 + 7 * 0.4):.1f}" == "2.1"
has(t, "1.18", "3.69", "4 / 3.4", "sqrt(13.6)", "2.1 effective")
rng = np.random.default_rng(5)
n_days = 4000
market = rng.normal(0, 0.01, n_days)
returns = pd.DataFrame({nm: 0.8 * market + 0.6 * rng.normal(0, 0.01, n_days) for nm in ["A", "B", "C", "D"]})
corr = returns.corr().to_numpy()
nn = len(corr)
avg = corr[np.triu_indices(nn, 1)].mean()
eff = nn / (1 + (nn - 1) * avg)
assert round(avg, 2) == 0.63 and round(eff, 2) == 1.38
has(t, "0.63 and 1.38")
close(300 + 450 + 520 + 230, 1500)
close(1500 / 40000 * 100, 3.75)
close(0.05 * 20_000 - 850, 150)
close(150 / 1.5, 100)
assert f"{5 / (1 + 4 * 0.6):.2f}" == "1.47" and f"{math.sqrt(5 + 20 * 0.6):.2f}" == "4.12" and f"{math.sqrt(5):.2f}" == "2.24"
close(200 * (55 - 50), 1000)
close(200 * (55 - 53), 400)
has(t, usd(1500, 0), "3.75%", usd(1000, 0), usd(150, 0), "100", "1.47", "4.12", "2.24", usd(400, 0), usd(600, 0), "sqrt(17)")

# ---- Lesson 8
t = lesson(F, 8)
eq = np.array([10000, 10600, 10200, 11200, 9800, 10300.0])
pk = np.maximum.accumulate(eq)
close(((pk - eq) / pk).max(), 0.125)
assert f"{(10600 - 10200) / 10600 * 100:.1f}" == "3.8" and f"{(11200 / 9800 - 1) * 100:.1f}" == "14.3"
has(t, "12.5%", "3.8%", "14.3%")
rr = sim.outcomes(paths=1, seed=7)
fin = {}
for f_ in sim.LEVELS:
    e = sim.curves(rr, f_)[0]
    fin[f_] = (e[-1], sim.max_drawdown(e[None, :])[0])
assert [round(fin[f_][0]) for f_ in sim.LEVELS] == [18533, 32829, 140475]
assert [f"{fin[f_][1] * 100:.1f}" for f_ in sim.LEVELS] == ["6.0", "12.0", "29.6"]
has(t, "US$18,533", "US$32,829", "US$140,475", "6.0%, 12.0% and 29.6%")
want = {0.01: ("19,674", "9.0", "0.00", "0.00"), 0.02: ("36,972", "17.9", "3.55", "0.00"), 0.05: ("188,338", "40.1", "91.40", "1.38")}
for f_, (fin_, dd, d30, half) in want.items():
    s = sim.stats(f_)
    assert f"{s['median_final']:,.0f}" == fin_, s
    assert f"{s['median_maxdd'] * 100:.1f}" == dd
    assert f"{s['p_dd30'] * 100:.2f}" == d30
    assert f"{s['p_half'] * 100:.2f}" == half
    has(t, f"| US${fin_} | {dd}% | {d30}% | {half}% |")
has(t, "91.4%", "66.7%", "40%")
close((0.45 / 0.55) ** 20, 0.018071595021380355)
assert f"{(0.45 / 0.55) ** 100:.1e}" == "1.9e-09"
has(t, "1.8%", "1.9 x 10^-9")
close((22000 - 17600) / 22000, 0.20)
assert f"{0.179 / (1 - 0.179) * 100:.1f}" == "21.8"
assert f"{(0.45 / 0.55) ** 50:.7f}" == "0.0000439" and f"{(0.48 / 0.52) ** 50:.4f}" == "0.0183"
assert round((0.48 / 0.52) ** 50 / (0.45 / 0.55) ** 50) == 416
has(t, "20.0%", "21.8%", "0.0000439", "0.0183", "416")
rng = np.random.default_rng(1)
w = rng.random((2000, 200)) < 0.45
r2 = np.where(w, 2.0, -1.0)
meds = []
for risk_ in (0.01, 0.02, 0.05):
    e = 10_000 * np.cumprod(1 + risk_ * r2, axis=1)
    p_ = np.maximum.accumulate(e, axis=1)
    meds.append(round(float(np.median(((p_ - e) / p_).max(axis=1))), 3))
assert meds == [0.089, 0.174, 0.401], meds
has(t, "0.089, 0.174 and 0.401")

# ---- Lesson 9
t = lesson(F, 9)
close(kelly(0.55, 1), 0.10)
gs = [growth(0.55, 1, f) for f in (0.05, 0.10, 0.20)]
assert [f"{g_ * 100:.4f}" for g_ in gs] == ["0.3753", "0.5008", "-0.0138"], gs
assert f"{gs[0] / gs[1] * 100:.0f}" == "75"
has(t, "0.00501", "0.00375", "-0.00014", "75%", "0.3753, 0.5008 and -0.0138")
g_true = growth(0.50, 1, 0.10)
assert f"{g_true:.5f}" == "-0.00503"
has(t, "-0.00503")
close(kelly(0.45, 2), 0.175)
has(t, "0.175", "8.75%", "17.5%")
for f_, dd, half in [(0.05, "40.1", "1.4"), (0.0875, "61.7", "11.4"), (0.175, "89.4", "45.4")]:
    s = sim.stats(f_)
    assert f"{s['median_maxdd'] * 100:.1f}" == dd and f"{s['p_half'] * 100:.1f}" == half, (f_, s)
    has(t, f"| {dd}% | {half}% |")
close(kelly(0.40, 2.5), 0.16)
close(kelly(0.30, 2), -0.05)
close(0.30 * 2 - 0.70, -0.10)
assert f"{growth(0.60, 1, 0.20):.5f}" == "0.02014"
g_half = growth(0.50, 1, 0.05)
assert f"{g_half:.5f}" == "-0.00125" and f"{g_half / g_true:.2f}" == "0.25"
has(t, "0.16", "-0.05", "-0.10R", "0.02014", "-0.00125")

# ---- Lesson 10
t = lesson(F, 10)
close(0.01 * 25_000, 250)
close(0.05 * 25_000, 1250)
close(0.02 * 25_000, 500)
close(25_000 * 0.90, 22_500)
close(22_500 * 0.005, 112.5)
close(25_000 * 0.85, 21_250)
assert f"{(1 / 0.9 - 1) * 100:.1f}" == "11.1"
has(t, usd(250, 0), usd(1250, 0), usd(500, 0), usd(22500, 0), usd(112.50), usd(21250, 0), "11.1%")
close(0.01 * 30_000, 300)
close(0.05 * 30_000, 1500)
close(2 * 300, 600)
close((30000 - 26400) / 30000, 0.12)
close(0.005 * 26_400, 132)
has(t, usd(300, 0), usd(1500, 0), usd(600, 0), "12.0%", usd(132.00))
assert f"{0.40 / 0.60 * 100:.1f}" == "66.7"
close((21.60 - 20.00) / (20.00 - 19.20), 2.0)
close(0.35 * 2.5 - 0.65, 0.225)
assert f"{100 / 3.5:.1f}" == "28.6"
has(t, "66.7%", "+2.0R", "+0.225R", "28.6%")
q4 = 0.005 * 20_000 / 1.40
assert f"{q4:.2f}" == "71.43" and math.floor(q4 / 2.0) == 35 and f"{q4 / 2:.2f}" == "35.71"
has(t, "71.43", "35.71", "35 shares")
close(300 + 450 + 200, 950)
close(950 / 20000 * 100, 4.75)
close(1050 / 20000 * 100, 5.25)
has(t, "4.75%", usd(1050, 0), "5.25%", usd(50, 0))
close(kelly(0.5, 2), 0.25)
has(t, "25%", "12.5%", "one twenty-fifth")
close((60 - 55) / (60 - 58), 2.5)
close((12000 - 10200) / 12000, 0.15)
assert f"{(12000 / 10200 - 1) * 100:.1f}" == "17.6"
has(t, "-2.5R", "15.0%", "17.6%")
