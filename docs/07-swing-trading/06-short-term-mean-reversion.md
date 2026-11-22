# Short-term mean reversion

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">SWNG</span>

After this lesson you can apply a 2-period RSI mean reversion rule, work out its entry, stop, exit and size, and say what the published tests of short-term reversal found and where they stop.

Before this: [Momentum indicators: RSI, MACD and stochastics](../05-reading-charts/06-momentum-indicators.md), [Moving averages](../05-reading-charts/05-moving-averages.md), [Market hours and auctions](../01-how-markets-work/03-market-hours-and-auctions.md). You need: a calculator.

## The idea

The first two setups follow price. This one does the opposite: after a stock in a long uptrend drops for a few days, it buys the drop and sells the bounce a few days later. The bet is that a sharp short-term fall in a strong stock goes too far and partly reverses.

**Mean reversion** is the tendency of a price that has moved far from its recent average to move back toward it. The setup measures "far" with a very short RSI, the 2-period RSI, written RSI(2).

## How it works

RSI(2) is the relative strength index from [Momentum indicators](../05-reading-charts/06-momentum-indicators.md) with a length of 2. It compares the average gain and average loss of the last two bars, with Wilder smoothing: the new average is (previous average + today's value) / 2. After two or three down closes in a row, RSI(2) falls below 10, a level a stock rarely reaches in an uptrend.

Rules for a long trade on daily bars, evaluated after the close. The numbers (10, 200 days, 2 ATR, 5-day SMA, 5 days) are this book's choices, built from the common version of the rule, not tested standards.

1. Filter: the close is above the 200-day SMA.
2. Trigger: RSI(2) closes below 10, and it is the first close below 10 since RSI(2) was last 10 or higher. Do not add to a trade or re-enter while RSI(2) stays low.
3. Entry: buy at the next open.
4. Initial stop: \(S = E - 2 \times ATR\), where \(E\) is the entry and ATR is the 14-day average true range on the trigger bar, rounded down to the cent.
5. Exit: sell at the close of the first session, starting with the entry day, that closes above the 5-day SMA. A market-on-close order does this ([Market hours and auctions](../01-how-markets-work/03-market-hours-and-auctions.md)).
6. Time stop: if the exit has not happened, sell at the close five trading days after the entry day.
7. Size: shares = floor(0.01 x account / \(R\)), with \(R = E - S\).

The stop is the book's addition, because part 3 sizes by the stop. It changes results in ways the original tests do not show. Connors and Alvarez's book *Short Term Trading Strategies That Work* (2009) popularised RSI(2). It is a trading book, not peer-reviewed research, with the authors' own tests, and I found no independent replication. Versions of the rule use thresholds such as 5 or 10 ([StockCharts ChartSchool](https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2) describes a common one).

<div class="example" markdown>

### Worked example: a bounce that pays 1.10R

Stock A (made-up data). Account US$25,000, risk 1%.

1. The close on March 2, 2026 is 57.53. The change from 58.48 is -0.95, and RSI(2) is 10.32, not under 10. No signal.
2. March 3 closes at 56.53, a change of -1.00. The previous averages were gain 0.0788 and loss 0.6842. New average gain = (0.0788 + 0) / 2 = 0.0394. New average loss = (0.6842 + 1.00) / 2 = 0.8421. RS = 0.0394 / 0.8421 = 0.0468, so RSI(2) = 100 - 100 / 1.0468 = 4.47.
3. The 200-day SMA is 47.17, and the close is above it. It is the first close under 10. Signal.
4. March 4 opens at US$56.41, the entry. The ATR on March 3 is 0.9447. Stop = 56.41 - 2 x 0.9447 = 54.52. \(R\) = US$1.89.
5. Size: 250 / 1.89 = 132.3, so 132 shares. Cost US$7,446.12. Risk US$249.48.
6. March 4 closes at 57.48, under the 5-day SMA of 57.84. Hold. March 5 closes at 58.48, above the 5-day SMA of 57.70. Sell at the close, US$58.48.
7. Result: (58.48 - 56.41) x 132 = US$273.24, which is 2.07 / 1.89 = +1.10R.

</div>

The chart shows the down closes, the signal on March 3, and the exit two sessions later.

```chart
data: 07-swing-trading/stock-a-rsi2-win.json
title: Stock A, daily: RSI(2) under 10 above the 200-day average
show: sma 5, sma 200, rsi 2
level: 54.52 | Stop
marker: 2026-03-03 | below | RSI(2) 4.5, signal
marker: 2026-03-05 | above | Sell 58.48
range: 2026-02-02 to 2026-03-09
caption: The close was far above the 200-day average (47.17). The exit came on the first close above the 5-day average.
```

<div class="example" markdown>

### Worked example: a drop that keeps going

Stock B (made-up data). Same account and rules.

1. March 16, 2026 closes at 53.83 with RSI(2) at 5.8, above its 200-day SMA of 42.52. It is the first close under 10. Signal.
2. March 17 opens at US$53.55, the entry. ATR is 0.8826. Stop = 53.55 - 2 x 0.8826 = 51.78. \(R\) = US$1.77. Size: 250 / 1.77 = 141.2, so 141 shares.
3. March 17 closes at 52.76 and the selling continues. On March 18 the stock opens at 52.42, above the stop, then trades down to 51.01, through it. The stop order fills at US$51.78.
4. Result: (51.78 - 53.55) x 141 = -US$249.57, which is -1.00R.

</div>

RSI(2) stayed under 10 on March 17 and 18, and the rule does not re-enter.

```chart
data: 07-swing-trading/stock-b-rsi2-loss.json
title: Stock B, daily: a drop that goes through the stop
show: sma 5, sma 200, rsi 2
level: 51.78 | Stop
marker: 2026-03-16 | below | RSI(2) 5.8, signal
marker: 2026-03-18 | below | Stop
range: 2026-02-16 to 2026-03-20
caption: The stock kept falling after the signal. The loss was 1R, because the stop filled at its price.
```

## When it fails, and what tests found

The setup fails when a drop starts a larger fall: news, a failed earnings report, a market crash. The 200-day average moves too slowly to help. The [regime filters](03-market-regime-filters.md) apply with less certainty, since this trade bets against the day's direction.

What the research found. Jegadeesh (1990) found that returns of individual US stocks reverse from one month to the next: stocks that did worst in a month tended to do better in the next, and portfolios built from that pattern earned abnormal returns (about 2.5% a month between the extreme deciles, 1934 to 1987, before costs) ([Journal of Finance, 45(3), 881-898](https://doi.org/10.1111/j.1540-6261.1990.tb05110.x)). Lehmann (1990) found the same for weekly returns ([Quarterly Journal of Economics, 105(1), 1-28](https://doi.org/10.2307/2937816)). Nagel (2012) argued that the returns of such reversal strategies are what liquidity providers earn for absorbing selling, and found that they rise when the VIX is high ([Review of Financial Studies, 25(7), 2005-2039](https://doi.org/10.1093/rfs/hhs066)). Lou, Polk and Skouras (2019) reported that across 14 strategies, the profits of reversal and of several momentum strategies are earned overnight, and the profits of others are earned during the trading day ([Journal of Financial Economics, 134(1), 192-213](https://doi.org/10.1016/j.jfineco.2019.03.011)).

These papers study portfolios of many stocks formed weekly or monthly. None tests an RSI(2) rule with a 200-day filter and a stop. They show that short-term reversal exists on average in US stocks, not that this rule earns money after costs.

## In code

RSI(2) from the sample file. Download [stock-a-rsi2.csv](../assets/data/stock-a-rsi2.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-a-rsi2.csv", parse_dates=["date"]).set_index("date")
change = bars["close"].diff()
gain = change.clip(lower=0)
loss = (-change).clip(lower=0)
avg_gain = gain.iloc[1:].ewm(alpha=0.5, adjust=False).mean()
avg_loss = loss.iloc[1:].ewm(alpha=0.5, adjust=False).mean()
rsi2 = 100 - 100 / (1 + avg_gain / avg_loss)
sma200 = bars["close"].rolling(200).mean()
day = pd.Timestamp("2026-03-03")
print(round(rsi2[day], 2), round(sma200[day], 2))
```

The code prints 4.47 and 47.17.

</details>

## Common mistakes

- Buying every drop. The filter and the first-close rule keep out a stock that stays weak.
- Averaging down. A second buy doubles the risk on a failing trade.
- Skipping the stop. The size was set from it.

## Try it

1\. RSI(2) averages are gain 0.10 and loss 0.50. The next close is down 0.60. What is the new RSI(2)?

<details class="solution" markdown>
<summary>Answer</summary>

New gain = (0.10 + 0) / 2 = 0.05. New loss = (0.50 + 0.60) / 2 = 0.55. RS = 0.05 / 0.55 = 0.0909. RSI = 100 - 100 / 1.0909 = 8.33.

</details>

2\. A stock opens at US$40.00 after a signal, with ATR 0.75. Stop and risk per share? Shares with a US$30,000 account at 1%?

<details class="solution" markdown>
<summary>Answer</summary>

Stop = 40.00 - 2 x 0.75 = 38.50. Risk per share = US$1.50. Risk = US$300. 300 / 1.50 = 200 shares.

</details>

3\. The entry day closes at 41.20 and the 5-day SMA is 41.45. The next day closes at 41.60 with the 5-day SMA at 41.50. When does the rule exit?

<details class="solution" markdown>
<summary>Answer</summary>

The first day is under the average, so hold. The second day closes at 41.60, above 41.50, so exit at that close.

</details>

4\. RSI(2) closes at 7 on Monday and 4 on Tuesday. How many signals is that?

<details class="solution" markdown>
<summary>Answer</summary>

One. Only Monday is the first close under 10. Tuesday is a continuation, so the rule gives no new entry.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Do the [chart drills](../practice/chart-drills.md) set 07-swing-trading, questions on RSI(2). |
| 3 | On a daily chart with RSI(2) on it, find two past signals and mark where the 5-day-average exit would have come. |
| 3 | Write one reason you might not take a mean reversion trade (for example, earnings in the next five days) in your plan. |

</div>

## Key terms

- **Mean reversion**: the tendency of a price that has moved far from its recent average to move back toward it.
- **RSI(2)**: the relative strength index with a length of 2, which reacts to two or three days of moves.
- **Short-term reversal**: the tendency of stocks that fell over the past week or month to outperform those that rose.
- **5-day exit**: selling at the first close above the 5-day SMA.

Next: [Entries, stops and targets](07-entries-stops-and-targets.md)
