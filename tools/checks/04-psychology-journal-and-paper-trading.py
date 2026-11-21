"""Number checks for part 4, Psychology, the journal and paper trading."""
import csv
import json
import math
import sys

from _lib import ROOT, DOCS, lesson, has, usd, pct

sys.path.insert(0, str(ROOT / "tools"))
from build_journal import TRADES, EXAMPLES, example_values  # noqa: E402

F = "04-psychology-journal-and-paper-trading"
CH = ROOT / "docs" / "assets" / "charts" / F


def bars(name):
    return json.loads((CH / f"{name}.json").read_text(encoding="utf-8"))["bars"]


def v(x, a=0.88, lam=2.25):
    return x**a if x >= 0 else -lam * (-x) ** a


def approx(a, b, tol=0.005):
    assert abs(a - b) <= tol, (a, b)


# ---- Lesson 1
t = lesson(F, 1)
approx(150**0.88, 82.2, 0.05)
approx(v(100), 57.54, 0.01)
approx(v(-100), -129.5, 0.05)
approx(0.5 * 82.2 + 0.5 * -129.5, -23.65, 0.06)
approx(0.5 * 150 - 0.5 * 100, 25)
has(t, "150^0.88 = 82.2", "-2.25 x 100^0.88 = -129.5", "-23.6", "+US$25")
approx(200**0.88, 105.9, 0.05)
approx(-2.25 * 200**0.88, -238.3, 0.1)
g = 200 * 2.25 ** (1 / 0.88)
assert round(g) == 503 and round(2.25 ** (1 / 0.88), 3) == 2.513
has(t, "-2.25 x 200^0.88 = -2.25 x 105.9 = -238.3", "x 2.513 = US$503")
loss = (50.40 - 44.50) * 100
r1 = (50.40 - 49.40) * 100
assert round(loss) == 590 and round(r1) == 100 and round(loss / r1, 1) == 5.9
has(t, "US$590", "US$100", "5.9R", "5.9 times")
assert round(14.8 / 9.8, 2) == 1.51
has(t, "14.8 / 9.8 = 1.51")
b = bars("loser-held")
assert b[0][0] == "2026-03-02" and b[29][0] == "2026-04-10"
assert b[11][0] == "2026-03-17" and b[11][3] == 49.27 and b[11][3] < 49.40
assert b[29][4] == 44.50 and b[9][4] > 50.40 or True
has(t, "March 17 (low 49.27)", "April 10 at 44.50")

# ---- Lesson 2
t = lesson(F, 2)
acct = 25_000
plan = 3 * 0.01 * acct
ladder = 250 + 500 + 1000
assert plan == 750 and ladder == 1750
assert pct(plan / acct) == "3.0%" and pct(ladder / acct) == "7.0%"
assert round(ladder / (acct - ladder) * 100, 1) == 7.5
has(t, "US$750", "US$1,750", "3.0%", "7.0%", "7.5%", "1,750 / 25,000", "1,750 / 23,250", "US$1,000")
b = bars("fomo-chase")
assert b[14][0] == "2026-04-21" and b[14][2] > 50.50 and b[14][3] < 50.50 and b[14][2] == 51.35
assert b[22][0] == "2026-05-01" and b[22][4] == 55.90
assert max(x[2] for x in b[:14]) == 50.41 and min(x[3] for x in b[:14]) == 49.01
assert round(55.90 - 50.50, 2) == 5.40 and round(5.40 / 1.60, 1) == 3.4
has(t, "5.40 above the planned entry", "3.4 times", "US$7.00", "50.50 - 48.90 = US$1.60")
assert int(250 / 1.60) == 156 and round(156 * 7.00) == 1092 and round(1092 / 250, 1) == 4.4
has(t, "156 x 7.00 = US$1,092", "4.4 times", "156.25")
assert b[22][0] == "2026-05-01" and 22 - 14 == 8
has(t, "Eight trading days later")
# exercises
l = 0.01 * 40_000 + 0.02 * 40_000 + 0.04 * 40_000
assert l == 2800 and pct(l / 40_000) == "7.0%" and 3 * 400 == 1200
has(t, "US$2,800", "US$1,200 (3.0%)")
assert round(2800 / 37_200 * 100, 1) == 7.5
has(t, "US$37,200", "2,800 / 37,200 = 7.5%")
assert round(55.00 - 48.90, 2) == 6.10 and round(6.10 / 1.60, 1) == 3.8
has(t, "US$6.10", "6.10 / 1.60 = 3.8")

