# Theta, vega and rho

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">OPT</span>

After this lesson you can say how much an option loses each day to time, how much it gains or loses when volatility changes, and when interest rates matter.

Before this: [Delta and gamma](06-delta-and-gamma.md). You need: a calculator.

## The idea

Delta and gamma describe what the stock does to an option. Three other things move an option's price while the stock sits still: the clock, the market's view of volatility, and interest rates. Each has a Greek.

All numbers below use the base case from lesson 4: Stock A at US$50, strike 50, three months left (\(T = 0.25\)), \(r = 4\%\), \(\sigma = 30\%\), no dividend. The Greeks are quoted per share, and one contract multiplies them by 100.

## Theta

**Theta** is the change in an option's price from one day passing, with everything else unchanged. It is negative for a long option: the option loses value as time runs out. For the base case, theta is -0.0189 per day for the call and -0.0135 for the put, which is a loss of US$1.89 and US$1.35 per contract per day.

Decay is not steady. The at-the-money call below loses little each day at first and much more near expiry.

| Days left | ATM call value | Theta per day (per contract) |
|---|---|---|
| 90 | 3.2060 | -US$1.90 |
| 60 | 2.5842 | -US$2.28 |
| 30 | 1.7956 | -US$3.12 |
| 14 | 1.2096 | -US$4.45 |
| 7 | 0.8476 | -US$6.19 |
| 1 | 0.3160 | -US$15.93 |

Time value shrinks roughly with the square root of the time left, so the last weeks lose the most. The left of the figure shows the curve: it steepens toward zero days.

