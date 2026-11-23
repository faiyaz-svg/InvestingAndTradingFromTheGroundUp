# Macro data from FRED and Treasury

<span class="tag tag-code">Code</span> <span class="tag tag-part">QUANT</span>

After this lesson you can read a FRED series and a Treasury yield file into pandas, turn an index into a yearly inflation rate and a yield curve spread, and line monthly macro data up with daily prices without using a number before its release.

Before this: [How the economy is measured](../11-macro-and-economic-data/01-how-the-economy-is-measured.md), [The yield curve](../12-bonds-and-the-yield-curve/03-the-yield-curve.md), [Python and pandas for prices](01-python-and-pandas-for-prices.md). You need: Python with pandas.

## The idea

Macro data comes in different shapes from prices. CPI is one number a month, published about two weeks after the month ends. The unemployment rate is also monthly. Treasury yields are daily. A price file has a row for each trading day, and the macro files have other rhythms and sometimes gaps.

Two problems repeat. First, the files have quirks: a missing value written as a period, dates in the American month-first order, the newest row at the top. Second, a monthly number is labelled with the month it describes, but nobody saw it until the release day. This lesson handles both.

The files are made up, in the layouts the real sources use: [fred-cpi-unrate.csv](../assets/data/fred-cpi-unrate.csv) (monthly CPI index and unemployment rate for 2022 to 2025, in FRED's layout) and [treasury-yields.csv](../assets/data/treasury-yields.csv) (daily 3-month, 2-year and 10-year yields, in the layout of the Treasury's daily par yield curve file). Their values are invented, so do not read them as history.

## How it works

### FRED

**FRED** is the Federal Reserve Bank of St. Louis's database of economic series. Each series has an ID: CPIAUCSL is a consumer price index and UNRATE is the unemployment rate. In the API, a missing observation arrives as the string ".", which would turn a whole column into text. Tell `read_csv` that "." means missing with `na_values="."`.

Two calculations come up all the time, as in part 11. The yearly rate is the change over 12 months, `pct_change(12)` for monthly data. A monthly change can be annualised by compounding: \((1 + m)^{12} - 1\), where \(m\) is the monthly change as a fraction.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

fred = pd.read_csv("fred-cpi-unrate.csv", parse_dates=["observation_date"], index_col="observation_date", na_values=".")
print(fred.isna().sum().to_dict(), fred[fred["UNRATE"].isna()].index[0].date())
cpi = fred["CPIAUCSL"]
yoy = cpi.pct_change(12)
print(round(yoy.loc["2023-01-01"], 4), round(yoy.loc["2025-12-01"], 4))
mom = cpi.pct_change().loc["2025-12-01"]
print(round(mom, 4), round((1 + mom) ** 12 - 1, 4))
print(fred["UNRATE"].ffill().loc["2023-10-01"], fred["UNRATE"].loc["2023-09-01"])
print(round(fred["UNRATE"].loc["2025-12-01"] - fred["UNRATE"].loc["2024-12-01"], 1))
```

There is one missing unemployment value, for October 1, 2023, and none in CPI. The made-up CPI rises 0.0801 (8.0%) over the year to January 2023 and 0.0267 (2.7%) over the year to December 2025. The December 2025 monthly change is 0.003, which annualises to 0.036 (3.6%). `ffill()` fills the gap with September's 3.7, and unemployment is 0.4 percentage points higher in December 2025 than a year earlier. Use `ffill` only when carrying the old value is honest. A missing release is not a zero.

</details>

### Treasury yields

The Treasury publishes the par yield curve each day: yields for 1 month to 30 years in percent. The CSV lists the newest day first and writes dates as month/day/year, so tell pandas the date format and sort the index. Then a spread is a subtraction of two columns, as part 12 defined it.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

ty = pd.read_csv("treasury-yields.csv", parse_dates=["Date"], date_format="%m/%d/%Y", index_col="Date").sort_index()
ty["2s10s"] = ty["10 Yr"] - ty["2 Yr"]
ty["3m10y"] = ty["10 Yr"] - ty["3 Mo"]
print(ty.index[0].date(), ty.index[-1].date(), len(ty))
print((ty["2s10s"] < 0).sum(), ty["2s10s"].idxmin().date(), round(ty["2s10s"].min(), 2), (ty["3m10y"] < 0).sum())
print(ty.index[(ty["2s10s"] >= 0).to_numpy().argmax()].date())
print(ty["2s10s"].resample("QE").last().round(2).iloc[[0, 4, 8, 11]].to_dict())
```

The file has 782 days, from January 2, 2023 to December 30, 2025. The 2s10s spread (10-year minus 2-year, in percentage points) is negative on 407 days and reaches its lowest, -0.80, on the first day. It first turns non-negative on July 24, 2024. The 3m10y spread is negative on all 782 days. At the end of the first quarter of 2023 the 2s10s spread is -0.72, a year later -0.22, then 0.26 at the end of March 2025, and 0.35 at the end of December 2025.

</details>

The figure draws the 2s10s spread. The shaded part is the stretch with an inverted curve, where the 2-year yield is above the 10-year.