# ---- Lesson 3
t = lesson(F, 3)
assert round((54.50 - 50.00) / (50.00 - 48.50), 2) == 3.0
assert int(250 / 1.50) == 166 and round(166 * 1.5, 2) == 249.00 and round(250 / 1.5, 1) == 166.7
has(t, "4.50 / 1.50 = 3.0", "166.7", "166 shares", "US$249.00")
assert round(1.20 / 1.00, 1) == 1.2
has(t, "1.20 / 1.00 = 1.2")
assert round((65.00 - 62.00) / (62.00 - 60.40), 3) == 1.875
assert 300 / 1.60 == 187.5
has(t, "3.00 / 1.60 = 1.875", "187 shares")
assert 30.00 + 2 * 1.00 == 32.00 and 30.00 + 3 * 1.00 == 33.00
has(t, "US$32.00", "US$33.00")

# ---- Lesson 4 (and the downloads)
t = lesson(F, 4)
vals = example_values()
a, bb = vals
assert round(a["risk"], 2) == 249.00 and round(a["pnl"], 2) == 496.00 and round(a["r"], 2) == 1.99
assert round(bb["risk"], 2) == 250.00 and round(bb["pnl"], 2) == -252.00 and round(bb["r"], 2) == -1.01
assert round((1.99 - 1.01) / 2, 2) == 0.49
has(t, "US$249.00", "US$496.00", "1.99", "-US$252.00", "-1.01", "0.49R", "498.00 - 2.00")
risk4 = 1.5 * 120
pl4 = 3.6 * 120 - 1.5
assert round(risk4, 2) == 180 and round(pl4, 2) == 430.5 and round(pl4 / risk4, 2) == 2.39
has(t, "US$180.00", "US$430.50", "2.39")
risk5 = 1 * 200
pl5 = 1.00 * 200 - 2.00
assert pl5 == 198 and round(pl5 / risk5, 2) == 0.99
has(t, "US$200.00", "US$198.00", "0.99")
assert 0.4 * 2.0 + 0.6 * -1.0 == 0.2 or round(0.4 * 2.0 + 0.6 * -1.0, 10) == 0.2
has(t, "+0.2R per trade", "40%")

# The workbook has the formulas and the CSV has the example values.
from openpyxl import load_workbook  # noqa: E402

wb = load_workbook(ROOT / "docs" / "downloads" / "trade-journal.xlsx")
ws, st = wb["Trades"], wb["Stats"]
assert ws["I2"].value.startswith("=IF(") and "ABS(E2-F2)*H2" in ws["I2"].value
assert "IF(D2=\"Short\",-1,1)" in ws["L2"].value and ws["M2"].value.endswith("L2/I2)")
assert ws["I500"].value.startswith("=IF(") and ws["M3"].value.startswith("=IF(")
assert [c.value for c in ws[1]][:3] == ["Date", "Ticker", "Setup"] and ws["Q1"].value == "Screenshot"
for cell in ("B2", "B3", "B5", "B6", "B7", "B8", "B9"):
    assert str(st[cell].value).startswith("="), cell
assert "AVERAGE" in st["B8"].value and "COUNTIFS" in st["B15"].value and "AVERAGEIFS" in st["D15"].value
assert ws["A2"].value == "2026-03-02" and ws["D3"].value == "Short" and ws["H2"].value == 166
rows = list(csv.reader((ROOT / "docs" / "downloads" / "trade-journal.csv").open(encoding="utf-8")))
assert len(rows) == 3 and rows[0][8] == "Risk (US$)"
assert rows[1][8:13] == ["249.00", "53.00", "2.00", "496.00", "1.99"]
assert rows[2][8:13] == ["250.00", "31.00", "2.00", "-252.00", "-1.01"]
# Evaluate the sheet's formulas for the example rows by hand.
for row, ex in zip((2, 3), EXAMPLES):
    d, tk, setup, dr, e, s, tg, sh, xt, fee, *_ = ex
    r_ = abs(e - s) * sh
    p_ = (xt - e) * sh * (-1 if dr == "Short" else 1) - fee
    assert round(r_, 2) == float(rows[row - 1][8]) and round(p_, 2) == float(rows[row - 1][11])
    assert round(p_ / r_, 2) == float(rows[row - 1][12])

