# Fair value gaps

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">ICT</span>

After this lesson you can find a bullish or bearish fair value gap from three bars, say what displacement and mitigation mean, work out a trade from a gap with its risk, and say what a fill rate does and does not show.

Before this: [Liquidity and stop runs](02-liquidity-and-stop-runs.md) and [Candles, bars and timeframes](../05-reading-charts/01-candles-bars-and-timeframes.md). You need: a calculator.

## The idea

Stock A trades around US$50 for weeks. Then one day a single candle runs from 50.70 up to 52.90 and closes at 52.70, on big volume. Look at the bar before it and the bar after it. The bar before never traded above 50.90. The bar after never traded below 52.30. Between those two prices, only the big middle candle traded.

ICT teachers call that stretch a **fair value gap** (FVG), an **imbalance** or an inefficiency. The idea is that during the fast move, buyers overwhelmed sellers so completely that the market skipped a price range, and that the market tends to come back to "rebalance" it.

The exact definition uses three consecutive bars, called bar 1, bar 2 and bar 3.

- A **bullish fair value gap** exists when the high of bar 1 is below the low of bar 3. The gap is the zone from bar 1's high up to bar 3's low.
- A **bearish fair value gap** exists when the low of bar 1 is above the high of bar 3. The gap is the zone from bar 3's high up to bar 1's low.

Bar 2 is the middle bar, and teachers want it to be a **displacement**: a strong, fast move with a large body, which they read as a sign of aggressive orders. No teacher gives one number for "large". A testable version is a range of at least 3 times the average range of the previous 10 bars. Use your own number and write it down.

One point is easy to miss. A fair value gap is not an empty price range like a daily gap (Gaps<!-- link: ../05-reading-charts/10-gaps.md -->). Bar 2 traded through the whole zone, so trades did happen there. Only bar 1 and bar 3 did not. The gap is a range where one candle did all the trading.

## How it works

Price returning into the zone is called **mitigation**, or filling the gap. It can be partial, or all the way across. The 50% point of the zone is called **consequent encroachment** (CE). Teachers watch whether price stops at the edge, at the CE, or goes through the whole gap, and read each as a sign of strength or weakness.

The rule set for a trade in the direction of the displacement:

1. Find a three-bar gap whose middle bar passes your displacement rule.
2. Place a limit order at the near edge of the gap (the top for a long, the bottom for a short). Some traders use the CE instead, which fills less often but gives a better price.
3. Place the protective stop beyond bar 2's extreme (below its low for a long, above its high for a short).
4. Target the next swing high or low.

The chart plants a bullish gap in Stock A.

```chart
data: 06-ict-and-smart-money-tested/fvg-bullish.json
title: Stock A, daily: a bullish fair value gap and a return
zone: 50.90-52.30 | 2026-02-18 to 2026-03-03 | Bullish FVG
level: 51.60 | Midpoint (CE)
marker: 2026-02-19 | below | Displacement
marker: 2026-03-03 | below | Return into the gap
show: volume
caption: Bar 1 (February 18) has a high of 50.90 and bar 3 (February 20) has a low of 52.30.
```

Bar 1 is February 18 (high 50.90), bar 2 is February 19 (range 50.70 to 52.90, close 52.70) and bar 3 is February 20 (low 52.30). The gap runs from 50.90 to 52.30, which is 1.40 wide, and its midpoint is 51.60. Bar 2's range of 2.20 is 6.0 times the average range of the 10 bars before it (0.37), so it passes a 3-times displacement rule. On March 3 the price falls to a low of 51.80, 0.50 into the gap, which is 36% of its width. It stops above the CE and rises.

<div class="example" markdown>

### Worked example: a long from the gap

Account US$25,000, risk 1% per trade, Stock A.

1. Entry: a buy limit at 52.30, the top of the gap. On March 3 the low is 51.80, so the order fills at 52.30. A limit at the CE (51.60) would not have filled, because the low stopped at 51.80.
2. Stop: 50.65, five cents below bar 2's low of 50.70.
3. Risk per share = 52.30 - 50.65 = US$1.65.
4. Dollars at risk = US$250. Shares = 250 / 1.65 = 151.5, so 151 shares.
5. Target: 54.90, the swing high of February 26. Reward per share = 54.90 - 52.30 = US$2.60.
6. Reward to risk = 2.60 / 1.65 = 1.58R.

On March 9 the high is 54.93, so the target fills. A stop-out loses 151 x 1.65 = US$249.15. The bearish chart works the same way in reverse: bar 1 low 55.10 and bar 3 high 53.60 give a gap of 53.60 to 55.10 (1.50 wide, CE 54.35). On March 3 the high is 54.40, slightly through the CE, and the close of 53.60 stays below it.

</div>