![The made-up 10-year minus 2-year yield spread, negative (inverted) until July 2024 and positive afterward](../assets/figures/20-quant-track-in-python/curve-spread-dark.svg#only-dark)
![The made-up 10-year minus 2-year yield spread, negative (inverted) until July 2024 and positive afterward](../assets/figures/20-quant-track-in-python/curve-spread-light.svg#only-light)

### Matching monthly data to daily prices

A monthly CPI value is stamped with the first of its month, but it came out in the middle of the next month. The CPI for January was public in mid-February. Join it to daily prices on the stamp and every day of February before the release sees an inflation number nobody had.

The fix is a second date column, the release date, and an "as of" join: for each trading day, take the latest row whose release date is on or before that day. In pandas that is `merge_asof`. The release date below is an assumption (the 15th of the next month); real release dates are on the schedules in part 11 ([The economic calendar](../11-macro-and-economic-data/07-the-economic-calendar.md)).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

cpi = pd.read_csv("fred-cpi-unrate.csv", parse_dates=["observation_date"], index_col="observation_date")["CPIAUCSL"]
yoy = cpi.pct_change(12).dropna().rename("cpi_yoy").to_frame()
yoy["release"] = yoy.index + pd.offsets.MonthBegin(1) + pd.Timedelta(days=14)   # assumed: mid-month after
index = pd.read_csv("index-x-3y.csv", parse_dates=["date"])[["date", "close"]]

naive = pd.merge_asof(index, yoy.reset_index(), left_on="date", right_on="observation_date")
safe = pd.merge_asof(index, yoy.sort_values("release"), left_on="date", right_on="release")
day = pd.Timestamp("2023-03-10")
print(round(naive.set_index("date").loc[day, "cpi_yoy"], 4), round(safe.set_index("date").loc[day, "cpi_yoy"], 4))
print(safe["cpi_yoy"].isna().sum(), safe.dropna().iloc[0]["date"].date())
```

On March 10, 2023 the naive join shows 0.0749, which is the yearly rate for March 2023, a month that had barely started. The safe join shows 0.0801, the January figure released on February 15. With release dates, the first 32 trading days have no inflation number, and the first value appears on February 15, 2023.

</details>

FRED also keeps old versions of a series. Statistical agencies revise numbers (part 11, lesson 1), and the API can return a series as it looked on a past date through its real-time parameters, `realtime_start` and `realtime_end` ([FRED series observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html)). A test of a rule that used a revised number as if it were the first print is flattered by information that did not exist.

### The live versions

FRED's API needs your own free key, which you request from a FRED account. Never paste someone else's, and do not commit yours to a public repository. The Treasury's file needs no key. Both snippets are only compiled by the checker.

<details class="code" markdown>
<summary>In code</summary>

```python
# needs internet
import pandas as pd
import requests

KEY = "YOUR_OWN_FRED_KEY"        # free; request it from your FRED account
url = "https://api.stlouisfed.org/fred/series/observations"
params = {"series_id": "UNRATE", "api_key": KEY, "file_type": "json"}
obs = requests.get(url, params=params, timeout=30).json()["observations"]
unrate = pd.Series({pd.Timestamp(o["date"]): o["value"] for o in obs})
unrate = pd.to_numeric(unrate, errors="coerce")   # "." becomes NaN
print(unrate.tail())

csv = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
       "daily-treasury-rates.csv/2025/all?type=daily_treasury_yield_curve&field_tdr_date_value=2025&page&_format=csv")
yields = pd.read_csv(csv, parse_dates=["Date"], date_format="%m/%d/%Y", index_col="Date").sort_index()
print((yields["10 Yr"] - yields["2 Yr"]).tail())
```

</details>

Some FRED series belong to private owners and are copyrighted, so check the notes on a series page before you republish one (see [Free data sources and their licences](../19-data-flows-and-forecasting/01-free-data-sources.md)). The Treasury address above follows the pattern the Treasury's own download page uses at the time of writing, and the pattern can change.

## Common mistakes

- Leaving "." in a numeric column. The column becomes text, and `mean()` fails or silently skips.
- Parsing 03/04/2023 the wrong way round. State the format, `%m/%d/%Y`.
- Joining a monthly number on the month it describes. Join on the day it was released.

## Try it

1\. CPI is 300.0 in January and 301.2 in February. What is the monthly change and its annualised rate?

<details class="solution" markdown>
<summary>Answer</summary>

301.2 / 300.0 - 1 = 0.0040, so 0.40%. Annualised: 1.004^12 - 1 = 0.0491, so 4.9%.

</details>

2\. CPI is 280.0 twelve months ago and 291.2 now. What is the yearly rate?

<details class="solution" markdown>
<summary>Answer</summary>

291.2 / 280.0 - 1 = 0.0400, so 4.0%.

</details>

3\. The 2-year yield is 4.35% and the 10-year yield is 4.10%. What is the 2s10s spread, and is the curve inverted?

<details class="solution" markdown>
<summary>Answer</summary>

4.10 - 4.35 = -0.25 percentage points. It is negative, so the part of the curve between 2 and 10 years is inverted.

</details>

4\. A report for March is released on April 10. On April 8, which month's value should a backtest hold?

<details class="solution" markdown>
<summary>Answer</summary>

February's, which was released in March. March's value does not exist publicly until April 10.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the second snippet and print the number of days the 3m10y spread was negative, then the last date it was. |
| 3 | In the third snippet change the release lag from 15 days to 30 days and write down how the number of empty days at the start changes. |
| 2 | Open FRED's page for UNRATE and write the date of its latest observation. |

</div>

## Key terms

- **FRED**: the Federal Reserve Bank of St. Louis's database of economic series, each with an ID.
- **Observation date**: the period a macro number describes.
- **Release date**: the day the number became public.
- **As-of join**: joining each row to the latest earlier row, in pandas `merge_asof`.
- **Real-time (vintage) data**: a series as it looked on a past date, before later revisions.

Next: [Correlation, beta and regression](06-correlation-beta-and-regression.md)