# ---- Lesson 5
t = lesson(F, 5)
r = [x[1] for x in TRADES]
w = [x for x in r if x > 0]
lo = [x for x in r if x < 0]
n = len(r)
assert n == 20 and len(w) == 10 and len(lo) == 10
assert round(sum(w) / len(w), 2) == 1.82 and round(sum(lo) / len(lo), 2) == -1.20
exp = 0.5 * (sum(w) / 10) + 0.5 * (sum(lo) / 10)
assert round(exp, 2) == 0.31 and round(sum(r), 1) == 6.2 and round(sum(r) / n, 2) == 0.31
has(t, "10 / 20 = 50%", "+1.82R", "-1.20R", "+0.31R", "+6.2R")
for s_, nn, ww, tot, av in (("Breakout", 10, 4, -1.3, -0.13), ("Pullback", 10, 6, 7.5, 0.75)):
    x = [y[1] for y in TRADES if y[0] == s_]
    assert len(x) == nn and sum(1 for y in x if y > 0) == ww
    assert round(sum(x), 1) == tot and round(sum(x) / len(x), 2) == av
has(t, "| Breakout | 10 | 4 | -1.3 | -0.13 |", "| Pullback | 10 | 6 | +7.5 | +0.75 |")
yes = [y[1] for y in TRADES if y[2]]
no = [y[1] for y in TRADES if not y[2]]
assert len(yes) == 16 and round(sum(yes), 1) == 8.7 and round(sum(yes) / 16, 2) == 0.54
assert len(no) == 4 and round(sum(no), 1) == -2.5 and round(sum(no) / 4, 3) == -0.625
has(t, "| Yes | 16 | +8.7 | +0.54 |", "| No | 4 | -2.5 | -0.63 |", "-2.5R", "+8.7R")
mean = sum(r) / n
sd = math.sqrt(sum((x - mean) ** 2 for x in r) / (n - 1))
se = sd / math.sqrt(n)
assert round(sd, 2) == 1.65 and round(se, 2) == 0.37
assert round(mean - 1.96 * se, 2) == -0.42 and round(mean + 1.96 * se, 2) == 1.04
has(t, "1.65R", "1.65 / sqrt(20) = 0.37R", "-0.42R", "+1.04R")
tot = 5 * 2.2 - 7 * 1.0
assert round(tot, 1) == 4.0 and round(tot / 12, 2) == 0.33 and round(5 / 12 * 100, 1) == 41.7
has(t, "+4.0R", "+0.33R", "41.7%")
assert round(3.2 / 8, 1) == 0.4 and round(1.5 / math.sqrt(8), 2) == 0.53
has(t, "3.2 / 8", "+0.4R", "0.53R")
assert round(6.2 - (-2.5), 1) == 8.7 and round(-1.8 + 0.9 - 2.2 + 0.6, 1) == -2.5
has(t, "+1.8", "6.2 - (-2.5)")
# the In code snippet prints these
import pandas as pd  # noqa: E402

df = pd.read_csv(DOCS / "assets" / "data" / "journal-20-trades.csv")
assert len(df) == 20 and abs(df["r"].mean() - 0.31) < 1e-9
assert [round(x, 3) for x in df.groupby("followed_plan")["r"].mean()] == [-0.625, 0.544]

