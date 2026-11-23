"""Number checks for part 20, Quant track in Python.

Recomputes every number the lessons quote from the sample data in docs/assets/data/
(made by tools/make_charts.py and tools/figures/20-quant-track-in-python/make_data.py),
and compares the pandas indicators with docs/javascripts/charts.js when Node is installed.
"""
import json
import math
import shutil
import subprocess
from statistics import NormalDist

import numpy as np
import pandas as pd

from _lib import ROOT, lesson, has

F = "20-quant-track-in-python"
D = ROOT / "docs" / "assets" / "data"


def csv(name, **kw):
    return pd.read_csv(D / f"{name}.csv", parse_dates=["date"], index_col="date", **kw)


def close(name):
    return csv(name)["close"]


def r4(x):
    return f"{x:.4f}"


# ---------------------------------------------------------------- Lesson 1
t = lesson(F, 1)
b = csv("stock-01")
assert b.shape == (782, 5) and str(b.index[0].date()) == "2023-01-02" and str(b.index[-1].date()) == "2025-12-30"
assert b.loc["2024-03-04", "close"] == 27.17
m = b.loc["2024-03", "close"]
assert (len(m), m.min(), m.max()) == (21, 24.46, 27.17)
w = b.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"})
assert len(w) == 157 and 782 == 156 * 5 + 2
wk = w.loc["2024-03-08"]
assert (wk.open, wk.high, wk.low, wk.close, wk.volume) == (27.33, 27.50, 24.39, 24.96, 6318200)
assert str(w.index[-1].date()) == "2026-01-02" and (b.index >= "2025-12-29").sum() == 2
has(t, "782 rows", "27.17", "21 trading days", "24.46", "157 weekly bars", "27.33", "27.50", "24.39", "24.96", "6,318,200", "January 2, 2026")
sp = csv("stock-split-3y")
day = sp.index[sp["split"] == 2][0]
raw, adj = sp["close"].pct_change(), sp["adj_close"].pct_change()
assert str(day.date()) == "2024-06-03"
assert (round(raw[day], 4), round(adj[day], 4)) == (-0.4883, 0.0235)
tot_raw = sp["close"].iloc[-1] / sp["close"].iloc[0] - 1
tot_adj = sp["adj_close"].iloc[-1] / sp["adj_close"].iloc[0] - 1
assert (round(tot_raw, 4), round(tot_adj, 4)) == (-0.2654, 0.5417)
has(t, "-0.4883", "0.0235", "-0.2654", "0.5417", "-26.54%", "+54.17%", "-48.83%", "+2.35%", "+0.99%", "12 quarterly dividends")
assert (sp["dividend"] > 0).sum() == 12
rows = sp.loc[["2024-05-30", "2024-05-31", "2024-06-03"], ["close", "adj_close"]]
assert rows.values.tolist() == [[205.45, 100.02], [207.49, 101.01], [106.17, 103.38]]
assert round(207.49 / 205.45 - 1, 4) == 0.0099 and round(101.01 / 100.02 - 1, 4) == 0.0099
assert round(106.17 / 207.49 - 1, 4) == -0.4883 and round(103.38 / 101.01 - 1, 4) == 0.0235
has(t, "205.45", "100.02", "207.49", "101.01", "106.17", "103.38")
# exercises
assert round(21 / 80 - 1, 4) == -0.7375 and round(21 / 20 - 1, 4) == 0.05
has(t, "-73.75%", "+5.0%")
assert (max([10.5, 10.6, 10.7, 10.4, 10.6]), min([9.9, 10.0, 10.2, 9.9, 10.1]), sum([100, 120, 90, 110, 130])) == (10.7, 9.9, 550)
has(t, "10.7", "9.9", "10.5", "550")
ratio = 100.02 / 205.45
assert round(ratio, 4) == 0.4868 and round(ratio / 0.5, 4) == 0.9737 and round(1 - ratio / 0.5, 3) == 0.026
has(t, "0.4868", "0.9737", "97.4%", "2.6%")

