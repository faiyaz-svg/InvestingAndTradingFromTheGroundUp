"""Number checks for part 16, Volatility and event trading."""
import math
import sys

import numpy as np
import pandas as pd

from _lib import ROOT, lesson, has, usd

F = "16-volatility-and-event-trading"
sys.path.insert(0, str(ROOT / "tools" / "figures" / F))
import vol_data  # noqa: E402
from vol_data import bs  # noqa: E402

R = 0.04


def close(a, b, tol=1e-9):
    assert abs(a - b) <= tol, (a, b)


def r4(x):
    return f"{x:.4f}"


DATA = ROOT / "docs" / "assets" / "data"
S252 = math.sqrt(252)

# ---------------------------------------------------------------- lesson 1
t = lesson(F, 1)
cl = [50.00, 50.80, 50.10, 51.20, 50.60, 51.40]
r = np.diff(np.log(cl))
s = r.std(ddof=1)
sig = s * S252
assert [f"{x:.5f}" for x in r] == ["0.01587", "-0.01388", "0.02172", "-0.01179", "0.01569"]
assert f"{r.mean():.5f}" == "0.00552" and f"{s:.6f}" == "0.016946" and f"{sig:.4f}" == "0.2690"
has(t, "0.01587, -0.01388, 0.02172, -0.01179, 0.01569", "0.00552", "0.016946", "0.2690", "26.9%", "15.87")
st = vol_data.stats()
assert f"{st['iv_mean']:.1f}" == "30.8" and f"{st['fwd_mean']:.1f}" == "26.2" and f"{st['share_iv_above'] * 100:.0f}" == "77"
close(round(st["iv_mean"] - st["fwd_mean"], 1), 4.6)
close(round(0.308**2 - 0.262**2, 4), 0.0262)
has(t, "30.8%", "26.2%", "77%", "4.6 points", "0.0262")
b = pd.read_csv(DATA / "index-x-regimes.csv")
lr = np.log(b["close"]).diff()


def ann(x):
    return x.dropna().std() * S252 * 100


assert f"{ann(lr.iloc[0:70]):.1f}" == "7.6" and f"{ann(lr.iloc[70:105]):.1f}" == "25.0"
assert f"{0.012 * S252:.4f}" == "0.1905"
has(t, "0.1905", "19.0%")
close(0.36**2 - 0.28**2, 0.0512)
has(t, "0.1296", "0.0784", "0.0512", "8 volatility points")
assert f"{math.log(82 / 80):.5f}" == "0.02469"
has(t, "0.02469", "2.47%", "2.50%")
assert f"{36 / S252:.2f}%" == "2.27%" and f"{28 / S252:.2f}%" == "1.76%"
has(t, "2.27%", "1.76%")
close(S252, 15.8745, 1e-4)

# ---------------------------------------------------------------- lesson 2
t = lesson(F, 2)
for v, m30, d1 in ((14.5, "4.16%", "0.91%"), (20, "5.73%", "1.26%"), (31, "8.89%", "1.95%"), (25, "7.17%", "1.57%")):
    assert f"{v * math.sqrt(30 / 365):.2f}%" == m30 and f"{v / S252:.2f}%" == d1
    has(t, m30, d1)
has(t, "0.2867")
c = vol_data.CONTANGO
m = (c["spot"] - c["futures"][0]) / c["futures"][0]
assert c["spot"] == 14.5 and c["futures"][0] == 15.8 and f"{m:.4f}" == "-0.0823" and f"{(1 + m) ** 12 - 1:.3f}" == "-0.643"
has(t, "-0.0823", "-8.2%", "-0.643", "-64.3%", "14.50", "15.80")
assert f"{(18.0 - 19.4) / 19.4:.4f}" == "-0.0722"
has(t, "-0.0722", "-7.2%")
assert round(vol_data.BACKWARDATION["spot"] - vol_data.BACKWARDATION["futures"][0], 1) == 2.1
has(t, "2.1 points", "18.6", "23.6")

