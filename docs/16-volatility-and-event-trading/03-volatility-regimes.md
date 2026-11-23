# Volatility regimes

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">VOL</span>

After this lesson you can label the current market as a high-volatility regime or a normal one with a written rule, scale your risk down in a high-volatility regime, and say what tests found about managing risk by volatility.

Before this: [Realized and implied volatility](01-realized-vs-implied-volatility.md), [Volatility indicators: ATR, Bollinger and Keltner](../05-reading-charts/07-volatility-indicators.md), [Fixed fractional sizing](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md). You need: a calculator.

## The idea

Index X rises steadily for 70 trading days, from January 5 to April 10, 2026, with a 20-day realized volatility of 6.9% on the last day. Then it falls from 5,234.34 on April 13 to 4,138.13 on May 29, and the 20-day figure reaches 25.0%. Before the fall, volatility had already changed state, from calm to turbulent.

Volatility does not jump around at random from day to day. Large moves tend to follow large moves, and small ones follow small ones, a pattern called **volatility clustering**. A stretch with a persistent level of volatility is a **volatility regime**. If you know the regime, you know roughly how big tomorrow's range is, and you can size for it.

## How it works

### Why volatility clusters

Engle (1982) introduced the ARCH model, in which today's variance depends on the size of recent shocks ([Econometrica, 50(4)](https://doi.org/10.2307/1912773)). Bollerslev (1986) generalized it to GARCH, which adds yesterday's variance:

\[ \sigma_t^2 = \omega + \alpha\, \varepsilon_{t-1}^2 + \beta\, \sigma_{t-1}^2 \]