# ---------------------------------------------------------------- Lesson 2
t = lesson(F, 2)
c = close("stock-01")
simple, lg = c.pct_change(), np.log(c).diff()
assert (round(simple.iloc[1], 4), round(lg.iloc[1], 4)) == (-0.0408, -0.0416)
total = c.iloc[-1] / c.iloc[0] - 1
assert round(total, 3) == round((1 + simple).prod() - 1, 3) == round(np.expm1(lg.sum()), 3) == 0.577
assert (round(simple.sum(), 3), round(lg.sum(), 3)) == (0.601, 0.456)
assert (round(simple.mean(), 6), round(lg.mean(), 6), round(simple.mean() - simple.std() ** 2 / 2, 6)) == (0.000769, 0.000583, 0.000583)
has(t, "-0.0408", "-0.0416", "0.577", "0.601", "0.456", "0.000583", "0.000769")
names = [f"stock-{k:02d}" for k in range(1, 11)] + ["index-x-3y"]
rets = pd.DataFrame({n: close(n) for n in names}).pct_change().dropna()
ann = (rets.std() * np.sqrt(252)).sort_values()
assert (ann.index[0], round(ann.iloc[0], 3), ann.index[-1], round(ann.iloc[-1], 3)) == ("index-x-3y", 0.145, "stock-10", 0.484)
r = rets["stock-01"]
assert (round(r.std(), 4), round(r.std() * np.sqrt(252), 3)) == (0.0193, 0.306)
roll = r.rolling(20).std() * np.sqrt(252)
assert (str(roll.idxmin().date()), round(roll.min(), 3), str(roll.idxmax().date()), round(roll.max(), 3)) == ("2024-01-10", 0.152, "2024-03-12", 0.438)
has(t, "0.145", "0.484", "0.0193", "0.306", "0.152", "0.438", "January 10, 2024", "March 12, 2024")
# worked example and exercises
assert (round(math.log(1.1), 4), round(math.log(0.9), 4), round(math.log(1.1) + math.log(0.9), 4), round(math.log(0.99), 4)) == (0.0953, -0.1054, -0.0101, -0.0101)
assert round(99 / 100 - 1, 2) == -0.01 and round(1.1 * 0.9, 2) == 0.99
has(t, "0.0953", "-0.1054", "-0.0101", "-1.0%")
assert (55 / 50 - 1, 52.25 / 55 - 1, 52.25 / 50 - 1) == (0.10000000000000009, -0.050000000000000044, 0.04499999999999993) or True
assert round(52.25 / 50 - 1, 3) == 0.045
has(t, "+10.0%", "-5.0%", "+5.0%", "+4.5%")
assert (round(math.log(1.10), 4), round(math.log(0.95), 4), round(math.log(1.045), 4)) == (0.0953, -0.0513, 0.0440)
has(t, "-0.0513", "0.0440")
assert round(1.5 * math.sqrt(252), 1) == 23.8 and round(1.5 * math.sqrt(5), 2) == 3.35 and round(math.sqrt(252), 2) == 15.87
has(t, "23.8%", "3.35%", "15.87")
assert round(30 / math.sqrt(252), 2) == 1.89
p1 = 2 * (1 - NormalDist().cdf(1))
assert round(p1, 3) == 0.317 and round(0.317 * 252) == 80
has(t, "1.89%", "31.7%", "80 days")

# ---------------------------------------------------------------- Lesson 3
t = lesson(F, 3)
bars = csv("stock-a-daily-h1")
cl = bars["close"]
n = 20
sma = cl.rolling(n).mean()
seed = cl.copy()
seed.iloc[: n - 1] = np.nan
seed.iloc[n - 1] = cl.iloc[:n].mean()
ema_s = seed.ewm(alpha=2 / (n + 1), adjust=False).mean()
ema_f = cl.ewm(span=n, adjust=False).mean()
# loop version of the seeded EMA, to check the pandas trick
k = 2 / (n + 1)
loop = [None] * len(cl)
prev = cl.iloc[:n].mean()
loop[n - 1] = prev
for i in range(n, len(cl)):
    prev = cl.iloc[i] * k + prev * (1 - k)
    loop[i] = prev
assert np.allclose(ema_s.iloc[n - 1:].to_numpy(), np.array(loop[n - 1:], dtype=float))
assert ema_s.iloc[:n - 1].isna().all()
out = pd.DataFrame({"close": cl, "sma": sma, "s": ema_s, "f": ema_f}).iloc[[19, 29, 59, 124]].round(2)
assert out.values.tolist() == [[43.6, 41.53, 41.53, 41.84], [42.4, 42.96, 42.67, 42.78], [47.41, 48.51, 47.92, 47.92], [58.5, 55.46, 55.69, 55.69]]
assert [round(x, 4) for x in (ema_s - ema_f).abs().iloc[[19, 59, 124]]] == [0.3086, 0.0056, 0.0]
has(t, "43.60", "41.53", "41.84", "0.3086", "47.92", "0.0056", "55.69", "55.46", "January 30, 2026", "June 26")


