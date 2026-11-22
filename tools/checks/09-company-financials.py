"""Number checks for part 9, Company financials.

One made-up company, Northwind Tools Inc., two fiscal years (FY2024 and FY2025,
year end December 31). Every number in every lesson comes from the model below.
US$ millions except per-share figures and share counts (millions of shares).
The figure scripts read this model too: everything above the marker line.
"""
# ---- The model (no imports needed above this line) ----
Y0, Y1 = "FY2024", "FY2025"
TAX = 0.25

IS = {  # income statements
    Y0: dict(rev=1000, cogs=600, sga=130, rd=60, da=30, interest=16, sbc=25),
    Y1: dict(rev=1150, cogs=667, sga=145, rd=68, da=35, interest=15, sbc=30),
}
for _y, d in IS.items():
    d["gp"] = d["rev"] - d["cogs"]
    d["opex"] = d["sga"] + d["rd"] + d["da"]
    d["ebit"] = d["gp"] - d["opex"]
    d["ebitda"] = d["ebit"] + d["da"]
    d["pretax"] = d["ebit"] - d["interest"]
    d["tax"] = d["pretax"] * TAX
    d["ni"] = d["pretax"] - d["tax"]

BS = {  # balance sheets at December 31
    Y0: dict(cash=150, ar=125, inv=100, prepaid=25, ppe=400, intang=60, goodwill=140,
             ap=80, accrued=45, cur_debt=25, lt_debt=275, apic=300, re=275, treasury=0),
    Y1: dict(cash=130, ar=150, inv=120, prepaid=30, ppe=450, intang=55, goodwill=140,
             ap=95, accrued=55, cur_debt=25, lt_debt=250, apic=340, re=410, treasury=-100),
}
for _y, d in BS.items():
    d["ca"] = d["cash"] + d["ar"] + d["inv"] + d["prepaid"]
    d["assets"] = d["ca"] + d["ppe"] + d["intang"] + d["goodwill"]
    d["cl"] = d["ap"] + d["accrued"] + d["cur_debt"]
    d["liab"] = d["cl"] + d["lt_debt"]
    d["equity"] = d["apic"] + d["re"] + d["treasury"]
    d["debt"] = d["cur_debt"] + d["lt_debt"]
    assert d["assets"] == d["liab"] + d["equity"], _y

# FY2025 cash flow statement, indirect method
DIV, BUYBACK, OPT_PROCEEDS, CAPEX, DEBT_REPAID = 30, 100, 10, 80, 25
d0, d1, i1 = BS[Y0], BS[Y1], IS[Y1]
CF = dict(
    ni=i1["ni"], da=i1["da"], sbc=i1["sbc"],
    d_ar=-(d1["ar"] - d0["ar"]), d_inv=-(d1["inv"] - d0["inv"]), d_prepaid=-(d1["prepaid"] - d0["prepaid"]),
    d_ap=d1["ap"] - d0["ap"], d_accrued=d1["accrued"] - d0["accrued"],
)
CF["d_wc"] = CF["d_ar"] + CF["d_inv"] + CF["d_prepaid"] + CF["d_ap"] + CF["d_accrued"]
CF["cfo"] = CF["ni"] + CF["da"] + CF["sbc"] + CF["d_wc"]
CF["capex"] = -CAPEX
CF["cfi"] = -CAPEX
CF["cff"] = -DEBT_REPAID - BUYBACK - DIV + OPT_PROCEEDS
CF["net"] = CF["cfo"] + CF["cfi"] + CF["cff"]
CF["fcf"] = CF["cfo"] - CAPEX
assert d0["cash"] + CF["net"] == d1["cash"]
# the other ties
assert d0["ppe"] + CAPEX - 30 == d1["ppe"]          # depreciation 30, amortization 5
assert d0["intang"] - 5 == d1["intang"]
assert d0["re"] + i1["ni"] - DIV == d1["re"]
assert d0["apic"] + i1["sbc"] + OPT_PROCEEDS == d1["apic"]
assert d0["treasury"] - BUYBACK == d1["treasury"]
assert d0["debt"] - DEBT_REPAID == d1["debt"]

