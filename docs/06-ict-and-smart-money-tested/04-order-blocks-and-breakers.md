# Order blocks and breakers

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">ICT</span>

After this lesson you can mark a bullish or bearish order block and a breaker block by a written rule, work out a trade from each with its risk, and name what a placebo test would check.

Before this: [Fair value gaps](03-fair-value-gaps.md) and [Support and resistance](../05-reading-charts/03-support-and-resistance.md). You need: a calculator.

## The idea

Stock A drifts down for three days, then jumps 4.3% in one candle and keeps rising. Which candle matters? Teachers of ICT and smart money concepts point to the last candle before the jump. In their account, a large trader was buying during that candle, the buying was not finished, and the trader will want to buy the rest if price comes back.

A **bullish order block** is the last down candle before a displacement upward that breaks structure. A **bearish order block** is the last up candle before a displacement downward that breaks structure. The block is the area of that candle, and the claim is that price returning to it finds orders again.

Teachers differ on what the area is: the body (open to close), the full range (high to low), or the 50% level of the body. Fix one definition, or you have too much freedom to fit the chart.

A **breaker block** (or breaker) is an order block that failed. If a bullish block is broken by a close below it, the block is said to flip: it is now a bearish zone, where price returning from below may be rejected. This is the same idea as role reversal in [Support and resistance](../05-reading-charts/03-support-and-resistance.md), applied to a candle zone.

## How it works

Rules for a bullish block, using the body as the zone. A bearish block mirrors them.

1. Find a displacement candle that closes above the last swing high (a break of structure, lesson 1).
2. Mark the last down candle before it. The zone is its body, from close to open.
3. Place a buy limit at the top of the zone, and the protective stop right below the candle's low.
4. Target the high of the move that started at the block.
5. If a candle closes below the zone before your order fills, drop the long. It is now a breaker candidate.

The chart shows the pattern in Stock A.

```chart
data: 06-ict-and-smart-money-tested/order-block.json
title: Stock A, daily: a bullish order block and its retest
zone: 51.00-51.70 | 2026-02-12 to 2026-02-20 | Bullish order block
level: 52.66 | Swing high broken
marker: 2026-02-12 | below | Last down candle
marker: 2026-02-13 | below | Displacement
marker: 2026-02-20 | below | Retest
show: volume
caption: The February 12 candle opens at 51.70 and closes at 51.00, then price breaks 52.66.
```

The swing high is 52.66 (February 6). The last down candle is February 12: open 51.70, close 51.00, high 51.80, low 50.90. The next bar opens at 51.00 and closes at 53.20, above 52.66, with a range of 2.40. The impulse peaks at 54.60 on February 17. On February 20 the low is 51.55, which is 0.15 inside the top of the block, and the close is 52.00.

<div class="example" markdown>

### Worked example: a long from the block

Account US$25,000, risk 1% per trade, Stock A.

1. Entry: a buy limit at 51.70, the top of the body. On February 20 the low is 51.55, so it fills.
2. Stop: 50.85, five cents under the block candle's low of 50.90.
3. Risk per share = 51.70 - 50.85 = US$0.85.
4. Dollars at risk = US$250. Shares = 250 / 0.85 = 294.1, so 294 shares. The position costs 294 x 51.70 = US$15,199.80, inside the account.
5. Target: 54.60. Reward per share = 54.60 - 51.70 = US$2.90.
6. Reward to risk = 2.90 / 0.85 = 3.4R.

On February 26 the high is 54.69, so the target fills. A stop-out loses 294 x 0.85 = US$249.90. The stop is tight because the candle is small.

</div>

Now the same block when it fails.

```chart
data: 06-ict-and-smart-money-tested/breaker-block.json
title: Stock A, daily: the same block fails and becomes a breaker
zone: 51.00-51.70 | 2026-02-23 to 2026-03-05 | Breaker (failed bullish block)
marker: 2026-02-23 | above | Close below the block
marker: 2026-02-27 | above | Rejected from below
show: volume
caption: A close at 49.80 breaks the block; the return to 51.45 fails.
```

Here price pulls back into the block on February 20 and closes at 51.10, inside it. On February 23 it closes at 49.80, below the block. That bar breaks the long, and the zone becomes a breaker. On February 27 price rises to a high of 51.45, 0.45 into the zone, and closes at 50.60.