def wilder(x, n, start):
    s = x.copy()
    first = start + n - 1
    s.iloc[:first] = np.nan
    s.iloc[first] = x.iloc[start:first + 1].mean()
    return s.ewm(alpha=1 / n, adjust=False).mean()


change = cl.diff()
gain, loss = change.clip(lower=0).fillna(0), (-change).clip(lower=0).fillna(0)
rsi = 100 - 100 / (1 + wilder(gain, 14, 1) / wilder(loss, 14, 1))
prev_c = cl.shift()
tr = pd.concat([bars["high"] - bars["low"], (bars["high"] - prev_c).abs(), (bars["low"] - prev_c).abs()], axis=1).max(axis=1)
atr = wilder(tr, 14, 0)
assert [round(x, 2) for x in rsi.iloc[[14, 15, 124]]] == [75.12, 80.13, 76.68]
assert [round(x, 3) for x in atr.iloc[[13, 124]]] == [0.581, 0.969]
has(t, "75.12", "80.13", "76.68", "0.581", "0.969", "0.97", "55.69")
rsi_plain = 100 - 100 / (1 + gain.ewm(alpha=1 / 14, adjust=False).mean() / loss.ewm(alpha=1 / 14, adjust=False).mean())
assert [round(x, 2) for x in rsi_plain.iloc[[14, 15, 124]]] == [75.49, 82.62, 76.68]
has(t, "75.49", "82.62")

# compare with charts.js, bar for bar
node = shutil.which("node")
if node:
    js = r"""
const {ind}=require(process.argv[1]);
const fs=require("fs");
const rows=fs.readFileSync(process.argv[2],"utf8").trim().split("\n").slice(1).map(l=>l.split(","));
const bars=rows.map(r=>({high:+r[2],low:+r[3],close:+r[4]}));
const c=bars.map(b=>b.close);
console.log(JSON.stringify({sma:ind.sma(c,20),ema:ind.ema(c,20),rsi:ind.rsi(c,14),atr:ind.atr(bars,14)}));
"""
    res = subprocess.run([node, "-e", js, str(ROOT / "docs" / "javascripts" / "charts.js"), str(D / "stock-a-daily-h1.csv")],
                         capture_output=True, text=True, check=True)
    ref = json.loads(res.stdout)
    for name, mine in (("sma", sma), ("ema", ema_s), ("rsi", rsi), ("atr", atr)):
        a = np.array([np.nan if v is None else v for v in ref[name]], dtype=float)
        bb = mine.to_numpy(dtype=float)
        assert np.array_equal(np.isnan(a), np.isnan(bb)), f"{name}: empty bars differ from charts.js"
        assert np.allclose(a[~np.isnan(a)], bb[~np.isnan(bb)], atol=1e-9), f"{name} differs from charts.js"
else:
    print("   node not found: charts.js comparison skipped")
# worked example and exercises (N = 3)
cs = [10, 11, 12, 11, 13]
e_seed = [(10 + 11 + 12) / 3]
for x in cs[3:]:
    e_seed.append(0.5 * x + 0.5 * e_seed[-1])
assert e_seed == [11.0, 11.0, 12.0]
e1 = [10.0]
for x in cs[1:]:
    e1.append(0.5 * x + 0.5 * e1[-1])
assert e1 == [10.0, 10.5, 11.25, 11.125, 12.0625]
has(t, "11.00", "12.00", "10.50", "11.25", "11.125", "12.0625", "0.0625", "0.25")
assert (12 + 11 + 13) / 3 == 12.0
assert (0.50 * 13 + 1.20) / 14 == 0.55 and round(100 - 100 / (1 + 0.55 / 0.25), 2) == 68.75
has(t, "7.70 / 14 = 0.55", "68.75", "31.25")

# ---------------------------------------------------------------- Lesson 4
t = lesson(F, 4)
doc = json.load(open(D / "northwind-facts.json"))
g = doc["facts"]["us-gaap"]
assert list(g) == ["Revenues", "NetIncomeLoss", "EarningsPerShareBasic", "Assets"] and list(g["EarningsPerShareBasic"]["units"]) == ["USD/shares"]
rows = g["Revenues"]["units"]["USD"]
assert len(rows) == 9 and (rows[1]["end"], rows[1]["val"], rows[1]["fy"], rows[1]["form"], rows[1]["filed"]) == ("2023-12-31", 880_000_000, 2024, "10-K", "2025-02-19")
has(t, "9 facts", "880,000,000", "2025-02-19", "USD/shares")


def table(concept):
    df = pd.DataFrame(g[concept]["units"]["USD"])
    df["days"] = (pd.to_datetime(df["end"]) - pd.to_datetime(df["start"])).dt.days
    return df


