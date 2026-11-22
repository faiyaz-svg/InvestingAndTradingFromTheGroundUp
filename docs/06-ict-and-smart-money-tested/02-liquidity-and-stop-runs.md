# Liquidity and stop runs

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">ICT</span>

After this lesson you can mark equal highs and equal lows, tell a sweep from a breakout by a written rule, work out a sweep trade with its risk, and say what is known about stop orders clustering at prices.

Before this: [What ICT and smart money concepts claim](01-what-ict-and-smc-claim.md), [Order types](../01-how-markets-work/05-order-types.md) and [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md). You need: a calculator.

## The idea

Stock A rises to US$55.00, falls back, rises again and stops at US$55.02. Two swing highs within two cents of each other. Where would traders put their stops?

A trader who is short Stock A puts a buy stop right above 55.02, because a move through that level says the short is wrong. A trader waiting for a breakout puts a buy order right above it. A stop order becomes a market order when its price trades ([Order types](../01-how-markets-work/05-order-types.md)). So if price trades through 55.02, those stops fire together, and their market buy orders find the sellers who were waiting.

ICT teachers call such a cluster of resting orders a **liquidity pool**. A pool above highs is **buy-side liquidity** (resting buy orders, from stopped-out shorts and breakout buyers). A pool below lows is **sell-side liquidity** (resting sell orders, from stopped-out longs and breakdown sellers). Two or more swing highs at nearly the same price are **equal highs**, and the same for **equal lows**. Teachers call them the most obvious pools, because many traders place the same stop.

A **stop run**, also called a **sweep** or a raid, is a move that trades through the pool and then returns. The claim is that large traders use the stops as counterparties, and that after the pool is taken the price moves the other way.

## How it works

A written rule has to separate a sweep from a breakout, because they look the same until the bar closes.

1. Mark equal highs: two swing highs within 0.2% of each other. Mark equal lows the same way.
2. Mark a sweep when a bar trades above the equal highs and closes back below them (for equal lows, trades below and closes back above).
3. Wait for a market structure shift: a close beyond the swing point between the two highs, in the direction of the reversal (lesson 1).
4. Enter with a stop order right beyond that swing point. Put the protective stop beyond the sweep's extreme.
5. Target the opposite pool: the next swing low or equal lows.

The chart plants this pattern in Stock A.

```chart
data: 06-ict-and-smart-money-tested/equal-highs-sweep.json
title: Stock A, daily: equal highs, a sweep, and a structure shift
level: 55.02 | Equal highs (55.00 and 55.02)
level: 52.90 | Swing low between the highs
marker: 2026-02-27 | above | Sweep
marker: 2026-03-03 | below | Structure shift
show: volume
range: 2026-02-02 to 2026-03-18
caption: The February 27 bar trades to 55.40 and closes at 54.35, back under the highs.
```

The two highs are 55.00 (February 16) and 55.02 (February 23), 0.04% apart, so they pass step 1. The swing low between them is 52.90 (February 19). On February 27 the bar trades to 55.40, which is 0.38 above 55.02, and closes at 54.35. That is a sweep by step 2. On March 3 the bar closes at 52.60, below 52.90, which is the shift in step 3.

<div class="example" markdown>

### Worked example: a short after the sweep

Your account is US$25,000 and you risk 1% per trade. All prices are Stock A's.

1. Entry: a sell stop at 52.85, five cents under the swing low of 52.90. On March 3 the bar trades down to 52.50, so the order fills at 52.85.
2. Protective stop: 55.45, five cents above the sweep high of 55.40.
3. Risk per share = 55.45 - 52.85 = US$2.60.
4. Dollars at risk = 1% of 25,000 = US$250. Shares = 250 / 2.60 = 96.2, so 96 shares (round down).
5. Target: 49.80, right above the first low of the chart (49.76 on February 2). Reward per share = 52.85 - 49.80 = US$3.05.
6. Reward to risk = 3.05 / 2.60 = 1.17R ([R-multiples](../03-risk-and-position-sizing/02-r-multiples.md)).

Price reached the target on March 11 (low 49.77), and the stop was not touched. A stop-out would lose 96 x 2.60 = US$249.60. With a 1.17R target, the break-even win rate is 1 / (1 + 1.17) = 46%, before costs ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)). Shorting needs a margin account ([Short selling](../01-how-markets-work/08-short-selling.md)).

</div>

A deep sweep means a wide stop and a smaller reward to risk.

## What tests found

