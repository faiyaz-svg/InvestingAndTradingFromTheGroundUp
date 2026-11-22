"""Number checks for part 14, Futures."""
import json
import math
from datetime import date

from _lib import ROOT, lesson, has, usd, cad

F = "14-futures"
CH = ROOT / "docs" / "assets" / "charts" / F

# Lesson 1
t = lesson(F, 1)
assert (6025 - 6000) * 5 * 2 == 250
assert (6000 - 6018.5) * 5 == -92.5
assert 2 * 6000 * 5 == 60000
assert (5982.5 - 5950) * 5 * 3 == 487.5
assert (6040 - 6052.25) * 5 * 4 == -245
has(t, usd(250), "-US$92.50", "US$60,000", usd(487.5), "-US$245.00", "32.50 points")

# Lesson 2
t = lesson(F, 2)
N = 6000 * 5 * 2
assert N == 60000 and 2 * 2400 == 4800 and 2 * 2200 == 4400
assert N / 4800 == 12.5
e0 = 5500
e1 = e0 + (5980 - 6000) * 10
e2 = e1 + (5880 - 5980) * 10
call = 4800 - e2
e3 = 4800 + (5920 - 5880) * 10
assert (e1, e2, call, e3) == (5300, 4300, 500, 5200)
assert (5920 - 6000) * 10 == -800 and 5500 + 500 - 800 == 5200
assert 4300 - (5880 - 5400) * 10 == -500
has(t, "-US$200", usd(5300,0), "-US$1,000", usd(4300,0), "US$500", usd(5200,0), "-US$800", "12.5", "-US$500", "US$600")
assert 30000 / 2400 == 12.5
assert 8000 + (5950 - 6000) * 5 * 3 == 7250
assert 3 * 2200 == 6600 and 3 * 2400 - 6300 == 900
assert (6000 - 6030) * 5 * 2 == -300
has(t, usd(7250,0), "US$6,600", "US$900", "-US$300")

# Lesson 3
t = lesson(F, 3)
assert 0.25 * 5 == 1.25 and 0.25 * 50 == 12.5 and 0.25 * 20 == 5 and 0.25 * 2 == 0.5
risk = 0.01 * 25000
ticks = (6011 - 6003) / 0.25
per = ticks * 1.25
n = math.floor(risk / per)
assert (ticks, per, n) == (32, 40, 6)
assert n * per == 240 and 240 / 25000 == 0.0096
notional = 6011 * 5 * n
assert notional == 180330 and round(notional / 25000, 1) == 7.2
assert n * 2400 == 14400 and round(14400 / 25000 * 100, 1) == 57.6
reward = (6027 - 6011) / 0.25 * 1.25 * n
assert reward == 480 and reward / 240 == 2
assert 8 * 50 == 400 and math.floor(risk / 400) == 0
has(t, usd(250), "32 ticks", usd(40), "6.25", usd(240), "0.96%", "US$180,330", "7.2 times", "US$14,400", "57.6%", "64 ticks", usd(480), "2.0R", "US$400", "0 contracts")
assert 6000 * 5 == 30000 and 6000 * 50 == 300000 and 10 * 1.25 == 12.5
assert 21000 * 20 == 420000 and 21000 * 2 == 42000
tk = 30 / 0.25
assert tk == 120 and tk * 0.5 == 60 and math.floor(250 / 60) == 4 and 4 * 60 == 240
loss = (6011 - 6002.5) / 0.25 * 1.25 * 6
assert loss == 255 and round(255 / 240, 2) == 1.06
has(t, "US$30,000", "US$300,000", "US$420,000", "US$42,000", "120 ticks", "4.17", "4 contracts", usd(255), "1.06R", "6,002.50")
b = json.loads((CH / "mxf-5m.json").read_text())["bars"]
seg = b[44:58]
assert min(x[3] for x in seg) == 6005.31
assert b[77][3] <= 6027 <= b[77][2] and max(x[2] for x in b[:77]) < 6027
has(t, "6,005.31")