```chart
data: 06-ict-and-smart-money-tested/fvg-bearish.json
title: Stock A, daily: a bearish fair value gap and a return
zone: 53.60-55.10 | 2026-02-18 to 2026-03-03 | Bearish FVG
level: 54.35 | Midpoint (CE)
marker: 2026-02-19 | above | Displacement
marker: 2026-03-03 | above | Return into the gap
show: volume
caption: Bar 1 (February 18) has a low of 55.10 and bar 3 (February 20) has a high of 53.60.
```

## What tests found

We found no peer-reviewed study that tests ICT's three-bar fair value gap as defined here. Studies of price gaps exist, but they cover the jump between one session's close and the next open, which is a different thing (see Gaps<!-- link: ../05-reading-charts/10-gaps.md -->).

The claim "price comes back to the gap" can be tested, and its weak point is the baseline. Price wanders, so it often revisits a recent price whether or not a gap was there. The code below counts bullish gaps in the made-up series [stock-b-daily.csv](../assets/data/stock-b-daily.csv) and checks how often the low of the following 10 bars reaches bar 3's low. It then asks the same question of every bar.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("stock-b-daily.csv", parse_dates=["date"])
gap_bottom = bars["high"].shift(2)          # bar 1 high
gap_top = bars["low"]                       # bar 3 low
bullish = gap_top > gap_bottom
next_lows = pd.concat([bars["low"].shift(-k) for k in range(1, 11)], axis=1).min(axis=1)
back = next_lows <= gap_top                 # price trades back to the gap top
valid = next_lows.notna()
print(int((bullish & valid).sum()), "bullish gaps")
print(f"returned within 10 bars: {back[bullish & valid].mean():.0%} of gaps, {back[valid].mean():.0%} of all bars")
```

</details>

It prints 38 bullish gaps. The price returned to the gap top within 10 bars in 79% of them, against 81% for all bars. In a series with no ICT logic, the gaps were revisited about as often as any other price. So "most gaps get filled" is not evidence by itself. A real test needs the fill rate to beat the baseline, and the trade to pay after costs: [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md).

Also check what happens when price does not return. A limit order at the edge of a gap fills only on a return, so the trades you miss are often the strongest moves. A backtest that counts only filled trades has to say so.

## Common mistakes

- Marking every three-bar gap. Without a displacement rule, small gaps appear all day and the method can explain any move.
- Putting the limit at the CE and assuming it fills. In the example the low stopped 0.20 above the CE, so the order would have missed.
- Treating "gap filled" as proof of the idea. Compare with all bars first.

## Try it

1\. Three bars: bar 1 has a high of 50.90, bar 2 trades 50.70 to 52.90, bar 3 has a low of 52.30. What kind of gap is it, and how wide?

<details class="solution" markdown>
<summary>Answer</summary>

Bar 1's high (50.90) is below bar 3's low (52.30), so it is a bullish gap. Width = 52.30 - 50.90 = 1.40.

</details>

2\. Find the midpoint (CE) of the bearish gap from 53.60 to 55.10.

<details class="solution" markdown>
<summary>Answer</summary>

(53.60 + 55.10) / 2 = 54.35.

</details>

3\. Bearish gap 53.60 to 55.10. You sell at the CE (54.35) with a stop at 55.25 (above bar 2's high of 55.20) and a target of 50.80. Shares for a 1% risk of US$250 and reward to risk?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share = 55.25 - 54.35 = 0.90. Shares = 250 / 0.90 = 277.8, so 277 shares. Reward per share = 54.35 - 50.80 = 3.55. Reward to risk = 3.55 / 0.90 = 3.9R. Clean planted charts give large ratios. Real gaps are messier, so test with real data.

</details>

4\. A study finds 80% of gaps get filled within 10 bars. What do you ask before believing it is an edge?

<details class="solution" markdown>
<summary>Answer</summary>

What share of ordinary bars (or random price levels) is revisited within 10 bars. In the made-up series above that baseline was 81%, higher than the gaps' 79%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | On a daily chart, mark every three-bar gap in the last 60 bars that passes a displacement rule you wrote down. For each, note whether price returned within 10 bars. |
| 3 | Do the fair value gap drills in [chart drills](../practice/chart-drills.md). |
| 2 | Write the sentence "My gap rule is: ..." with the displacement number in your [trade journal](../practice/trade-journal.md). |

</div>

## Key terms

- **Fair value gap (FVG)**: a three-bar imbalance. Bullish when bar 1's high is below bar 3's low, bearish when bar 1's low is above bar 3's high.
- **Imbalance**: another name for the zone of a fair value gap.
- **Displacement**: a strong, fast middle bar, read as aggressive orders.
- **Mitigation**: price returning into a gap or a block, in part or all the way.
- **Consequent encroachment (CE)**: the 50% midpoint of a gap.

Next: [Order blocks and breakers](04-order-blocks-and-breakers.md)
