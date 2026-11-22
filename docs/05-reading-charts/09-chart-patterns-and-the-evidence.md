# Chart patterns and the evidence

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can recognise four common chart patterns, work out a pattern's breakout level, stop and measured target, and say what tests found about them.

Before this: [Support and resistance](03-support-and-resistance.md) and [Volume and relative volume](04-volume-and-relative-volume.md). You need: a calculator.

## The idea

A **chart pattern** is a shape in the price that traders name and read as a sign of what comes next: a pause in a trend, or a turn. The shapes are built from the swing points and levels of lessons 2 and 3. Each pattern comes with a trigger (a close beyond a level), a stop (the level that proves the shape wrong) and a **measured move**, a target set by the height of the pattern.

Every chart in this lesson is made-up data, with each pattern planted in it. Real charts are messier, and the same shape that looks clear afterwards is often unclear while it forms. Keep that in mind when reading the numbers.

## How it works

Four patterns, each with its rule.

**Bull flag** (continuation). A sharp rise (the pole), then a short, shallow drift down on low volume (the flag), then a close above the flag's top on high volume. Target: the pole's height added to the breakout. Traders often look for a flag of 5 to 15 bars.

```chart
data: 05-reading-charts/bull-flag.json
title: Stock A, daily: a bull flag
level: 46.21 | Flag high
level: 44.57 | Flag low
marker: 2026-03-03 | above | Pole top 46.21
marker: 2026-03-16 | below | Breakout
show: volume
range: 2026-02-02 to 2026-03-30
caption: Pole from 39.91 to 46.21, a flag that drifts to 44.57, and a breakout on 3,600,000 shares.
```

The pole runs from a low of 39.91 on February 18 to a high of 46.21 on March 3, a rise of 6.30. The flag lasts eight bars, March 4 to March 13, with volume of 0.7 to 1.5 million shares against the pole's 2.2 to 4.5 million. The breakout bar on March 16 closes at 46.38 on 3,600,000 shares.

<div class="example" markdown>

### Worked example: trading the flag

You place a buy stop at US$46.30, above the flag high of 46.21. It fills on March 16, when the bar trades from 44.51 to 46.61.

1. Stop: US$44.40, below the lowest low of the flag and breakout bar (44.51). Risk per share = 46.30 - 44.40 = US$1.90.
2. Target: the pole's height added to the entry = 46.30 + 6.30 = US$52.60. Reward per share = 6.30, so the trade is 6.30 / 1.90 = 3.3R.
3. Size: with US$25,000 and 1% risk, the risk is US$250, so 250 / 1.90 = 131.6, or 131 shares.

The data ends on March 30 with a close of 51.00 and a high of 51.02, so the target has not been reached: the open profit is (51.00 - 46.30) / 1.90 = 2.5R. A flag that breaks down instead hits the stop for a loss of 131 x 1.90 = US$248.90, about 1R.

</div>

**Ascending triangle** (usually continuation). Resistance stays flat while the lows rise, so the price is squeezed against the ceiling. Trigger: a close above the flat top. Target: the triangle's widest height added to the breakout.

```chart
data: 05-reading-charts/ascending-triangle.json
title: Stock A, daily: an ascending triangle
level: 59.78 | Flat top
line: 2026-02-19 54.86 to 2026-03-19 57.84 | Rising lows
marker: 2026-03-25 | below | Breakout
show: volume
caption: Highs of 59.78, 59.77 and 59.51 and lows of 54.86, 56.35 and 57.84, then a close at 61.08 on 3,900,000 shares.
```

The swing highs are 59.78 (February 11), 59.77 (February 27) and 59.51 (March 13). The swing lows are 54.86, 56.35 and 57.84. On March 25 the close is 61.08 on 3,900,000 shares. The widest height is 59.78 - 54.86 = 4.92, so the measured target is 59.78 + 4.92 = 64.70. The data reaches a high of 64.16.

**Head and shoulders** (reversal). Three peaks, the middle one the highest, with the lows between them joined into a **neckline**. Trigger: a close below the neckline. Target: the head's height above the neckline, subtracted from the break.

```chart
data: 05-reading-charts/head-and-shoulders.json
title: Stock A, daily: a head and shoulders
level: 50.50 | Neckline
marker: 2026-01-26 | above | Left shoulder 54.21
marker: 2026-02-13 | above | Head 59.56
marker: 2026-03-10 | above | Right shoulder 54.73
marker: 2026-03-16 | below | Close below neckline
caption: Shoulders at 54.21 and 54.73, a head at 59.56 and a neckline near 50.50.
```

The neckline joins the lows of 50.33 (February 2) and 50.75 (February 27), which this book rounds to 50.50. On March 16 the close is 50.46, below it. The head is 59.56 - 50.50 = 9.06 above the neckline, so the target is 50.50 - 9.06 = 41.44. The data ends at 44.00 on March 30. Trading it means a short sale, which has its own rules and costs ([Short selling](../01-how-markets-work/08-short-selling.md)).

**Double top** (reversal). Two peaks at about the same price with a low between them. Trigger: a close below that low. Target: the height from the low to the peaks, subtracted from the break.