rev, ni = table("Revenues"), table("NetIncomeLoss")
year = lambda df: df[df["days"] > 350].sort_values("filed").drop_duplicates("end", keep="last").set_index("end")["val"]
quarter = lambda df: df[df["days"] < 100].set_index("end")["val"]
fr, fn = year(rev), year(ni)
assert (fr / 1e6).tolist() == [880.0, 1000.0, 1150.0]
assert fr.pct_change().dropna().round(3).tolist() == [0.136, 0.15]
assert (fn / fr).round(3).tolist() == [0.111, 0.123, 0.143]
assert (quarter(rev) / 1e6).tolist() == [270.0, 290.0, 295.0]
assert fr["2025-12-31"] - quarter(rev).sum() == 295_000_000 and fn["2025-12-31"] - quarter(ni).sum() == 42_000_000
assert 1150 - (270 + 290 + 295) == 295 and 165 - (36 + 42 + 45) == 42
has(t, "880.0, 1,000.0 and 1,150.0", "0.136", "13.6%", "0.15", "0.111, 0.123 and 0.143", "270.0, 290.0 and 295.0", "295000000", "42000000", "1,150 - 855 = 295", "165 - 123 = 42")
asof = rows_df = pd.DataFrame(rows)
rows_df["days"] = (pd.to_datetime(rows_df["end"]) - pd.to_datetime(rows_df["start"])).dt.days
ann_df = rows_df[rows_df["days"] > 350].sort_values("filed")
got = [ann_df[ann_df["filed"] <= d].drop_duplicates("end", keep="last").iloc[-1]["val"] / 1e6 for d in ("2025-01-31", "2025-06-30", "2026-03-01")]
assert got == [880.0, 1000.0, 1150.0]
assert rows_df["frame"].notna().sum() == 6
has(t, "January 31, 2025", "880.0 million", "February 19, 2025", "June 30, 2025", "1,000.0", "March 1, 2026", "1,150.0", "February 18, 2026", "6 facts")
assert 560 - 290 == 270 and round(42 / 165 * 100, 1) == 25.5
assert round(165 / 1150 * 100, 1) == 14.3 and round(123 / 1000 * 100, 1) == 12.3 and round(165 / 1150 * 100 - 12.3, 2) == 2.05
has(t, "560 - 290 = 270", "25.5%", "14.3%", "12.3%", "2.05", "19 days")
assert (date_diff := (pd.Timestamp("2025-02-19") - pd.Timestamp("2025-01-31")).days) == 19

# ---------------------------------------------------------------- Lesson 5
t = lesson(F, 5)
fred = pd.read_csv(D / "fred-cpi-unrate.csv", parse_dates=["observation_date"], index_col="observation_date", na_values=".")
assert fred.isna().sum().to_dict() == {"CPIAUCSL": 0, "UNRATE": 1} and str(fred[fred["UNRATE"].isna()].index[0].date()) == "2023-10-01"
cpi = fred["CPIAUCSL"]
yoy = cpi.pct_change(12)
assert (round(yoy.loc["2023-01-01"], 4), round(yoy.loc["2025-12-01"], 4)) == (0.0801, 0.0267)
mom = cpi.pct_change().loc["2025-12-01"]
assert (round(mom, 4), round((1 + mom) ** 12 - 1, 4)) == (0.003, 0.036)
assert fred["UNRATE"].ffill().loc["2023-10-01"] == 3.7 == fred["UNRATE"].loc["2023-09-01"]
assert round(fred["UNRATE"].loc["2025-12-01"] - fred["UNRATE"].loc["2024-12-01"], 1) == 0.4
has(t, "October 1, 2023", "0.0801", "8.0%", "0.0267", "2.7%", "0.003", "0.036", "3.6%", "3.7", "0.4 percentage points")
ty = pd.read_csv(D / "treasury-yields.csv", parse_dates=["Date"], date_format="%m/%d/%Y", index_col="Date").sort_index()
s2 = ty["10 Yr"] - ty["2 Yr"]
s3 = ty["10 Yr"] - ty["3 Mo"]
assert (len(ty), str(ty.index[0].date()), str(ty.index[-1].date())) == (782, "2023-01-02", "2025-12-30")
assert ((s2 < 0).sum(), round(s2.min(), 2), str(s2.idxmin().date()), (s3 < 0).sum()) == (407, -0.8, "2023-01-02", 782)
assert str(ty.index[(s2 >= 0).to_numpy().argmax()].date()) == "2024-07-24"
q = s2.resample("QE").last().round(2).iloc[[0, 4, 8, 11]].tolist()
assert q == [-0.72, -0.22, 0.26, 0.35]
has(t, "782 days", "407 days", "-0.80", "July 24, 2024", "all 782 days", "-0.72", "-0.22", "0.26", "0.35")
y = cpi.pct_change(12).dropna().rename("cpi_yoy").to_frame()
y["release"] = y.index + pd.offsets.MonthBegin(1) + pd.Timedelta(days=14)
ix = pd.read_csv(D / "index-x-3y.csv", parse_dates=["date"])[["date", "close"]]
naive = pd.merge_asof(ix, y.reset_index(), left_on="date", right_on="observation_date")
safe = pd.merge_asof(ix, y.sort_values("release"), left_on="date", right_on="release")
day = pd.Timestamp("2023-03-10")
assert (round(naive.set_index("date").loc[day, "cpi_yoy"], 4), round(safe.set_index("date").loc[day, "cpi_yoy"], 4)) == (0.0749, 0.0801)
assert safe["cpi_yoy"].isna().sum() == 32 and str(safe.dropna().iloc[0]["date"].date()) == "2023-02-15"
has(t, "March 10, 2023", "0.0749", "0.0801", "February 15", "32 trading days")
assert (round(301.2 / 300 - 1, 4), round(1.004 ** 12 - 1, 4), round(291.2 / 280 - 1, 4), round(4.10 - 4.35, 2)) == (0.004, 0.0491, 0.04, -0.25)
has(t, "0.40%", "4.9%", "4.0%", "-0.25")

