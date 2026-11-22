# Momentum indicators: RSI, MACD and stochastics

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">CHRT</span>

After this lesson you can compute RSI, MACD and the stochastic oscillator from price bars, read a divergence on a chart, and say what tests found about these indicators.

Before this: [Moving averages](05-moving-averages.md). You need: a calculator.

## The idea

Two rises can look alike on a price chart and differ in strength. In one, nearly every day closes higher. In the other, up days barely outnumber down days. A **momentum indicator** measures how strong the recent move has been, in a number on a fixed scale, and shows it in a panel under the price. This lesson covers three. Each is built only from past prices, so each lags the price.

## How it works

### RSI

The **relative strength index** (RSI), from J. Welles Wilder, compares the average size of up closes with the average size of down closes over \(N\) bars (14 is the usual length):

\[ \text{RSI} = 100 - \frac{100}{1 + RS}, \qquad RS = \frac{\text{average gain}}{\text{average loss}} \]

- A gain is a close above the previous close, measured in US$; a loss is the size of a close below it. A bar with no change has both at zero.
- The first averages are the plain averages of the first 14 gains and 14 losses. After that, Wilder smoothing updates them: new average = (13 x previous average + today's value) / 14.
- RSI runs from 0 to 100. Traders often mark 70 and 30 as "overbought" and "oversold", which describes recent strength and is not a signal by itself.

<div class="example" markdown>

### Worked example: RSI at bars 15 and 16

In a made-up stock the first 15 closes are 100.61, 102.58, 100.00, 99.23, 100.89, 100.76, 100.43, 100.24, 99.22, 98.27, 100.05, 102.04, 102.56, 106.16 and 104.58, and the 16th is 106.33.

1. The 14 changes from bar 2 to bar 15 have gains totalling 11.52 and losses totalling 7.55.
2. Average gain = 11.52 / 14 = 0.8229. Average loss = 7.55 / 14 = 0.5393.
3. RS = 0.8229 / 0.5393 = 1.526, so RSI = 100 - 100 / 2.526 = 60.4.
4. Bar 16 rises by 106.33 - 104.58 = 1.75. Average gain = (13 x 0.8229 + 1.75) / 14 = 0.8891. Average loss = (13 x 0.5393 + 0) / 14 = 0.5008.
5. RS = 1.775, RSI = 100 - 100 / 2.775 = 64.0.

</div>

The chart plants a **divergence**: the price makes a higher high while the indicator makes a lower high. Look at the two marked highs and the RSI under each.

```chart
data: 05-reading-charts/rsi-divergence.json
title: Stock A, daily: a higher high with a lower RSI
show: rsi 14
marker: 2026-02-13 | above | High 130.27, RSI 85
marker: 2026-03-16 | above | High 134.88, RSI 62
caption: The price rises 3.5% from the first high to the second, while RSI falls from 85 to 62.
```

On February 13 the high is 130.27 and RSI is 85.2. On March 16 the high is 134.88, 3.5% higher, and RSI is 61.6. The second push was weaker. The price closes at 114.00 on April 7, 15.5% below the March high. Divergences also fail: a rise can stay weak and keep going, so one is a reason to tighten a stop, not a reason to sell on its own.

### MACD

The **moving average convergence divergence** (MACD), from Gerald Appel, uses two EMAs (lesson 5: [Moving averages](05-moving-averages.md)):

\[ \text{MACD} = \text{EMA}_{12} - \text{EMA}_{26}, \quad \text{Signal} = \text{EMA}_9(\text{MACD}), \quad \text{Histogram} = \text{MACD} - \text{Signal} \]

- \(\text{EMA}_{12}\) and \(\text{EMA}_{26}\) are the 12- and 26-bar EMAs of the close, in US$. MACD is their gap, in US$: positive when the faster average is above the slower one.
- The signal line is a 9-bar EMA of the MACD line. The histogram is the gap between the two, and it crosses zero when MACD crosses the signal line.

On February 13 in the chart above the EMA 12 is 122.36 and the EMA 26 is 113.21, so MACD = 9.15. On March 16 MACD is 3.98 and the signal line is 4.13, a histogram of -0.15: MACD is below its signal line as the price makes its high.

Here MACD on the moving-average chart of lesson 5. Look at the crossings around December.

```chart
data: 05-reading-charts/ma-cross.json
title: Stock A, daily: MACD 12, 26, 9
show: macd 12 26 9
range: 2025-11-17 to 2026-03-13
marker: 2025-12-10 | below | Up
marker: 2025-12-11 | above | Down
marker: 2025-12-12 | below | Up
caption: In a range, MACD crossed its signal line three days in a row, December 10 to 12.
```

MACD crosses its signal line up on December 10, down on December 11 and up again on December 12, the same whipsaw problem as in lesson 5. In the trend that follows, crossings come every few weeks.

### Stochastic oscillator

The **stochastic oscillator** says where the close sits in the recent high-low range:

\[ \text{raw } \%K = 100 \times \frac{C - LL_{14}}{HH_{14} - LL_{14}} \]

- \(C\) is the close. \(HH_{14}\) and \(LL_{14}\) are the highest high and lowest low of the last 14 bars, in US$.
- The slow version used in this book smooths raw %K with a 3-bar SMA to get %K, and %D is a 3-bar SMA of %K. Readings above 80 and below 20 are the usual marks.

On March 6, 2026 in the range of lesson 3, the close is 101.86, the 14-bar high is 107.77 and the 14-bar low is 100.53, so raw %K = (101.86 - 100.53) / 7.24 x 100 = 18.4. The close sits in the bottom fifth of the range, next to support.

```chart
data: 05-reading-charts/range-sr.json
title: Stock A, daily: stochastic 14, 3, 3 in a range
show: stoch 14 3 3
range: 2026-01-05 to 2026-03-20
caption: The stochastic swings between low and high readings as the price moves between support and resistance.
```

## What tests found

Chong and Ng (2008) tested MACD and RSI rules on 60 years of the London FT30 index and reported that the rules beat buy and hold in most cases ([Applied Economics Letters, 15(14), 1111-1114](https://doi.org/10.1080/13504850600993598)). Park and Irwin's review of 95 modern studies counts 56 positive, 20 negative and 19 mixed results for technical strategies, with profits through the early 1990s and with problems such as data snooping ([Journal of Economic Surveys, 21(4), 786-826](https://doi.org/10.1111/j.1467-6419.2007.00519.x)). Data snooping is explained in lesson 5.

This book knows of no widely cited peer-reviewed test of the stochastic oscillator, or of RSI and MACD divergences, so it makes no claim about them.

RSI and the stochastic oscillator are mostly used in ranges, where reversals are common. In a strong trend they stay "overbought" for weeks: in the chart above RSI stayed above 70 for 15 trading days, January 28 to February 17, while the price rose to its high on February 13.

## Common mistakes

- Selling because RSI is above 70. In a strong trend it can stay there.
- Using the default settings without testing the length. A shorter length reacts faster and signals more often, with more false signals.
- Trading every MACD cross. In a range the crosses come in pairs that lose money.

## Try it

1\. Over 14 bars the average gain is 0.60 and the average loss is 0.40. What is RSI?

<details class="solution" markdown>
<summary>Answer</summary>

RS = 0.60 / 0.40 = 1.5. RSI = 100 - 100 / 2.5 = 60.

</details>

2\. The next bar rises 1.40. Update both averages with Wilder smoothing and give the new RSI.

<details class="solution" markdown>
<summary>Answer</summary>

Average gain = (13 x 0.60 + 1.40) / 14 = 0.6571. Average loss = (13 x 0.40 + 0) / 14 = 0.3714. RS = 1.769, RSI = 100 - 100 / 2.769 = 63.9.

</details>

3\. The EMA 12 is 55.20 and the EMA 26 is 54.10. The signal line is 0.90. What are MACD and the histogram?

<details class="solution" markdown>
<summary>Answer</summary>

MACD = 55.20 - 54.10 = 1.10. Histogram = 1.10 - 0.90 = 0.20. MACD is above its signal line.

</details>

4\. A close of 49.50 with a 14-bar high of 52.00 and low of 48.00. What is raw %K?

<details class="solution" markdown>
<summary>Answer</summary>

100 x (49.50 - 48.00) / (52.00 - 48.00) = 100 x 1.50 / 4.00 = 37.5.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Run a set of [chart drills](../practice/chart-drills.md) and say whether each chart shows a divergence. |
| 4 | Open a daily chart you follow with RSI 14. Mark the last two swing highs and write the RSI at each. Is there a divergence? |
| 2 | Write one line in your [trade journal](../practice/trade-journal.md) on what you would do if you saw one in a trade you hold. |

</div>

## Key terms

- **Momentum indicator**: a number built from past prices that shows how strong a recent move has been.
- **Relative strength index (RSI)**: 100 minus 100 / (1 + RS), where RS is the average gain divided by the average loss over N bars.
- **Wilder smoothing**: an average updated as (previous x (N - 1) + new value) / N.
- **Divergence**: the price makes a new high or low while the indicator does not.
- **MACD**: the 12-bar EMA minus the 26-bar EMA of the close.
- **Signal line**: a 9-bar EMA of MACD.
- **Histogram**: MACD minus the signal line.
- **Stochastic oscillator**: where the close sits in the last N bars' high-low range, 0 to 100.
- **Overbought and oversold**: RSI above 70 or below 30 (stochastic above 80 or below 20).

Next: [Volatility indicators: ATR, Bollinger and Keltner](07-volatility-indicators.md)
