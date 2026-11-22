"""Number checks for part 10, Valuation and research.

Starts from Northwind Tools Inc. (part 9, tools/checks/09-company-financials.py):
FY2025 revenue 1,150, EBIT 235, EBITDA 270, net income 165, debt 275, cash 130.
Everything added here is made up: the share price, the market inputs and the
five-year forecast. US$ millions except per-share figures and share counts
(millions of shares). The figure scripts read this model too: everything above
the marker line.
"""
from pathlib import Path

_p = Path(__file__).resolve().parent / "09-company-financials.py"
_n9: dict = {}
exec(_p.read_text(encoding="utf-8").split("# ==== LESSON" + " CHECKS")[0], _n9)

IS25, BS25, CF25 = _n9["IS"]["FY2025"], _n9["BS"]["FY2025"], _n9["CF"]
TAX = _n9["TAX"]
REV0, EBIT0, EBITDA0, NI0, DA0 = IS25["rev"], IS25["ebit"], IS25["ebitda"], IS25["ni"], IS25["da"]
DEBT, CASH, EQUITY = BS25["debt"], BS25["cash"], BS25["equity"]
SH_BASIC = _n9["SH_END"]                                  # 98.5 million shares outstanding
OPT_N, OPT_K, RSU = _n9["OPT_N"], _n9["OPT_K"], _n9["RSU"]
W_DIL = _n9["W_DIL"]                                      # 102.5 weighted diluted shares
EPS = NI0 / W_DIL

# ---- Made up for part 10 ----
PRICE = 50.0
OPT_NET = OPT_N - OPT_N * OPT_K / PRICE                   # treasury stock method at US$50
SH_DIL = SH_BASIC + OPT_NET + RSU                         # 101.5
MCAP = PRICE * SH_BASIC                                   # 4,925
EQ_DIL = PRICE * SH_DIL                                   # 5,075
EV = EQ_DIL + DEBT - CASH                                 # 5,220

RF, ERP, BETA = 0.0492, 0.045, 1.0
KD_PRE = 0.052
KE = RF + BETA * ERP
KD = KD_PRE * (1 - TAX)
WACC_EXACT = EQ_DIL / (EQ_DIL + DEBT) * KE + DEBT / (EQ_DIL + DEBT) * KD
WACC = 0.091
TG = 0.03
EXIT_MULT = 13.0

D_PCT, NWC_PCT = 0.03, 0.17


def forecast(growth, margin, capex):
    """Yearly rows (revenue, EBIT, NOPAT, D&A, capex, change in NWC, UFCF, EBITDA) for FY2026 on."""
    rows, r = [], REV0
    for g, m, c in zip(growth, margin, capex):
        rev = r * (1 + g)
        ebit = rev * m
        nopat = ebit * (1 - TAX)
        da = rev * D_PCT
        cx = rev * c
        dnwc = (rev - r) * NWC_PCT
        rows.append(dict(rev=rev, ebit=ebit, nopat=nopat, da=da, capex=cx, dnwc=dnwc,
                         ufcf=nopat + da - cx - dnwc, ebitda=ebit + da))
        r = rev
    return rows


BASE = dict(growth=[.15, .13, .11, .09, .07], margin=[.215, .225, .23, .235, .24],
            capex=[.065, .058, .052, .047, .042])
BEAR = dict(growth=[.10, .08, .07, .06, .05], margin=[.21, .21, .21, .21, .21],
            capex=[.065, .06, .055, .05, .045])
BULL = dict(growth=[.20, .18, .16, .14, .12], margin=[.22, .235, .25, .26, .27],
            capex=[.065, .058, .052, .047, .042])


def dcf(s=BASE, wacc=WACC, tg=TG, exit_mult=None):
    rows = forecast(**s)
    pv_fcf = sum(r["ufcf"] / (1 + wacc) ** (i + 1) for i, r in enumerate(rows))
    if exit_mult is None:
        tv = rows[-1]["ufcf"] * (1 + tg) / (wacc - tg)
    else:
        tv = rows[-1]["ebitda"] * exit_mult
    pv_tv = tv / (1 + wacc) ** len(rows)
    ev = pv_fcf + pv_tv
    eq = ev - DEBT + CASH
    return dict(rows=rows, pv_fcf=pv_fcf, tv=tv, pv_tv=pv_tv, ev=ev, eq=eq, ps=eq / SH_DIL, tv_share=pv_tv / ev)