# Shares (millions)
SH_START, SH_ISSUED, SH_BOUGHT, BUY_PRICE = 100.0, 0.5, 2.0, 50.0
SH_END = SH_START + SH_ISSUED - SH_BOUGHT
W_BASIC = 99.5
OPT_N, OPT_K, AVG_PRICE, RSU = 4.0, 20.0, 50.0, 0.6
OPT_NET = OPT_N - OPT_N * OPT_K / AVG_PRICE
W_DIL = W_BASIC + OPT_NET + RSU
assert SH_BOUGHT * BUY_PRICE == BUYBACK

# ==== LESSON CHECKS (the figure scripts stop reading here) ====
from _lib import ROOT, lesson, has, usd, pct  # noqa: E402,F401
import json  # noqa: E402
from datetime import date  # noqa: E402

F = "09-company-financials"


def r1(x):
    """Round half up to one decimal, as a reader with a calculator would."""
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(str(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def p1(x):
    return f"{r1(100 * x):.1f}%"


i0, i1 = IS[Y0], IS[Y1]
b0, b1 = BS[Y0], BS[Y1]

# ---- Lesson 1
t = lesson(F, 1)
has(t, "Northwind Tools Inc.", "December 31", "FY2024 and FY2025", "Three 10-Qs", "one 10-K",
    "Item 2.02", "Item 5.02", "Item 1.01", "0000320193", "# needs internet",
    '{"User-Agent": "Your Name your.email@example.com"}', "10 per second", "SEDAR+", "IFRS Accounting Standards")
for item in ["| 1 | Business |", "| 1A | Risk Factors |", "| 7 | Management's Discussion and Analysis (MD&A) |",
             "| 8 | Financial Statements and Supplementary Data |", "| 9A | Controls and Procedures |"]:
    has(t, item)

# ---- Lesson 2
t = lesson(F, 2)
assert round(12 * 0 + 2.4 / 12, 2) == 0.2 and round(3 * 0.2, 2) == 0.6 and round(2.4 - 0.6, 2) == 1.8
has(t, "US$12 million", "US$2.4 million", "US$0.2 million a month", "3 x 0.2 = US$0.6 million", "US$1.8 million")
for k, v in [("Revenue", "rev"), ("Cost of goods sold", "cogs"), ("Gross profit", "gp"), ("SG&A", "sga"), ("R&D", "rd"),
             ("Depreciation and amortization", "da"), ("Operating income (EBIT)", "ebit"), ("Interest expense", "interest"),
             ("Income before taxes", "pretax"), ("Income taxes (25%)", "tax"), ("Net income", "ni")]:
    a, b = i0[v], i1[v]
    has(t, f"| {k} | {a:,.0f} | {b:,.0f} |")
assert i1["sga"] + i1["rd"] + i1["da"] == i1["opex"] == 248
assert i1["gp"] == 483 and i1["ebit"] == 235 and i1["ebitda"] == 270 and i1["pretax"] == 220 and i1["tax"] == 55 and i1["ni"] == 165
has(t, "1,150 - 667 = US$483 million", "145 + 68 + 35 = US$248 million", "483 - 248 = US$235 million",
    "235 + 35 = US$270 million", "235 - 15 = US$220 million", "0.25 x 220 = US$55 million", "220 - 55 = US$165 million")
assert p1(i1["gp"] / i1["rev"]) == "42.0%" and p1(i1["ebit"] / i1["rev"]) == "20.4%" and p1(i1["ni"] / i1["rev"]) == "14.3%"
has(t, "483 / 1,150 = 42.0%", "235 / 1,150 = 20.4%", "165 / 1,150 = 14.3%", "US$25 million in FY2024 and US$30 million in FY2025")
assert i0["gp"] == 400 and i0["ebit"] == 180 and i0["pretax"] == 164 and i0["tax"] == 41 and i0["ni"] == 123
has(t, "US$400 million", "US$180 million", "Pretax = 180 - 16 = 164", "Tax = 0.25 x 164 = 41", "Net income = US$123 million")
assert i0["ebitda"] == 210 and 210 / 1000 == 0.21
has(t, "180 + 30 = US$210 million", "210 / 1,000 = 21.0%")
assert 3.6 / 12 == 0.3 and round(3 * 0.3, 2) == 0.9 and round(3.6 - 0.9, 2) == 2.7
has(t, "US$0.3 million", "US$0.9 million", "US$2.7 million")
assert 55 / 220 == 0.25 and 220 - 20 == 200
has(t, "55 / 220 = 25.0%", "US$200 million")

# ---- Lesson 3
t = lesson(F, 3)
assert b1["assets"] == 1075 and b1["liab"] == 425 and b1["equity"] == 650
has(t, "US$1,075 million of assets", "US$425 million", "US$650 million", "425 + 650 = US$1,075 million")
rows = [("Cash", "cash"), ("Accounts receivable", "ar"), ("Inventory", "inv"), ("Prepaid and other", "prepaid"),
        ("Total current assets", "ca"), ("Property, plant and equipment (PP&E), net", "ppe"), ("Intangible assets", "intang"),
        ("Goodwill", "goodwill"), ("Total assets", "assets"), ("Accounts payable", "ap"), ("Accrued expenses", "accrued"),
        ("Current portion of debt", "cur_debt"), ("Total current liabilities", "cl"), ("Long-term debt", "lt_debt"),
        ("Total liabilities", "liab"), ("Common stock and paid-in capital", "apic"), ("Retained earnings", "re"),
        ("Treasury stock", "treasury"), ("Total shareholders' equity", "equity")]
for k, v in rows:
    has(t, f"| {k} | {b0[v]:,.0f} | {b1[v]:,.0f} |")
has(t, f"| Total liabilities and equity | {b0['liab'] + b0['equity']:,} | {b1['liab'] + b1['equity']:,} |")
assert b1["ap"] + b1["accrued"] == 150
has(t, "95 + 55 = 150")
assert b1["ca"] - b1["cl"] == 255 and b0["ca"] - b0["cl"] == 250
has(t, "430 - 175 = US$255 million", "400 - 150 = US$250 million")
assert 60 / 10 == 6 and 60 - 3 * 6 == 42 and 400 + 80 - 30 == 450
has(t, "60 / 10 = US$6 million", "60 - 18 = US$42 million", "400 + 80 - 30 = US$450 million")
assert 90 - 70 == 20
has(t, "90 - 70 = US$20 million")
assert b1["debt"] == 275 and 275 + 165 - 30 == 410
has(t, "US$275 million in total", "275 + 165 net income - 30 dividends = 410")
assert (48 - 8) / 8 == 5 and 48 - 4 * 5 == 28
has(t, "(48 - 8) / 8 = US$5 million", "48 - 20 = US$28 million")
assert 140 - 40 == 100 and 150 - 100 == 50
has(t, "140 - 40 = US$100 million", "150 - 100 = US$50 million", "275 + 165 - 30 = US$410 million")

# ---- Lesson 4
t = lesson(F, 4)
assert CF["d_wc"] == -25 and CF["cfo"] == 205 and CF["cfi"] == -80 and CF["cff"] == -145 and CF["net"] == -20 and CF["fcf"] == 125
has(t, "-25 - 20 - 5 + 15 + 10 = -25", "165 + 35 + 30 - 25 = US$205 million", "CFI = -US$80 million",
    "-25 - 100 - 30 + 10 = -US$145 million", "205 - 80 - 145 = -US$20 million", "150 - 20 = US$130 million")
for k, v in [("Net income", 165), ("Depreciation and amortization", 35), ("Stock-based compensation", 30), ("Change in receivables", -25),
             ("Change in inventory", -20), ("Change in prepaid and other", -5), ("Change in accounts payable", 15),
             ("Change in accrued expenses", 10), ("Cash from operating activities", 205), ("Capital expenditures", -80),
             ("Cash from investing activities", -80), ("Repayment of debt", -25), ("Share repurchases", -100), ("Dividends paid", -30),
             ("Proceeds from option exercises", 10), ("Cash from financing activities", -145), ("Net change in cash", -20),
             ("Cash at start of year", 150), ("Cash at end of year", 130)]:
    has(t, f"| {k} | {v} |")
assert p1(125 / 1150) == "10.9%" and 100 + 30 == 130 and 125 - 30 == 95
has(t, "205 - 80 = US$125 million", "125 / 1,150 = 10.9%", "100 + 30 = US$130 million", "125 - 30 = US$95 million", "20% against revenue growth of 15%")
assert b1["ar"] / b0["ar"] == 1.2 and i1["rev"] / i0["rev"] == 1.15
assert 80 + 20 + 10 - 15 + 5 == 100 and 100 - 35 == 65 and p1(65 / 80) == "81.3%"
has(t, "80 + 20 + 10 - 15 + 5 = US$100 million", "100 - 35 = US$65 million", "65 / 80 = 81.3%", "US$20 million", "150 + 205 - 80 - 145 = US$130 million")

# ---- Lesson 5
t = lesson(F, 5)
assert 275 + 165 - 30 == 410 and 150 - 20 == 130 and 400 + 80 - 30 == 450 and 300 - 25 == 275
has(t, "Opening 275 + net income 165 - dividends 30", "Opening 150 + net change (-20)", "Opening 400 + capex 80 - depreciation 30", "Opening 300 - repayment 25")
assert 300 + 30 + 10 == 340 and 0 - 100 == -100 and 1075 == 425 + 650
has(t, "paid-in capital 300 + stock-based pay 30 + option proceeds 10 = 340", "assets 1,075 = liabilities 425 + equity 650")
pre = i1["ebit"] - 10 - i1["interest"]
assert pre == 210 and pre * TAX == 52.5 and pre - pre * TAX == 157.5 and 205 - 7.5 + 10 == 207.5
has(t, "220 to 210", "55 to 52.5", "210 - 52.5 = US$157.5 million", "205 - 7.5 + 10 = US$207.5 million", "25% of 10")
assert 410 + 190 - 35 == 565
has(t, "410 + 190 - 35 = US$565 million", "1,075 - 10 = 1,065", "650 - 10 = 640", "425 + 640 = 1,065")

# ---- Lesson 6
t = lesson(F, 6)
for name, key, a, b, c in [("Gross margin", "gp", "40.0%", "42.0%", "+2.0"), ("EBITDA margin", "ebitda", "21.0%", "23.5%", "+2.5"),
                           ("Operating margin", "ebit", "18.0%", "20.4%", "+2.4"), ("Net margin", "ni", "12.3%", "14.3%", "+2.0")]:
    m0, m1 = i0[key] / i0["rev"], i1[key] / i1["rev"]
    assert p1(m0) == a and p1(m1) == b and f"{r1(100 * (m1 - m0)):+.1f}" == c, name
    has(t, f"| {name} | {a} | {b} | {c} |")
g_rev, g_ebit, g_ni = i1["rev"] / i0["rev"] - 1, i1["ebit"] / i0["ebit"] - 1, i1["ni"] / i0["ni"] - 1
assert p1(g_rev) == "15.0%" and p1(g_ebit) == "30.6%" and p1(g_ni) == "34.1%"
has(t, "(1,150 - 1,000) / 1,000 = 15.0%", "(235 - 180) / 180 = 30.6%", "(165 - 123) / 123 = 34.1%")
assert round(30.6 / 15.0, 2) == 2.04
has(t, "30.6 / 15.0 = 2.04")
assert p1(130 / 1000) == "13.0%" and p1(145 / 1150) == "12.6%" and p1(60 / 1000) == "6.0%" and p1(68 / 1150) == "5.9%"
has(t, "130 / 1,000 = 13.0%", "145 / 1,150 = 12.6%", "6.0% to 5.9%")
assert p1((864 / 600) ** (1 / 3) - 1) == "12.9%" and round(1.44 ** (1 / 3), 4) == 1.1292
has(t, "1.1292", "12.9% a year")
assert 400 / 1000 == 0.4 and p1(483 / 1150) == "42.0%"
has(t, "400 / 1,000 = 40.0%", "483 / 1,150 = 42.0%")
assert 20 / 8 == 2.5 and 2.5 * 5 == 12.5
has(t, "20 / 8 = 2.5", "12.5%")
assert 0.13 * 1150 == 149.5 and 149.5 - 145 == 4.5 and 235 - 4.5 == 230.5
has(t, "US$149.5 million", "US$4.5 million lower", "230.5")

# ---- Lesson 7
t = lesson(F, 7)
ae, aa = (b0["equity"] + b1["equity"]) / 2, (b0["assets"] + b1["assets"]) / 2
assert ae == 612.5 and aa == 1037.5
has(t, "(575 + 650) / 2 = US$612.5 million", "(1,000 + 1,075) / 2 = US$1,037.5 million")
roe, roa = i1["ni"] / ae, i1["ni"] / aa
nopat = i1["ebit"] * (1 - TAX)
ic0, ic1 = b0["debt"] + b0["equity"] - b0["cash"], b1["debt"] + b1["equity"] - b1["cash"]
roic = nopat / ((ic0 + ic1) / 2)
assert p1(roe) == "26.9%" and p1(roa) == "15.9%" and nopat == 176.25 and ic0 == 725 and ic1 == 795 and (ic0 + ic1) / 2 == 760 and p1(roic) == "23.2%"
has(t, "165 / 612.5 = 26.9%", "165 / 1,037.5 = 15.9%", "235 x (1 - 0.25) = US$176.25 million", "300 + 575 - 150 = 725", "275 + 650 - 130 = 795",
    "US$760 million", "176.25 / 760 = 23.2%")
nm, at, em = i1["ni"] / i1["rev"], i1["rev"] / aa, aa / ae
assert p1(nm) == "14.3%" and round(at, 3) == 1.108 and round(em, 3) == 1.694 and p1(nm * at * em) == "26.9%"
has(t, "165 / 1,150 = 14.3% net margin", "1,150 / 1,037.5 = 1.108 asset turnover", "1,037.5 / 612.5 = 1.694 equity multiplier", "0.1435 x 1.108 x 1.694 = 26.9%")
assert 50 / 500 == 0.10 and 50 / 200 == 0.25 and 500 / 200 == 2.5
has(t, "50 / 500 = 10.0%", "50 / 200 = 25.0%", "500 / 200 = 2.5")
assert round(100 * 0.79, 2) == 79 and 300 + 400 - 100 == 600 and p1(79 / 600) == "13.2%"
has(t, "100 x (1 - 0.21) = US$79 million", "300 + 400 - 100 = US$600 million", "79 / 600 = 13.2%")
assert p1(165 / 650) == "25.4%" and p1(165 / 750) == "22.0%" and r1(100 * (165 / 650 - 165 / 750)) == 3.4
has(t, "165 / 650 = 25.4%", "165 / 750 = 22.0%", "3.4 percentage points")
assert round(0.05 * 3 * 2, 4) == 0.30 and round(0.20 * 0.5 * 3, 4) == 0.30
has(t, "0.05 x 3.0 x 2.0 = 30.0%", "0.20 x 0.5 x 3.0 = 30.0%")

# ---- Lesson 8
t = lesson(F, 8)
cr, qr = b1["ca"] / b1["cl"], (b1["cash"] + b1["ar"]) / b1["cl"]
de, nd = b1["debt"] / b1["equity"], b1["debt"] - b1["cash"]
assert round(cr, 2) == 2.46 and round(qr, 2) == 1.60 and round(de, 2) == 0.42 and nd == 145 and round(nd / i1["ebitda"], 2) == 0.54
cov = i1["ebit"] / i1["interest"]
assert round(cov, 1) == 15.7
has(t, "430 / 175 = 2.46", "(130 + 150) / 175 = 1.60", "275 / 650 = 0.42", "275 - 130 = US$145 million", "145 / 270 = 0.54 times", "235 / 15 = 15.7 times")
assert round(b0["ca"] / b0["cl"], 2) == 2.67 and round((b0["cash"] + b0["ar"]) / b0["cl"], 2) == 1.83 and round(b0["debt"] / b0["equity"], 2) == 0.52
assert 180 / 16 == 11.25
has(t, "400 / 150 = 2.67", "275 / 150 = 1.83", "300 / 575 = 0.52", "300 - 150 = US$150 million", "180 / 16 = 11.3 times")
assert 15 / ((300 + 275) / 2) == 15 / 287.5 and p1(15 / 287.5) == "5.2%" and 117.5 / 15 > 7.8
assert round(117.5 / 15, 1) == 7.8 and 25 / 130 < 0.2
has(t, "117.5 / 15 = 7.8 times", "US$287.5 million of debt is an average rate of 5.2%", "under 20%")
assert 240 / 150 == 1.6 and (40 + 80) / 150 == 0.8
has(t, "240 / 150 = 1.60", "(40 + 80) / 150 = 0.80")
assert 320 / 400 == 0.8 and 320 - 40 == 280 and 280 / 100 == 2.8
has(t, "320 / 400 = 0.80", "320 - 40 = US$280 million", "280 / 100 = 2.8 times")
assert 270 / 15 == 18.0 and 60 / 40 == 1.5 and 60 * 0.7 == 42 and round(42 / 40, 2) == 1.05
has(t, "270 / 15 = 18.0 times", "60 / 40 = 1.5 times", "42 / 40 = 1.05 times")

# ---- Lesson 9
t = lesson(F, 9)
assert SH_END == 98.5 and W_BASIC == 99.5
eps_b, eps_d = i1["ni"] / W_BASIC, i1["ni"] / W_DIL
assert round(eps_b, 2) == 1.66 and round(eps_d, 2) == 1.61 and OPT_N * OPT_K == 80 and 80 / 50 == 1.6 and round(OPT_NET, 1) == 2.4 and W_DIL == 102.5
has(t, "100.0 + 0.5 - 2.0 = 98.5 million", "165 / 99.5 = US$1.66", "4.0 x 20 = US$80 million", "80 / 50 = 1.6 million", "4.0 - 1.6 = 2.4 million",
    "99.5 + 2.4 + 0.6 = 102.5 million", "165 / 102.5 = US$1.61")
assert p1(1 - eps_d / eps_b) == "2.9%"
has(t, "from 1.66 to 1.61, which is 2.9%")
assert p1(30 / 1150) == "2.6%" and 30 / 50 == 0.6
has(t, "30 / 1,150 = 2.6% of revenue", "0.6 million shares")
mcap = 98.5 * 50
assert mcap == 4925 and p1(100 / mcap) == "2.0%" and p1(130 / mcap) == "2.6%" and SH_BOUGHT - SH_ISSUED == 1.5
has(t, "98.5 x 50 = US$4,925 million", "100 / 4,925 = 2.0%", "130 / 4,925 = 2.6%", "1.5 million, or 1.5% of 100.0", "US$100 million to buy back 2.0 million shares")
assert 80 / 40 == 2 and round(10 - 10 * 30 / 45, 2) == 3.33 and round(80 / (40 + 10 - 10 * 30 / 45), 2) == 1.85
has(t, "80 / 40 = US$2.00", "10 - (10 x 30) / 45 = 10 - 6.67 = 3.33 million", "43.33 million", "80 / 43.33 = US$1.85")
assert 10 * 30 / 25 > 10
has(t, "None. The options are out of the money")
assert 400 / 200 == 2 and round(400 / 190, 2) == 2.11 and r1(100 * (200 / 190 - 1)) == 5.3
has(t, "400 / 200 = US$2.00", "400 / 190 = US$2.11", "up 5.3%")
assert 0.5 / 2.0 == 0.25
has(t, "0.5 / 2.0 = 25%")

# ---- Lesson 10
t = lesson(F, 10)
adj_ni = i1["ni"] + 30 * (1 - TAX)
adj_eps = adj_ni / W_DIL
assert adj_ni == 187.5 and round(adj_eps, 2) == 1.83 and round(eps_d, 2) == 1.61 and round(adj_eps - eps_d, 2) == 0.22
has(t, "US$1.61", "US$1.83", "30 x (1 - 0.25) = US$22.5 million", "165 + 22.5 = US$187.5 million", "187.5 / 102.5 = US$1.83", "US$0.22 a share")
assert 165 + 15 + 55 + 35 == 270 and 270 + 30 == 300 and p1(300 / 1150) == "26.1%" and p1(270 / 1150) == "23.5%"
has(t, "| EBITDA | 270 |", "| Adjusted EBITDA | 300 |", "300 / 1,150 = 26.1%", "23.5%")
cc = CF["cfo"] / i1["ni"]
accr = (i1["ni"] - CF["cfo"]) / aa
assert round(cc, 2) == 1.24 and p1(accr) == "-3.9%" and p1(125 / 165) == "75.8%" and round(125 / 165, 2) == 0.76
has(t, "205 / 165 = 1.24", "(165 - 205) / 1,037.5 = -3.9%", "125 / 165 = 0.76")
dso0, dso1 = b0["ar"] / i0["rev"] * 365, b1["ar"] / i1["rev"] * 365
dio0, dio1 = b0["inv"] / i0["cogs"] * 365, b1["inv"] / i1["cogs"] * 365
assert r1(dso0) == 45.6 and r1(dso1) == 47.6 and r1(dio0) == 60.8 and r1(dio1) == 65.7
has(t, "125 / 1,000 x 365 = 45.6 days", "150 / 1,150 x 365 = 47.6 days", "100 / 600 x 365 = 60.8 days", "120 / 667 x 365 = 65.7 days")
assert b1["ar"] / b0["ar"] == 1.2 and b1["inv"] / b0["inv"] == 1.2
has(t, "both grew 20% against revenue growth of 15%")
assert 90 / 50 == 1.8 and 90 + 15 + 12 == 117 and 117 / 50 == 2.34 and round(2.34 - 1.8, 2) == 0.54 and 0.54 / 1.8 == 0.30
has(t, "90 / 50 = US$1.80", "90 + 15 + 12 = US$117 million", "117 / 50 = US$2.34", "US$0.54, or 30% of GAAP EPS")
assert 45 / 60 == 0.75 and (60 - 45) / 600 == 0.025
has(t, "45 / 60 = 0.75", "(60 - 45) / 600 = 2.5%")
d0, d1 = 80 / 600 * 365, 130 / 700 * 365
assert r1(d0) == 48.7 and r1(d1) == 67.8 and r1(d1 - d0) == 19.1 and r1(100 * (700 / 600 - 1)) == 16.7 and 130 / 80 == 1.625
has(t, "80 / 600 x 365 = 48.7 days", "130 / 700 x 365 = 67.8 days", "19.1 days", "16.7%", "62.5%")
assert 95 / 125 == 0.76 and 30 / 125 == 0.24
has(t, "125 - 30 = US$95 million", "76.0% of FCF", "24.0%")

# ---- Lesson 11
t = lesson(F, 11)
assert date(2026, 2, 4).weekday() == 2 and date(2026, 2, 5).weekday() == 3
has(t, "Wednesday, February 4, 2026", "Thursday, February 5")
q4_ni, q4_eps = 46, 46 / W_DIL
assert 840 + 310 == 1150 and round(q4_eps, 2) == 0.45 and 165 - 46 == 119
has(t, "US$840 million", "46 / 102.5 = US$0.45")
assert round(0.45 - 0.42, 2) == 0.03 and p1(0.03 / 0.42) == "7.1%" and 310 - 300 == 10 and p1(10 / 300) == "3.3%"
has(t, "0.45 - 0.42 = US$0.03", "0.03 / 0.42 = 7.1%", "310 - 300 = US$10 million", "10 / 300 = 3.3%")
mid = (1.74 + 1.84) / 2
assert round(mid, 2) == 1.79 and p1(1.79 / 1.86 - 1) == "-3.8%" and (1250 + 1290) / 2 == 1270 and p1(1270 / 1150 - 1) == "10.4%"
assert p1(1.79 / round(eps_d, 2) - 1) == "11.2%"
has(t, "1.79 / 1.86 - 1 = -3.8%", "US$1,250 to 1,290 million", "midpoint of 1,270", "up 10.4% from 1,150", "1.79 / 1.61 - 1 = +11.2%")
cb = json.loads((ROOT / "docs" / "assets" / "charts" / F / "northwind-earnings-gap.json").read_text(encoding="utf-8"))["bars"]
byd = {b[0]: b for b in cb}
pre, ev = byd["2026-02-04"], byd["2026-02-05"]
assert pre[4] == 50.00 and ev[1] == 47.50 and ev[4] == 46.90 and ev[5] == 4050000 and pre[5] == 1170800
assert p1(47.5 / 50 - 1) == "-5.0%" and p1(46.9 / 50 - 1) == "-6.2%"
post = [b for b in cb if b[0] > "2026-02-05"]
assert len(post) == 12 and min(b[3] for b in post) == 46.82 and max(b[2] for b in post) == 48.26
has(t, "opens 5.0% lower", "47.50", "46.90", "6.2% below 50.00", "4,050,000 shares", "1,170,800", "next 12 sessions", "between 46.82 and 48.26")
assert round(1.20 - 1.05, 2) == 0.15 and p1(0.15 / 1.05) == "14.3%"
has(t, "1.20 - 1.05 = US$0.15", "0.15 / 1.05 = 14.3%")
assert round(-0.20 - -0.25, 2) == 0.05 and p1(0.05 / 0.25) == "20.0%"
has(t, "-0.20 - (-0.25) = +US$0.05", "0.05 / |-0.25| = 20.0%")
assert p1(84.8 / 80 - 1) == "6.0%"
has(t, "(84.80 - 80.00) / 80.00 = +6.0%")
# part check
assert 800 - 480 == 320 and 320 - 220 == 100 and (100 - 20) * 0.75 == 60
has(t, "800 - 480 = US$320 million", "320 - 220 = US$100 million", "80 x 0.75 = US$60 million")
assert 60 + 15 + 5 - 10 + 4 == 74 and 74 - 30 == 44
has(t, "60 + 15 + 5 - 10 + 4 = US$74 million", "74 - 30 = US$44 million")
assert 300 / 200 == 1.5 and 250 - 50 == 200 and 80 / 16 == 5.0
has(t, "300 / 200 = 1.50", "250 - 50 = US$200 million", "80 / 16 = 5.0 times")
assert 6 - 6 * 20 / 40 == 3 and round(100 / 53, 2) == 1.89
has(t, "6 - (6 x 20) / 40 = 6 - 3 = 3 million", "100 / 53 = US$1.89")
has(t, "US$0.60 of add-backs", "35% growth against 10% revenue growth")