# ---------------------------------------------------------------- lesson 3
t = lesson(F, 3)
rv = lr.rolling(20).std() * S252 * 100
med = rv.shift(1).rolling(120, min_periods=30).median()
ratio = rv / med
high = ratio > 1.5
assert str(b["date"][high].iloc[0]) == "2026-04-15" and str(b["date"][high].iloc[-1]) == "2026-06-26" and int(high.sum()) == 53
assert high.iloc[72:125].all()
assert f"{ratio.iloc[69]:.2f}" == "0.84" and f"{ratio.iloc[72]:.2f}" == "1.63" and f"{rv.iloc[72]:.1f}" == "13.3" and f"{med.iloc[72]:.1f}" == "8.2"
assert f"{ratio.iloc[125]:.2f}" == "1.35" and f"{rv.iloc[125]:.1f}" == "18.0" and not high.iloc[125]
assert f"{rv.iloc[69]:.1f}" == "6.9" and f"{rv.iloc[104]:.1f}" == "25.0"
assert f"{med.iloc[124]:.2f}" == "11.93" and f"{med.iloc[125]:.2f}" == "13.33" and f"{rv.iloc[125]:.2f}" == "17.97"
assert f"{b['close'][70]:.2f}" == "5234.34" and f"{b['close'][104]:.2f}" == "4138.13"
has(t, "0.84", "1.63", "13.3%", "8.2", "53 trading days", "June 26", "1.35", "18.0%", "6.9%", "25.0%", "5,234.34", "4,138.13",
    "11.93", "13.33", "17.97 / 13.33 = 1.35", "13.33 / 8.20 = 1.63")
prev = b["close"].shift(1)
tr = pd.concat([b["high"] - b["low"], (b["high"] - prev).abs(), (b["low"] - prev).abs()], axis=1).max(axis=1)
tr.iloc[0] = b["high"].iloc[0] - b["low"].iloc[0]
atr = pd.Series(np.nan, index=b.index)
atr.iloc[13] = tr.iloc[:14].mean()
for i in range(14, len(b)):
    atr.iloc[i] = (atr.iloc[i - 1] * 13 + tr.iloc[i]) / 14
assert f"{atr.iloc[69]:.1f}" == "39.4" and f"{atr.iloc[69] / b['close'][69] * 100:.2f}" == "0.75"
assert f"{atr.iloc[89]:.1f}" == "95.0" and f"{atr.iloc[89] / b['close'][89] * 100:.1f}" == "2.1"
assert f"{atr.iloc[104]:.1f}" == "114.1" and f"{atr.iloc[104] / b['close'][104] * 100:.1f}" == "2.8"
assert str(b["date"][89]) == "2026-05-08" and f"{b['close'][89]:.2f}" == "4522.37"
has(t, "39.4", "0.75%", "95.0", "2.1%", "114.1", "2.8%")
S0 = 60.00
atr_n, atr_h = 0.0075 * S0, 0.021 * S0
close(atr_n, 0.45)
close(atr_h, 1.26)
stop_n = 2 * atr_n
sh_n = int(250 / stop_n)
assert f"{250 / stop_n:.1f}" == "277.8" and sh_n == 277 and f"{sh_n * stop_n:.2f}" == "249.30"
close(S0 - stop_n, 59.10)
close(S0 + 2 * stop_n, 61.80)
stop_h = 2 * atr_h
sh_h = int(125 / stop_h)
assert f"{125 / stop_h:.1f}" == "49.6" and sh_h == 49 and f"{sh_h * stop_h:.2f}" == "123.48"
close(S0 - stop_h, 57.48)
close(S0 + 2 * stop_h, 65.04)
assert round((1 - 49 / 277) * 100) == 82
has(t, "0.90", "59.10", "277.8", "277 shares", "US$249.30", "61.80", "2.52", "57.48", "125 / 2.52 = 49.6", "49 shares", "US$123.48", "65.04", "82%")
assert 10 / 25 == 0.4 and min(1, 10 / 7.6) == 1
has(t, "10 / 25 = 0.40", "0.40")
assert int(125 / 1.60) == 78 and f"{125 / 1.6:.1f}" == "78.1"
has(t, "78.1", "78 shares")

