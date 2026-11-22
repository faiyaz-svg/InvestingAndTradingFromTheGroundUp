# Market regime filters

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">SWNG</span>

After this lesson you can classify the market as favourable or unfavourable for new long trades with three written tests (trend, breadth and volatility), and say what published tests found about trend filters.

Before this: [Moving averages](../05-reading-charts/05-moving-averages.md), [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md). You need: a calculator.

## The idea

Most stocks move with the market. When an index falls 20% over two months, a pullback setup on one stock is still pulled along by the same selling.

A **market regime** is the state of the market (trending up, trending down, calm, turbulent) that decides which setups you take and at what size. A **regime filter** is a written test that sorts today into one regime or another. It does not predict. It only says which of two rule sets applies today.

The three tests below are the book's starting rules.

## How it works

### Test 1: trend, the 200-day average

The **200-day filter** says: new long swing trades only when the index closes above its own 200-day simple moving average (SMA). The SMA is the mean of the last 200 closes ([Moving averages](../05-reading-charts/05-moving-averages.md)). Use a broad index or an ETF that tracks one, such as SPY for the S&P 500.

The chart is made-up data for an "Index X". Look at December 16, 2025, when the close first falls under the 200-day average, and April 27, 2026, when it first closes back above.

```chart
data: 07-swing-trading/index-x-regime.json
title: Index X, daily: closing below and back above the 200-day average
show: volume, sma 50, sma 200
marker: 2025-11-20 | above | Peak close 4,759.80
marker: 2025-12-16 | above | Close 4,173.84 under the SMA 4,206.06
marker: 2026-04-27 | below | Close 4,014.31 over the SMA 4,007.10
range: 2025-09-01 to 2026-05-22
caption: The index peaked on November 20, 2025, closed under its 200-day average on December 16, and stayed under it for 94 sessions.
```

The index peaked at 4,759.80 on November 20, 2025. On December 16 it closed at 4,173.84, below the 200-day average of 4,206.06 and already 12.3% under the peak. The low close was 3,347.24 on January 23, 2026, 29.7% under the peak. The index first closed above its average again on April 27, 2026 (4,014.31 against 4,007.10), and then crossed it four more times in eight sessions (May 1, 4, 6 and 7), a whipsaw. A trader who took new longs only above the average would have taken none for 94 sessions, and would have taken none of the decline.

The cost of this rule is the whipsaw, and a late return after a rally has started ([Moving averages](../05-reading-charts/05-moving-averages.md)).

### Test 2: breadth

**Breadth** measures how many stocks take part in a move, as opposed to the index level, which a few large stocks can lift. A common measure is the percent of stocks in an index that close above their own 50-day average. If the index rises while that percentage falls, fewer stocks are carrying it.

The book's rule of thumb is: take pullback and breakout setups when more than half the stocks in your universe are above their 50-day average, and trade smaller (half size) when fewer than half are. The 50% line is a planning number, not a tested threshold.

### Test 3: volatility

Volatility is how much prices swing. The **VIX** is the Cboe's index of the market's expected 30-day volatility in the S&P 500, calculated from index option prices (part 16 explains it in The VIX and the term structure<!-- link: ../16-volatility-and-event-trading/02-the-vix-and-term-structure.md --> and builds the idea in Volatility regimes<!-- link: ../16-volatility-and-event-trading/03-volatility-regimes.md -->). A higher VIX means larger expected daily moves.

You do not need a VIX cut-off. Position sizing already handles volatility: when ATR rises, your stop distance rises and your share count falls (part 3). The test adds a pause: when the index moves more than about 2% in a day several times in a week, wait before opening new trades.

### Putting the three together

| Test | Favourable | Unfavourable |
|---|---|---|
| Trend | Index closes above its 200-day SMA | Index closes below it |
| Breadth | More than 50% of the universe above its 50-day average | 50% or fewer |
| Volatility | Daily index moves mostly under 2% | Several moves of 2% or more this week |

All three favourable: full size, any of the three setups. Trend favourable and one other not: half size. Trend unfavourable: no new longs from the pullback or breakout setups. Mean reversion needs its own care, which [Short-term mean reversion](06-short-term-mean-reversion.md) covers. The combination is the book's choice and was not tested as a package.

## What tests found

Faber (2007) tested holding a US stock index only when its month-end price was above its 10-month average and holding cash otherwise. The paper reported lower drawdowns than buy and hold for the US index and for several other asset classes ([Journal of Wealth Management, 9(4), 69-79; SSRN 962461](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461)). It uses monthly data, not the daily 200-day rule.