![At-the-money call and put value against days left, and vega against stock price](../assets/figures/15-options/theta-vega-dark.svg#only-dark)
![At-the-money call and put value against days left, and vega against stock price](../assets/figures/15-options/theta-vega-light.svg#only-light)

Theta is the price of owning gamma. A long option pays theta every day and earns back from large moves (gamma, lesson 6). A short option collects theta and pays out when the stock moves hard. Neither side has an edge by itself: the model prices the decay so that it balances the expected benefit of moves of the size implied by the volatility. The edge, if any, comes from the stock moving more or less than that volatility, which is the topic of lesson 8 and part 16.

## Vega

**Vega** is the change in an option's price when volatility rises by one point (one percentage point, such as 30% to 31%).

\[ \mathcal{V} = \frac{S\, e^{-qT}\, n(d_1)\, \sqrt{T}}{100} \]

- \(\mathcal{V}\) is vega, in US$ per share per volatility point. A call and a put with the same strike and expiry have the same vega.
- \(n(d_1)\) is the normal density (the height of the bell curve) at \(d_1\) from lesson 4.
- \(S\), \(T\), \(q\) are the stock price, the years to expiry and the dividend yield. The 100 turns "per 1.00" into "per one point".

For the base case, vega is 0.0987 per share, or US$9.87 per contract. If volatility rises from 30% to 35% with nothing else changed, the call rises by 0.49 to 3.72, and so does the put, from 2.73 to 3.23.

Vega is largest at the money and for longer expiries. At the money, a contract with three months left has vega US$9.87, and one with about a month left (\(T = 0.08\)) has US$5.62. The right of the figure shows both humps. A far out-of-the-money option has little vega, because volatility changes little about how likely it is to pay.

<div class="example" markdown>

### Worked example: volatility falls and the stock does not move

Stock A is US$50. Earnings are due tomorrow. The market prices a 30-day, 50-strike call at a volatility of 60%. The call is 3.5040, or US$350.40.

1. Earnings come out and the stock closes at US$50, unchanged. The uncertainty is gone and volatility falls to 35%.
2. One day has passed, so 29 days are left. The call is now worth 2.0443.
3. The change is 2.0443 - 3.5040 = -1.4597, a loss of US$145.97 per contract, with the stock exactly where it was.

Most of that is vega (the volatility drop of 25 points) and a little is theta. Traders call this **IV crush**: implied volatility falls after a known event. Buying an option before the event means paying a high price for volatility and then watching it fall. Part 16 returns to it (Earnings trades and IV crush<!-- link: ../16-volatility-and-event-trading/04-earnings-trades-and-iv-crush.md -->).

</div>

## Rho

**Rho** is the change in an option's price when the interest rate rises by one percentage point. For the base case, rho is 0.0615 per share for the call, which is US$6.15 per contract, and -0.0623 for the put. A rate change of one point is a large one, and a three-month option barely reacts.

Rho matters for options with a long life. A call with two years left has a rho of 0.4529 per share, US$45.29 per contract for each percentage point. For most trades in this book you can ignore it.

Rates enter through the discounted strike, \(K e^{-rT}\). A higher rate lowers the present value of the strike you will pay, which helps a call and hurts a put (lesson 5).

## Greeks together

| Greek | Moves with | A long option | At its largest |
|---|---|---|---|
| Delta | The stock price | Call positive, put negative | Deep in the money |
| Gamma | The stock price, twice | Positive | At the money, near expiry |
| Theta | The days left | Negative | At the money, near expiry |
| Vega | Volatility | Positive | At the money, long expiry |
| Rho | The interest rate | Call positive, put negative | Long expiry |

A real position has all five at once. A broker's option page often shows them for a position as a total, which is the sum of each leg's Greek times its quantity and the 100 multiplier.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def N(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
def pdf(x): return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)

def call_price_and_greeks(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    price = S * N(d1) - K * math.exp(-r * T) * N(d2)
    theta = (-S * pdf(d1) * sigma / (2 * math.sqrt(T)) - r * K * math.exp(-r * T) * N(d2)) / 365
    vega = S * pdf(d1) * math.sqrt(T) / 100
    rho = K * T * math.exp(-r * T) * N(d2) / 100
    return price, theta, vega, rho

print([round(x, 4) for x in call_price_and_greeks(50, 50, 0.25, 0.04, 0.30)])
before = call_price_and_greeks(50, 50, 30 / 365, 0.04, 0.60)[0]
after = call_price_and_greeks(50, 50, 29 / 365, 0.04, 0.35)[0]
print(round(before, 4), round(after, 4), round((after - before) * 100, 2))
```

</details>

## Common mistakes

- Thinking time decay is steady. It speeds up near expiry, which is why a short-dated option can lose most of its value in the last week.
- Buying an option into an event because the move looks likely. The price already contains a high volatility, and it falls once the event passes.
- Quoting a Greek per share when you hold contracts. Multiply by 100 and by the number of contracts.

## Try it

1\. You hold 2 contracts of the 14-day at-the-money call, theta -0.0445 per share per day. About how much do you lose in 3 days if nothing else changes?

<details class="solution" markdown>
<summary>Answer</summary>

0.0445 x 100 x 2 = US$8.90 per day, so about US$26.70 in 3 days. Theta grows as expiry nears, so the true loss is a little larger.

</details>

2\. Vega is 0.0987 per share and implied volatility falls 4 points. What is the change for one contract, other inputs unchanged?

<details class="solution" markdown>
<summary>Answer</summary>

-0.09874 x 4 = -0.3950 per share, which is -US$39.50 per contract.

</details>

3\. Which has more vega: the 3-month at-the-money option or the 1-month one?

<details class="solution" markdown>
<summary>Answer</summary>

The 3-month one: US$9.87 against US$5.62 per contract. Vega grows with the square root of the time left.

</details>

4\. A 2-year at-the-money call has rho 0.4529 per share. Rates rise from 4% to 5%. What is the approximate gain per contract?

<details class="solution" markdown>
<summary>Answer</summary>

0.4529 x 100 = US$45.29 per contract for one percentage point.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On a chain that shows Greeks, find the ATM call's theta and vega for the nearest expiry and one three months out. Convert both to US$ per contract. |
| 3 | Compare the call's theta near expiry and far from expiry. Write the ratio. |
| 3 | Find a stock with earnings this week. Write its implied volatility now and plan to write it again after the report. |

</div>

## Key terms

- **Theta**: the change in an option's price from one day passing.
- **Vega**: the change in an option's price for a one-point rise in volatility.
- **Rho**: the change in an option's price for a one-percentage-point rise in the interest rate.
- **IV crush**: the fall in implied volatility after a known event passes.

Next: [Implied volatility](08-implied-volatility.md)
