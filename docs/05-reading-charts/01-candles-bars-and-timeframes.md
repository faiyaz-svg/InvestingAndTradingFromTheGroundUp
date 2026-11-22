# Candles, bars and timeframes

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can read one candle (open, high, low, close, body and wicks), build a weekly bar from five daily bars, and say what a candle shape does and does not tell you.

Before this: [Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md). You need: a calculator.

## The idea

On Friday, March 20, 2026, Stock A opens at US$50.93. It trades as high as US$52.67 and as low as US$50.78, and it closes the day at US$52.46. Four prices describe the whole day: the open, the high, the low and the close, written **OHLC**. A chart bar is a picture of those four numbers, plus the volume (the shares traded) under it.

A **candlestick** (candle for short) draws them like this. The **body** is the box between the open and the close. The **wicks** (also called shadows) are the thin lines above and below the body that reach to the high and the low. In this book a candle is green when the close is above the open (an up candle) and red when the close is below the open (a down candle).

The figure shows the March 20 candle next to a down candle from March 26.

![Parts of an up candle and a down candle: open, high, low, close, body and wicks](../assets/figures/05-reading-charts/candle-anatomy-dark.svg#only-dark)
![Parts of an up candle and a down candle: open, high, low, close, body and wicks](../assets/figures/05-reading-charts/candle-anatomy-light.svg#only-light)

Other chart types show the same data with less detail. An **OHLC bar** is a vertical line from the low to the high with a tick on the left for the open and a tick on the right for the close. A **line chart** joins only the closes. Candles are the common choice because the body makes the open-to-close direction easy to see. This book uses candles unless it says otherwise.

## Reading one bar

Four measurements describe a candle. Take the March 20 numbers.

\[ \text{Range} = H - L, \quad \text{Body} = |C - O|, \quad \text{Upper wick} = H - \max(O, C), \quad \text{Lower wick} = \min(O, C) - L \]

- \(O\), \(H\), \(L\), \(C\) are the open, high, low and close in US$.
- Range is the full height of the bar in US$. Body and wicks are the parts of it.

For March 20: range = 52.67 - 50.78 = US$1.89, body = 52.46 - 50.93 = US$1.53, upper wick = 52.67 - 52.46 = US$0.21, lower wick = 50.93 - 50.78 = US$0.15. The body is 81% of the range and the close is near the high. The **close location** says where in the range the day closed:

\[ \text{CL} = \frac{C - L}{H - L} \]

For March 20: (52.46 - 50.78) / 1.89 = 88.9%. A value near 100% means buyers were in control at the close, and a value near 0% means sellers were.

The chart shows five shapes in a row, with the dates marked. Look at the body size and the wicks on each.

```chart
data: 05-reading-charts/candle-anatomy.json
title: Stock A, daily: five candle shapes
marker: 2026-03-20 | below | Long body
marker: 2026-03-23 | below | Small body
marker: 2026-03-24 | below | Long lower wick
marker: 2026-03-25 | above | Long upper wick
marker: 2026-03-26 | above | Long red body
show: volume
range: 2026-03-02 to 2026-03-31
caption: Each marked candle has a different split between body and wicks.
```

| Date | Open | High | Low | Close | Body | Upper wick | Lower wick |
|---|---|---|---|---|---|---|---|
| March 20 | 50.93 | 52.67 | 50.78 | 52.46 | 1.53 | 0.21 | 0.15 |
| March 23 | 52.46 | 53.09 | 51.89 | 52.49 | 0.03 | 0.60 | 0.57 |
| March 24 | 52.49 | 52.70 | 50.91 | 52.65 | 0.16 | 0.05 | 1.58 |
| March 25 | 52.65 | 54.38 | 52.49 | 52.75 | 0.10 | 1.63 | 0.16 |
| March 26 | 52.75 | 52.86 | 51.06 | 51.17 | 1.58 | 0.11 | 0.11 |

Each shape has a name. A **doji** has a body close to zero (March 23: the open and close differ by 3 cents). A candle with a long lower wick and a small body near the top (March 24) is called a **hammer** when it follows a fall, and one with a long upper wick (March 25) is a **shooting star** when it follows a rise. The names matter less than the story each tells about one day: March 24 traded 1.58 below the open and then recovered, and March 25 traded 1.63 above the open and then fell back.

Here is the same stretch as a line chart of closes. The wicks and the opens are gone, and so is most of the story of each day.

```chart
data: 05-reading-charts/candle-anatomy.json
title: Stock A, daily: the same bars as a line of closes
type: line
range: 2026-03-02 to 2026-03-31
caption: A line chart keeps only the closing price.
```

### What tests found

Marshall, Young and Rose (2006) tested candlestick rules on the stocks in the Dow Jones Industrial Average from 1992 to 2002 and found no evidence that trading the patterns earned a profit ([Journal of Banking and Finance, 30(8), 2303-2323](https://econpapers.repec.org/RePEc:eee:jbfina:v:30:y:2006:i:8:p:2303-2323)). A candle is a good summary of one period. A single candle shape is not a reliable signal on its own, and later lessons use candles together with levels, volume and trend.

## Timeframes

A **timeframe** is the length of time each bar covers: 1 minute, 5 minutes, 1 day, 1 week. Every bar on a chart has the same length. A regular session of 6.5 hours has 78 five-minute bars. A weekly bar combines the daily bars of a week:

1. Open: the open of the first day.
2. High: the highest high of the five days.
3. Low: the lowest low of the five days.
4. Close: the close of the last day.
5. Volume: the sum of the five daily volumes.

<div class="example" markdown>

### Worked example: building a weekly bar

The first five daily bars of Stock A's chart (January 5 to January 9, 2026):

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| Jan 5 | 40.00 | 40.05 | 39.71 | 39.78 | 2,305,300 |
| Jan 6 | 39.85 | 40.21 | 39.81 | 40.10 | 3,274,700 |
| Jan 7 | 40.08 | 40.32 | 40.00 | 40.32 | 1,731,200 |
| Jan 8 | 40.28 | 41.03 | 40.05 | 40.72 | 1,517,800 |
| Jan 9 | 40.73 | 40.96 | 40.18 | 40.46 | 2,001,400 |

The weekly bar: open 40.00 (Monday), high 41.03 (Thursday), low 39.71 (Monday), close 40.46 (Friday), volume 10,830,400. The week is an up candle even though Monday closed lower than it opened.

</div>

The two views below are the same made-up stock. The daily chart has 125 bars and the weekly chart has 25. Lesson 11 uses both to trade with the larger trend ([Multiple timeframes and relative strength](11-multi-timeframe-and-relative-strength.md)).

```chart
data: 05-reading-charts/stock-a-daily.json
title: Stock A, daily
show: volume
caption: 125 daily bars from January 5 to June 26, 2026.
```

```chart
data: 05-reading-charts/stock-a-weekly.json
title: Stock A, weekly
show: volume
caption: The same stock as 25 weekly bars.
```

A shorter timeframe shows more detail and more noise. A longer one shows the larger moves and hides the entries. The price you see on any timeframe is the same price, only summarised differently.

## In code

The weekly bar above is a one-line resample in pandas. Download [stock-a-daily-h1.csv](../assets/data/stock-a-daily-h1.csv) into the folder where you run the code.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-daily-h1.csv", parse_dates=["date"], index_col="date")
weekly = bars.resample("W-FRI").agg(
    {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
)
print(weekly.head(1))
```

The first row is the week ending January 9: open 40.00, high 41.03, low 39.71, close 40.46, volume 10830400.

</details>

<div class="canada" markdown>

### For Canadians

A stock listed in both Toronto and New York has two charts in two currencies, and the bars differ. Look for the currency label on your charting tool before you read a level. Check, too, whether the chart includes extended-hours trades (lesson 3 of Part 1: [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)), because that changes the open, high, low and close.

</div>

## Common mistakes

- Treating a candle's colour as a prediction. Colour only says that the close was above or below the open.
- Reading a gap as part of the body. A candle opens at the open price, which can be far from the previous close ([Gaps](10-gaps.md)).
- Comparing candles across timeframes. A long daily body and a long weekly body are different sizes of move.

## Try it

1\. A bar has open 48.00, high 49.50, low 47.40 and close 49.20. Find the range, body, upper wick, lower wick and close location.

<details class="solution" markdown>
<summary>Answer</summary>

Range = 49.50 - 47.40 = 2.10. Body = 49.20 - 48.00 = 1.20. Upper wick = 49.50 - 49.20 = 0.30. Lower wick = 48.00 - 47.40 = 0.60. Close location = (49.20 - 47.40) / 2.10 = 85.7%.

</details>

2\. A week of daily bars has opens of 20.00 on Monday, highs of 20.80, 21.40, 21.10, 21.60 and 21.30, lows of 19.70, 20.30, 20.40, 20.90 and 20.60, and a Friday close of 21.20. What is the weekly bar?

<details class="solution" markdown>
<summary>Answer</summary>

Open 20.00, high 21.60 (Thursday), low 19.70 (Monday), close 21.20. The week is an up candle with a body of 1.20.

</details>

3\. How many 15-minute bars are in a regular session (9:30 a.m. to 4:00 p.m. ET)?

<details class="solution" markdown>
<summary>Answer</summary>

The session is 390 minutes. 390 / 15 = 26 bars.

</details>

4\. On March 25, Stock A opened at 52.65, rose to 54.38 and closed at 52.75. Write one sentence on what the bar says.

<details class="solution" markdown>
<summary>Answer</summary>

Buyers pushed the price 1.73 above the open, then sellers took all of it back and closed it 0.10 above the open. The long upper wick (1.63) says the high prices were rejected that day.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run a set of [chart drills](../practice/chart-drills.md) and read the body and wicks of each candle before answering. |
| 3 | Open one stock in your charting tool. Switch between 5-minute, daily and weekly candles and note which shows the clearest trend. |
| 2 | Pick yesterday's daily candle for that stock and write its range, body and close location. |

</div>

## Key terms

- **OHLC**: the open, high, low and close of a bar.
- **Candlestick**: a bar drawn as a body with wicks, green or red by direction.
- **Body**: the box between the open and the close.
- **Wick (shadow)**: the line from the body to the high or the low.
- **OHLC bar**: a bar drawn as a line from low to high with ticks for the open and close.
- **Line chart**: a chart that joins the closing prices.
- **Close location**: where the close sits in the bar's range, as a percentage.
- **Doji**: a candle whose open and close are almost equal.
- **Hammer**: a small body near the top with a long lower wick, after a fall.
- **Shooting star**: a small body near the bottom with a long upper wick, after a rise.
- **Timeframe**: the length of time one bar covers.

Next: [Trend and market structure](02-trend-and-market-structure.md)
