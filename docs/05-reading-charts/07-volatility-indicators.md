# Volatility indicators: ATR, Bollinger and Keltner

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can compute the average true range and Bollinger Bands, read a squeeze on a chart, and use ATR to size a stop.

Before this: [Moving averages](05-moving-averages.md). You need: a calculator.

## The idea

Stock A trades inside a band about US$1.20 wide for seven weeks, then rises US$3.53 in five days (the close of 50.97 on April 3 to 54.50 on April 10). The direction was not on the chart, but the quiet before the move was. **Volatility** is how far a price moves in a given time. It is the size of the swings, not their direction.

Volatility indicators put a number on that size. They answer two practical questions: how far should my stop be from the entry, and is the market quiet or active now? Part 3 gave ATR a short first definition ([Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md)), and this lesson gives the full formula. The math background is the [standard deviation](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/01-descriptive-statistics-and-study-design/).

## How it works

### True range and ATR

A bar's high minus low misses gaps. The **true range** (TR) of a bar is the largest of three numbers:

\[ TR = \max\big(H - L,\ |H - C_{prev}|,\ |L - C_{prev}|\big) \]

- \(H\) and \(L\) are the bar's high and low, and \(C_{prev}\) is the previous close, all in US$.
- The last two terms capture a gap: the move from yesterday's close to today's extremes.

The figure shows a bar that opens 5% above the previous close.