def implied_growth(target=PRICE, wacc=WACC, tg=TG):
    """Constant revenue growth for FY2026 to FY2030 (same margins and capex as BASE) that gives `target` per share."""
    lo, hi = 0.0, 0.6
    for _ in range(80):
        mid = (lo + hi) / 2
        s = dict(BASE, growth=[mid] * 5)
        if dcf(s, wacc, tg)["ps"] < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def implied_wacc(target=PRICE, tg=TG):
    lo, hi = tg + 0.005, 0.30
    for _ in range(80):
        mid = (lo + hi) / 2
        if dcf(BASE, mid, tg)["ps"] > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ==== LESSON CHECKS (the figure scripts stop reading here) ====
from _lib import ROOT, lesson, has, usd, pct, num  # noqa: E402,F401

F = "10-valuation-and-research"
import statistics  # noqa: E402


def near(a, b, tol=0.005):
    assert abs(a - b) <= tol, (a, b)


# ---------------- Lesson 1: multiples ----------------
t = lesson(F, 1)
assert round(EPS, 2) == 1.61
pe = PRICE / EPS
near(pe, 31.06, 0.01)
fni = (forecast(**BASE)[0]["ebit"] - 15) * (1 - TAX)
feps = fni / SH_DIL
near(fni, 202.0, 0.05)
assert round(feps, 2) == 1.99
near(PRICE / round(feps, 2), 25.1, 0.05)
has(t, "31.1", "US$1.99", "25.1", "US$202.0 million", "101.5 million")
near(EPS / PRICE, 0.0322, 0.00005)
has(t, "3.22%", "4.92%")
near(MCAP / REV0, 4.28, 0.005)
near(MCAP / EQUITY, 7.58, 0.005)
near(pe / 15, 2.07, 0.005)
has(t, "4.28", "7.58", "2.07", "US$4,925 million", "US$1.61")
assert 40 / 2 == 20 and 40 / 1 == 40 and 2 / 40 == 0.05 and 1 / 40 == 0.025
assert 20 / 5 == 4.0 and 40 / 25 == 1.6
has(t, "40 / 2.00 = 20.0", "20.0 / 5 = 4.0", "40.0 / 25 = 1.6")
has(t, "36 / 2.40 = 15.0", "6.67%")
assert round(2.40 / 36 * 100, 2) == 6.67
near(36 / 2.70, 13.33, 0.005)
near(2.70 / 2.40 - 1, 0.125, 1e-9)
has(t, "13.3", "12.5%", "15.0 / 12.5 = 1.2")
assert 25 * 40 == 1000
near(1000 / 600, 1.67, 0.005)
assert 1000 / 200 == 5.0
has(t, "US$1,000 million", "1.67", "5.00")

# ---------------- Lesson 2: enterprise value ----------------
t = lesson(F, 2)
assert OPT_NET == 2.4 and SH_DIL == 101.5 and EQ_DIL == 5075 and EV == 5220
assert EBITDA0 == 270
near(EV / EBITDA0, 19.33, 0.005)
near(EV / EBIT0, 22.21, 0.005)
near(EV / REV0, 4.539, 0.001)
has(t, "US$5,075 million", "US$5,220 million", "19.3", "22.2", "4.54", "2.4 million", "101.5 million",
    "235 + 35 = US$270 million")
