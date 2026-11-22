# Trend and market structure

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can mark swing highs and swing lows on a chart, call the trend from them with a written rule, and name the price that would end the trend.

Before this: [Candles, bars and timeframes](01-candles-bars-and-timeframes.md). You need: a calculator.

## The idea

Stock A rises from US$40 to US$54.77 over three months, but not in a straight line. It climbs for a few days, falls back, and climbs again. Each rise ends higher than the last one, and each pullback ends higher than the last one. The shape of those turning points is what traders call the trend.

A **swing high** is a bar whose high is the highest of the bars around it. A **swing low** is a bar whose low is the lowest of the bars around it. Both are turning points. In this book a swing point uses 5 bars on each side: a swing high is a bar whose high is at least as high as the highs of the 5 bars before it and the 5 bars after it.

**Market structure** is the sequence of swing highs and swing lows. From it we read three states.

- An **uptrend** has higher highs and higher lows: each swing high is above the previous one, and each swing low is above the previous one.
- A **downtrend** has lower highs and lower lows.
- A **range** (or sideways market) has swing highs and lows that stay in a band without a direction.

## How it works

1. Mark the swing highs and swing lows with the 5-bar rule.
2. Compare each swing high with the one before it, and each swing low with the one before it.
3. If both rise, call an uptrend. If both fall, call a downtrend. If they mix or stay level, call it a range or an unclear trend.
4. Write down the **invalidation level**: in an uptrend, the most recent swing low; in a downtrend, the most recent swing high. A close beyond it ends the trend call. Traders call this a break of structure.

The first chart marks the swing points of Stock A. Look for the highs stepping up, the lows stepping up, and then the first low that is lower than the one before.

```chart
data: 05-reading-charts/uptrend-structure.json
title: Stock A, daily: an uptrend and then a break of structure
marker: 2026-01-21 | above | High 44.17
marker: 2026-01-28 | below | Low 41.61
marker: 2026-02-13 | above | High 47.78
marker: 2026-02-24 | below | Low 44.71
marker: 2026-03-13 | above | High 51.76
marker: 2026-03-24 | below | Low 48.43
marker: 2026-04-06 | above | High 54.77
marker: 2026-04-17 | below | Low 46.84
level: 48.43 | Last higher low
caption: Three higher lows, four swing highs, and then a close below the last higher low on April 15.
```

The swing highs are 44.17 (January 21), 47.78 (February 13), 51.76 (March 13) and 54.77 (April 6). The swing lows are 41.61 (January 28), 44.71 (February 24) and 48.43 (March 24). Each is above the one before, so by step 3 this is an uptrend from January to early April.

Then the sequence breaks. On April 15 the close is US$48.21, below the last higher low of 48.43. Two days later the swing low is 46.84, lower than 48.43, and the next swing high (April 24) is 50.61, lower than 54.77. The trend call changes from uptrend to unclear, and by May 7 the low is 43.97: lower highs and lower lows.

<div class="warning" markdown>

A swing point is only known after the fact. With a 5-bar rule, the swing high on April 6 is confirmed five trading days later, on April 13. The chart shows it at its true date, but at the time you could not have marked it yet. When you test an idea on past charts, mark swing points only with the information you had on that day.

</div>

The downtrend is the mirror image. Look at the highs and lows stepping down.

```chart
data: 05-reading-charts/downtrend-structure.json
title: Stock A, daily: a downtrend
marker: 2026-02-20 | above | High 58.11
marker: 2026-03-18 | above | High 55.04
marker: 2026-04-13 | above | High 51.81
marker: 2026-02-16 | below | Low 55.30
marker: 2026-03-11 | below | Low 51.92
marker: 2026-04-02 | below | Low 48.33
caption: Lower highs (58.11, 55.04, 51.81) and lower lows (55.30, 51.92, 48.33).
```

A range has no direction in its swing points. In this one the price stays between 29.00 and 31.03 for 55 bars, and the first and last closes are 29.77 and 29.84.

```chart
data: 05-reading-charts/sideways.json
title: Stock B, daily: a range
level: 31.03 | Range high
level: 29.00 | Range low
caption: The price stays between 29.00 and 31.03 for 55 bars with no higher highs or lower lows.
```

<div class="example" markdown>

