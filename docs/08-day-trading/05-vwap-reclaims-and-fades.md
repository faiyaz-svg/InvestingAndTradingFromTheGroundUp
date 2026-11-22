# VWAP reclaims and fades

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">DAY</span>

After this lesson you can write the rules for a VWAP reclaim (a long) and a VWAP fade (a short), size each from the stop, and work out its result in R, including why the fade pays less than the reclaim.

Before this: [Intraday charts and VWAP](03-intraday-charts-and-vwap.md), [The opening range breakout](04-opening-range-breakout.md) and [Short selling](../01-how-markets-work/08-short-selling.md). You need: a calculator.

## The idea

Session VWAP (lesson 3) is the average price paid today. A stock that spends the morning below it has sellers in control of the day's average. When the price closes back above it after a long time below, buyers have pushed the stock over the average of everyone who bought today, which is a change of mood. A **VWAP reclaim** buys that change.

The mirror idea is the **VWAP fade**: a stock that runs far above VWAP is paying much more than today's average, and if it stalls, the line pulls it back. A fade sells the stall and aims at VWAP. Both setups treat VWAP as a magnet. Both fail when the day turns into a one-way trend.

## How it works

### The reclaim, in rules

1. The stock closed below VWAP on at least 12 straight 5-minute bars, which is one hour (made up).
2. The **reclaim bar** is the first 5-minute bar that closes above VWAP. Write its high \(H\) and low \(L\).
3. Entry: a buy stop at \(H + 0.01\).
4. Cancel the order if any bar trades below \(L\) before it fills.
5. Stop: 0.02 below the lowest low of the six bars before the reclaim bar (the base the stock built).
6. Size: 1% of the account over the risk per share, rounded down.
7. Target: 2R. Exit at 3:55 p.m. ET if neither has filled.
8. There is no skip rule for a level less than 2R away (lesson 4's rule 8 is for the opening range breakout only).

<div class="example" markdown>

### Worked example: a reclaim

Stock A on September 22, 2026 opens at 60.00 and sells off. It closes below VWAP on 33 straight 5-minute bars, from 9:35 to 12:15. Account US$25,000, 1R = US$250.

1. The 12:20 p.m. bar is the reclaim bar: open 58.79, high 58.97, low 58.78, close 58.96, against a VWAP of 58.92.
2. Buy stop at 58.98.
3. The base is the six bars from 11:50 a.m. to 12:15 p.m. Their lowest low is 58.18, so the stop is 58.16. Risk per share = 58.98 - 58.16 = US$0.82.
4. Shares = 250 / 0.82 = 304.9, so 304. One R is 304 x 0.82 = US$249.28. Position = 304 x 58.98 = US$17,929.92.
5. The 12:25 p.m. bar trades to 59.25, so the order fills at 58.98. The 2R target is 58.98 + 1.64 = US$60.62, reached in the 1:30 p.m. bar.
6. Gross gain = 304 x 1.64 = US$498.56. Fees at US$0.005 per share per side (made up) = 2 x 1.52 = US$3.04. Net = US$495.52, which is 495.52 / 249.28 = +1.99R.

The morning high, 60.19, sits 1.48R above the entry. Lesson 4's skip rule (skip when a level is less than 2R away) belongs to the opening range breakout only, and the reclaim rules above do not use it, so this trade is taken. If you add that skip rule to the reclaim, this trade is skipped and a +1.99R winner is missed. Pick one version, write it in your plan, and test it in your paper block.

</div>

Look at the long stretch below the line, the reclaim bar and the steady climb.

```chart
data: 08-day-trading/vwap-reclaim.json
title: Stock A, 5-minute: a VWAP reclaim after a morning below the line
show: vwap
level: 58.98 | Buy stop 58.98
level: 58.16 | Stop 58.16
level: 60.62 | Target 60.62
marker: 2026-09-22 12:20 | below | Reclaim bar
range: 2026-09-22 09:30 to 2026-09-22 15:55
caption: Price closed under VWAP from 9:35 to 12:15, closed above it at 12:20, and reached the 2R target at 1:30 p.m.
```

### The fade, in rules

1. The stock makes a new high of the day at least 2% above VWAP (made up).
2. The **rejection bar** makes that high, closes below its open and closes in the lower half of its range.
3. Entry: a sell stop (a short) at the rejection bar's low minus 0.01.
4. Stop: 0.02 above the rejection bar's high.
5. Size: 1% over the risk per share.
6. Target: a buy limit at VWAP (measured at the close of the entry bar) plus 0.01, so that it fills before the line.

A short sale needs a margin account at a broker that can locate shares to borrow (Part 1, [Short selling](../01-how-markets-work/08-short-selling.md)). It is not available in a TFSA or RRSP ([Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md)). Check the stock is not under the short sale restriction in lesson 6.

<div class="example" markdown>

### Worked example: a fade

Stock A on September 23, 2026 opens at 25.00 and runs up. Account US$25,000.

1. The 10:00 a.m. bar makes the day's high of 26.42, which is 3.0% above a VWAP of 25.65. It opens 26.30 and closes 26.15, which is the bottom of its range 26.15 to 26.42. This is the rejection bar.
2. Sell stop at 26.15 - 0.01 = 26.14. Stop at 26.42 + 0.02 = 26.44. Risk per share = 0.30.
3. Shares = 250 / 0.30 = 833.3, so 833. One R is 833 x 0.30 = US$249.90. Position = 833 x 26.14 = US$21,774.62.
4. The 10:05 bar trades to 25.98, so the short fills at 26.14. VWAP at the close of that bar is 25.69, so the target is 25.70.
5. The 10:25 bar trades to 25.69 and the target fills. Gain per share = 26.14 - 25.70 = 0.44. Gross = 833 x 0.44 = US$366.52.
6. Fees = 2 x 833 x 0.005 = US$8.33. Net = US$358.19, which is 358.19 / 249.90 = +1.43R.

</div>

The fade's reward is the distance from the entry to VWAP. Here that is 0.44 against a risk of 0.30, or 1.47R before costs. A fade pays less than 2R because VWAP is the target, so a trade with a small distance to the line is not worth taking. The break-even win rate (Part 3, [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)) for a 1.43R payoff is 1 / (1 + 1.43) = 41.2%.

```chart
data: 08-day-trading/vwap-fade.json
title: Stock A, 5-minute: a fade from 3% above VWAP back to the line
show: vwap
level: 26.14 | Sell stop 26.14
level: 26.44 | Stop 26.44
level: 25.70 | Target 25.70
marker: 2026-09-23 10:00 | above | Rejection bar
range: 2026-09-23 09:30 to 2026-09-23 15:55
caption: The 10:00 bar made the high and closed at its low, and the 10:25 bar traded down to the target.
```

### When they fail, and what tests found

A reclaim fails when the bounce is only a short squeeze or when the whole market falls again. A fade fails on a trend day, when strength keeps buying every dip and VWAP rises to meet the price instead. No published test of either rule as a retail setup was found for this book. VWAP is a documented benchmark for execution quality, but a benchmark is not a signal. The index result in lesson 1 (intraday momentum) points the other way from a fade, though it covers an ETF and does not test this rule. Use your paper block to measure the setup.

## Common mistakes

- Buying the first cross above VWAP in the first 30 minutes. VWAP is close to the price then, so a cross says little (lesson 3).
- Fading a stock with a fresh catalyst and rising volume. The news can keep pushing it, and the line follows slowly.
- Setting the target at VWAP when VWAP is only a few cents away. The reward is smaller than the costs.

## Try it

1\. Reclaim: the reclaim bar of Stock B has high 33.40 and low 33.05. The six bars before it have a lowest low of 32.60. Account US$20,000, risk 1%. Give the trigger, stop, shares and 2R target.

<details class="solution" markdown>
<summary>Answer</summary>

Trigger 33.41. Stop 32.60 - 0.02 = 32.58. Risk = 0.83. Risk amount = US$200. Shares = 200 / 0.83 = 240.96, so 240. Target = 33.41 + 1.66 = US$35.07.

</details>

2\. Fade: the rejection bar has high 52.60 and low 52.10, and VWAP is 51.40 at the entry bar's close. Give the entry, stop, target and the reward-to-risk ratio.

<details class="solution" markdown>
<summary>Answer</summary>

Entry (sell stop) 52.09. Stop 52.62. Risk = 0.53. Target = 51.41. Reward = 52.09 - 51.41 = 0.68. Reward to risk = 0.68 / 0.53 = 1.28.

</details>

3\. What is the break-even win rate for the fade in exercise 2, before costs?

<details class="solution" markdown>
<summary>Answer</summary>

1 / (1 + 1.28) = 43.9%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Do the VWAP items in [chart drills](../practice/chart-drills.md): find the reclaim bar and the fade's stop. |
| 5 | Open a 5-minute chart with VWAP from any recent day. Count the bars closing below VWAP before the first close above it. |

</div>

## Key terms

- **VWAP reclaim**: a long entry after a long stretch below VWAP, when a bar closes back above it.
- **Reclaim bar**: the first 5-minute bar that closes above VWAP after the stretch below.
- **VWAP fade**: a short entry after a stock stalls far above VWAP, aiming at the line.
- **Rejection bar**: a bar that makes a new high and closes near its low.

Next: [News, momentum and halts](06-news-momentum-and-halts.md)