assert 1000 + 400 - 100 == 1300
d_ev = 2000 + 600 + 100 + 80 - 150
assert d_ev == 2630
near(d_ev / 250, 10.52, 0.005)
has(t, "US$2,630 million", "10.5", "US$1,300 million")
assert round(106.25 / 270, 2) == 0.39
has(t, "US$106.25 million", "39%")
assert 3000 + 800 - 300 == 3500 and 3500 / 250 == 14.0 and (3000 - 300) / 250 == 10.8
has(t, "US$3,500 million", "14.0", "US$2,700 million", "10.8")
nn = 6 - 6 * 10 / 20
assert nn == 3 and 20 * (50 + nn) == 1060
has(t, "US$1,060 million")
nn4 = OPT_N - OPT_N * OPT_K / 40
assert nn4 == 2.0
sh4 = 98.5 + nn4 + RSU
assert abs(sh4 - 101.1) < 1e-9 and abs(40 * sh4 - 4044) < 1e-6 and abs(40 * sh4 + 275 - 130 - 4189) < 1e-6
has(t, "101.1 million", "US$4,044 million", "US$4,189 million")

# ---------------- Lesson 3: free cash flow ----------------
t = lesson(F, 3)
nwc0 = 125 + 100 + 25 - 80 - 45
nwc1 = 150 + 120 + 30 - 95 - 55
assert (nwc0, nwc1) == (125, 150)
nopat = EBIT0 * (1 - TAX)
ufcf0 = nopat + DA0 - 80 - (nwc1 - nwc0)
assert nopat == 176.25 and ufcf0 == 106.25
assert CF25["capex"] == -80 and CF25["d_wc"] == -25
assert BS25["ar"] + BS25["inv"] + BS25["prepaid"] - BS25["ap"] - BS25["accrued"] == nwc1
ati = IS25["interest"] * (1 - TAX)
assert ati == 11.25
assert ufcf0 - ati + IS25["sbc"] == 125 == CF25["fcf"]
assert CF25["cfo"] - 80 == 125
has(t, "US$176.25 million", "US$106.25 million", "US$11.25 million", "US$125 million", "205 - 80",
    "125 - 30 = US$95 million")
near(125 / MCAP, 0.0254, 0.00005)
near(125 / 165, 0.758, 0.001)
has(t, "2.54%", "76%")
assert 80 * 0.75 + 10 - 25 - 5 == 40 and 62 - 25 == 37
has(t, "US$40 million", "US$37 million")
near(95 / MCAP, 0.0193, 0.00005)
near(106.25 / EV, 0.0204, 0.00005)
has(t, "1.93%", "2.04%")

# ---------------- Lesson 4: CAPM and WACC ----------------
t = lesson(F, 4)
near(KE, 0.0942, 1e-9)
assert abs(15 / ((300 + 275) / 2) - 0.0522) < 0.0001
assert round(KD_PRE, 3) == 0.052 and abs(KD - 0.039) < 1e-9
we, wd = EQ_DIL / (EQ_DIL + DEBT), DEBT / (EQ_DIL + DEBT)
near(we, 0.9486, 0.00005)
near(wd, 0.0514, 0.00005)
near(we * KE * 100, 8.936, 0.001)
near(wd * KD * 100, 0.2005, 0.001)
near(WACC_EXACT, 0.0914, 0.00005)
has(t, "9.42%", "3.9%", "94.86%", "5.14%", "8.936%", "0.200%", "9.14%", "5,350", "287.5")
ke14 = RF + 1.4 * ERP
near(ke14, 0.1122, 1e-9)
w14 = we * ke14 + wd * KD
near(w14, 0.1084, 0.00005)
near(dcf(wacc=0.1084)["ps"], 29.84, 0.005)
has(t, "11.22%", "10.84%", "US$29.84", "US$39.42", "8.52%")
assert abs(0.04 + 1.2 * 0.05 - 0.10) < 1e-12 and abs(0.06 * 0.75 - 0.045) < 1e-12
near(0.7 * 0.10 + 0.3 * 0.045, 0.0835, 1e-9)
has(t, "10.0%", "4.5%", "8.35%", "1.35%")
has(t, "10.64% + 0.20% = 10.84%")