Brock, Lakonishok and LeBaron (1992) found that moving-average buy signals on the Dow from 1897 to 1986 were followed by higher returns than sell signals ([Journal of Finance, 47(5), 1731-1764](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x)), and later work questioned how much survives data snooping.

Moskowitz, Ooi and Pedersen (2012) tested 58 liquid futures and forward contracts (equity indexes, currencies, commodities and bonds). They found that each contract's own return over the past 1 to 12 months predicted its next-month return, which they called time-series momentum ([Journal of Financial Economics, 104(2), 228-250](https://doi.org/10.1016/j.jfineco.2011.11.003)). It tests futures, not individual stocks, and not a filter on swing setups.

None of these tests checks a regime filter on a swing setup. Trend filters have some support as a way to cut drawdowns. The numbers in this lesson are choices to test in your journal.

<div class="example" markdown>

### Worked example: the filter on three dates

Using the Index X chart:

1. November 7, 2025: close 4,515.79, 200-day SMA 4,130.17. Close is above, so favourable on trend.
2. December 16, 2025: close 4,173.84, SMA 4,206.06. The close is below by 32.22 points (0.77%). Unfavourable.
3. April 27, 2026: close 4,014.31, SMA 4,007.10. Above by 7.21 points. Favourable again, for four days.

On December 16 a pullback setup on any stock in the book's rules is skipped.

</div>

## In code

The same filter on the sample file of Index X. Download [index-x-daily.csv](../assets/data/index-x-daily.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("index-x-daily.csv", parse_dates=["date"])
bars["sma200"] = bars["close"].rolling(200).mean()
bars["above"] = bars["close"] > bars["sma200"]
valid = bars.dropna(subset=["sma200"])
first_below = valid[~valid["above"]].iloc[0]
print(first_below["date"].date(), first_below["close"], round(first_below["sma200"], 2))
back_above = valid[(valid["date"] > first_below["date"]) & valid["above"]].iloc[0]
print(back_above["date"].date(), back_above["close"], round(back_above["sma200"], 2))
```


The code prints 2025-12-16 4173.84 4206.06 and then 2026-04-27 4014.31 4007.1.

</details>

## Common mistakes

- Using the filter on each stock and not on the market. A stock above its own 200-day average in a falling market still gets pulled down.
- Changing the filter after a bad month. Pick the number, write it down, and review it once a quarter.
- Reading a filter as a forecast. It says which rule set applies. The market can fall the day after a favourable reading.

## Try it

1\. Index X closes at 4,200.00 and its 200-day SMA is 4,150.00. Is trend favourable? By how many percent is the close above the average?

<details class="solution" markdown>
<summary>Answer</summary>

Yes, the close is above the average. (4,200 - 4,150) / 4,150 = 1.2%.

</details>

2\. In your universe of 200 stocks, 84 close above their 50-day average. What is the breadth reading and what does the book's rule say?

<details class="solution" markdown>
<summary>Answer</summary>

84 / 200 = 42%. That is 50% or fewer, so trade half size under the rule of thumb.

</details>

3\. Trend is favourable, breadth is 62%, and the index moved 2.3%, 2.6% and 2.1% on three days this week. What does the table say?

<details class="solution" markdown>
<summary>Answer</summary>

Trend and breadth are favourable, volatility is not (three moves of 2% or more). That is trend favourable with one other test unfavourable, so half size.

</details>

4\. The index closes under its 200-day average on a Tuesday and back above it on Thursday. What is the name for that, and what does it cost a trader who followed the rule?

<details class="solution" markdown>
<summary>Answer</summary>

A whipsaw. The trader skipped or closed trades for two days and may have missed gains if the rally continued.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Write today's regime for a real index you follow: is the close above its 200-day average? Record the date and the two numbers. |
| 3 | Count how many stocks on your watchlist are above their 50-day average. Write the percentage. |
| 3 | Add the three tests and the book's combination table to your trading plan, with your own thresholds if you changed them. |

</div>

## Key terms

- **Market regime**: the state of the market that decides which setups you take and at what size.
- **Regime filter**: a written test that sorts the market into favourable or unfavourable for a setup.
- **200-day filter**: take new long swing trades only when the index closes above its 200-day SMA.
- **Breadth**: how many stocks take part in a move, often the percent of stocks above their 50-day average.
- **VIX**: the Cboe's index of expected 30-day volatility in the S&P 500, calculated from option prices.
- **Time-series momentum**: the tendency of an asset's own past return over 1 to 12 months to predict its next return.

Next: [Trend pullback setups](04-trend-pullback-setups.md)
