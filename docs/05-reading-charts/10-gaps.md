# Gaps

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can measure a gap in dollars, percent and ATR, name the four common gap types from their position and volume, and say why a gap can't be classified until you see what follows.

Before this: [Volatility indicators: ATR, Bollinger and Keltner](07-volatility-indicators.md) and [Volume and relative volume](04-volume-and-relative-volume.md). You need: a calculator.

## The idea

A **gap** is a space on the chart where no trades happened: the low of one bar is above the high of the previous bar (a gap up), or the high is below the previous low (a gap down). It forms when the price opens away from where it closed, usually after news arrives while the market is closed (Part 1: [What a stock is and why prices move](../01-how-markets-work/01-what-a-stock-is.md), and [Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)).

The same 3% gap can come from a routine move or from an event that changes the story, and the chart can't tell you which at the open. What helps is the context: where the gap sits in the trend, and how much volume trades.

A gap here is not the three-bar **fair value gap** of Part 6 ([Fair value gaps](../06-ict-and-smart-money-tested/03-fair-value-gaps.md)). A daily gap is empty space between two consecutive bars, and no regular-session trades happened in it. A fair value gap is a range between bar 1 and bar 3 that bar 2 traded straight through, so trades did happen there. They are different things, and the evidence in this lesson is not about fair value gaps.

## How it works

Measure every gap three ways:

\[ \text{Gap} = O_t - C_{t-1}, \qquad \text{Gap \%} = \frac{O_t - C_{t-1}}{C_{t-1}}, \qquad \text{Gap in ATR} = \frac{O_t - C_{t-1}}{ATR_{t-1}} \]

- \(O_t\) is today's open and \(C_{t-1}\) is yesterday's close, in US$.
- \(ATR_{t-1}\) is the 14-bar average true range at yesterday's close ([Volatility indicators](07-volatility-indicators.md)), in US$.
- The empty space itself, from yesterday's high to today's low (for a gap up), is the **gap area**.

Traders sort gaps into four types by position and volume. The chart has one of each, marked with a shaded band over the gap area.

```chart
data: 05-reading-charts/gap-types.json
title: Stock A, daily: four kinds of gap
zone: 51.58-52.29 | 2026-02-06 to 2026-02-11 | Common gap
zone: 51.37-53.60 | 2026-02-24 to 2026-04-10 | Breakaway gap
zone: 58.06-59.57 | 2026-03-17 to 2026-04-10 | Runaway gap
zone: 64.11-66.05 | 2026-03-31 to 2026-04-01 | Exhaustion gap
show: volume
range: 2026-01-05 to 2026-04-10
caption: Four gaps in one made-up stock. Only the common and exhaustion gaps are filled, and each is filled within days.
```

| Date | Type | Gap area | Open vs previous close | Gap in ATR | RVOL | Filled? |
|---|---|---|---|---|---|---|
| Feb 6 | Common | 51.58 to 52.29 | +2.0% | 1.9 | 1.14 | February 11 |
| Feb 24 | Breakaway | 51.37 to 53.60 | +5.0% | 4.5 | 4.02 | No |
| Mar 17 | Runaway | 58.06 to 59.57 | +3.0% | 2.4 | 1.23 | No |
| Mar 31 | Exhaustion | 64.11 to 66.05 | +3.5% | 2.8 | 3.09 | April 1 |

A gap is **filled** when the price trades back through the whole gap area.

1. A **common gap** appears inside a range, on ordinary volume, and tends to fill within days. On February 6 the price opens at 52.37, 2.0% up, in a sideways stretch, and by February 11 it trades back down to 50.85, through the whole gap area.
2. A **breakaway gap** leaves a range or a pattern, on heavy volume. On February 24 the price opens 5.0% higher, out of a range with a top near 52.67, on 5,400,000 shares, 4.0 times the 20-day average. The gap area is not revisited.
3. A **runaway gap** (or continuation gap) appears in the middle of a trend, on moderate volume. March 17 opens 3.0% higher in a rise from 51 to 64, with RVOL of 1.23.
4. An **exhaustion gap** appears late in a trend, on very heavy volume, and is followed by a reversal. March 31 opens 3.5% higher after a 25% rise from the February 23 close, on 6,300,000 shares (RVOL 3.09). The next day trades down to 63.32, below the bottom of the gap area, so the gap fills in one session.

<div class="warning" markdown>