# ---------------- Lesson 5: DCF ----------------
t = lesson(F, 5)
base = dcf()
rows = base["rows"]
exp_rev = [1322.5, 1494.4, 1658.8, 1808.1, 1934.7]
exp_ebit = [284.3, 336.2, 381.5, 424.9, 464.3]
exp_nopat = [213.3, 252.2, 286.1, 318.7, 348.2]
exp_da = [39.7, 44.8, 49.8, 54.2, 58.0]
exp_cx = [86.0, 86.7, 86.3, 85.0, 81.3]
exp_nwc = [29.3, 29.2, 27.9, 25.4, 21.5]
exp_u = [137.6, 181.1, 221.7, 262.6, 303.5]
for i, r in enumerate(rows):
    for key, exp in (("rev", exp_rev), ("ebit", exp_ebit), ("nopat", exp_nopat), ("da", exp_da),
                     ("capex", exp_cx), ("dnwc", exp_nwc), ("ufcf", exp_u)):
        near(r[key], exp[i], 0.051)
for vals in (exp_rev, exp_ebit, exp_nopat, exp_da, exp_cx, exp_nwc, exp_u):
    has(t, " | ".join(f"{v:,.1f}" for v in vals))
dfs = [1 / 1.091 ** n for n in range(1, 6)]
has(t, *[f"{x:.4f}" for x in dfs])
pvs = [r["ufcf"] * f for r, f in zip(rows, dfs)]
has(t, " + ".join(f"{x:.1f}" for x in pvs))
near(base["pv_fcf"], 830.7, 0.05)
near(base["tv"], 5124.8, 0.05)
near(base["pv_tv"], 3315.5, 0.05)
near(base["ev"], 4146.3, 0.05)
near(base["eq"], 4001.3, 0.05)
near(base["ps"], 39.42, 0.005)
near(base["tv_share"], 0.80, 0.005)
has(t, "US$830.7 million", "US$5,124.8 million", "US$3,315.5 million", "US$4,146.3 million",
    "US$4,001.3 million", "US$39.42", "80%", "0.788")
near(39.42 / 50, 0.788, 0.0005)
ex = dcf(exit_mult=EXIT_MULT)
near(rows[-1]["ebitda"], 522.4, 0.05)
near(ex["tv"], 6790.7, 0.05)
near(ex["pv_tv"], 4393.3, 0.05)
near(ex["ev"], 5224.0, 0.05)
near(ex["eq"], 5079.0, 0.05)
near(ex["ps"], 50.04, 0.005)
near(ex["tv_share"], 0.84, 0.005)
has(t, "US$522.4 million", "US$6,790.7 million", "US$4,393.3 million", "US$5,224.0 million",
    "US$5,079.0 million", "US$50.04", "84%", "US$10.62")
near(ex["ps"] - base["ps"], 10.62, 0.005)
near(base["tv"] / rows[-1]["ebitda"], 9.8, 0.05)
g_impl = (ex["tv"] * WACC - rows[-1]["ufcf"]) / (ex["tv"] + rows[-1]["ufcf"])
near(g_impl, 0.044, 0.0005)
has(t, "9.8 times", "4.4%")
grid = {}
for w in (0.081, 0.086, 0.091, 0.096, 0.101):
    line = [dcf(wacc=w, tg=g)["ps"] for g in (0.02, 0.025, 0.03, 0.035, 0.04)]
    grid[w] = line
    has(t, " | ".join(f"{v:.2f}" for v in line))
near(grid[0.081][2] / grid[0.091][2] - 1, 0.22, 0.005)
has(t, "22%", "US$47.91")
assert sum(1 for line in grid.values() for v in line if v >= PRICE) == 3
dr = dcf(wacc=0.101, tg=0.02)
near(dr["tv_share"], 0.75, 0.005)
near(dr["ev"], 3169, 0.5)
tv1 = 100 * 1.03 / 0.07
near(tv1, 1471.4, 0.05)
near(tv1 / 1.1 ** 5, 913.6, 0.05)
has(t, "US$1,471.4 million", "US$913.6 million")
ev1 = 300 + 913.6
near((ev1 - 200 + 50) / 100, 10.64, 0.005)
near(913.6 / ev1, 0.75, 0.005)
has(t, "1,213.6", "1,063.6", "US$10.64")
near(grid[0.096][1], 33.93, 0.005)
near((50 - 33.93) / 50, 0.32, 0.005)
has(t, "US$33.93", "US$16.07", "32%")
near(2000 / 1.08 ** 5, 1361.2, 0.05)
has(t, "US$1,361.2 million")


