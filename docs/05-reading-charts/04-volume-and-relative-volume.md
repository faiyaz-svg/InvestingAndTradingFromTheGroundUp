# Volume and relative volume

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can compute relative volume, tell a breakout on heavy volume from one on light volume, and say what volume can and cannot tell you about the next move.

Before this: [Support and resistance](03-support-and-resistance.md) and [Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md). You need: a calculator.

## The idea

Two days in a row, Stock A closes above its resistance. On the first day 5.1 million shares trade. On the second day 1.35 million trade. Both are breakouts on the chart, and they are not the same event.

**Volume** is the number of shares traded in a bar. A price move says where the market went. Volume says how many shares agreed to the new price. A move that many traders took part in is harder to reverse than a move that a few shares made. Volume also shows when a level was tested by real activity and when it was only brushed.

Raw volume is hard to judge on its own, because 2 million shares is busy for one stock and quiet for another. **Relative volume** (RVOL) compares today's volume with the stock's usual volume:

\[ \text{RVOL} = \frac{V_t}{\bar{V}_{20}} \]

- \(V_t\) is the volume of the bar you are reading, in shares.
- \(\bar{V}_{20}\) is the average volume of the 20 bars before it, in shares. The bar itself is left out so a spike doesn't raise its own average.
- RVOL has no unit. A value of 1 is a normal day, 2 is twice the usual volume, 0.5 is half.

Lesson 11 of Part 1 gave this ratio for a quote page ([Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md)). Here the average is the previous 20 bars.

## How it works

Look at two breakouts from the same kind of range. Each range has 30 bars with a high of about 52.7, and on February 16, 2026 the price closes above it. The first chart has heavy volume on the breakout bar.

```chart
data: 05-reading-charts/breakout-volume.json
title: Stock A, daily: a breakout on heavy volume
level: 52.72 | Range high
marker: 2026-02-16 | below | Breakout, RVOL 3.3
show: volume
range: 2026-01-05 to 2026-03-04
caption: The breakout bar trades 5,100,000 shares against a 20-day average of 1,531,450.
```

On February 16 the bar opens at 51.56, reaches 54.14 and closes at 53.88, above the range high of 52.72. The volume is 5,100,000 shares. The average of the 20 bars before it is 1,531,450, so RVOL = 5,100,000 / 1,531,450 = 3.33. The next two days have RVOL of 1.30 and 1.32, and the price keeps rising.

The second chart has the same breakout move with ordinary volume.

```chart
data: 05-reading-charts/false-breakout.json
title: Stock A, daily: a breakout on light volume that fails
level: 52.74 | Range high
marker: 2026-02-16 | below | Breakout, RVOL 1.0
marker: 2026-02-19 | above | Back inside
show: volume
range: 2026-01-05 to 2026-03-05
caption: The breakout bar trades 1,350,000 shares against a 20-day average of 1,375,660.
```

Here the bar closes at 54.34, above the range high of 52.74, but the volume is 1,350,000 and the average is 1,375,660, so RVOL = 0.98. On February 19 the close is 52.50, back inside the range, and the price ends the chart at 49.00 on March 5. This is a **false breakout**: a close beyond a level that does not hold.

<div class="example" markdown>

### Worked example: filtering breakouts with RVOL

You have a rule: only take a breakout close if RVOL is at least 1.5. Apply it to both charts.

1. Heavy chart: RVOL = 5,100,000 / 1,531,450 = 3.33. The rule passes. You buy at the close of US$53.88 with a stop below the range high at US$51.90, which is US$1.98 of risk per share.
2. Light chart: RVOL = 1,350,000 / 1,375,660 = 0.98. The rule fails. You skip it.

The rule kept you out of the trade that failed and into the one that worked. Two charts prove nothing about the rule. The next sections say what tests found, and when it fails.

</div>

### Volume in other places

- Pullbacks in a healthy uptrend usually come on lower volume than the rises, and the made-up uptrend in [Trend and market structure](02-trend-and-market-structure.md) was drawn that way.
- A very high volume bar after a long rise can mark the end of the move, because many holders sell at once. A **volume spike** like that is read together with the candle and the trend, never alone.
- Intraday volume is high at the open and the close and low at midday (Part 1: [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)). Compare a bar with the usual volume at the same time of day, not with the whole-day average, or every morning looks busy.