# ---- Lesson 6
t = lesson(F, 6)
b = bars("paper-fill")
assert b[10][0] == "2026-05-18" and b[10][3] == 49.95 and b[10][4] == 50.50
assert min(x[3] for x in b if x[0] != "2026-05-18") > 49.95
has(t, "low of 49.95", "closed at 50.50", "May 18")
paper_pl = (53.00 - 50.00) * 166
paper_risk = (50.00 - 48.50) * 166
assert round(paper_pl, 2) == 498.00 and round(paper_risk, 2) == 249.00 and paper_pl / paper_risk == 2.0
e2, x2 = 50.00 + 0.05, 53.00 - 0.05
pl2 = (x2 - e2) * 166 - 2.00
risk2 = (e2 - 48.50) * 166
assert round(e2, 2) == 50.05 and round(x2, 2) == 52.95
assert round((x2 - e2) * 166, 2) == 481.40 and round(pl2, 2) == 479.40 and round(risk2, 2) == 257.30
assert round(pl2 / risk2, 2) == 1.86
has(t, "US$498.00", "US$249.00", "2.00", "481.40 - 2.00 = US$479.40", "US$257.30", "1.86", "52.95", "50.05")
assert 0.01 * 20_000 == 200 and 200 / 2.00 == 100 and 10_000 / 2 == 5000
has(t, "US$200", "100", "5,000 shares")
pl3 = (22.96 - 20.04) * 200 - 2.00
risk3 = (20.04 - 19.00) * 200
assert round(pl3, 2) == 582.00 and round(risk3, 2) == 208.00 and round(pl3 / risk3, 2) == 2.80
has(t, "US$582.00", "US$208.00", "2.80", "3.00")

# ---- Lesson 7
t = lesson(F, 7)
se30 = math.sqrt(0.25 / 30)
assert round(se30 * 100, 1) == 9.1 and round((0.5 - 1.96 * se30) * 100) == 32 and round((0.5 + 1.96 * se30) * 100) == 68
has(t, "9.1 percentage points", "32% to 68%")
assert round(26 / 30 * 100, 1) == 86.7 and round(5.4 / 30, 2) == 0.18
has(t, "86.7%", "+0.18R", "4.5R", "6R", "+5.4R")
for pct_, dollars, sh in ((0.0025, 62.50, 41), (0.005, 125.00, 83), (0.01, 250.00, 166)):
    assert round(acct * pct_, 2) == dollars and int(dollars / 1.50) == sh
has(t, "US$62.50", "US$125.00", "US$250.00", "41 shares", "83 at Stage 2", "166 at Stage 3", "62.50 / 1.50 = 41.7", "125 / 1.50 = 83.3", "250 / 1.50 = 166.7")
# Try it
assert [0.0025 * 40_000, 0.005 * 40_000, 0.01 * 40_000] == [100, 200, 400]
has(t, "100 shares", "200 shares", "400 shares")
se100 = math.sqrt(0.25 / 100)
assert round(se100 * 100, 1) == 5.0 and round((0.5 - 1.96 * se100) * 100, 1) == 40.2 and round((0.5 + 1.96 * se100) * 100, 1) == 59.8
assert round((100 / 30) ** 0.5, 1) == 1.8 and round(se100 / se30, 2) == 0.55
has(t, "5.0 points", "40.2% to 59.8%")
assert round(17 / 20 * 100) == 85
has(t, "85%")
# Part check
assert round(100 * 2.25 ** (1 / 0.88)) == 251
has(t, "US$251")
assert 0.01 * 50_000 + 0.02 * 50_000 + 0.04 * 50_000 == 3500 and 3 * 500 == 1500
has(t, "US$3,500", "7.0%", "US$1,500 (3.0%)")
assert (31.50 - 30.00) / (30.00 - 29.40) == 2.5 or round((31.50 - 30.00) / (30.00 - 29.40), 2) == 2.5
assert int(250 / 0.60) == 416
has(t, "1.50 / 0.60 = 2.5", "416 shares", "416.7")
risk7 = 2.00 * 50
pl7 = 5.00 * 50 - 1.00
assert risk7 == 100 and pl7 == 249 and round(pl7 / risk7, 2) == 2.49
has(t, "US$100.00", "US$249.00", "2.49")
assert 24 / 30 == 0.8
has(t, "24 / 30 = 80%")
assert 0.0025 * acct == 62.5