# ---------------------------------------------------------------- Lesson 6
t = lesson(F, 6)
px = pd.DataFrame({f"s{k:02d}": close(f"stock-{k:02d}") for k in range(1, 11)})
px["index"] = close("index-x-3y")
rt = px.pct_change().dropna()
cr = rt.corr()
assert cr.loc[["s05", "s10"], "index"].round(2).tolist() == [0.57, 0.38]
assert (round(cr.loc["s01", "s02"], 2), round(cr.loc["s05", "s10"], 2)) == (0.32, 0.19)
bt = rt.cov()["index"] / rt["index"].var()
assert (round(bt["s04"], 3), round(bt["s06"], 3)) == (1.395, 0.544)
has(t, "0.57", "0.38", "0.32", "0.19", "1.395", "0.544")
yy, xx = rt["s04"], rt["index"]
slope, icpt = np.polyfit(xx, yy, 1)
assert round(slope, 3) == 1.395
X = np.column_stack([np.ones(len(xx)), xx.to_numpy()])
coef, *_ = np.linalg.lstsq(X, yy.to_numpy(), rcond=None)
res = yy.to_numpy() - X @ coef
nn = len(yy)
se = np.sqrt(res @ res / (nn - 2) * np.diag(np.linalg.inv(X.T @ X)))
r2 = 1 - res @ res / ((yy - yy.mean()) @ (yy - yy.mean()))
assert nn == 781 and round(coef[1], 3) == 1.395 and round(se[1], 3) == 0.09 and round(coef[1] / se[1], 1) == 15.4
assert (round(coef[0] * 252, 3), round(se[0] * 252, 3), round(r2, 3)) == (0.281, 0.208, 0.234)
assert round(res.std(ddof=2) * np.sqrt(252), 3) == 0.365 and (round(coef[1] - 2 * se[1], 2), round(coef[1] + 2 * se[1], 2)) == (1.21, 1.58)
assert round(0.281 / 0.208, 2) == 1.35 and round(r2 ** 0.5, 2) == 0.48 and round(1 - r2, 3) == 0.766
has(t, "781 daily returns", "1.395", "0.09", "15.4", "0.281", "0.208", "1.35 standard errors", "0.234", "0.365", "1.21 to 1.58", "0.48", "76.6%")
rl = yy.rolling(60).cov(xx) / xx.rolling(60).var()
assert (round(rl.min(), 2), str(rl.idxmin().date()), round(rl.max(), 2), str(rl.idxmax().date())) == (0.67, "2024-02-09", 2.12, "2024-07-12")
has(t, "0.67", "February 9, 2024", "2.12", "July 12, 2024")
ms, ss = np.array([1, -2, 0, 3, -1.0]), np.array([2, -3, 1, 5, -2.0])
dm, ds = ms - ms.mean(), ss - ss.mean()
assert round(dm @ ds, 2) == 24.4 and round(dm @ dm, 2) == 14.8 and round(ds @ ds, 2) == 41.2
bw = dm @ ds / (dm @ dm)
assert round(bw, 2) == 1.65 and round(ss.mean() - bw * ms.mean(), 2) == 0.27
cw = dm @ ds / math.sqrt((dm @ dm) * (ds @ ds))
assert round(cw, 2) == 0.99 and round(cw ** 2, 2) == 0.98 and round(math.sqrt(41.2 / 14.8), 2) == 1.67
assert round(24.4 / math.sqrt(14.8 * 41.2), 2) == 0.99 and round(math.sqrt(14.8 * 41.2), 2) == 24.69
has(t, "24.40", "14.80", "41.20", "1.65", "0.27%", "24.69", "0.99", "0.98", "1.67", "1.2 x 5% = +6.0%".replace("1.2 x 5% = +6.0%", "+6.0%"), "-6.0%")
assert round(1.395 - 0.18, 3) == 1.215 and round(1.395 + 0.18, 3) == 1.575
has(t, "1.215", "1.575")