```chart
data: 05-reading-charts/double-top.json
title: Stock A, daily: a double top
level: 53.48 | Neckline
marker: 2026-01-30 | above | Peak 59.70
marker: 2026-02-26 | above | Peak 59.46
marker: 2026-03-04 | below | Close below
caption: Peaks at 59.70 and 59.46 and a low of 53.48 between them.
```

The peaks are 59.70 (January 30) and 59.46 (February 26), and the low between is 53.48 (February 12). The first close below it is 52.87 on March 4. The height is 59.70 - 53.48 = 6.22, so the target is 53.48 - 6.22 = 47.26.

### When it fails

The next chart has the same double top. This time the close below the low on March 4 reverses at once.

```chart
data: 05-reading-charts/failed-double-top.json
title: Stock A, daily: a double top that fails
level: 53.17 | Neckline
marker: 2026-03-04 | below | Close below 53.17
range: 2026-01-05 to 2026-04-01
caption: The close of 52.80 on March 4 is followed by a rise to a new high of 66.09 by April 1.
```

The first close below 53.17 is 52.80 on March 4. The next day the bar trades up to 54.27, and the price ends at 66.00 on April 1, above both peaks. A short at 52.80 with a stop at 54.30 would have lost 1.50 a share. A **failed pattern** is a trigger that reverses; a stop is what limits it. Patterns fail often, and the stop is part of the pattern.

## What tests found

Lo, Mamaysky and Wang (2000) wrote an algorithm that finds patterns in prices without eyeballing them (head and shoulders, double tops and bottoms, triangles and others). On US stocks from 1962 to 1996 they compared the returns after each pattern with all returns, and found that several patterns carried incremental information, more so for Nasdaq stocks than for NYSE and AMEX stocks. They do not claim that the patterns pay after costs ([Journal of Finance, 55(4), 1705-1765](https://doi.org/10.1111/0022-1082.00265)).

Park and Irwin (2007) reviewed 95 modern studies of technical analysis: 56 positive, 20 negative and 19 mixed, with profits through the early 1990s and weaknesses in testing, such as data snooping ([Journal of Economic Surveys, 21(4), 786-826](https://doi.org/10.1111/j.1467-6419.2007.00519.x)). Sullivan, Timmermann and White (1999) show how to adjust for it ([lesson 5](05-moving-averages.md)).

Published success rates for each named pattern come mostly from people picking patterns after the fact, so this book does not quote them.

## Common mistakes

- Seeing a pattern before it is complete. A head and shoulders is only a head and shoulders once the right shoulder has formed.
- Skipping the stop because the pattern "must" work. Every pattern here has a failure on the same chart.
- Taking the measured move as a promise. It is a way to compare reward with risk, not a forecast.

## Try it

1\. A flag has a pole from 20.00 to 25.00 and a flag high of 24.50. You enter at 24.60 with a stop at 23.40. What is the target and the reward to risk?

<details class="solution" markdown>
<summary>Answer</summary>

Pole height = 5.00, so the target is 24.60 + 5.00 = 29.60. Risk = 24.60 - 23.40 = 1.20. Reward to risk = 5.00 / 1.20 = 4.2.

</details>

2\. A head and shoulders has a head at 80.00 and a neckline at 72.00. The close breaks the neckline at 71.80. What is the measured target?

<details class="solution" markdown>
<summary>Answer</summary>

Height = 80.00 - 72.00 = 8.00. Target = 72.00 - 8.00 = 64.00.

</details>

3\. On the ascending triangle chart, how much of a gain per share is the measured move from the breakout close of 61.08 to the target of 64.70?

<details class="solution" markdown>
<summary>Answer</summary>

64.70 - 61.08 = US$3.62 per share, or 3.62 / 61.08 = 5.9%.

</details>

4\. Name the evidence for chart patterns in one sentence, with the limit.

<details class="solution" markdown>
<summary>Answer</summary>

Lo, Mamaysky and Wang (2000) found that several patterns carried incremental information about returns in US stocks from 1962 to 1996, but that does not show a rule that pays after costs, and Park and Irwin (2007) note data-snooping weaknesses across such tests.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run a set of [chart drills](../practice/chart-drills.md) and name the pattern in each chart before the explanation. |
| 5 | Find one flag or triangle on a stock you follow. Write the trigger, stop, measured target and reward to risk, and save it in your [trade journal](../practice/trade-journal.md) without trading it. |

</div>

## Key terms

- **Chart pattern**: a named shape in the price that traders read as a sign of what comes next.
- **Measured move**: a target set by the height of the pattern.
- **Bull flag**: a sharp rise, a shallow drift down on low volume, then a breakout.
- **Pole**: the sharp rise before a flag.
- **Ascending triangle**: a flat top with rising lows.
- **Head and shoulders**: three peaks with the middle one highest, ending in a break of the neckline.
- **Neckline**: the line through the lows between the peaks of a head and shoulders.
- **Double top**: two peaks at about the same price with a low between them.
- **Failed pattern**: a trigger that reverses soon after.

Next: [Gaps](10-gaps.md)
