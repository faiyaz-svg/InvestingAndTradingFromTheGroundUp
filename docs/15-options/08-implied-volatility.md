# Implied volatility

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">OPT</span>

After this lesson you can solve for implied volatility from an option's price, turn it into an expected move, and explain the volatility skew you see on a chain.

Before this: [What sets an option's price](04-what-sets-an-option-price.md), [Theta, vega and rho](07-theta-vega-and-rho.md). You need: a calculator or Python.

## The idea

In lesson 4, you put a volatility into Black-Scholes and got a price. The market works the other way. The price is on the screen, and the volatility is unknown. **Implied volatility (IV)** is the volatility that makes the model price equal the market price.

For the 50-strike call on the lesson 3 chain, the midpoint is 3.40, the stock is US$50.20, three months are left, and the rate is 4%. We ask: which \(\sigma\) gives a Black-Scholes price of 3.40? The answer is 30.6%.

IV is the option's price written in a different unit. A trader who says "the option is at 30 vol" is quoting the price the way a bond trader quotes a yield instead of a dollar price. It lets you compare options with different strikes and expiries, which dollar prices do not.

## How to solve for it

There is no formula for \(\sigma\) in terms of the price, so a program searches. The simple search is **bisection**.

1. Pick a low and a high volatility that bracket the answer, such as 10% and 60%.
2. Price the option at the midpoint of the two.
3. If the model price is above the market price, the volatility is too high, so the midpoint becomes the new high. If it is below, the midpoint becomes the new low.
4. Repeat until the range is narrower than you need.

This works because the price rises with volatility at every step (vega is positive). Each step halves the range.

<div class="example" markdown>

### Worked example: bisection on the 50-strike call

Target price 3.40 (the midpoint). \(S = 50.20\), \(K = 50\), \(T = 0.25\), \(r = 4\%\).

| Step | Volatility tried | Model price | Compare with 3.40 |
|---|---|---|---|
| 1 | 35.000% | 3.8358 | Too high |
| 2 | 22.500% | 2.6022 | Too low |
| 3 | 28.750% | 3.2187 | Too low |
| 4 | 31.875% | 3.5272 | Too high |
| 5 | 30.312% | 3.3729 | Too low |
| 6 | 31.094% | 3.4500 | Too high |
| 7 | 30.703% | 3.4115 | Too high |
| 8 | 30.508% | 3.3922 | Too low |

After 8 steps the answer sits between 30.5% and 30.7%. Run it to a tight tolerance and the result is 30.59%, which the chain shows as 30.6%. The 50-strike put, at its 2.70 midpoint, gives 30.56%, within 0.03 points of the call, as put-call parity predicts (lesson 5).

</div>

## Reading IV

IV is stated as a percentage per year, and it is the market's pricing of how much the stock will move. Take the base 30.6% and three months. The expected one-standard-deviation move over the life of the option is

\[ \text{expected move} \approx S \times \text{IV} \times \sqrt{T} \]

- \(S\) is the stock price in US$ and IV is a decimal per year.
- \(T\) is the years to expiry. The \(\sqrt{T}\) is there because volatility grows with the square root of time (math book lesson on the [normal distribution](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/04-continuous-random-variables-and-the-normal/)).

For Stock A: 50.20 x 0.3059 x 0.5 = US$7.68, which is 15.3% of the price. In the model, the stock ends within about US$7.68 of today's price on roughly two out of three outcomes. To get a daily figure, divide the yearly IV by \(\sqrt{252}\), the square root of the number of trading days in a year: 30% becomes 0.30 / 15.87 = 1.9% a day, or US$0.94 on a US$50 stock.

IV is not a forecast of what the stock will do. It is what the market charges for the possibility. It is also not constant across a chain.

## The smile and the skew

Black-Scholes says one \(\sigma\) should work for every strike of the same expiry. The market disagrees. Plot IV against strike for the chain in lesson 3.

![Implied volatility against strike for Stock A, calls and puts, same expiry](../assets/figures/15-options/iv-skew-dark.svg#only-dark)
![Implied volatility against strike for Stock A, calls and puts, same expiry](../assets/figures/15-options/iv-skew-light.svg#only-light)

IV is highest for the low strikes (36.1% at 45) and falls toward the high strikes (28.6% at 55). The calls and puts agree, which parity requires. This slope is the **volatility skew**. When both ends of the curve rise above the middle, it is a **volatility smile**. Equity options usually show a skew: puts below the stock cost more, in vol terms, than calls above it. Index options show it strongly. Common explanations are that investors pay for protection against falls, and that stocks tend to fall faster than they rise. The explanations are debated, but the shape is a regular feature of stock and index options, which Black-Scholes alone does not produce.

The skew also means the "right" volatility for your trade depends on the strike. An out-of-the-money put is priced at a higher IV than an at-the-money call, and that gap is itself something you can buy or sell. IV also differs by expiry. Part 16 covers how IV moves across expiries and over time (Realized and implied volatility<!-- link: ../16-volatility-and-event-trading/01-realized-vs-implied-volatility.md -->).

A caution on the numbers: the broker's IV for an American option comes from a model that allows early exercise, and with dividends it makes more assumptions. The Black-Scholes IV above is a close approximation for a stock with no dividend and options not deep in the money. Do not expect to match a broker's screen to the last decimal.

## IV and realized volatility

**Realized volatility** is how much the stock actually moved: the standard deviation of its daily returns, scaled to a year. IV is forward looking, and realized volatility looks back. When IV is higher than the volatility that follows, a seller of options profits on average, and when it is lower, a buyer does. Whether and when that holds is an empirical question, and part 16 covers it, with the sources.

## In code

Stock A's 83-day sample, [stock-a-daily.csv](../assets/data/stock-a-daily.csv), gives a realized volatility to hold against an IV. It comes from a different made-up stock than the chain, so the gap shows the method, not a trade.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import numpy as np
import pandas as pd

def N(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def call(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
    return S * N(d1) - K * math.exp(-r * T) * N(d1 - sigma * math.sqrt(T))

def implied_vol(price, S, K, T, r, lo=0.01, hi=3.0):
    for _ in range(100):
        mid = (lo + hi) / 2
        if call(S, K, T, r, mid) < price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

iv = implied_vol(3.40, 50.20, 50, 0.25, 0.04)
print(round(iv * 100, 2))

bars = pd.read_csv("stock-a-daily.csv")
returns = np.log(bars["close"]).diff().dropna()
print(len(bars), round(returns.std() * math.sqrt(252) * 100, 2))
```

</details>

## Common mistakes

- Reading IV as a forecast. It is the market's price for movement, and the stock can move more or less.
- Comparing IV across expiries without care. A one-week and a three-month IV answer different questions.
- Quoting a daily move with the yearly IV. Divide by \(\sqrt{252}\) for one day.

## Try it

1\. Stock A is US$100 with an IV of 40% and three months left. What is the one-standard-deviation expected move?

<details class="solution" markdown>
<summary>Answer</summary>

100 x 0.40 x \(\sqrt{0.25}\) = 100 x 0.40 x 0.5 = US$20, which is 20% of the price.

</details>

2\. An IV of 30% is quoted. How big is a typical daily move on a US$50 stock?

<details class="solution" markdown>
<summary>Answer</summary>

0.30 / \(\sqrt{252}\) = 0.30 / 15.875 = 1.89% a day, which is 50 x 0.0189 = US$0.94.

</details>

3\. In the bisection example, at 35% the model price is 3.8358 against a market 3.40. Which way does the next guess go?

<details class="solution" markdown>
<summary>Answer</summary>

The model price is too high, so 35% is too high. The new range is 10% to 35% and the next guess is 22.5%.

</details>

4\. On the chain, the 45-strike put has an IV of 36.1% and the 55-strike call has 28.6%. What does the difference say?

<details class="solution" markdown>
<summary>Answer</summary>

The market charges more, in volatility terms, for the out-of-the-money put than for the out-of-the-money call. That is the skew: IV falls as the strike rises. The gap is 36.1 - 28.6 = 7.5 volatility points.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On your broker's chain for one stock, write the IV for five strikes of one expiry and sketch the shape. |
| 3 | Compute the expected move to that expiry for the at-the-money option: \(S \times \text{IV} \times \sqrt{T}\). |
| 3 | Run the code with that call's mid price and compare your IV with the broker's. Note the gap. |

</div>

## Key terms

- **Implied volatility (IV)**: the volatility that makes the model price equal the market price.
- **Bisection**: a search that halves a range containing the answer at each step.
- **Expected move**: the one-standard-deviation price change implied by IV, \(S \times \text{IV} \times \sqrt{T}\).
- **Volatility skew**: IV that changes steadily with the strike, usually higher for lower strikes.
- **Volatility smile**: IV that is higher at both low and high strikes than in the middle.
- **Realized volatility**: the annualized standard deviation of a stock's actual returns.

Next: [Covered calls and cash-secured puts](09-covered-calls-and-cash-secured-puts.md)