![A gap-up bar: the high minus the low is 1.59, but the true range from the previous close to the high is 3.85](../assets/figures/05-reading-charts/true-range-dark.svg#only-dark)
![A gap-up bar: the high minus the low is 1.59, but the true range from the previous close to the high is 3.85](../assets/figures/05-reading-charts/true-range-light.svg#only-light)

On February 24 the high is 55.19, the low is 53.60 and the previous close is 51.34. The three candidates are 1.59, 3.85 and 2.26, so TR = 3.85.

The **average true range** (ATR), from J. Welles Wilder, is a smoothed average of TR over \(N\) bars (14 is the usual). The first ATR is the plain average of the first 14 TR values. After that, Wilder smoothing applies:

\[ ATR_t = \frac{(N-1)\,ATR_{t-1} + TR_t}{N} \]

- \(ATR_t\) is today's ATR and \(ATR_{t-1}\) is yesterday's, in US$ per share.
- \(TR_t\) is today's true range in US$. \(N\) is 14.

<div class="example" markdown>

### Worked example: ATR update and an ATR stop

In the chart below, the ATR 14 on April 3, 2026 is US$0.349 (0.68% of the 50.97 close). On April 6 the bar has high 51.92, low 50.85 and the previous close was 50.97.

1. TR = max(1.07, 0.95, 0.12) = 1.07.
2. ATR = (13 x 0.349 + 1.07) / 14 = 5.607 / 14 = 0.40.

One wide bar lifts ATR from 0.349 to 0.40. A common way to set a stop is a multiple of ATR below the entry. With an entry of US$51.75 and a stop of 2 x ATR below, the stop is 51.75 - 2 x 0.40 = US$50.95, a risk of US$0.80 per share. With a US$250 risk budget, the size is 250 / 0.80 = 312.5, so 312 shares.

</div>

### Bollinger bands and Keltner channels

**Bollinger Bands**, from John Bollinger, wrap the price in a band whose width follows its recent spread:

\[ \text{Middle} = \text{SMA}_{20}, \qquad \text{Upper} = \text{Middle} + 2\sigma, \qquad \text{Lower} = \text{Middle} - 2\sigma \]

- \(\sigma\) is the standard deviation of the last 20 closes (the population version, dividing by 20), in US$.
- \(2\) is the usual multiplier. A larger multiplier widens the bands.

On April 3 the 20 closes have a mean of 50.57 and \(\sigma\) = 0.231, so the bands are 50.57 plus or minus 0.46, or 50.11 and 51.03. **Bandwidth** = (upper - lower) / middle = 0.92 / 50.57 = 1.8%. On February 13 it was 7.9%.

**Keltner Channels** use the same idea with ATR instead of the standard deviation: the middle is the EMA 20, and the bands are the EMA plus and minus 1.5 times ATR (here the ATR uses 20 bars, the same length as the EMA).

A **squeeze** is a stretch where the Bollinger Bands sit inside the Keltner Channel: the closes are quieter than the true ranges. Here it runs from March 12 to April 3. Look at the bands narrowing, then spreading when the price breaks out.

```chart
data: 05-reading-charts/squeeze.json
title: Stock A, daily: a squeeze and then expansion
show: bb 20 2, keltner 20 1.5
marker: 2026-04-06 | below | Close above the upper band
range: 2026-02-02 to 2026-05-12
caption: Bollinger Bands inside the Keltner Channel from March 12 to April 3, then a close at 51.75 above the upper band on April 6.
```

On April 3 the Bollinger Bands are 50.11 to 51.03 and the Keltner Channel is 49.99 to 51.31. On April 6 the close is 51.75, above the upper band at 51.32. Bandwidth rises from 1.8% to 11.7% by April 13.

The ATR panel shows the same story in dollars.

```chart
data: 05-reading-charts/squeeze.json
title: Stock A, daily: ATR 14
show: atr 14
range: 2026-02-02 to 2026-05-12
caption: ATR 14 is 1.21 on February 13, 0.349 on April 3 and 1.078 on May 11.
```

<div class="warning" markdown>

A squeeze says the market is quiet. It does not say which way the break will go, or that a break is coming. Volatility clusters: large moves tend to follow large moves and small ones follow small ones, so a quiet period can last. Wait for the break and let the direction come from price.

</div>

## What tests found

Lento, Gradojevic and Wright (2007) tested Bollinger Band trading rules and found that, after transaction costs, the rules did not consistently earn more than buy and hold; a contrarian version did better ([Applied Financial Economics Letters, 3(4), 263-267](https://doi.org/10.1080/17446540701206576)). Engle (1982) introduced the ARCH model, in which the variance of a series depends on the size of its recent shocks. He fitted it to United Kingdom inflation, and the same clustering of large and small moves has since been found in asset returns ([Econometrica, 50(4), 987-1007](https://doi.org/10.2307/1912773)). Clustering is why a recent measure of size, such as ATR or bandwidth, is a useful guide to near-term risk. This book knows of no peer-reviewed test of the squeeze as an entry signal, so it makes no claim about one.

## In code

ATR with Wilder smoothing and Bollinger Bands on the squeeze chart's data, [stock-a-squeeze-daily.csv](../assets/data/stock-a-squeeze-daily.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

b = pd.read_csv("stock-a-squeeze-daily.csv", parse_dates=["date"], index_col="date")
prev = b["close"].shift(1)
tr = pd.concat([b["high"] - b["low"], (b["high"] - prev).abs(), (b["low"] - prev).abs()], axis=1).max(axis=1)
tr.iloc[0] = b["high"].iloc[0] - b["low"].iloc[0]

atr = pd.Series(float("nan"), index=b.index)
atr.iloc[13] = tr.iloc[:14].mean()
for i in range(14, len(b)):
    atr.iloc[i] = (atr.iloc[i - 1] * 13 + tr.iloc[i]) / 14

mid = b["close"].rolling(20).mean()
sd = b["close"].rolling(20).std(ddof=0)
day = "2026-04-03"
print(day, round(atr[day], 3), round(mid[day], 2), round(mid[day] - 2 * sd[day], 2), round(mid[day] + 2 * sd[day], 2))
```

It prints 2026-04-03 0.349 50.57 50.11 51.03.

</details>

## Common mistakes

- Setting a stop inside the normal noise. If ATR is 0.40 and the stop is 0.30 from the entry, ordinary movement can hit it.
- Reading a band touch as a reversal. In a strong trend the price walks along the upper band.
- Mixing up the two standard deviations. The bands here divide by 20; pandas divides by 19 unless you set `ddof=0`.

## Try it

1\. A bar has high 25.40, low 24.80, and the previous close was 24.10. What is TR?

<details class="solution" markdown>
<summary>Answer</summary>

H - L = 0.60. |H - C_prev| = 1.30. |L - C_prev| = 0.70. TR = 1.30.

</details>

2\. ATR is 0.80 yesterday and today's TR is 1.52. What is today's ATR with N = 14?

<details class="solution" markdown>
<summary>Answer</summary>

(13 x 0.80 + 1.52) / 14 = 11.92 / 14 = 0.851.

</details>

3\. A stock at US$40.00 has ATR 0.90. You use a stop of 2.5 x ATR below the entry and risk US$300. How many shares?

<details class="solution" markdown>
<summary>Answer</summary>

Stop distance = 2.5 x 0.90 = 2.25, so the stop is at 37.75. Shares = 300 / 2.25 = 133.3, so 133 shares.

</details>

4\. The 20 closes have a mean of 80.00 and a standard deviation of 1.25. What are the Bollinger Bands and the bandwidth?

<details class="solution" markdown>
<summary>Answer</summary>

Upper = 80 + 2 x 1.25 = 82.50. Lower = 77.50. Bandwidth = 5.00 / 80.00 = 6.25%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Run a set of [chart drills](../practice/chart-drills.md) with ATR questions. Compute each answer before checking. |
| 4 | Add ATR 14 and Bollinger Bands to a daily chart you follow. Write today's ATR as a percentage of the price. |
| 2 | In your [trade journal](../practice/trade-journal.md), note the stop distance of your last trade as a multiple of ATR. |

</div>

## Key terms

- **Volatility**: how far a price moves in a given time, without regard to direction.
- **True range (TR)**: the largest of high minus low, and the gaps from the previous close to the high and the low.
- **Average true range (ATR)**: a Wilder-smoothed average of TR over N bars.
- **Bollinger Bands**: the 20-bar SMA plus and minus 2 standard deviations of the closes.
- **Bandwidth**: the distance between the upper and lower band divided by the middle band.
- **Keltner Channel**: the EMA 20 plus and minus 1.5 times ATR.
- **Squeeze**: a stretch where the Bollinger Bands sit inside the Keltner Channel.

Next: [VWAP and anchored VWAP](08-vwap-and-anchored-vwap.md)