def run_code_dcf(wacc=0.091, g=0.03, exit_multiple=None):
    """Same logic as the lesson 5 snippet."""
    growth = [0.15, 0.13, 0.11, 0.09, 0.07]
    margin = [0.215, 0.225, 0.23, 0.235, 0.24]
    capex = [0.065, 0.058, 0.052, 0.047, 0.042]
    rev, pv = 1150, 0.0
    for n, (gr, m, cx) in enumerate(zip(growth, margin, capex), start=1):
        new = rev * (1 + gr)
        u = new * m * 0.75 + new * 0.03 - new * cx - (new - rev) * 0.17
        pv += u / (1 + wacc) ** n
        rev = new
    ebitda = rev * (margin[-1] + 0.03)
    tv = ebitda * exit_multiple if exit_multiple else u * (1 + g) / (wacc - g)
    return (pv + tv / (1 + wacc) ** 5 - 275 + 130) / 101.5


near(run_code_dcf(), base["ps"], 1e-9)
near(run_code_dcf(exit_multiple=13), ex["ps"], 1e-9)

# ---------------- Lesson 6: reverse DCF ----------------
t = lesson(F, 6)
ig = implied_growth()
near(ig, 0.194, 0.0005)
near(REV0 * (1 + ig) ** 5, 2794, 0.5)
near((rows[-1]["rev"] / REV0) ** 0.2 - 1, 0.110, 0.0005)
has(t, "19.4%", "US$2,794 million", "US$1,935 million", "11.0%")
iw = implied_wacc()
near(iw, 0.079, 0.0005)
has(t, "7.9%")
lo, hi = 0.0, WACC - 0.0005
for _ in range(80):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if dcf(tg=mid)["ps"] < PRICE else (lo, mid)
near(mid, 0.044, 0.0005)
has(t, "4.4%")
g_q = (WACC * EV - 106.25) / (EV + 106.25)
near(g_q, 0.069, 0.0005)
near(WACC * EV - 106.25, 368.8, 0.05)
near(EV + 106.25, 5326.3, 0.06)
has(t, "368.8 / 5,326.3 = 6.9%")
near((0.08 * 2000 - 80) / 2080, 0.0385, 0.00005)
has(t, "80 / 2,080 = 3.85%")
near(1.194 ** 5, 2.43, 0.005)
has(t, "2.43", "2.4 times", "US$10.58")
near(PRICE - base["ps"], 10.58, 0.005)
near((PRICE - base["ps"]) / PRICE, 0.21, 0.005)
has(t, "21%")

# ---------------- Lesson 7: comparables ----------------
t = lesson(F, 7)
peers = {"B": (2900, 200), "C": (6800, 400), "D": (4200, 200), "E": (3000, 250)}
mult = {k: ev / e for k, (ev, e) in peers.items()}
assert mult == {"B": 14.5, "C": 17.0, "D": 21.0, "E": 12.0}
med = statistics.median(mult.values())
assert med == 15.75
vpers = (med * EBITDA0 - DEBT + CASH) / SH_DIL
near(vpers, 40.47, 0.005)
near(med * 270, 4252.5, 0.05)
near((12 * 270 - 145) / SH_DIL, 30.49, 0.005)
near((21 * 270 - 145) / SH_DIL, 54.43, 0.005)
assert statistics.median([8, 12, 20, 4]) == 10
near(EBITDA0 / REV0, 0.235, 0.0005)
has(t, "15.75", "US$4,252.5 million", "US$4,107.5 million", "US$40.47", "US$30.49", "US$54.43", "23.5%", "19.3")
assert (100 + 18 - 4 - 6) / 100 == 1.08 and (100 - 4 - 6) / 100 == 0.9 and 28 + 14 == 42
has(t, "108%", "90%", "42")
assert 1200 / 30000 == 0.04 and 1200 / (1200 + 800) == 0.6 and 9000 / 75000 == 0.12
has(t, "4.0%", "60%", "12.0%")
near(520 / 500 - 1, 0.04, 1e-9)
near(667 / 120, 5.56, 0.005)
near(365 / (667 / 120), 65.7, 0.05)
has(t, "5.56", "65.7 days")
assert 600 / 50 == 12 and 12 + 6 + 22 + 5 == 45 and 70 - 45 == 25 and 50 - 45 == 5
has(t, "12 years", "US$45 a barrel", "US$25 a barrel", "US$5")
assert statistics.median([8, 10, 12, 30]) == 11 and (8 + 10 + 12 + 30) / 4 == 15
assert (11 * 80 - 150 + 30) / 20 == 38.0
assert (200 + 30 - 10 - 14) / 200 == 1.03 and (200 - 10 - 14) / 200 == 0.88
assert 600 / 15000 == 0.04 and 550 / 1000 == 0.55
has(t, "US$38.00", "103%", "88%", "55%")

