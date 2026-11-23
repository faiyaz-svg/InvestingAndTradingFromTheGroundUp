# Python and pandas for prices

<span class="tag tag-code">Code</span> <span class="tag tag-part">QUANT</span>

After this lesson you can load a file of daily prices into pandas, pick out dates and ranges, build weekly bars from daily ones, and say when to use a raw close and when to use an adjusted close.

Before this: [Dividends, splits and corporate actions](../01-how-markets-work/09-dividends-splits-and-corporate-actions.md), [Candles, bars and timeframes](../05-reading-charts/01-candles-bars-and-timeframes.md), and the CS book's Python basics, starting with [values, types and variables](https://faiyaz-svg.github.io/CSFromTheGroundUp/03-programming-fundamentals/01-python-basics/01-values-types-and-variables/) and [files and I/O](https://faiyaz-svg.github.io/CSFromTheGroundUp/03-programming-fundamentals/01-python-basics/07-files-and-io/). You need: Python 3 with pandas and numpy installed.

## The idea

Price data fits a table: each row is a day and each column a measurement. This part uses **pandas**, the standard Python library for tables, and every lesson runs offline on made-up data that you download from this site.

The table is a **DataFrame**. One column of it is a **Series**: a list of values with a label for each value. The labels are the **index**. For prices the index is the date, which pandas stores as a **DatetimeIndex**, so you can ask for "March 2024" or "the week of March 4" without writing a loop.

The columns are the ones from lesson 1 of part 5: open, high, low, close and volume (OHLCV), stored in a CSV file, a text file with one row per day and commas between the values.

## How it works

1. Read the file with `read_csv`. Give it `parse_dates=["date"]` so the date column becomes real dates, and `index_col="date"` to make them the index. Without `parse_dates` the dates stay as text and slicing by date fails.
2. Select by label with `.loc`. A single date gives one row, a month string such as `"2024-03"` gives every day in that month, and `"2024-03-04":"2024-03-08"` gives a range with both ends included.
3. Change the timeframe with `resample`. Daily to weekly means grouping days by week and combining each column in the way that column needs: open is the first value, high the maximum, low the minimum, close the last value and volume the sum.
4. Choose the close you need. A **raw close** is the price the last trade of the day was done at. An **adjusted close** is the history rewritten so that splits and dividends do not look like price moves.

Download [stock-01.csv](../assets/data/stock-01.csv) and [stock-split-3y.csv](../assets/data/stock-split-3y.csv). Both are made up. The first is 782 trading days from January 2, 2023 to December 30, 2025.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-01.csv", parse_dates=["date"], index_col="date")
print(bars.shape, bars.index[0].date(), bars.index[-1].date())
print(bars.loc["2024-03-04", "close"])
print(bars.loc["2024-03", "close"].agg(["count", "min", "max"]))
print(bars.loc["2024-03-04":"2024-03-08", ["open", "close"]])
```

The file has 782 rows and 5 columns. The close on March 4, 2024 is 27.17. March 2024 has 21 trading days, with closes from 24.46 to 27.17.

</details>

`W-FRI` means weeks that end on Friday.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-01.csv", parse_dates=["date"], index_col="date")
weekly = bars.resample("W-FRI").agg(
    {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
)
print(len(weekly))
print(weekly.loc["2024-03-08"])
print(weekly.tail(2))
```

There are 157 weekly bars. The week ending Friday, March 8, 2024 opened at 27.33, reached a high of 27.50 and a low of 24.39, closed at 24.96 and traded 6,318,200 shares. The last bar is labelled January 2, 2026 but holds only two days (December 29 and 30), so it is a partial week.

</details>

<div class="example" markdown>

### Worked example: a split in the data

The made-up stock in `stock-split-3y.csv` did a 2-for-1 split on June 3, 2024: each share became two, and the price roughly halved. Its raw and adjusted closes around that day are:

| Date | Raw close | Adjusted close |
|---|---|---|
| 2024-05-30 | 205.45 | 100.02 |
| 2024-05-31 | 207.49 | 101.01 |
| 2024-06-03 | 106.17 | 103.38 |

1. Return on May 31 from the raw close: 207.49 / 205.45 - 1 = 0.0099, so +0.99%. From the adjusted close: 101.01 / 100.02 - 1 = +0.99%. The same, because nothing happened that day.
2. Return on June 3 from the raw close: 106.17 / 207.49 - 1 = -0.4883, so -48.83%. Nobody lost half their money; the shares were split.
3. Return on June 3 from the adjusted close: 103.38 / 101.01 - 1 = +0.0235, so +2.35%. This is what a holder earned.

</div>

The figure shows why. The raw line falls off a cliff on the split date, while the adjusted line moves smoothly and sits below the raw line before the split.