- \( \sigma_t^2 \) is today's variance forecast, a fraction squared per day.
- \( \varepsilon_{t-1}^2 \) is yesterday's squared surprise return, and \( \sigma_{t-1}^2 \) is yesterday's variance forecast.
- \( \omega \), \( \alpha \) and \( \beta \) are positive numbers fitted to the data. A large \( \beta \) means volatility fades slowly, which is the clustering ([Bollerslev, 1986](https://doi.org/10.1016/0304-4076(86)90063-1)).

You do not need to fit GARCH to use the idea. A rule built from realized volatility does the job.

### A simple regime rule

1. Each day, compute the 20-day realized volatility, annualized (lesson 1).
2. Take the median of those 20-day values over the previous 120 days (at least 30 days of history).
3. Divide today's value by that median. Call it the ratio.
4. A ratio above 1.5 is a high-volatility regime. Otherwise the regime is normal.

On Index X the ratio is 0.84 on April 10, so the regime is normal. On April 15 it is 1.63 (13.3% against a median of 8.2%), and the rule flags a high-volatility regime. The flag stays on for 53 trading days, through June 26, and is off from June 29. The chart marks the flag and the stretch, with the ATR panel below.

```chart
data: 16-volatility-and-event-trading/index-x-regimes.json
title: Index X, daily: a calm regime and a turbulent one
show: atr 14
marker: 2026-04-15 | above | Rule flags high volatility
zone: 4050-5350 | 2026-04-15 to 2026-06-26 | High-volatility regime
range: 2026-02-02 to 2026-08-14
caption: ATR 14 is 39.4 on April 10 (0.75% of the close), 95.0 on May 8 (2.1%) and 114.1 on May 29 (2.8%).
```

The rule has a cost. It reacts after the first large moves, so it flags the regime a few days late. And because the baseline is a median of recent days, the ratio falls as a high-volatility stretch ages: on June 29 it is 1.35 and the flag is off, although 20-day volatility is still 18.0%, more than double its calm level. Rules built from lagged data behave this way.

### Scaling risk with the regime

There are two ways to use the label, and they stack.

First, size from volatility. A stop set from ATR (part 3, [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md)) widens when volatility rises, so the same dollar risk buys fewer shares. Second, cut the risk itself: this plan uses 1% of the account per trade in a normal regime and 0.5% in a high-volatility one. Both choices are rules in your plan, not tested standards.

<div class="example" markdown>

### Worked example: the same setup in two regimes

Stock A trades at US$60.00. The account is US$25,000. The stop is 2 x ATR below the entry, and the target is 2R above it.

Normal regime: ATR is 0.75% of the price, which is 0.45.

1. Stop distance = 2 x 0.45 = 0.90, so the stop is 59.10.
2. Risk = 1% of 25,000 = US$250. Shares = 250 / 0.90 = 277.8, so 277 shares (rounded down), risking US$249.30.
3. Target = 60.00 + 2 x 0.90 = 61.80.

High-volatility regime: ATR is 2.1% of the price, which is 1.26.

1. Stop distance = 2 x 1.26 = 2.52, so the stop is 57.48.
2. Risk = 0.5% of 25,000 = US$125. Shares = 125 / 2.52 = 49.6, so 49 shares, risking US$123.48.
3. Target = 60.00 + 2 x 2.52 = 65.04.

The position falls from 277 shares to 49, a cut of 82%, and the dollar risk is about half. The target is further away because the stock is expected to move more.

</div>

### Volatility targeting

A fund can go one step further and scale its whole exposure so its volatility stays near a target:

\[ w = \min\left(1,\ \frac{\sigma_{target}}{\sigma_{realized}}\right) \]

- \( w \) is the fraction of the normal position to hold, from 0 to 1 (no leverage in this version).
- \( \sigma_{target} \) is the volatility you aim for, such as 10% per year, and \( \sigma_{realized} \) is the recent realized volatility, in the same units.

At the turbulent stretch's 25.0%, \( w = 10 / 25 = 0.40 \). In the calm stretch's 7.6%, \( w = \min(1, 10/7.6) = 1 \).

## What tests found

Moreira and Muir (Journal of Finance, 2017) scaled factor portfolios by the inverse of the previous month's realized variance and found that the managed versions had higher Sharpe ratios and alphas than the unmanaged ones ([paper](https://doi.org/10.1111/jofi.12513)). Cederburg, O'Doherty, Wang and Yan (Journal of Financial Economics, 2020) revisited the evidence across 103 strategies. They confirmed the in-sample alphas but found weak results when the rule is applied in real time, and that volatility-managed portfolios do not systematically beat their unmanaged counterparts ([paper](https://econpapers.repec.org/RePEc:eee:jfinec:v:138:y:2020:i:1:p:95-117)).

So the evidence is mixed. Cutting size when volatility is high is a way to control the dollar risk you take. This book does not claim it raises returns.

## When it fails

A volatility regime rule is late, so it cuts after the drop and restores size after the rebound, and it can miss a quick recovery. It also says nothing about direction. And a low-volatility reading is not safety: quiet markets can turn in a day.

## In code

The same rule on [index-x-regimes.csv](../assets/data/index-x-regimes.csv).

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

b = pd.read_csv("index-x-regimes.csv", parse_dates=["date"])
r = np.log(b["close"]).diff()
rv = r.rolling(20).std() * np.sqrt(252) * 100
median = rv.shift(1).rolling(120, min_periods=30).median()
ratio = rv / median
high = ratio > 1.5

days = b.loc[high, "date"]
print(days.iloc[0].date(), days.iloc[-1].date(), int(high.sum()))
print(round(ratio.iloc[69], 2), round(ratio.iloc[72], 2))
```

</details>

## Common mistakes

- Cutting size by feel after a bad day. Write the rule and apply it the same way every time.
- Keeping the same share count when volatility doubles. The dollar risk doubles with it.
- Reading a calm regime as a reason to take more risk than your plan allows.

## Try it

1\. Realized volatility is 25% and your target is 10%. What fraction of the normal position do you hold?

<details class="solution" markdown>
<summary>Answer</summary>

w = 10 / 25 = 0.40, so 40% of the normal position.

</details>

2\. On April 15, 20-day realized volatility is 13.3% and the median of the previous 120 days (at least 30) is 8.2%. What is the ratio, and which regime is it?

<details class="solution" markdown>
<summary>Answer</summary>

13.33 / 8.20 = 1.63, which is above 1.5, so a high-volatility regime.

</details>

3\. Stock B trades at US$40.00 with an ATR of 0.80, in a high-volatility regime. The stop is 2 x ATR below the entry and risk is 0.5% of a US$25,000 account. How many shares?

<details class="solution" markdown>
<summary>Answer</summary>

Stop distance = 1.60. Risk = US$125. Shares = 125 / 1.60 = 78.1, so 78 shares.

</details>

4\. Why did the ratio fall to 1.35 on June 29 while 20-day volatility stayed at 18.0%?

<details class="solution" markdown>
<summary>Answer</summary>

The baseline is the median of the previous 120 days of 20-day volatility. As turbulent days enter it, the median rises (from 11.93 on June 26 to 13.33 on June 29), and the ratio shrinks even though the current level is almost unchanged: 17.97 / 13.33 = 1.35.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the code above and change the 1.5 threshold to 1.3 and 2.0. Write how many days are flagged each time. |
| 3 | Open [chart drills](../practice/chart-drills.md) and answer the regime items. |
| 2 | Write your own risk rule for a high-volatility regime in one sentence, with the percentage. |

</div>

## Key terms

- **Volatility clustering**: the tendency of large moves to follow large moves and small ones to follow small ones.
- **Volatility regime**: a stretch of time with a persistent level of volatility.
- **GARCH**: a model in which today's variance depends on yesterday's squared return and yesterday's variance.
- **Volatility targeting**: scaling exposure by the ratio of a target volatility to recent realized volatility.

Next: [Earnings trades and IV crush](04-earnings-trades-and-iv-crush.md)
