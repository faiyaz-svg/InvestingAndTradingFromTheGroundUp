# Realized and implied volatility

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">VOL</span>

After this lesson you can compute a stock's realized volatility from closing prices, annualize it, put it next to implied volatility, and say what the gap between them has meant for option sellers and buyers.

Before this: [Implied volatility](../15-options/08-implied-volatility.md), [Volatility indicators: ATR, Bollinger and Keltner](../05-reading-charts/07-volatility-indicators.md). For the standard deviation and the logarithm, see [descriptive statistics](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/01-descriptive-statistics-and-study-design/) and [logarithms](https://faiyaz-svg.github.io/MathFromTheGroundUp/03-high-school/07-exponentials-and-logarithms/02-logarithms/) in the math book. You need: a calculator.

## The idea

Stock A closes at US$50.00, 50.80, 50.10, 51.20, 50.60 and 51.40 on six days in a row. The daily moves are +1.6%, -1.4%, +2.2%, -1.2% and +1.6%. The stock went up US$1.40 over the week, but it swung up and down far more than that net change suggests. One number for the size of the swings is **realized volatility**: the standard deviation of the stock's returns over a past window, scaled to a year.

Part 15 gave the other side. **Implied volatility** (IV) is the volatility that makes an option model match the option's price ([Implied volatility](../15-options/08-implied-volatility.md)). Realized volatility looks back at what the stock did. IV looks forward and is what the market charges for what the stock might do. This lesson shows how to measure the first and how the two compare.

## How it works

### Close-to-close realized volatility

1. For each day, compute the log return from the previous close: \( r_t = \ln(C_t / C_{t-1}) \).
2. Take the sample standard deviation \( s \) of the returns in the window.
3. Multiply by \( \sqrt{252} \) to state it per year.

\[ \sigma_{realized} = s \times \sqrt{252} \]

- \( C_t \) is the close on day \( t \), in US$, and \( \ln \) is the natural logarithm. For small moves \( r_t \) is close to the percentage change.
- \( s \) is the standard deviation of the daily returns, a fraction per day (sample version, dividing by \( n - 1 \)).
- 252 is the usual count of trading days in a year. Volatility grows with the square root of time, so a daily figure times \( \sqrt{252} = 15.87 \) is the yearly figure. This is **annualizing**.
- The result is a fraction per year; 0.27 is "27% volatility".

This is **close-to-close** volatility because it uses only closing prices. It counts overnight gaps, such as an earnings gap, as part of a day's return. It misses moves inside the day that return to the previous close.

<div class="example" markdown>

### Worked example: six closes

1. Log returns: 0.01587, -0.01388, 0.02172, -0.01179, 0.01569.
2. Their mean is 0.00552, and the sample standard deviation is \( s = \) 0.016946, or 1.69% a day.
3. Annualized: 0.016946 x 15.8745 = 0.2690, so 26.9%.

Five returns are too few to trust. A 21-trading-day window, about one calendar month, is the usual choice because it matches the life of a front-month option.

</div>

### Realized against implied

Look at the figure. It shows a made-up stock over a year: the blue line is 21-day realized volatility, and the orange line is a made-up implied volatility, built to sit a little above what the stock then did. Both are in percent per year.

![Implied volatility and 21-day realized volatility of a made-up stock over 252 days](../assets/figures/16-volatility-and-event-trading/realized-vs-implied-dark.svg#only-dark)
![Implied volatility and 21-day realized volatility of a made-up stock over 252 days](../assets/figures/16-volatility-and-event-trading/realized-vs-implied-light.svg#only-light)

In this made-up year the implied line averages 30.8%, and the volatility the stock then realized over the next 21 days averages 26.2%. IV is above the later realized figure on 77% of the days. Realized volatility is above IV during the stress period in the middle, when the stock moved more than the market had priced. The figure shows how the comparison works. It is not a measurement of any real stock.

### The variance risk premium

The gap has a name. The **variance risk premium** is the difference between the variance the options market prices and the variance that is later realized. In volatility points, it is \( IV - \sigma_{realized} \). The 30.8% against 26.2% above is 4.6 points. In variance terms, it is \( 0.308^2 - 0.262^2 = 0.0262 \).

What tests found: Carr and Wu (Review of Financial Studies, 2009) studied variance swap rates, which are the market's price for future realized variance, and found that on stock indexes the rates sat on average above the variance later realized, so sellers of variance were paid for taking the risk. They found the premiums smaller in size for single stocks than for the indexes ([Carr and Wu, 2009](https://doi.org/10.1093/rfs/hhn038)). Bollerslev, Tauchen and Zhou (Review of Financial Studies, 2009) found that the difference between implied and realized variance for the S&P 500 explained part of the variation in the index's returns over the following quarter ([Bollerslev, Tauchen and Zhou, 2009](https://doi.org/10.1093/rfs/hhp008)).

Read those results modestly. They are about averages over past samples, on indexes, before trading costs, spreads and margin. The premium is compensation for risk: sellers pay out in the weeks when realized volatility jumps above IV, as in the middle of the figure. IV above realized on average does not make any one option a good sale.

## In code

The made-up Index X sample, [index-x-regimes.csv](../assets/data/index-x-regimes.csv), has a calm stretch and a turbulent one. This computes realized volatility for each.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

b = pd.read_csv("index-x-regimes.csv", parse_dates=["date"])
r = np.log(b["close"]).diff()

def ann(x):
    return x.dropna().std() * np.sqrt(252) * 100

print(round(ann(r), 1))
print(round(ann(r.iloc[0:70]), 1))
print(round(ann(r.iloc[70:105]), 1))
```

</details>

## Common mistakes

- Comparing windows that do not match. A 21-day realized figure answers a one-month question, and a one-week IV answers a one-week question.
- Using 365 or 360 instead of 252 in \( \sqrt{252} \). Returns exist only on trading days.
- Treating "IV above realized" as a sell signal. It is an average over many months, and the average hides the months when it flips.

## Try it

1\. The standard deviation of a stock's daily returns over 21 days is 1.2%. What is its annualized volatility?

<details class="solution" markdown>
<summary>Answer</summary>

0.012 x 15.8745 = 0.1905, so 19.0% per year.

</details>

2\. A stock's 30-day IV is 36% and its last 21 days realized 28%. What is the gap in volatility points, and in variance?

<details class="solution" markdown>
<summary>Answer</summary>

36 - 28 = 8 volatility points. In variance: 0.36 squared is 0.1296, 0.28 squared is 0.0784, and the difference is 0.0512.

</details>

3\. Stock B closes at US$80.00 and then US$82.00. What is the log return, and how does it compare with the percentage change?

<details class="solution" markdown>
<summary>Answer</summary>

ln(82 / 80) = ln(1.025) = 0.02469, so 2.47%. The percentage change is 2.50%. They are close for a small move.

</details>

4\. A 36% IV is quoted. What daily move does it imply, and what does 28% imply?

<details class="solution" markdown>
<summary>Answer</summary>

36 / 15.8745 = 2.27% a day. 28 / 15.8745 = 1.76% a day.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a stock you know. Find its 30-day implied volatility on your broker's chain or quote page and write it down. |
| 4 | Download 22 closing prices for it, compute the 21 log returns and the annualized realized volatility. |
| 2 | Write the gap in volatility points and one sentence on why it might be that size. |

</div>

## Key terms

- **Realized volatility**: the annualized standard deviation of a stock's actual returns over a past window.
- **Close-to-close volatility**: realized volatility computed from closing prices only.
- **Annualizing**: scaling a daily volatility to a year by multiplying by the square root of 252.
- **Variance risk premium**: the difference between the variance the options market prices and the variance later realized.

Next: [The VIX and the term structure](02-the-vix-and-term-structure.md)
