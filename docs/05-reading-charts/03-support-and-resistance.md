# Support and resistance

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can mark support and resistance zones from swing points, say when a level has broken, and place a trade and a stop around a level with the risk worked out.

Before this: [Trend and market structure](02-trend-and-market-structure.md). You need: a calculator.

## The idea

Stock A trades between about US$100 and US$108 for two months. Each time it falls to about US$100.50, buyers appear and it rises. Each time it rises to about US$107.50, sellers appear and it falls. Those two prices act like a floor and a ceiling.

**Support** is a price area where buying has repeatedly stopped a fall. **Resistance** is a price area where selling has repeatedly stopped a rise. Both come from swing lows and swing highs ([Trend and market structure](02-trend-and-market-structure.md)) that land at about the same price.

Why would a price remember? Three reasons are common. Traders who bought near a level and watched it fall back may sell when it returns, to get out even. Traders who missed a move may place orders at the level they wish they had bought. And many traders watch the same obvious levels, so their orders pile up there. None of these is certain, which is why a level is a zone and not an exact price.

## How it works

1. Mark the swing highs and swing lows from lesson 2.
2. Look for two or more swing points within a narrow band, say within 0.5% of each other.
3. Draw a zone from the lowest to the highest of those points. A zone of 107.28 to 107.77 is more honest than a line at 107.50.
4. Count the touches. A zone with three touches has more history than one with two.
5. Decide what counts as a break: a close beyond the zone. A wick through it is not enough. A bar that trades above resistance and closes back inside has not broken it.

The chart shows Stock A in a range. Look at the three swing highs near the top and the three swing lows near the bottom.

```chart
data: 05-reading-charts/range-sr.json
title: Stock A, daily: a range, a breakout and a retest
zone: 107.28-107.77 | Resistance zone
zone: 100.22-100.79 | Support zone
marker: 2026-03-18 | below | First close above 107.77
marker: 2026-04-07 | below | Retest holds
show: volume
caption: Three swing highs in 107.28 to 107.77, three swing lows in 100.22 to 100.79, and then a break.
```

The swing highs are 107.28 (January 12), 107.28 (February 4) and 107.77 (February 24). The swing lows are 100.22 (January 22), 100.79 (February 12) and 100.53 (March 6). The resistance zone is 107.28 to 107.77, 0.49 wide. The support zone is 100.22 to 100.79, 0.57 wide.

On March 18 the close is 108.09, above the top of the resistance zone, on volume of 3,247,200 shares. By March 23 the high is 111.83. Then the price returns. On April 7 the low is 107.16 and the close is 107.98, back above the old resistance zone. The old resistance has become support. This is called **role reversal**: a broken resistance zone often acts as support when the price comes back to it, and a broken support zone as resistance.

<div class="example" markdown>

### Worked example: buying the retest

The retest on April 7 closes at 107.98. You buy at US$107.98 with a stop at US$106.90, below the retest low of 107.16. You aim at the March 23 high of 111.83. Your account is US$25,000 and you risk 1% per trade.

1. Risk per share = 107.98 - 106.90 = US$1.08.
2. Dollars at risk = 1% x 25,000 = US$250.
3. Shares = 250 / 1.08 = 231.5, so 231 shares (round down).
4. Reward per share = 111.83 - 107.98 = US$3.85.
5. Reward to risk = 3.85 / 1.08 = 3.6, so the target is 3.6R (see [R-multiples](../03-risk-and-position-sizing/02-r-multiples.md)).

In the chart's data, the price closed at 113.50 on April 14, past the target. A retest can also fail, and then the stop at 106.90 takes a loss of 231 x 1.08 = US$249.48, about 1R. Position sizing from risk is in Part 3 ([Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md)).

</div>

## What tests found

Osler (2000) took the support and resistance levels that six foreign exchange firms supplied and found strong evidence that they helped predict pauses in intraday exchange-rate trends, though the power varied across currencies and firms ([Federal Reserve Bank of New York, Economic Policy Review 6(2), 53-68](https://www.newyorkfed.org/research/epr/00v06n2/0007osle.html)). Kavajecz and Odders-White (2004) found that support and resistance levels on NYSE stocks lined up with peaks of resting limit orders in the order book ([Review of Financial Studies, 17(4), 1043-1071](https://doi.org/10.1093/rfs/hhg057)). That fits the reasons above: orders do cluster at visible prices. Both papers are about the existence of the effect, not about a trading rule that pays after costs. Brock, Lakonishok and LeBaron (1992) tested a trading-range breakout rule on the Dow Jones index and found returns after buy signals above those after sell signals (lesson 5 gives the details: [Moving averages](05-moving-averages.md)).

Levels fail often. A zone that held three times can break on the fourth, and many breaks are false: the price closes beyond the zone and returns within days. Lesson 4 adds volume to help tell the two apart ([Volume and relative volume](04-volume-and-relative-volume.md)).

## Common mistakes

- Drawing a thin line and treating a wick through it as a break. Use a zone and a close.
- Drawing levels from the whole chart. Old levels from many months ago have weaker links to today's traders than levels from the last few months.
- Placing the stop exactly at the level. A stop right on the zone is where many other stops sit, and noise can trigger it. Put it past the zone, as 106.90 sits below 107.16.

## Try it

1\. Swing highs on a chart are 52.10, 52.45 and 52.30. Draw the resistance zone and give its width.

<details class="solution" markdown>
<summary>Answer</summary>

Lowest 52.10, highest 52.45. The zone is 52.10 to 52.45 and its width is 0.35.

</details>

2\. A bar opens at 51.90, trades up to 52.60 and closes at 52.20 against the zone in exercise 1. Has resistance broken?

<details class="solution" markdown>
<summary>Answer</summary>

The bar traded above the zone (52.60 is above 52.45), but the close of 52.20 is inside the zone. By the close rule, resistance has not broken.

</details>

3\. You buy 100 shares at US$107.98 with a stop at US$106.90 and a target of US$111.83. What is the loss at the stop, the gain at the target, and the reward to risk?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (107.98 - 106.90) x 100 = US$108. Gain = (111.83 - 107.98) x 100 = US$385. Reward to risk = 385 / 108 = 3.6.

</details>

4\. With a US$40,000 account risking 0.5% per trade, how many shares can you buy with the same entry and stop (107.98 and 106.90)?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = 0.5% x 40,000 = US$200. Shares = 200 / 1.08 = 185.2, so 185 shares.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run a set of [chart drills](../practice/chart-drills.md) and click each support and resistance level before you reveal it. |
| 5 | Open a daily chart you follow. Mark one support zone and one resistance zone from swing points, write the touches for each, and note what a close beyond each would mean. |

</div>

## Key terms

- **Support**: a price area where buying has repeatedly stopped a fall.
- **Resistance**: a price area where selling has repeatedly stopped a rise.
- **Zone**: a band of prices drawn around two or more swing points.
- **Touch**: a swing point that reaches a zone.
- **Break**: a close beyond a zone.
- **Role reversal**: a broken resistance zone turning into support, or a broken support zone into resistance.
- **Retest**: a return of price to a broken zone.

Next: [Volume and relative volume](04-volume-and-relative-volume.md)