The best evidence is about the first link in the chain: stop orders do cluster at visible prices. Osler (2003) used the first data on individual stop-loss and take-profit orders in the currency market, from a large dealing bank. She found that take-profit orders cluster strongly at round numbers and stop-loss orders cluster right beyond them. She argued that this could explain why currency trends tend to reverse at round-number levels and then run fast once those levels are crossed ([Journal of Finance 58(5), 1791-1819](https://ideas.repec.org/a/bla/jfinan/v58y2003i5p1791-1819.html)). In a second paper she argued that stop-loss orders can set off self-reinforcing moves, and found trends unusually fast at levels where stop-loss orders cluster, and a price response to stop-loss orders that is larger than to take-profit orders and lasts hours, not days (Osler 2005, working-paper version [New York Fed Staff Report 150](https://www.newyorkfed.org/research/staff_reports/sr150.html), 2002).

Two earlier results fit the same picture: Osler (2000) on currency trends and Kavajecz and Odders-White (2004) on NYSE limit orders, both cited in [Support and resistance](../05-reading-charts/03-support-and-resistance.md).

What these papers do not show matters as much. They cover currencies and one bank's clients, mostly round numbers, not equal highs on stocks. They show that orders cluster and that prices react at the clusters. They do not test "sweep, then reverse" as a rule, and none reports results after costs. We found no published test of that rule on stocks. The claim that price is moved to the stops on purpose cannot be tested, and the clustering result does not need it.

## In code

The code marks sweeps and breakouts on the made-up series [stock-b-daily.csv](../assets/data/stock-b-daily.csv) (360 bars, a random walk with drift, with no ICT logic in it) and compares what happened next.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-b-daily.csv", parse_dates=["date"])
prior_high = bars["high"].rolling(20).max().shift(1)
sweep = (bars["high"] > prior_high) & (bars["close"] < prior_high)
breakout = bars["close"] > prior_high
fwd5 = bars["close"].shift(-5) / bars["close"] - 1
print(sweep.sum(), "sweeps and", breakout.sum(), "breakouts in", len(bars), "bars")
print(f"5-bar return after a sweep {fwd5[sweep].mean():.2%}, after a breakout {fwd5[breakout].mean():.2%}, all bars {fwd5.mean():.2%}")
```

</details>

It prints 37 sweeps and 26 breakouts in 360 bars. The mean 5-bar return is -0.20% after a sweep, -0.04% after a breakout and 0.25% over all bars. The series has no ICT logic in it, so 37 events cannot separate a real effect from noise. A test needs the baseline and the sample size, and the pattern alone is not enough.

## Common mistakes

- Calling every wick through a high a sweep. Without the close-back rule, a breakout that continues is also a "sweep", and the idea cannot be wrong.
- Entering at the sweep bar's close, before the structure shift confirms it.

## Try it

1\. Highs of 55.00 and 55.02: are they equal highs under the 0.2% rule?

<details class="solution" markdown>
<summary>Answer</summary>

The gap is 0.02, and 0.02 / 55.00 = 0.04%, which is under 0.2%. Yes.

</details>

2\. The sweep bar trades to 55.40 and closes at 54.35. How far above the equal highs did it trade, as a percentage of 55.02? Is it a sweep or a breakout under the rule?

<details class="solution" markdown>
<summary>Answer</summary>

55.40 - 55.02 = 0.38, and 0.38 / 55.02 = 0.69%. The close (54.35) is below 55.02, so it is a sweep. A close above 55.02 would have been a breakout.

</details>

3\. Your account is US$25,000 and you risk 1%. Use the entry 52.85, stop 55.45 and a target of 50.50. How many shares, and what is the reward to risk?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share = 55.45 - 52.85 = 2.60. Shares = 250 / 2.60 = 96. Reward per share = 52.85 - 50.50 = 2.35. Reward to risk = 2.35 / 2.60 = 0.90R. A target this close gives less than 1R, so the trade needs a win rate above 1 / (1 + 0.90) = 53% to break even.

</details>

4\. Osler (2003) found that currency stop-loss orders cluster beyond round numbers. Does that show a stock trader can profit from sweeps of equal highs? Give one reason.

<details class="solution" markdown>
<summary>Answer</summary>

No. The study covers currency orders at one bank, round numbers and price reactions, not a trading rule on stocks and not results after costs.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | On a daily chart, find three pairs of equal highs or lows (within 0.2%). For each, write whether the next bar through the level closed back inside (sweep) or held beyond (breakout). |
| 3 | Do the sweep drills in [chart drills](../practice/chart-drills.md). |
| 2 | Write your tolerance for "equal" in your [trade journal](../practice/trade-journal.md) notes so you do not change it later. |

</div>

## Key terms

- **Liquidity pool**: orders resting at known prices, mostly stops beyond obvious highs and lows.
- **Buy-side liquidity**: resting buy orders above highs, from stopped-out shorts and breakout buyers.
- **Sell-side liquidity**: resting sell orders below lows, from stopped-out longs and breakdown sellers.
- **Equal highs and equal lows**: two or more swing points at nearly the same price.
- **Sweep**: a bar that trades through a pool and closes back inside; also called a stop run or raid.

Next: [Fair value gaps](03-fair-value-gaps.md)