The names are known only afterwards. The breakaway gap on February 24 and the exhaustion gap on March 31 look alike on the day: a large gap on high volume. What separates them is where they sit in the trend and what the next days do. If you decide the type before the next days, you are guessing.

</div>

<div class="example" markdown>

### Worked example: the size of a gap against your plan

You are short 200 shares of Stock A from the close of February 23 at US$51.34, with a buy stop at US$52.00. The 14-day ATR is 0.574.

1. The next open is 53.91. Gap = 53.91 - 51.34 = US$2.57, which is 5.0% of 51.34 and 2.57 / 0.574 = 4.5 ATR.
2. The planned loss at the stop is (52.00 - 51.34) x 200 = US$132.
3. The stop triggers at the open and fills near 53.91, a loss of 2.57 x 200 = US$514, which is 3.9 times the plan.

A stop does not protect against a gap, because the price passes through it ([Order types](../01-how-markets-work/05-order-types.md)). Gap risk is managed with position size, and part 3 covers it ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

</div>

### Earnings gaps

Many large gaps follow earnings reports. Part 1 had one, an 8.0% gap up from 49.40 to 53.35 ([What a stock is and why prices move](../01-how-markets-work/01-what-a-stock-is.md)). Before holding through a report, find the date on the company's calendar. Companies announce them in advance.

## What tests found

This book knows of no peer-reviewed test of the four-way classification above. The names are chart lore, and they are only identified in hindsight, so they are hard to test without bias.

There is evidence about what often follows news gaps. Bernard and Thomas (1989) found that after large earnings surprises, stock prices kept drifting in the same direction for about 60 trading days, which is called post-earnings-announcement drift ([Journal of Accounting Research, 27 (Supplement), 1-36](https://doi.org/10.2307/2491062)). It means that after big earnings news the price tends, on average, to keep moving the same way for a while. It does not say that every gap holds, and the exhaustion gap above is the counter-example.

## Common mistakes

- Trading every gap fill as a rule. Some gaps are never filled, as on February 24.
- Ignoring the gap when you size a position. The stop is not where you will get out.
- Calling a type at the open. Wait for the volume and the next bars.

## Try it

1\. A stock closes at 80.00 and opens at 83.20. ATR is 1.60. What are the gap in dollars, percent and ATR?

<details class="solution" markdown>
<summary>Answer</summary>

Gap = 3.20. Percent = 3.20 / 80.00 = 4.0%. In ATR = 3.20 / 1.60 = 2.0.

</details>

2\. The previous bar's high is 80.60 and today's low is 82.90. What is the gap area? Does a low of 81.00 two days later fill it?

<details class="solution" markdown>
<summary>Answer</summary>

The gap area is 80.60 to 82.90. A low of 81.00 enters the gap but does not reach 80.60, so the gap is only partly filled.

</details>

3\. On the chart, the breakaway gap came with 5,400,000 shares and a 20-day average of 1,343,000. What is RVOL?

<details class="solution" markdown>
<summary>Answer</summary>

5,400,000 / 1,343,000 = 4.0.

</details>

4\. You own 300 shares at 40.00 with a stop at 38.50. The stock opens at 36.80 on bad news. What was the planned loss and what is the actual loss?

<details class="solution" markdown>
<summary>Answer</summary>

Planned = (40.00 - 38.50) x 300 = US$450. Actual = (40.00 - 36.80) x 300 = US$960, which is 2.1 times the plan.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Run a set of [chart drills](../practice/chart-drills.md) with gap charts. Name the type before you open the answer. |
| 4 | Find the last three gaps over 3% on a stock you follow. For each, write the gap in percent and ATR, the volume and whether it filled in the next 10 days. |
| 2 | Write a rule for what you do with an open position before an earnings date. Save it in your [trade journal](../practice/trade-journal.md). |

</div>

## Key terms

- **Gap**: a space on the chart where no trades happened between two bars.
- **Gap area**: the price range between the previous bar's extreme and the next bar's.
- **Filled gap**: a gap that the price has traded back through completely.
- **Common gap**: a gap inside a range on ordinary volume that tends to fill soon.
- **Breakaway gap**: a gap out of a range or pattern on heavy volume.
- **Runaway gap**: a gap in the middle of a trend on moderate volume.
- **Exhaustion gap**: a gap late in a trend on heavy volume, followed by a reversal.
- **Post-earnings-announcement drift**: the tendency for a stock to keep moving in the direction of an earnings surprise.

Next: [Multiple timeframes and relative strength](11-multi-timeframe-and-relative-strength.md)