A short from the breaker: sell limit at the midpoint of the zone, 51.35 (it fills on February 27), a stop at 52.00 (0.20 above the block's top wick of 51.80), and a target of 49.50. Risk per share = 52.00 - 51.35 = 0.65. Shares = 250 / 0.65 = 384.6, so 384. Reward = 51.35 - 49.50 = 1.85, so the reward to risk is 2.8R. The low on March 5 is 49.44, so the target fills.

## What tests found

We found no peer-reviewed study that tests order blocks or breakers as the teachers define them. The idea has one mechanism and one family of evidence.

The mechanism is that a candle holds the unfilled part of a large order. Public price data cannot confirm that. Large orders are usually split into many smaller ones and traded over time, and a chart does not show whose orders made a candle. Proponents say the leftover orders still leave a footprint at the block. That claim can be tested only through its predictions, not by looking at the candle.

The related evidence is about levels that price reacts to. Chung and Bellotti (2021) built an algorithm that finds support and resistance levels in intraday price series. They report that the levels reversed price trends at a statistically significant rate<!-- lint-ok: significant (statistical sense) -->, that price was more likely to bounce at levels with more earlier bounces, and that the bounce probability decayed over time ([arXiv preprint 2101.07410](https://arxiv.org/abs/2101.07410); we could not confirm that it has been published in a journal). Osler (2000) and Kavajecz and Odders-White (2004) found similar reactions at levels, in currencies and in NYSE stocks (see [Liquidity and stop runs](02-liquidity-and-stop-runs.md)). None of these tests a single candle's body as a zone.

A fair test of an order block is a placebo test.

1. Write the rule: which candle, which zone, which entry, stop and target.
2. Apply it to every displacement in a long sample, and record each trade's R.
3. Apply the same entry, stop and target rules to placebo candles, such as a candle chosen at random before each displacement, or the second-to-last candle.
4. Count costs, and compare the two sets of trades on a period the rule was not tuned on.

If the true block does no better than the placebo, the zone adds nothing. If it does better, you still need enough trades: 40 trades leave a win rate with a 95% range of about 30 points ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)).

## Common mistakes

- Picking the block after seeing the move. The last down candle is only identifiable once the displacement has happened, so you can only trade the retest, and you must have the rule written before.
- Drawing the zone wider after price trades through it. A zone that stretches to include the wick fits any outcome.

## Try it

1\. In the order block chart, the candle of February 12 opens at 51.70 and closes at 51.00. What are the body zone and the full-range zone (high 51.80, low 50.90)?

<details class="solution" markdown>
<summary>Answer</summary>

Body: 51.00 to 51.70. Full range: 50.90 to 51.80. The rule you choose changes the entry and the stop, so fix it first.

</details>

2\. Risk 1% of US$25,000. Entry 51.70, stop 50.85, target 54.60. How many shares, and what is the reward to risk?

<details class="solution" markdown>
<summary>Answer</summary>

Risk per share 0.85, shares = 250 / 0.85 = 294. Reward per share 2.90, so 2.90 / 0.85 = 3.4R.

</details>

3\. A bar closes at 49.80 below a bullish block of 51.00 to 51.70. What do teachers call the block now, and which way would a trade from it point?

<details class="solution" markdown>
<summary>Answer</summary>

A breaker. The zone is treated as resistance, so a trade from it points short, on a return from below.

</details>

4\. Why is the placebo test more convincing than counting how often price bounces at blocks?

<details class="solution" markdown>
<summary>Answer</summary>

Price bounces from many levels by chance. The placebo test applies the same entry, stop and target to ordinary candles, so it shows whether the block adds anything over the baseline.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Find three displacements on a daily chart. For each, mark the block by your written rule and note whether price returned to it and what happened. |
| 3 | Do the order block drills in [chart drills](../practice/chart-drills.md). |
| 2 | In your [trade journal](../practice/trade-journal.md), add "OB" and "breaker" as setup names with the rule in one line. |

</div>

## Key terms

- **Order block**: the last opposite-colour candle before a displacement that breaks structure.
- **Bullish order block**: the last down candle before an upward displacement.
- **Bearish order block**: the last up candle before a downward displacement.
- **Breaker block**: an order block that price closed through, now treated as a zone with the opposite role.
- **Placebo test**: running the same rules on ordinary candles to see whether the special candle adds anything.

Next: [Sessions, kill zones and premium and discount](05-sessions-kill-zones-and-premium-discount.md)
