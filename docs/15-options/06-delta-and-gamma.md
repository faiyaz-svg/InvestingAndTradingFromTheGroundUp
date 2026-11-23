# Delta and gamma

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">OPT</span>

After this lesson you can say how much an option's price moves when the stock moves, turn an option position into an equivalent number of shares, and explain how delta itself changes.

Before this: [What sets an option's price](04-what-sets-an-option-price.md), [The options chain and moneyness](03-the-chain-and-moneyness.md). You need: a calculator.

## The idea

You own one call on Stock A (strike 50, three months left, stock at US$50). The stock rises US$1 to US$51. How much does your call gain? About US$0.56 per share. If the stock rises US$1 again, the gain is a little larger than 0.56. The rate at which the option moves with the stock is its **delta**, and the rate at which delta changes is its **gamma**. Together with theta, vega and rho (lesson 7) they are the **Greeks**: the sensitivities of an option's price to each of its inputs.

The numbers in this lesson come from the Black-Scholes model with the base case from lesson 4: \(S = 50\), \(K = 50\), \(T = 0.25\), \(r = 4\%\), \(\sigma = 30\%\), no dividend.

## Delta

\[ \Delta = \frac{\text{change in option price}}{\text{change in stock price}} \]

- \(\Delta\) (delta) is in US$ of option price per US$1 of stock price, so it is a pure number.
- For a call, delta is between 0 and 1. In Black-Scholes without dividends it is \(N(d_1)\) from lesson 4.
- For a put, delta is between -1 and 0. It equals the call's delta minus 1 (here 0.5563 - 1 = -0.4437).

For the base case, the call's delta is 0.5563 and the put's is -0.4437. A US$1 rise in the stock adds about US$0.56 to the call and takes about US$0.44 off the put.

Delta has two useful readings.

First, a **hedge ratio**, the number of shares that has the same exposure to small moves as the option. One call contract covers 100 shares, so it behaves like 0.5563 x 100 = 55.63 shares. A long call has positive delta (it gains when the stock rises), a long put negative delta. A trader who holds one call and sells 56 shares is nearly **delta neutral**: a small move up or down in the stock changes the total by almost nothing. Market makers do this all day, which is how they can quote both sides.

Second, a rough probability. The delta of a call is close to the chance, in the model, that it finishes in the money. A call with delta 0.31 is roughly a 31% chance, and one with delta 0.80 roughly 80%. Be careful: it is only a proxy. The model's chance is a risk-neutral one (lesson 4), not a forecast, and the exact in-the-money probability in the model is \(N(d_2)\), not \(N(d_1)\). For the 55-strike call in the lesson 3 chain, delta is 0.31 but \(N(d_2)\) is 0.26. Use delta as a rough guide to how far out of the money an option is.

The figure on the left shows delta against the stock price. It is a smooth S-shaped curve. A deep out-of-the-money call has a delta near 0 (it barely reacts), a deep in-the-money call near 1 (it moves like the stock), and an at-the-money call near 0.5.

![Delta and gamma of a call against the stock price, three months and 11 days left](../assets/figures/15-options/delta-gamma-dark.svg#only-dark)
![Delta and gamma of a call against the stock price, three months and 11 days left](../assets/figures/15-options/delta-gamma-light.svg#only-light)

| Stock A | Call delta | Put delta |
|---|---|---|
| US$40 | 0.0892 | -0.9108 |
| US$45 | 0.2875 | -0.7125 |
| US$50 | 0.5563 | -0.4437 |
| US$55 | 0.7814 | -0.2186 |
| US$60 | 0.9126 | -0.0874 |

## Gamma

Delta is not fixed. When the stock moves, delta changes, and gamma measures by how much.

\[ \Gamma = \frac{\text{change in delta}}{\text{change in stock price}} \]

- \(\Gamma\) (gamma) is in delta per US$1 of stock price. A call and a put with the same strike and expiry have the same gamma.
- Gamma is positive for every long option and negative for every short one.

The base case has \(\Gamma = 0.0527\): after a US$1 rise, delta goes from 0.5563 to about 0.6090 (the exact figure is 0.6078). So a long option gets more sensitive as it moves in your favour, and less sensitive as it moves against you.

Gamma is highest at the money, and it grows as expiry nears. On the right of the figure, the 11-day curve is tall and narrow, and the three-month curve is low and wide. For the at-the-money call, gamma is 0.0527 with three months left, 0.0925 with 30 days and 0.1605 with 10 days.

<div class="example" markdown>

### Worked example: delta, gamma and a three dollar move

One call (strike 50, 3 months left) costs 3.2297 with Stock A at US$50. The stock rises to US$53.

1. Delta alone: 0.5563 x 3 = +1.669. The estimate is 3.2297 + 1.669 = 4.899.
2. Add gamma: 0.5 x 0.0527 x 3 x 3 = +0.237. The estimate is 4.899 + 0.237 = 5.136, so the change is +1.906.
3. The model's exact price at US$53 is 5.1241, a change of +1.8943.

Delta alone understates the gain by about 0.23 per share (US$23 per contract), and adding gamma cuts the error to about 0.01. For a fall to US$47, delta alone gives -1.669 and adding gamma gives -1.432 against an exact change of -1.4258: the call loses less than delta alone predicts. A long option gains more than delta predicts when the stock moves a lot in either direction, which is the benefit of positive gamma.

</div>

The cost of that benefit is theta, the daily decay in lesson 7. Short option positions are the reverse: they collect the decay and carry negative gamma, so a large move against them gets worse each dollar. Gamma risk is behind much of the trading around expiry ([Opex, gamma and index rebalances](../16-volatility-and-event-trading/06-opex-gamma-and-index-rebalances.md)).

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def N(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
def pdf(x): return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)

def delta_gamma(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
    return N(d1), pdf(d1) / (S * sigma * math.sqrt(T))

d, g = delta_gamma(50, 50, 0.25, 0.04, 0.30)
print(round(d, 4), round(g, 4), round(d * 100, 2))
print(round(delta_gamma(51, 50, 0.25, 0.04, 0.30)[0], 4))
```

</details>

## Common mistakes

- Reading delta as an exact probability. It is a rough proxy and differs from the model's own \(N(d_2)\).
- Forgetting that delta changes. A hedge that is neutral at US$50 is not neutral at US$53.
- Ignoring the 100. A delta of 0.56 is 56 shares for one contract.

## Try it

1\. You hold 5 contracts of a call with delta 0.31. How many shares is that, and what is the approximate gain for a US$1 rise?

<details class="solution" markdown>
<summary>Answer</summary>

0.31 x 100 x 5 = 155 shares. A US$1 rise gains about US$155.

</details>

2\. A put has delta -0.44. The stock falls US$2. What is the approximate gain per contract?

<details class="solution" markdown>
<summary>Answer</summary>

Price change per share = -0.44 x (-2) = +0.88. Per contract = US$88.

</details>

3\. The call has delta 0.5563 and gamma 0.0527. Estimate the new delta after a US$1 rise.

<details class="solution" markdown>
<summary>Answer</summary>

0.5563 + 0.0527 = 0.6090 (the exact model value is 0.6078, so about 0.61).

</details>

4\. You are short 3 call contracts with delta 0.5563 each. How many shares do you buy to be delta neutral?

<details class="solution" markdown>
<summary>Answer</summary>

Short calls have delta -0.5563 x 100 x 3 = -166.9 shares. Buy about 167 shares.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On a chain, find the delta of the ATM call and put and an OTM call. Convert each to shares for one contract. |
| 3 | Pick a call and estimate its price change for a US$2 rise using delta. |
| 3 | Run the code for a strike and expiry from the chain and compare with your broker's delta. |

</div>

## Key terms

- **Greeks**: the sensitivities of an option's price to its inputs.
- **Delta**: the change in an option's price per US$1 change in the stock.
- **Hedge ratio**: the number of shares that matches an option's small-move exposure.
- **Delta neutral**: a position whose total delta is zero.
- **Gamma**: the change in delta per US$1 change in the stock.

Next: [Theta, vega and rho](07-theta-vega-and-rho.md)
