# What sets an option's price

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">OPT</span>

After this lesson you can name the inputs that set an option's price, say which way each one pushes a call and a put, and use the Black-Scholes formula as a calculator.

Before this: [The options chain and moneyness](03-the-chain-and-moneyness.md). The math book's lessons on the [normal distribution](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/04-continuous-random-variables-and-the-normal/) and [logarithms](https://faiyaz-svg.github.io/MathFromTheGroundUp/03-high-school/07-exponentials-and-logarithms/02-logarithms/) help: you need to know what a cumulative normal probability and \(\ln\) are. You need: a calculator or Python.

## The idea

Lesson 3 showed a chain of prices. Where do they come from? Market makers quote them, but they quote from a model, so the prices follow a pattern. Six things set the price of an option on a stock.

| Input | Symbol | Call price if it rises | Put price if it rises |
|---|---|---|---|
| Stock price | \(S\) | Up | Down |
| Strike | \(K\) | Down | Up |
| Time to expiry | \(T\) | Up | Up (usually) |
| Volatility | \(\sigma\) | Up | Up |
| Interest rate | \(r\) | Up | Down |
| Dividend yield | \(q\) | Down | Up |

Take Stock A at US$50, a 50-strike option, three months left (\(T = 0.25\) years), a 4% rate, 30% volatility and no dividend. The model (below) gives the call US$3.23 and the put US$2.73. Change one input at a time:

| Change | Call | Put |
|---|---|---|
| Base case | 3.23 | 2.73 |
| Stock 50 to 51 | 3.81 | 2.31 |
| Strike 50 to 51 | 2.76 | 3.26 |
| Time 0.25 to 0.30 years | 3.56 | 2.96 |
| Volatility 30% to 35% | 3.72 | 3.23 |
| Rate 4% to 5% | 3.29 | 2.67 |
| Dividend yield 0% to 2% | 3.09 | 2.84 |

Volatility, the yearly spread of the stock's returns, is the one input you cannot read off a screen. It is a guess about the future, so the market argues about it, and lesson 8 is about it. A higher rate raises a call because paying for the stock later, with money earning interest, is worth more. A dividend lowers a call, because the stock price drops when it pays and the call holder does not receive it.

## A tree with two outcomes

The simplest honest model has two outcomes. This is a **one-step binomial tree**, introduced by Cox, Ross and Rubinstein (1979, see the sources below).

Stock A is US$50. In three months it will be US$55 or US$45 (up or down 10%). The rate is 4%. A call with strike 50 pays US$5 if the stock goes up and US$0 if it goes down. What is it worth now?

<div class="example" markdown>

### Worked example: pricing a call by replication

Build the same payoff from shares and a loan.

1. Buy 0.5 shares and borrow money to be repaid in three months. If the stock is US$45, the half-share is worth US$22.50, and a loan of US$22.50 leaves nothing, matching the call's US$0. If the stock is US$55, the half-share is worth US$27.50 and after repaying US$22.50 you have US$5, matching the call.
2. The loan of US$22.50 due in three months costs 22.50 x \(e^{-0.04 \times 0.25}\) = US$22.28 today.
3. The cost today is 0.5 x 50 - 22.28 = 25 - 22.28 = US$2.72.

Any other price lets a trader buy the cheaper side, sell the dearer side and lock in a gain, so the call is worth US$2.72. The probability that the stock rises did not appear anywhere.

The same number comes from a "risk-neutral" probability \(p = (e^{rT} - 0.9) / (1.1 - 0.9)\) = 0.5503. Value = \(e^{-rT} \times p \times 5\) = 0.9900 x 0.5503 x 5 = US$2.72. The probability \(p\) is not a forecast. It is the number that makes the stock earn the risk-free rate in the model.

</div>

With many small steps, the outcomes spread into a bell shape, and in the limit the tree gives the Black-Scholes formula.

## The Black-Scholes formula

Black and Scholes (1973) and Merton (1973) priced a European option with a formula. You do not need to derive it. Here it is as a calculator, for a stock paying a continuous dividend yield \(q\).

\[ C = S e^{-qT} N(d_1) - K e^{-rT} N(d_2) \qquad P = K e^{-rT} N(-d_2) - S e^{-qT} N(-d_1) \]

\[ d_1 = \frac{\ln(S/K) + (r - q + \sigma^2/2)\,T}{\sigma \sqrt{T}} \qquad d_2 = d_1 - \sigma \sqrt{T} \]

- \(C\) and \(P\) are the call and put prices in US$ per share.
- \(S\) is the stock price and \(K\) the strike, both in US$.
- \(T\) is the time to expiry in years (days divided by 365).
- \(r\) is the risk-free rate (continuously compounded, per year) and \(q\) the dividend yield (per year), as decimals.
- \(\sigma\) is the volatility, the standard deviation of the stock's yearly return, as a decimal.
- \(N(x)\) is the cumulative normal distribution: the probability that a standard normal variable is at most \(x\).
- \(e^{-rT}\) discounts a future amount to today, so \(K e^{-rT}\) is the present value of the strike.

The call is "what you receive minus what you pay". \(S e^{-qT} N(d_1)\) is the stock you get, weighted by how deep in the money you end up. \(K e^{-rT} N(d_2)\) is the present value of the strike you pay, times \(N(d_2)\), the risk-neutral probability that the call finishes in the money. The put is the mirror image.

<div class="example" markdown>

### Worked example: the base case by hand

Stock A at US$50, strike 50, \(T = 0.25\), \(r = 4\%\), \(\sigma = 30\%\), \(q = 0\).