## What tests found

Gervais, Kaniel and Mingelgrin (2001) found that stocks with unusually high volume over a day or a week tended to earn higher returns over the following month than similar stocks with normal volume. They call it the high-volume return premium, and they connect it to attention: a stock that has become visible gets more buyers ([Journal of Finance, 56(3), 877-919](https://doi.org/10.1111/0022-1082.00349)). Blume, Easley and O'Hara (1994) showed in a model and in data that volume carries information about how reliable the price signal is, which gives a reason to read price and volume together ([Journal of Finance, 49(1), 153-181](https://doi.org/10.1111/j.1540-6261.1994.tb04424.x)).

Neither paper tests the rule of "RVOL above 1.5 on a breakout". The evidence says volume has information. It does not say that every breakout on heavy volume works, and it does not give a threshold.

Volume also fails in practice. A high-volume breakout can reverse the next day, and a quiet breakout can run. A stock's volume rises around news and index events that have nothing to do with the level you are watching.

## In code

RVOL for every bar of Stock A, with the previous 20 bars as the average. Use [stock-a-daily-h1.csv](../assets/data/stock-a-daily-h1.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-daily-h1.csv", parse_dates=["date"], index_col="date")
average = bars["volume"].rolling(20).mean().shift(1)
rvol = bars["volume"] / average
print(rvol.idxmax().date(), round(rvol.max(), 2))
```

The highest RVOL is 2.30 on 2026-06-05: 4,208,600 shares against a 20-day average of 1,827,160.

</details>

## Common mistakes

- Reading volume without the average. 3 million shares means nothing until you know the stock's usual volume.
- Using the whole-day average to judge a morning bar. Volume is highest at the open, so compare the same time of day.
- Treating one heavy bar as a signal by itself. Heavy volume after a long fall can be a selling climax or the start of a bigger fall, and the volume alone does not say which.

## Try it

1\. Stock B's volume today is 2,400,000 shares. The average of the previous 20 days is 1,600,000. What is RVOL?

<details class="solution" markdown>
<summary>Answer</summary>

2,400,000 / 1,600,000 = 1.5.

</details>

2\. A breakout bar on Stock B has RVOL of 0.8. Under the rule "RVOL at least 1.5", do you take it? What would change your mind?

<details class="solution" markdown>
<summary>Answer</summary>

No, 0.8 is below 1.5. The volume is 20% below normal, so few shares agreed to the new price. If the price holds above the level and the next bars come on higher volume, the breakout gets more support, and you can reassess then.

</details>

3\. At 10:00 a.m. ET Stock B has traded 800,000 shares. At the same time on a normal day it has traded about 500,000. What is RVOL at 10:00, and why is it better than comparing 800,000 with the full-day average of 1,500,000?

<details class="solution" markdown>
<summary>Answer</summary>

800,000 / 500,000 = 1.6. The full-day comparison gives 0.53, which wrongly says the stock is quiet. Half an hour after the open a stock has traded only part of its day, so the comparison has to use the same time of day.

</details>

4\. On the heavy-volume chart, the breakout bar has RVOL of 3.33. If the average of the previous 20 days had been 2,550,000 instead of 1,531,450, what RVOL would the same bar have?

<details class="solution" markdown>
<summary>Answer</summary>

5,100,000 / 2,550,000 = 2.0.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Run a set of [chart drills](../practice/chart-drills.md) and decide for each breakout whether the volume supports it. |
| 4 | On a daily chart you follow, find the three highest-volume bars of the last six months. Write their RVOL and what the price did in the next five days. |
| 2 | Write your own rule for a breakout (for example, RVOL at least 1.5). Save it in your [trade journal](../practice/trade-journal.md) to test later. |

</div>

## Key terms

- **Volume**: the number of shares traded in a bar.
- **Relative volume (RVOL)**: a bar's volume divided by the average volume of the previous 20 bars.
- **Volume spike**: a bar with volume far above the average.
- **False breakout**: a close beyond a level that does not hold.

Next: [Moving averages](05-moving-averages.md)
