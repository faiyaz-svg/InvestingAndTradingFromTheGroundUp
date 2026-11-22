# Intraday charts and VWAP

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">DAY</span>

After this lesson you can choose a bar size for a day trade, say what changes when you move between 1-minute and 5-minute bars, and use the session VWAP as a reference line that slows down through the day.

Before this: [Candles, bars and timeframes](../05-reading-charts/01-candles-bars-and-timeframes.md) and [VWAP and anchored VWAP](../05-reading-charts/08-vwap-and-anchored-vwap.md). You need: a calculator.

## The idea

A 5-minute bar is 5 one-minute bars squeezed into one candle: the open of the first, the high of the highest, the low of the lowest, the close of the last, and the sum of the volumes. The data is the same. Only the view changes, and each view hides something.

Stock A traded 4,054,500 shares between 9:30 and 11:30 a.m. on September 17, 2026. On the 1-minute chart that is 120 candles. On the 5-minute chart it is 24. The 1-minute chart shows every wobble, including ones that are noise. The 5-minute chart shows the structure, and hides the exact minute a stop was hit.

## How it works

### Choosing a bar size

A bar size is a trade-off between noise and delay.

| Bar | Use it for | Cost |
|---|---|---|
| 1 minute | Timing an entry or an exit once you have a plan | Much noise, so many false signals |
| 5 minutes | Setups: opening range, reclaims, fades (lessons 4 and 5) | A signal arrives 5 minutes after it began |
| 15 minutes | Context: is the day a trend or a range? | Few bars in the first hour |

A rule that works for the stop: the stop should be wider than the usual range of two or three bars on your chart. If a 5-minute bar of Stock B typically spans US$0.20 and your stop is US$0.15, a normal bar can stop you out. Part 3 gave the ATR for this ([Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md)).

### Session VWAP

The volume-weighted average price from Part 5 ([VWAP and anchored VWAP](../05-reading-charts/08-vwap-and-anchored-vwap.md)) is the average price paid so far, weighted by shares. On an intraday chart it is the **session VWAP**: it starts at the open and resets the next morning. Charting tools differ on whether premarket trades count. Many start the line at 9:30 a.m.; check what yours does and write it down, because a VWAP that includes the premarket is a different line.

\[ \text{VWAP}_t = \frac{\sum_{i=1}^{t} TP_i \times V_i}{\sum_{i=1}^{t} V_i} \]

- \(TP_i\) is the typical price of bar \(i\), (high + low + close) / 3, in US$.
- \(V_i\) is the volume of bar \(i), in shares.
- The sums run from the first bar of the session to bar \(t\).

Because the denominator grows all day, **VWAP gets slower as the day goes on**. Early bars move it a lot, late bars move it little.

```chart
data: 08-day-trading/vwap-1m.json
title: Stock A, 1-minute: the first two hours and VWAP
show: vwap, volume
range: 2026-09-17 09:30 to 2026-09-17 11:29
caption: Price ends the two hours at 81.20, above a VWAP of 80.61, and VWAP moved only a few cents after 10:00.
```

<div class="example" markdown>

### Worked example: how little a late bar moves VWAP

At 11:29 a.m. the VWAP of Stock A is US$80.61 on 4,054,500 shares (made-up data). The last close is 81.20, 0.59 above VWAP.

1. A new 1-minute bar trades 20,000 shares at a typical price of US$81.50.
2. New VWAP = (80.6114 x 4,054,500 + 81.50 x 20,000) / (4,054,500 + 20,000) = 80.6158.
3. The change is 80.6158 - 80.6114 = US$0.0044, less than half a cent.

At 9:59 a.m., after 1,854,500 shares, the same bar would have moved VWAP by 20,000 x (81.50 - 80.4996) / (1,854,500 + 20,000) = US$0.0107, more than twice as much.

</div>

Two uses follow. A VWAP that is far from the price pulls back slowly, so a price 1% above VWAP at noon may stay there for hours. And in the first 30 minutes, VWAP follows the price closely, so crossing it then means less than crossing it in the afternoon.

### What the line is and is not

VWAP is an average of what traders paid today. Traders and algorithms use it as a benchmark, so many orders are placed near it. That can make it a level where price pauses. It does not predict direction. Lessons 5 and 6 use it as a filter and a target, not as a forecast.

## In code

The code computes VWAP from the 1-minute file and again after resampling to 5-minute bars, so you can see that the two views give close but not identical lines (80.61 and 80.62).

Download [stock-a-1m.csv](../assets/data/stock-a-1m.csv). It holds Stock A's first two hours on September 17, 2026, with columns datetime (New York time), open, high, low, close and volume.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-1m.csv", parse_dates=["datetime"]).set_index("datetime")

def vwap(df):
    tp = (df["high"] + df["low"] + df["close"]) / 3
    return (tp * df["volume"]).sum() / df["volume"].sum()

five = bars.resample("5min").agg(
    {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
)
print("1-minute bars:", len(bars), "VWAP", round(vwap(bars), 2))
print("5-minute bars:", len(five), "VWAP", round(vwap(five), 2))
```

</details>

## Common mistakes

- Reading VWAP in the first minutes. With little volume, the line is the first few bars, and a cross means little.
- Using a different VWAP from the one you tested. A line that includes premarket trades is not the same line.
- Trading the 1-minute chart with a 5-minute stop. Decide the bar size first, then place the stop in that chart's terms.

## Try it

1\. Three 1-minute bars have typical prices 50.00, 50.10 and 50.20 and volumes 1,000, 2,000 and 1,000 shares. What is the VWAP after the third bar?

<details class="solution" markdown>
<summary>Answer</summary>

(50.00 x 1,000 + 50.10 x 2,000 + 50.20 x 1,000) / 4,000 = 200,400 / 4,000 = US$50.10.

</details>

2\. VWAP is US$40.00 on 2,000,000 shares. A bar trades 100,000 shares at US$41.00. What is the new VWAP?

<details class="solution" markdown>
<summary>Answer</summary>

(40.00 x 2,000,000 + 41.00 x 100,000) / 2,100,000 = 84,100,000 / 2,100,000 = US$40.0476, or about 40.05.

</details>

3\. Stock B's 5-minute bars span about US$0.25 each. Is a stop 0.20 away from the entry reasonable on that chart?

<details class="solution" markdown>
<summary>Answer</summary>

No. The stop is inside one normal bar range, so ordinary movement can reach it. A stop at least 2 to 3 bar ranges away (0.50 to 0.75) is more reasonable, and the position size shrinks to keep the risk at 1R.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Put the same stock on 1-minute, 5-minute and 15-minute charts with VWAP. Write the bar range of each in dollars. |
| 3 | Find out whether your charting tool's VWAP includes the premarket, and note it in your plan. |
| 3 | Run the In code snippet and change the resample to 15 minutes. |

</div>

## Key terms

- **Session VWAP**: the volume-weighted average price from the open of the session, reset each day.
- **Typical price**: the average of a bar's high, low and close.
- **Resampling**: building larger bars from smaller ones by combining their open, high, low, close and volume.

Next: [The opening range breakout](04-opening-range-breakout.md)