# ---------------------------------------------------------------- lesson 4
t = lesson(F, 4)
SA, KA, TA, IVA = 60.51, 60.50, 7 / 365, 0.55
ca, pa = bs.price(SA, KA, TA, R, IVA), bs.price(SA, KA, TA, R, IVA, kind="put")
assert (r4(ca), r4(pa), r4(round(ca, 4) + round(pa, 4))) == ("1.8657", "1.8093", "3.6750")
stra = round(ca, 4) + round(pa, 4)
assert f"{stra / SA:.4f}" == "0.0607"
close(round(KA - stra, 2), 56.83)
close(round(KA + stra, 2), 64.17)
S1, T1 = 54.15, 4 / 365
c1, p1 = bs.price(S1, KA, T1, R, 0.32), bs.price(S1, KA, T1, R, 0.32, kind="put")
assert (r4(c1), r4(p1)) == ("0.0002", "6.3237")
post = round(c1, 4) + round(p1, 4)
assert f"{post:.4f}" == "6.3239" and f"{post - stra:.4f}" == "2.6489" and f"{(post - stra) / stra * 100:.0f}" == "72"
assert f"{(S1 / SA - 1) * 100:.1f}" == "-10.5" and f"{(54.82 / SA - 1) * 100:.1f}" == "-9.4"
flat = bs.price(SA, KA, T1, R, 0.32) + bs.price(SA, KA, T1, R, 0.32, kind="put")
assert f"{flat:.4f}" == "1.6170" and f"{stra - flat:.4f}" == "2.0580" and f"{(stra - flat) / stra * 100:.0f}" == "56"
has(t, "1.8657", "1.8093", "3.6750", usd(367.50), "6.1%", "56.83", "64.17", "0.0002", "6.3237", "6.3239", "2.6489", usd(264.89),
    "10.5%", "54.82", "9.4%", "1.6170", "2.0580", usd(205.80), "-56%", "1.47R")
assert f"{3.675 * 100 / 250:.2f}" == "1.47"
SB, KB, IVB = 47.28, 47.50, 0.50
cb, pb = bs.price(SB, KB, TA, R, IVB), bs.price(SB, KB, TA, R, IVB, kind="put")
assert (r4(cb), r4(pb)) == ("1.2186", "1.4022")
strb = round(cb, 4) + round(pb, 4)
assert f"{strb:.4f}" == "2.6208" and f"{strb / SB:.3f}" == "0.055"
cb1, pb1 = bs.price(48.23, KB, T1, R, 0.30), bs.price(48.23, KB, T1, R, 0.30, kind="put")
assert (r4(cb1), r4(pb1)) == ("1.0482", "0.2974")
postb = round(cb1, 4) + round(pb1, 4)
assert f"{postb:.4f}" == "1.3456" and f"{postb - strb:.4f}" == "-1.2752" and f"{(postb - strb) / strb * 100:.1f}" == "-48.7"
assert f"{(48.23 / SB - 1) * 100:.1f}" == "2.0" and f"{(48.13 / SB - 1) * 100:.1f}" == "1.8"
has(t, "1.2186", "1.4022", usd(262.08), "2.6208", "5.5%", "48.13", "1.0482", "0.2974", "1.3456", "-1.2752", "-US$127.52", "-48.7%")
legs = (("p42.5", 42.5, "put", 0.0810, 0.0), ("p45", 45, "put", 0.4371, 0.0067), ("c50", 50, "call", 0.4067, 0.0989),
        ("c52.5", 52.5, "call", 0.1007, 0.0017))
for k, K, kind, now, aft in legs:
    assert r4(bs.price(SB, K, TA, R, IVB, kind=kind)) == f"{now:.4f}", k
    assert r4(bs.price(48.23, K, T1, R, 0.30, kind=kind)) == f"{aft:.4f}", k
credit = 0.4371 + 0.4067 - 0.0810 - 0.1007
assert f"{credit:.4f}" == "0.6621"
maxloss = (2.50 - 0.6621) * 100
assert f"{maxloss:.2f}" == "183.79" and f"{maxloss / 250:.2f}" == "0.74" and int(250 / maxloss) == 1
back = 0.0067 + 0.0989 - 0.0017
assert f"{back:.4f}" == "0.1039" and f"{credit - back:.4f}" == "0.5582" and f"{(credit - back) * 100 / 250:.2f}" == "0.22"
has(t, "0.0810", "0.4371", "0.4067", "0.1007", "0.6621", usd(66.21), usd(183.79), "0.74R", "0.1039", "0.5582", usd(55.82), "0.22R", "1.36")
assert f"{250 / maxloss:.2f}" == "1.36" and f"{262.08 / 250:.2f}" == "1.05"
assert f"{3.0 / 5.5:.2f}" == "0.55"
has(t, "0.0607", "0.55", "1.05R")