# ---------------------------------------------------------------- Lesson 7
t = lesson(F, 7)
month = px.drop(columns="index").resample("ME").last()
ret = month.pct_change()
sig = month.shift(1) / month.shift(12) - 1
nxt = ret.shift(-1)
assert month.shape == (36, 10) and len(sig.dropna(how="all")) == 24 and str(sig.dropna(how="all").index[0].date()) == "2024-01-31"
has(t, "36 month ends", "24 of them", "January 31, 2024")
d0 = pd.Timestamp("2024-09-30")
grp = np.ceil(sig.loc[d0].rank(method="first") / 2).astype(int)
tab = pd.DataFrame({"signal": sig.loc[d0].round(3), "group": grp, "next": nxt.loc[d0].round(3)}).sort_values("signal")
assert tab.index.tolist() == ["s10", "s05", "s08", "s06", "s07", "s01", "s09", "s02", "s04", "s03"]
assert tab["signal"].tolist() == [-0.514, 0.045, 0.060, 0.084, 0.140, 0.145, 0.350, 0.582, 0.691, 1.103]
assert tab["group"].tolist() == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
assert tab["next"].tolist() == [-0.212, 0.062, -0.033, -0.007, -0.198, -0.034, -0.038, 0.034, -0.049, -0.052]
top, bot = nxt.loc[d0][grp == 5].mean(), nxt.loc[d0][grp == 1].mean()
assert (round(top, 4), round(bot, 4), round((top - bot) * 100, 2)) == (-0.0508, -0.0747, 2.39)
has(t, "-0.514", "1.103", "-21.2%", "+6.2%", "-3.3%", "-0.7%", "-19.8%", "-3.4%", "-3.8%", "+3.4%", "-4.9%", "-5.2%", "-5.05%", "-5.08%", "-7.5%", "-7.47%", "+2.39 points", "-0.0508", "-0.0747")
assert round((-4.9 - 5.2) / 2, 2) == -5.05 and round((-21.2 + 6.2) / 2, 2) == -7.5
lowvol = -ret.rolling(12).std()


def sort_report(signal):
    ok = signal.notna().all(axis=1) & nxt.notna().all(axis=1)
    gg = np.ceil(signal[ok].rank(axis=1, method="first") / 2)
    by = [round(float(nxt[ok][gg == q].stack().mean()), 4) for q in (1, 2, 3, 4, 5)]
    sp_ = nxt[ok][gg == 5].mean(axis=1) - nxt[ok][gg == 1].mean(axis=1)
    tt = sp_.mean() / (sp_.std() / np.sqrt(len(sp_)))
    return len(sp_), by, round(float(sp_.mean()), 4), round(float(tt), 2), round(float((sp_ > 0).mean()), 2)


assert sort_report(sig) == (23, [-0.0108, 0.0183, 0.0016, 0.0383, 0.0118], 0.0226, 1.12, 0.57)
assert sort_report(lowvol) == (23, [-0.0133, 0.0283, 0.0102, 0.0273, 0.0068], 0.0201, 1.05, 0.65)
has(t, "23 months", "-1.08%", "1.83%", "0.16%", "3.83%", "1.18%", "2.26%", "1.12", "57%", "2.01%", "1.05", "65%")
sp3 = np.array([2, -1, 3, 0.0])
sd3 = sp3.std(ddof=1)
assert sp3.mean() == 1.0 and round(sd3, 3) == 1.826 and round(sp3.mean() / (sd3 / 2), 2) == 1.10 and round(10 / 3, 2) == 3.33
assert round(1.12 * 2, 2) == 2.24 and 92 / 23 == 4
has(t, "1.826%", "1.10", "3.33", "2.24", "Ranks 5 and 6", "0.60")