### Worked example: a stop at the invalidation level

On March 25, with the higher low of 48.43 in place, you buy 100 shares of Stock A at US$50.00. The day traded between 49.78 and 51.15, so the fill is possible. You place a sell stop at US$48.30, below the swing low, because a close under 48.43 would end the uptrend call.

1. Risk per share = 50.00 - 48.30 = US$1.70.
2. Risk on 100 shares = 1.70 x 100 = US$170.
3. The stop triggers on April 15, when the day trades down to 48.20. The market order fills near 48.30 and the loss is about US$170, or 1R (one unit of risk).

Before the stop, the price had reached 54.77 on April 6, a gain of 4.77 per share. The stop did its job: it kept the loss to the planned US$170. Whether to take profit near the high is a question for the exit rules in Part 7. Part 3 shows how to choose the stop and the size together ([Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md)).

</div>

### Trendlines

A **trendline** is a straight line drawn through swing lows in an uptrend (or swing highs in a downtrend). It is a quick visual, but two people draw different lines through the same points, and the line changes each time a new swing point appears. The swing-point rule above is exact, so this book uses it for decisions and uses trendlines only for the picture.

## What tests found

Moskowitz, Ooi and Pedersen (2012) studied 58 liquid futures and forward contracts and found that an instrument's return over the past 1 to 12 months tended to continue in the next month, a pattern they call time-series momentum. It appeared in equity indexes, currencies, commodities and bonds, and it partly reversed over longer horizons ([Journal of Financial Economics, 104(2), 228-250](https://doi.org/10.1016/j.jfineco.2011.11.003)). This supports the broad idea that trends have tended to persist over months. It does not test the swing-point rule above, and it is an average over many markets, not a promise for one stock.

## Common mistakes

- Marking a swing point too soon. A swing high is not a swing high until the bars after it have confirmed it.
- Calling a trend from two points. Two swing highs and two swing lows are the minimum, and three each is better.
- Moving the invalidation level after the price breaks it. Write the level down before the trade.

## Try it

1\. A stock has swing highs of 20.00, 21.50 and 21.00, and swing lows of 18.00, 19.00 and 19.80. Is it an uptrend? What price ends the call?

<details class="solution" markdown>
<summary>Answer</summary>

The lows rise (18.00, 19.00, 19.80), but the last swing high (21.00) is below the one before (21.50), so the highs are no longer rising. It is an uptrend that is losing strength. The last swing low is 19.80, so a close below 19.80 ends the call.

</details>

2\. On the first chart, on what date does a close first fall below the last higher low of 48.43, and at what close?

<details class="solution" markdown>
<summary>Answer</summary>

April 15, 2026, at a close of 48.21.

</details>

3\. On the downtrend chart, how much lower is each swing high than the one before?

<details class="solution" markdown>
<summary>Answer</summary>

58.11 - 55.04 = 3.07, and 55.04 - 51.81 = 3.23.

</details>

4\. You buy 100 shares at US$50.00 with a stop at US$48.30. What is the loss if the stop fills at US$48.30, and what if a gap fills it at US$47.20?

<details class="solution" markdown>
<summary>Answer</summary>

At 48.30: (50.00 - 48.30) x 100 = US$170. At 47.20: (50.00 - 47.20) x 100 = US$280.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run a set of [chart drills](../practice/chart-drills.md) and mark the stop below the swing low where asked. |
| 5 | Open a daily chart and mark the last three swing highs and swing lows with the 5-bar rule. Write whether it is an uptrend, a downtrend or a range, and the invalidation level. |

</div>

## Key terms

- **Swing high**: a bar whose high is at least as high as the highs of the 5 bars on each side.
- **Swing low**: a bar whose low is at least as low as the lows of the 5 bars on each side.
- **Market structure**: the sequence of swing highs and swing lows.
- **Uptrend**: higher swing highs and higher swing lows.
- **Downtrend**: lower swing highs and lower swing lows.
- **Range**: swing points that stay in a band without a direction.
- **Invalidation level**: the price that ends the trend call, usually the last swing low in an uptrend.
- **Break of structure**: a close beyond the last swing point that ends the trend.
- **Trendline**: a straight line through swing lows or swing highs.

Next: [Support and resistance](03-support-and-resistance.md)