# ---------------------------------------------------------------- lesson 5
t = lesson(F, 5)
f5 = pd.read_csv(DATA / "index-x-fomc-5m.csv")
f5["rng"] = f5["high"] - f5["low"]
morning = f5["rng"].iloc[:54].mean()
assert f"{morning:.2f}" == "3.06" and f"{f5['rng'].iloc[54]:.2f}" == "25.02" and f"{f5['rng'].iloc[55]:.2f}" == "34.15"
assert f"{f5['rng'].iloc[54] / morning:.1f}" == "8.2"
assert f"{f5['high'].iloc[:54].max() - f5['low'].iloc[:54].min():.0f}" == "13"
assert str(f5["datetime"][54]) == "2026-10-28 14:00" and f"{f5['high'][54]:.2f}" == "5025.53" and f"{f5['low'][54]:.2f}" == "5000.51"
assert f"{f5['close'][54]:.2f}" == "5022.53"
assert f"{f5['low'][55]:.2f}" == "4991.39" and f"{f5['low'].min():.2f}" == "4947.74" and f"{f5['close'].iloc[-1]:.2f}" == "4962.00"
assert f"{f5['high'][55]:.2f}" == "5025.54" and f5["high"].iloc[56:].max() < 5026.0
assert str(f5["datetime"][61]) == "2026-10-28 14:35" and f"{f5['low'][61]:.2f}" == "4949.95" and f5["low"][60] > 4958.50 > f5["low"][61]
has(t, "3.1 points", "25.0 points", "34.1", "13-point", "5,025.53", "4,947.74", "5,000.51", "4,991.39", "4,962.00", "4,949.95",
    "3.06", "25.02", "8.2 times")
entry = 4999.00
risk_pts = 5026.00 - entry
risk = risk_pts * 5
assert risk_pts == 27 and risk == 135 and f"{250 / risk:.2f}" == "1.85" and int(250 / risk) == 1
tgt = entry - 1.5 * risk_pts
assert tgt == 4958.50 and (entry - tgt) * 5 == 202.5
assert (5029.00 - entry) * 5 == 150 and f"{150 / 135:.2f}" == "1.11"
has(t, "27.00 points", usd(135, 0), "1.85", "4,958.50", usd(202.50), "1.5R", "5,029.00", usd(150, 0), "1.11R", "4,999.00", "5,026.00")

# ---------------------------------------------------------------- lesson 6
t = lesson(F, 6)
g30 = bs.greeks(50, 50, 30 / 365, R, 0.30)["gamma"]
g1 = bs.greeks(50, 50, 1 / 365, R, 0.30)["gamma"]
assert r4(g30) == "0.0925" and r4(g1) == "0.5081"
assert round(200_000 * 0.0925) == 18_500 and round(200_000 * 0.5081) == 101_620 and f"{0.5081 / 0.0925:.1f}" == "5.5"
has(t, "0.0925", "0.5081", "18,500", "101,620", "5.5 times")
import json  # noqa: E402

ia = json.loads((ROOT / "docs" / "assets" / "charts" / F / "stock-b-index-add.json").read_text(encoding="utf-8"))["bars"]
bars = {x[0]: x for x in ia}
assert bars["2026-07-03"][4] == 33.03 and bars["2026-07-06"][1] == 35.18 and bars["2026-07-13"][4] == 37.0
assert bars["2026-07-17"][4] == 35.70 and bars["2026-08-11"][4] == 33.75 and bars["2026-07-06"][4] == 35.08
assert f"{(35.18 / 33.03 - 1) * 100:.1f}" == "6.5" and f"{(35.70 / 33.03 - 1) * 100:.1f}" == "8.1"
assert f"{(33.75 / 33.03 - 1) * 100:.1f}" == "2.2" and f"{(33.75 / 35.08 - 1) * 100:.1f}" == "-3.8"
has(t, "33.03", "35.18", "+6.5%", "37.00", "35.70", "33.75", "8.1%", "2.2%", "3.8%", "35.08")
assert 30 - 24 == 6 and f"{20 / S252:.2f}%" == "1.26%" and f"{(18.5 - 20) / 20:.3f}" == "-0.075" and f"{15 / 9:.2f}" == "1.67"
assert f"{4.10 / 82:.2f}" == "0.05" and 22 * 5 == 110 and int(200 / 110) == 1 and 26 * 5 == 130 and 130 / 200 == 0.65
assert 100_000 * 0.0925 == 9_250
assert f"{44 / 37 - 1:.3f}" == "0.189" and round(44 / 40 - 1, 4) == 0.1 and 500 * 100 * 0.0925 == 4625
import datetime  # noqa: E402

assert datetime.date(2026, 12, 18).weekday() == 4 and 15 <= 18 <= 21
has(t, "+18.9%", "10.0%", "4,625", "December 18, 2026")
has(t, "1.26%", "-0.075", "1.67", "5.0%", "US$110", "US$130", "0.65R", "9,250")

# ---------------------------------------------------------------- the expected-move figure agrees with lesson 4
from expected_move import STRADDLE  # noqa: E402

assert r4(STRADDLE) == "3.6750"