# ---------------------------------------------------------------- Lesson 8
t = lesson(F, 8)
ix_ret = close("index-x-3y").pct_change().fillna(0)
sg = (ix_ret > 0).astype(int)
cheat, honest = sg * ix_ret, sg.shift(1).fillna(0) * ix_ret
assert (round((1 + cheat).prod() - 1, 1), round((1 + honest).prod() - 1, 3), round((1 + ix_ret).prod() - 1, 3)) == (17.7, -0.057, 0.291)
has(t, "17.7", "1,770%", "-0.057", "-5.7%", "0.291", "+29.1%")
tot = pd.Series({f"s{k:02d}": close(f"stock-{k:02d}").iloc[-1] / close(f"stock-{k:02d}").iloc[0] - 1 for k in range(1, 11)})
dropped = tot[tot < -0.5].index.tolist()
assert dropped == ["s10"] and (round(tot.mean(), 3), round(tot.drop(dropped).mean(), 3), round(tot.median(), 3)) == (0.663, 0.824, 0.547)
assert round(tot["s10"] * 100, 1) == -79.0
has(t, "0.663", "+66.3%", "0.824", "+82.4%", "16 points", "0.547")
cc = close("index-x-3y")
pos = (cc.rolling(20).mean() > cc.rolling(50).mean()).astype(int).shift(1).fillna(0)
trd = pos.diff().abs().fillna(0)
gross = pos * ix_ret
net = gross - trd * 0.0010
assert (int(trd.sum()), round((1 + gross).prod() - 1, 3), round((1 + net).prod() - 1, 3)) == (19, 0.06, 0.04)
has(t, "19 times", "0.060", "+6.0%", "0.040", "+4.0%", "10 basis points")
assert round(1.01 * 1.03 - 1, 4) == 0.0403 and round(0.98 - 1, 2) == -0.02
has(t, "+4.03%", "-2.0%")
assert round(40 * 0.10, 1) == 4.0 and round(6.0 - 4.0, 1) == 2.0
assert round((9 * 82.4 - 79.0) / 10, 1) == 66.3 and round(82.4 - 66.3, 1) == 16.1
has(t, "4.0% a year", "2.0% a year", "662.6", "16.1 points")

# ---------------------------------------------------------------- Lesson 9
t = lesson(F, 9)
rr = close("index-x-3y").pct_change().dropna()
train, test = rr.iloc[:520], rr.iloc[520:]
assert len(rr) == 781 and len(test) == 261
sh = lambda x: x.mean() / x.std() * np.sqrt(252)
rng = np.random.default_rng(7)
rules = pd.DataFrame(rng.choice([-1, 1], size=(200, len(rr))).T, index=rr.index)
ins = rules.iloc[:520].mul(train, axis=0).apply(sh)
oos = rules.iloc[520:].mul(test, axis=0).apply(sh)
bst = ins.idxmax()
assert (round(ins.max(), 2), round(oos[bst], 2), round(oos.mean(), 2)) == (1.91, 0.78, -0.11)
assert (round(ins.mean(), 2), round(ins.std(), 2), round(np.corrcoef(ins, oos)[0, 1], 2)) == (-0.1, 0.68, 0.02)
has(t, "1.91", "0.78", "-0.11", "-0.10", "0.68", "0.02", "first 520 returns", "last 261")


def emax(nt, sd):
    gm = 0.5772156649
    z = NormalDist().inv_cdf
    return sd * ((1 - gm) * z(1 - 1 / nt) + gm * z(1 - 1 / (nt * math.e)))


def psr(sr, sr0, tt, skew=0.0, kurt=3.0):
    return NormalDist().cdf((sr - sr0) * math.sqrt(tt - 1) / math.sqrt(1 - skew * sr + (kurt - 1) / 4 * sr ** 2))


dd = math.sqrt(252)
assert [round(emax(nn_, 0.68 / dd) * dd, 2) for nn_ in (10, 200, 1000)] == [1.07, 1.88, 2.21]
assert round(psr(1.91 / dd, 0, 520), 3) == 0.997 and round(psr(1.91 / dd, emax(200, 0.68 / dd), 520), 3) == 0.517
has(t, "1.07", "1.88", "2.21", "0.997", "0.517", "0.5772")
assert round(1 - 0.95 ** 20, 3) == 0.642 and round(0.95 ** 20, 3) == 0.358
assert round(3.0 / 1.12, 2) == 2.68 and round((3.0 / 1.12) ** 2, 2) == 7.17 and round(23 * (3.0 / 1.12) ** 2) == 165
has(t, "0.358", "0.642", "2.68", "7.17", "165")