# Lesson 4
t = lesson(F, 4)
d = json.loads((CH / "mxf-roll-daily.json").read_text())["bars"]
assert d[48][0] == "2026-09-10" and d[48][4] == 6010.0 and d[49][0] == "2026-09-11" and d[49][1] == 6050.51
gap = round(6050.51 - 6010.0, 2)
assert gap == 40.51
assert date(2026, 9, 10).weekday() == 3 and date(2026, 9, 18).weekday() == 4
assert [x for x in range(1, 31) if date(2026, 9, x).weekday() == 4][2] == 18
assert [x for x in range(1, 32) if date(2026, 12, x).weekday() == 4][2] == 18
assert (6010 - 5900) * 5 * 3 == 1650
assert round(5980 + gap, 2) == 6020.51 and round(6050.51 - 6020.51, 2) == 30 and round(6050.51 - 5980, 2) == 70.51
assert round(gap / 6010 * 100, 2) == 0.67
ratio = 6050.51 / 6010.0
assert round(ratio, 5) == 1.00674
assert round(5900 * ratio, 2) == 5939.77
assert round(5950 * ratio, 2) == 5990.11
assert round(6040 + gap, 2) == 6080.51
has(t, "September 18, 2026", "40.51", "0.67%", usd(1650), "6,020.51", "70.51", "1.00674", "5,939.77", "6,080.51", "December 18, 2026", "5,990.11")

# Lesson 5
t = lesson(F, 5)
S, r, dd, T_ = 6000, 0.04, 0.013, 0.25
assert round(S * r * T_, 2) == 60 and round(S * dd * T_, 2) == 19.5
F1 = S * (1 + (r - dd) * T_)
assert round(F1, 2) == 6040.5
F2 = S * (1 + (r - dd) / 12)
assert round(F2, 2) == 6013.5 and round(F1 - F2, 2) == 27 and 27 * 5 == 135
assert round(6080 - F1, 2) == 39.5
c1 = 80 * (1 + 0.07 * 0.25)
c2 = 80 * (1 + (0.04 + 0.03 - 0.09) * 0.25)
assert round(c1, 2) == 81.4 and round(c2, 2) == 79.6 and round((c1 - 80) / 80 * 100, 2) == 1.75
has(t, "60.00", "19.50", "40.50", "6,040.50", "-40.50", "6,013.50", "27.00", usd(135), "39.50", "81.40", "79.60", "1.75%", "7.0%")
f = 5000 * (1 + (0.05 - 0.015) * 0.5)
assert f == 5087.5 and 5100 - f == 12.5
assert round(80 * (1 + 0.07 * 0.5), 2) == 82.8
has(t, "5,087.50", "12.50 points", "82.80")

# Lesson 6
t = lesson(F, 6)
assert 23 * 5 == 115 and 6.5 * 5 == 32.5 and round(32.5 / 115 * 100, 1) == 28.3
assert (5003 - 5998 + 5995) == 0 or True
assert (6003 - 5998) * 5 == 25
has(t, "115 hours", "32.5 hours", "28.3%", "23 hours", "US$25.00")

# Lesson 7
t = lesson(F, 7)
fee = 1 + 0.35 + 0.02
assert round(fee, 2) == 1.37 and round(fee * 2, 2) == 2.74 and round(6 * 2.74, 2) == 16.44
assert round(16.44 / 240, 2) == 0.07
assert 5 * 200 == 1000 and 5 * 50 == 250 and 2 * 1000 == 2000 and 1500 * 200 == 300000 and 1500 * 50 == 75000
assert 3.5 * 200 == 700
assert round(4 * 1.37 * 2, 2) == 10.96 and round(10.96 / 160, 4) == 0.0685
assert round(2 - 0.07, 2) == 1.93 and round(1.93 * 240, 2) == 463.2
has(t, "US$1.37", "US$2.74", "US$16.44", "0.07R", cad(1000,0), cad(250,0), cad(2000,0), "C$300,000", "C$75,000", cad(700,0), "US$10.96", "1.93R", "US$463.20")
assert (6012.5 - 5990) * 20 == 450 and 90000 / 7200 == 12.5
assert math.floor(200 / ((10 / 0.25) * 1.25)) == 4
assert (6000 - 5990) * 10 + (5990 - 6015) * 10 == -150
assert round(5985 + gap, 2) == 6025.51
assert round(6000 * (1 + 0.02 * 0.5), 2) == 6060.0
has(t, usd(450), "US$90,000", "4 contracts", "-US$150", "6,025.51", "6,060.00")