# ---------------- Lesson 8: moats ----------------
t = lesson(F, 8)
near(176.25 / 760, 0.2319, 0.0001)
ep = 176.25 - 0.091 * 760
near(ep, 107.09, 0.005)
has(t, "23.2%", "9.1%", "69.16", "US$107.1 million", "US$176.25 million", "US$760 million")
fni27 = (forecast(**BASE)[1]["ebit"] - 15) * (1 - TAX)
feps27 = fni27 / SH_DIL
near(fni27, 240.9, 0.05)
near(feps27, 2.374, 0.0005)
tgt = feps27 * 22
near(tgt, 52.22, 0.005)
near(tgt / PRICE - 1, 0.044, 0.0005)
has(t, "US$2.37", "US$240.9 million", "2.374 x 22 = US$52.22", "4.4%", "9.4%")
assert 90 / 600 == 0.15 and 90 - 0.09 * 600 == 36
assert 48 - 0.09 * 600 == -6
has(t, "15.0%", "US$36 million", "-US$6 million")
assert 3.00 * 18 == 54
near(54 / 50 - 1, 0.08, 1e-9)
has(t, "US$54", "8.0%")

# ---------------- Lesson 9: pitch and part check ----------------
t = lesson(F, 9)
bear, bull = dcf(BEAR)["ps"], dcf(BULL)["ps"]
near(bear, 28.75, 0.005)
near(bull, 53.24, 0.005)
ev_s = 0.25 * bear + 0.5 * base["ps"] + 0.25 * bull
near(ev_s, 40.21, 0.005)
near(PRICE / ev_s - 1, 0.244, 0.001)
near(bear / PRICE - 1, -0.425, 0.0005)
near(bull / PRICE - 1, 0.065, 0.001)
near(ev_s / 1.10, 36.55, 0.005)
near(dcf(wacc=0.101)["ps"], 33.33, 0.005)
has(t, "US$28.75", "US$39.42", "US$53.24", "US$40.21", "24%", "42.5%", "6.5%", "40.21 / 1.10 = 36.55",
    "US$36.50", "US$33.33", "19.4%", "23.2%")
alt = 0.4 * round(bear, 2) + 0.4 * round(base["ps"], 2) + 0.2 * round(bull, 2)
near(alt, 37.92, 0.005)
near(PRICE / 37.92 - 1, 0.319, 0.0005)
has(t, "US$37.92", "31.9%")
near(40.21 / 1.15, 34.97, 0.005)
has(t, "US$34.97")
assert 60 / 2.5 == 24.0 and round(2.5 / 60 * 100, 2) == 4.17
assert 3000 + 800 + 100 - 300 == 3600 and 3600 / 300 == 12.0
assert 120 * 0.75 + 20 - 45 - 10 == 55
ke_p = 0.045 + 1.1 * 0.05
assert abs(ke_p - 0.10) < 1e-12 and abs(0.8 * ke_p + 0.2 * 0.04 - 0.088) < 1e-12
tvp = 60 * 1.03 / 0.06
near(tvp, 1030, 1e-9)
near(tvp / 1.09 ** 5, 669.4, 0.05)
near(40 / 38 - 1, 0.053, 0.0005)
has(t, "24.0", "4.17%", "US$3,600 million", "12.0", "US$55 million", "8.8%", "US$1,030 million",
    "US$669.4 million", "5.3%")