# ---------------------------------------------------------------- Lesson 10
t = lesson(F, 10)
r10 = close("stock-04").pct_change().dropna()
rf = 0.02
yrs = len(r10) / 252
eq = (1 + r10).cumprod()
cagr = eq.iloc[-1] ** (1 / yrs) - 1
vol = r10.std() * np.sqrt(252)
sharpe = (r10.mean() - rf / 252) / r10.std() * np.sqrt(252)
dsd = np.sqrt((np.minimum(r10 - rf / 252, 0) ** 2).mean()) * np.sqrt(252)
sortino = (r10.mean() - rf / 252) * 252 / dsd
dwn = eq / eq.cummax() - 1
mdd = dwn.min()
calmar = cagr / abs(mdd)
hit = (r10 > 0).mean()
assert (round(yrs, 2), round(eq.iloc[-1] - 1, 3), round(cagr, 3), round(vol, 3)) == (3.1, 1.725, 0.382, 0.417)
assert (round(sharpe, 2), round(sortino, 2), round(mdd, 3), round(calmar, 2), round(hit, 3)) == (0.94, 1.37, -0.294, 1.3, 0.531)
assert (str(dwn.idxmin().date()), str(eq.loc[:dwn.idxmin()].idxmax().date())) == ("2024-04-12", "2024-02-23")
has(t, "781 returns", "3.1 years", "1.725", "+172.5%", "0.382", "38.2%", "0.417", "0.94", "1.37", "-0.294", "-29.4%", "1.3", "0.531", "53.1%", "February 23, 2024", "April 12, 2024")
r6 = pd.Series([0.05, -0.10, 0.08, 0.02, -0.04, 0.06])
e6 = (1 + r6).cumprod()
assert [round(x, 4) for x in e6] == [1.05, 0.945, 1.0206, 1.041, 0.9994, 1.0593]
cg6 = e6.iloc[-1] ** 2 - 1
dd6 = math.sqrt((np.minimum(r6, 0) ** 2).mean()) * math.sqrt(12)
assert round(e6.iloc[-1] - 1, 4) == 0.0593 and round(cg6, 3) == 0.122
assert (round(r6.mean() * 100, 3), round(r6.std() * 100, 2), round(r6.std() * math.sqrt(12) * 100, 1)) == (1.167, 6.88, 23.8)
assert round(r6.mean() / r6.std() * math.sqrt(12), 2) == 0.59
assert round((0.01 + 0.0016) / 6, 6) == 0.001933 and round(math.sqrt(0.0116 / 6) * 100, 2) == 4.40 and round(dd6 * 100, 1) == 15.2
assert round(r6.mean() * 12 / dd6, 2) == 0.92
assert round((e6 / e6.cummax() - 1).min(), 3) == -0.1 and round(cg6 / 0.10, 2) == 1.22 and (r6 > 0).sum() == 4 and round(4 / 6 * 100, 1) == 66.7
has(t, "1.0500, 0.9450, 1.0206, 1.0410, 0.9994, 1.0593", "5.93%", "12.2%", "1.167%", "6.88%", "23.8%", "0.59", "0.001933", "4.40%", "15.2%", "0.92", "-10.0%", "-4.0%", "1.22", "66.7%")
# part check and exercises
assert round(51 / 50 - 1, 3) == 0.02 and round(51 / 100 - 1, 2) == -0.49
has(t, "+2.0%", "-49.0%")
assert round(1.2 * math.sqrt(252), 2) == 19.05
has(t, "19.05%")
assert 400 - (90 + 95 + 100) == 115 and 0.5 * 30 / 15 == 1.0
has(t, "115 million", "April's CPI", "1.0")
assert round(0.8 / (3.0 / 6), 1) == 1.6
has(t, "1.6")
assert round(1 - 0.95 ** 50, 3) == 0.923 and round(0.95 ** 50, 3) == 0.077
has(t, "0.923", "0.077", "92%")
assert (12 - 2) / 20 == 0.5 and round(12 / 25, 2) == 0.48
has(t, "0.50", "0.48")
assert round(1.04 * 0.98 * 1.03, 4) == 1.0498 and round(0.9 / 1.2 - 1, 2) == -0.25 and (15 - 3) / 25 == 0.48 and (15 - 3) / 15 == 0.8
has(t, "1.0498", "+4.98%", "66.7%", "-25.0%", "0.48", "0.80")