1. \(\sigma \sqrt{T}\) = 0.30 x 0.5 = 0.15.
2. \(d_1\) = (ln(1) + (0.04 + 0.045) x 0.25) / 0.15 = 0.02125 / 0.15 = 0.1417.
3. \(d_2\) = 0.1417 - 0.15 = -0.0083.
4. \(N(d_1)\) = 0.5563 and \(N(d_2)\) = 0.4967.
5. \(e^{-rT}\) = 0.9900, so \(K e^{-rT}\) = 49.50.
6. Call = 50 x 0.5563 - 49.50 x 0.4967 = 27.82 - 24.59 = US$3.23.
7. Put = 49.50 x \(N(0.0083)\) - 50 x \(N(-0.1417)\) = 49.50 x 0.5033 - 50 x 0.4437 = 24.92 - 22.18 = US$2.73.

Rounding the intermediate numbers shifts the last digit; the code below gives 3.2297 and 2.7322.

</div>

The figure shows the call's value now (curves) against its value at expiry (the sharp line).

![A call's value against the stock price: three months left, 18 days left, and at expiry](../assets/figures/15-options/value-before-expiry-dark.svg#only-dark)
![A call's value against the stock price: three months left, 18 days left, and at expiry](../assets/figures/15-options/value-before-expiry-light.svg#only-light)

The gap between a curve and the expiry line is the time value from lesson 3. It is widest at the money.

## Where the formula fails

Black-Scholes assumes constant volatility, a smooth price with no jumps, constant rates, no costs and a European option. Real stocks gap on earnings, and volatility changes. Single-stock options are American. Merton (1973) showed that an American call on a stock that pays no dividend is never worth exercising early, so the formula fits it; early exercise can matter for puts and for calls before a dividend. Tree models with many steps handle it. Traders still quote prices in Black-Scholes terms and correct for its gaps (lesson 8's smile).

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def black_scholes(S, K, T, r, sigma, q=0.0, kind="call"):
    d1 = (math.log(S / K) + (r - q + sigma**2 / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if kind == "call":
        return S * math.exp(-q * T) * N(d1) - K * math.exp(-r * T) * N(d2)
    return K * math.exp(-r * T) * N(-d2) - S * math.exp(-q * T) * N(-d1)

print(round(black_scholes(50, 50, 0.25, 0.04, 0.30), 4))
print(round(black_scholes(50, 50, 0.25, 0.04, 0.30, kind="put"), 4))
print(round(black_scholes(50, 50, 0.25, 0.04, 0.35), 4))
```

</details>

## Sources

- Black, F. and Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy* 81(3), 637-654. [doi:10.1086/260062](https://doi.org/10.1086/260062).
- Merton, R. C. (1973), "Theory of Rational Option Pricing", *Bell Journal of Economics and Management Science* 4(1), 141-183. [doi:10.2307/3003143](https://doi.org/10.2307/3003143).
- Cox, J. C., Ross, S. A. and Rubinstein, M. (1979), "Option Pricing: A Simplified Approach", *Journal of Financial Economics* 7(3), 229-263. [doi:10.1016/0304-405X(79)90015-1](https://doi.org/10.1016/0304-405X(79)90015-1).

## Common mistakes

- Treating the model price as the right price. It is the price for a given volatility. A different volatility gives a different price.
- Reading the risk-neutral probability \(p\) or \(N(d_2)\) as the real chance the stock rises. They come from the pricing argument.
- Using days in place of years for \(T\). Divide the days by 365.

## Try it

1\. Using the table, by how much does the 50-strike call rise if Stock A goes from US$50 to US$51? How many US$ per contract?

<details class="solution" markdown>
<summary>Answer</summary>

3.81 - 3.23 = 0.58 per share, which is about US$58 per contract (exact 0.5823, US$58.23).

</details>

2\. In the one-step tree, the stock goes to US$60 or US$40, with \(K = 50\), \(r = 0\) and one period. What is the call worth?

<details class="solution" markdown>
<summary>Answer</summary>

The call pays 10 or 0. The risk-neutral probability with \(r = 0\) is p = (1 - 0.8) / (1.2 - 0.8) = 0.5. Value = 0.5 x 10 = US$5.00. Replication: 0.5 shares and a loan of 0.5 x 40 = US$20 gives 10 or 0, costing 25 - 20 = US$5.

</details>

3\. Why does a higher volatility raise both the call and the put?

<details class="solution" markdown>
<summary>Answer</summary>

Each option has a capped loss (the premium) and an open-ended gain on one side. A wider spread of outcomes raises the average gain without raising the loss, so both gain value. The table shows it: 3.23 to 3.72 and 2.73 to 3.23.

</details>

4\. Compute the call and put with a 2% dividend yield and compare them with the base case.

<details class="solution" markdown>
<summary>Answer</summary>

Call 3.09 (down from 3.23), put 2.84 (up from 2.73), from the code above with q = 0.02.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the code with a stock price, strike and expiry from a real chain on your broker, using a volatility of 30%. Compare the model price with the chain's mid. |
| 3 | Change one input at a time (stock, volatility, days) and write which way each moves the call. |
| 2 | Note the gap between the model and the chain and which input you would change to close it. |

</div>

## Key terms

- **Volatility**: the yearly standard deviation of a stock's returns, as a percent.
- **Risk-free rate**: the interest rate on a safe loan, used to discount.
- **Dividend yield**: the yearly dividend as a share of the stock price.
- **Binomial tree**: a model in which the stock moves to one of two prices each step.
- **Risk-neutral probability**: the probability that makes a model price match the replication price.
- **Black-Scholes**: a formula for the price of a European option.

Next: [Put-call parity](05-put-call-parity.md)