![The raw close of a made-up stock halves on the split date in June 2024 while the adjusted close does not](../assets/figures/20-quant-track-in-python/raw-vs-adjusted-dark.svg#only-dark)
![The raw close of a made-up stock halves on the split date in June 2024 while the adjusted close does not](../assets/figures/20-quant-track-in-python/raw-vs-adjusted-light.svg#only-light)

Before the split the adjusted line sits a little below half of the raw line. The stock paid 12 quarterly dividends, and each payout scales the older adjusted prices down by a small factor.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

sp = pd.read_csv("stock-split-3y.csv", parse_dates=["date"], index_col="date")
raw = sp["close"].pct_change()
adj = sp["adj_close"].pct_change()
day = sp.index[sp["split"] == 2][0]
print(day.date(), round(raw[day], 4), round(adj[day], 4))
first, last = sp.iloc[0], sp.iloc[-1]
print(round(last["close"] / first["close"] - 1, 4), round(last["adj_close"] / first["adj_close"] - 1, 4))
```

The split day is 2024-06-03, with a raw return of -0.4883 and an adjusted return of 0.0235. Over the three years, the raw closes give -0.2654 (-26.54%) and the adjusted closes give 0.5417 (+54.17%). The raw number is wrong because it counts the split as a loss and ignores the dividends.

</details>

Use the adjusted close for returns, backtests and any comparison across time. Use the raw close when you need the price that was on the screen: a stop level, a gap, or a round number traders watched. Adjusted history is rewritten with every new split or dividend, so an old adjusted price is not one you could have traded at.

### Getting real data

This snippet reads real prices through `yfinance`, an open-source library that uses Yahoo's public data. By its own notice it is meant for research and education and is not affiliated with Yahoo. Check Yahoo's terms before you use the data for anything beyond personal study ([Free data sources and their licences](../19-data-flows-and-forecasting/01-free-data-sources.md)). With `auto_adjust=False` you get both the `Close` column, which yfinance has already adjusted for splits, and `Adj Close`, which also adjusts for dividends.

<details class="code" markdown>
<summary>In code</summary>

```python
# needs internet
import yfinance as yf

history = yf.Ticker("SPY").history(period="1y", auto_adjust=False)
print(history[["Close", "Adj Close", "Volume"]].tail())
```

</details>

<div class="canada" markdown>

### For Canadians

A TSX-listed stock has the suffix `.TO` on Yahoo, and its prices are in CAD. The same company listed in the US has a different ticker and USD prices, so a file never mixes the two. Part 2 covers what the currency does to your return ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)).

</div>

## Common mistakes

- Taking returns from the raw close across a split. The split day shows a fake crash, and any indicator built on it is wrong for months.
- Reading dates as text. Without `parse_dates`, `loc["2024-03"]` raises an error or returns nothing, and sorting puts "10" before "9".
- Resampling every column with `mean`. A weekly bar needs the first open, the highest high, the lowest low, the last close and the total volume.

## Try it

1\. A stock closes at 80.00 the day before a 4-for-1 split and 21.00 the day it starts trading after the split. What is the raw return, and what is the split-adjusted return?

<details class="solution" markdown>
<summary>Answer</summary>

Raw: 21.00 / 80.00 - 1 = -0.7375, so -73.75%. After a 4-for-1 split the old price in new shares is 80.00 / 4 = 20.00, so the adjusted return is 21.00 / 20.00 - 1 = +5.0%.

</details>

2\. Five daily bars have opens 10.0, 10.2, 10.4, 10.1, 10.3; highs 10.5, 10.6, 10.7, 10.4, 10.6; lows 9.9, 10.0, 10.2, 9.9, 10.1; closes 10.2, 10.4, 10.1, 10.3, 10.5; volumes 100, 120, 90, 110, 130. Build the weekly bar.

<details class="solution" markdown>
<summary>Answer</summary>

Open 10.0 (the first open), high 10.7 (the largest high), low 9.9 (the smallest low), close 10.5 (the last close), volume 100 + 120 + 90 + 110 + 130 = 550.

</details>

3\. The file has 782 daily rows, but the weekly table has 157 rows, not 782 / 5 = 156.4. Why 157?

<details class="solution" markdown>
<summary>Answer</summary>

782 = 156 x 5 + 2. There are 156 full weeks plus a partial week of two days (Monday, December 29 and Tuesday, December 30, 2025), and resample gives the partial week its own row.

</details>

4\. In the worked example, the adjusted close on May 30 (100.02) is 0.4868 of the raw close (205.45). The split alone explains a factor of 0.5. What factor is left for the dividends?

<details class="solution" markdown>
<summary>Answer</summary>

100.02 / 205.45 = 0.4868. Divide by 0.5 to remove the split: 0.4868 / 0.5 = 0.9737. The dividends paid after May 30 scale the older prices down to 97.4% of their value, about 2.6%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Download `stock-01.csv`, load it, and print the lowest close and the date it happened. |
| 4 | Resample it to month-end (`"ME"`) and print the month with the highest return, from one month-end close to the next. |
| 2 | Write one sentence on which close, raw or adjusted, you would use to measure a three-year return, and why. |

</div>

## Key terms

- **pandas**: the Python library for tables of data.
- **DataFrame**: a table with labelled rows and columns.
- **Series**: one column of a table, with an index.
- **Index**: the labels of the rows; for prices, the dates.
- **DatetimeIndex**: an index of real dates that pandas can slice and group.
- **Resample**: regroup time-indexed rows into a longer timeframe, such as days into weeks.
- **Raw close**: the closing price as traded on the day.
- **Adjusted close**: a close rewritten for splits and dividends, so returns from it are total returns.

Next: [Returns and volatility in pandas](02-returns-and-volatility.md)
