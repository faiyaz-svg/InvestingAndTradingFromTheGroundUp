"""Sample data for part 20. Everything here is made up.

Run after tools/make_charts.py 20-quant-track-in-python (it writes index-x-3y.csv):

    .venv/Scripts/python tools/figures/20-quant-track-in-python/make_data.py

Writes into docs/assets/data/:
  stock-01.csv ... stock-10.csv   daily OHLCV, 3 years, each = beta x index + own drift + own noise
  stock-split-3y.csv              one stock with a 2-for-1 split and quarterly dividends (raw and adjusted close)
  northwind-facts.json            Northwind Tools' numbers in the shape of an EDGAR companyfacts file
  fred-cpi-unrate.csv             monthly CPI index and unemployment rate in FRED's CSV layout (made up)
  treasury-yields.csv             daily 3-month, 2-year and 10-year yields in Treasury's CSV layout (made up)
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "assets" / "data"

idx = pd.read_csv(DATA / "index-x-3y.csv", parse_dates=["date"], index_col="date")
m = np.log(idx["close"]).diff().fillna(0.0).to_numpy()
dates = idx.index
n = len(dates)

# beta, own annual drift, own annual volatility, start price
UNIVERSE = {
    1: (1.2, 0.20, 0.25, 40.0),
    2: (0.9, 0.12, 0.20, 75.0),
    3: (1.0, 0.08, 0.30, 25.0),
    4: (1.4, 0.15, 0.35, 120.0),
    5: (0.7, 0.05, 0.15, 60.0),
    6: (0.6, 0.02, 0.18, 90.0),
    7: (1.1, 0.10, 0.28, 55.0),
    8: (1.0, -0.05, 0.30, 35.0),
    9: (0.8, 0.00, 0.22, 48.0),
    10: (1.3, -0.70, 0.45, 80.0),
}


def ohlc(close, rng, vol_day, base_volume):
    open_ = np.empty(n)
    open_[0] = close[0]
    open_[1:] = close[:-1] * (1 + rng.normal(0, vol_day / 4, n - 1))
    top = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, vol_day / 2, n)))
    bot = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, vol_day / 2, n)))
    volume = base_volume * np.exp(rng.normal(0, 0.3, n))
    return open_, top, bot, volume


def write_bars(name, close, open_, high, low, volume, extra=None):
    df = pd.DataFrame({"open": open_, "high": high, "low": low, "close": close}, index=dates).round(2)
    df["high"] = df[["open", "high", "close"]].max(axis=1)
    df["low"] = df[["open", "low", "close"]].min(axis=1)
    df["volume"] = (np.round(volume, -2)).astype(int)
    if extra:
        for k, v in extra.items():
            df[k] = v
    df.index.name = "date"
    df.to_csv(DATA / name, lineterminator="\n")


for k, (beta, mu, sig, p0) in UNIVERSE.items():
    rng = np.random.default_rng(3000 + k)
    r = beta * m + mu / 252 + rng.normal(0, sig / np.sqrt(252), n)
    r[0] = 0.0
    close = p0 * np.exp(np.cumsum(r))
    o, h, lo, v = ohlc(close, rng, sig / np.sqrt(252), 1_500_000)
    write_bars(f"stock-{k:02d}.csv", close, o, h, lo, v)

# A stock with a 2-for-1 split and quarterly dividends.
rng = np.random.default_rng(3100)
r = 0.9 * m + 0.10 / 252 + rng.normal(0, 0.22 / np.sqrt(252), n)
r[0] = 0.0
adj_split = 90.0 * np.exp(np.cumsum(r))  # price in today's (post-split) shares
split_i = int(np.searchsorted(dates, pd.Timestamp("2024-06-03")))
raw = adj_split * np.where(np.arange(n) < split_i, 2.0, 1.0)
div_dates = ["2023-03-15", "2023-06-15", "2023-09-15", "2023-12-15", "2024-03-15", "2024-06-14",
             "2024-09-16", "2024-12-16", "2025-03-14", "2025-06-16", "2025-09-15", "2025-12-15"]
div_days = [int(np.searchsorted(dates, pd.Timestamp(d))) for d in div_dates]
dividend = np.zeros(n)
factor = np.ones(n)
for d in div_days:
    dividend[d] = 0.80 if d < split_i else 0.40  # cash per share as paid then
    factor[:d] *= 1 - dividend[d] / raw[d - 1]
adj_close = adj_split * factor
o, h, lo, v = ohlc(raw, rng, 0.22 / np.sqrt(252), 1_200_000)
write_bars("stock-split-3y.csv", raw, o, h, lo, v,
           extra={"adj_close": np.round(adj_close, 2), "dividend": dividend,
                  "split": np.where(np.arange(n) == split_i, 2, 1)})
sp = pd.read_csv(DATA / "stock-split-3y.csv")
sp = sp[["date", "open", "high", "low", "close", "adj_close", "volume", "dividend", "split"]]
sp.to_csv(DATA / "stock-split-3y.csv", index=False, lineterminator="\n")


# Northwind Tools in companyfacts shape (US$, whole dollars). Made up; FY2024 and FY2025 match part 9.
def fact(start, end, val, fy, fp, form, filed, accn, frame=None):
    d = {}
    if start:
        d["start"] = start
    d.update({"end": end, "val": val, "accn": accn, "fy": fy, "fp": fp, "form": form, "filed": filed})
    if frame:
        d["frame"] = frame
    return d


A23, A24, A25 = "0009990001-24-000010", "0009990001-25-000010", "0009990001-26-000010"
rev = [
    fact("2023-01-01", "2023-12-31", 880_000_000, 2023, "FY", "10-K", "2024-02-20", A23, "CY2023"),
    fact("2023-01-01", "2023-12-31", 880_000_000, 2024, "FY", "10-K", "2025-02-19", A24),
    fact("2024-01-01", "2024-12-31", 1_000_000_000, 2024, "FY", "10-K", "2025-02-19", A24, "CY2024"),
    fact("2025-01-01", "2025-03-31", 270_000_000, 2025, "Q1", "10-Q", "2025-05-07", "0009990001-25-000040", "CY2025Q1"),
    fact("2025-01-01", "2025-06-30", 560_000_000, 2025, "Q2", "10-Q", "2025-08-06", "0009990001-25-000060"),
    fact("2025-04-01", "2025-06-30", 290_000_000, 2025, "Q2", "10-Q", "2025-08-06", "0009990001-25-000060", "CY2025Q2"),
    fact("2025-01-01", "2025-09-30", 855_000_000, 2025, "Q3", "10-Q", "2025-11-05", "0009990001-25-000080"),
    fact("2025-07-01", "2025-09-30", 295_000_000, 2025, "Q3", "10-Q", "2025-11-05", "0009990001-25-000080", "CY2025Q3"),
    fact("2025-01-01", "2025-12-31", 1_150_000_000, 2025, "FY", "10-K", "2026-02-18", A25, "CY2025"),
]
ni = [
    fact("2023-01-01", "2023-12-31", 98_000_000, 2023, "FY", "10-K", "2024-02-20", A23, "CY2023"),
    fact("2024-01-01", "2024-12-31", 123_000_000, 2024, "FY", "10-K", "2025-02-19", A24, "CY2024"),
    fact("2025-01-01", "2025-03-31", 36_000_000, 2025, "Q1", "10-Q", "2025-05-07", "0009990001-25-000040", "CY2025Q1"),
    fact("2025-01-01", "2025-06-30", 78_000_000, 2025, "Q2", "10-Q", "2025-08-06", "0009990001-25-000060"),
    fact("2025-04-01", "2025-06-30", 42_000_000, 2025, "Q2", "10-Q", "2025-08-06", "0009990001-25-000060", "CY2025Q2"),
    fact("2025-01-01", "2025-09-30", 123_000_000, 2025, "Q3", "10-Q", "2025-11-05", "0009990001-25-000080"),
    fact("2025-07-01", "2025-09-30", 45_000_000, 2025, "Q3", "10-Q", "2025-11-05", "0009990001-25-000080", "CY2025Q3"),
    fact("2025-01-01", "2025-12-31", 165_000_000, 2025, "FY", "10-K", "2026-02-18", A25, "CY2025"),
]
eps = [
    fact("2024-01-01", "2024-12-31", 1.23, 2024, "FY", "10-K", "2025-02-19", A24, "CY2024"),
    fact("2025-01-01", "2025-12-31", 1.66, 2025, "FY", "10-K", "2026-02-18", A25, "CY2025"),
]
assets = [
    fact(None, "2024-12-31", 1_000_000_000, 2024, "FY", "10-K", "2025-02-19", A24, "CY2024Q4I"),
    fact(None, "2025-12-31", 1_075_000_000, 2025, "FY", "10-K", "2026-02-18", A25, "CY2025Q4I"),
]
doc = {
    "cik": 9990001,
    "entityName": "Northwind Tools Inc. (made up)",
    "facts": {
        "us-gaap": {
            "Revenues": {"label": "Revenues", "description": "Made-up revenue.", "units": {"USD": rev}},
            "NetIncomeLoss": {"label": "Net Income (Loss)", "description": "Made-up net income.", "units": {"USD": ni}},
            "EarningsPerShareBasic": {"label": "EPS, basic", "description": "Made-up EPS.", "units": {"USD/shares": eps}},
            "Assets": {"label": "Assets", "description": "Made-up total assets.", "units": {"USD": assets}},
        }
    },
}
(DATA / "northwind-facts.json").write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8", newline="\n")

# Monthly macro in FRED's CSV layout. "." marks a missing value, as FRED does.
rng = np.random.default_rng(3200)
months = pd.date_range("2022-01-01", "2025-12-01", freq="MS")
infl = np.concatenate([np.full(12, 0.0065), np.full(12, 0.0035), np.full(12, 0.0028), np.full(12, 0.0025)])
cpi = 281.0 * np.cumprod(1 + infl + rng.normal(0, 0.0008, len(months)))
un = np.concatenate([np.linspace(4.0, 3.6, 12), np.linspace(3.6, 3.7, 12), np.linspace(3.7, 4.1, 12), np.linspace(4.1, 4.5, 12)])
un = np.round(un + rng.normal(0, 0.05, len(months)), 1)
fred = pd.DataFrame({"observation_date": months.strftime("%Y-%m-%d"), "CPIAUCSL": np.round(cpi, 3), "UNRATE": un})
fred["UNRATE"] = fred["UNRATE"].astype(str)
fred.loc[21, "UNRATE"] = "."
fred.to_csv(DATA / "fred-cpi-unrate.csv", index=False, lineterminator="\n")

# Daily yields in Treasury's CSV layout (newest row first, MM/DD/YYYY, percent).
rng = np.random.default_rng(3300)
k = np.arange(n)
y3m = 4.9 + np.where(k > 450, -0.0016 * (k - 450), 0) + rng.normal(0, 0.012, n).cumsum() * 0.3
y3m = np.clip(y3m, 3.2, 5.3)
y2 = np.interp(k, [0, 500, n - 1], [4.7, 3.7, 3.9]) + rng.normal(0, 0.02, n).cumsum() * 0.1
y10 = np.interp(k, [0, 300, n - 1], [3.9, 3.8, 4.4]) + rng.normal(0, 0.02, n).cumsum() * 0.1
tr = pd.DataFrame({"Date": dates.strftime("%m/%d/%Y"), "3 Mo": np.round(y3m, 2), "2 Yr": np.round(y2, 2), "10 Yr": np.round(y10, 2)})
tr.iloc[::-1].to_csv(DATA / "treasury-yields.csv", index=False, lineterminator="\n", quoting=1)
print("ok")
