# Portfolio heat and correlation

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">RISK</span>

After this lesson you can add up the risk of all your open positions, set a cap on it, and say when several positions are really one bet.

Before this: [Position sizing with fixed fractional risk](04-fixed-fractional-sizing.md). The math book's [correlation](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/04-correlation-and-linear-regression/) lesson explains correlation. You need: a calculator.

## The idea

You risk 1% on each trade, which feels safe. Then you open a fifth position, and a sixth. If the market falls hard, how much can you lose on one day?

If every stop were hit, six trades at 1% lose 6% of the account. That is the sum of the open risk, and it is the number to watch, not the 1% on any one trade. The total open risk of your positions, as a percent of the account, is the **portfolio heat**.

There is a second problem. Six positions in six different companies are not six independent bets if all six are chip makers. They tend to fall on the same day, for the same reason. Stocks that move together are **correlated**, and a heavy portfolio of correlated stocks behaves like a single large position.

## How it works

### Heat

For a long position, the open risk is what you would lose from the current price if the stop fills:

\[ \text{open risk} = N \times (P - S) \qquad \text{heat} = \frac{\sum \text{open risk}}{A} \]

- \(N\) is the number of shares, \(P\) the current price and \(S\) the current stop, in US$.
- \(A\) is the account value, and the sum runs over every open position.
- Raising a stop towards the price lowers a position's open risk. A stop at or above your entry price means you can no longer lose your original money.

<div class="example" markdown>

### Worked example: four open positions

Account US$25,000. All figures are for made-up stocks.

| Position | Shares | Entry | Price now | Stop | Open risk |
|---|---|---|---|---|---|
| Stock A | 166 | 48.20 | 49.10 | 46.70 | 166 x 2.40 = US$398.40 |
| Stock B | 80 | 62.00 | 61.40 | 59.50 | 80 x 1.90 = US$152.00 |
| Stock C | 300 | 12.50 | 12.80 | 11.90 | 300 x 0.90 = US$270.00 |
| Stock D | 55 | 90.00 | 93.00 | 90.00 | 55 x 3.00 = US$165.00 |

1. Total open risk = 398.40 + 152.00 + 270.00 + 165.00 = US$985.40.
2. Heat = 985.40 / 25,000 = 3.94%.
3. Suppose your plan caps heat at 6% (an example limit, not a recommendation). Stock E would risk 1%, which is US$250.00. 985.40 + 250.00 = US$1,235.40, and 1,235.40 / 25,000 = 4.94%. That is under the cap, so the trade is allowed.

Stock D's stop is at its entry, so its original money is safe, but the US$165.00 of open profit is still at risk. That is why the table counts from the current price.

</div>

A cap is a rule you set once, in the plan (lesson 10), so you do not decide it again in the middle of a trade.

### Correlation

The **correlation** of two stocks' returns runs from -1 to +1. At +1 they move in lockstep, at 0 they are unrelated and at -1 they move in opposite directions. Suppose you hold \(n\) positions that each risk about the same amount, and the average correlation between their returns is \(\rho\). Then:

\[ \text{effective bets} = \frac{n}{1 + (n - 1)\rho} \qquad \text{spread of outcomes} = \sqrt{n + n(n - 1)\rho} \times \sigma \]

- \(n\) is the number of positions and \(\rho\) is the average correlation, with no unit.
- \(\sigma\) is the standard deviation of one position's result, for example 1R.
- At \(\rho = 0\), effective bets equal \(n\). At \(\rho = 1\) they equal 1.

For four positions at \(\rho = 0.8\): effective bets = 4 / (1 + 3 x 0.8) = 4 / 3.4 = 1.18. The spread of outcomes is sqrt(4 + 12 x 0.8) = sqrt(13.6) = 3.69 times that of one position. Four independent positions would have a spread of sqrt(4) = 2 times, and four identical ones 4 times. Four positions at 0.8 correlation are close to one position four times as large.

The curve shows how fast the effective count falls. A modest correlation of 0.4 already takes eight positions down to about 2.1 effective bets.

![Effective independent bets against correlation, for 4 and 8 positions](../assets/figures/03-risk-and-position-sizing/effective-bets-dark.svg#only-dark)
![Effective independent bets against correlation, for 4 and 8 positions](../assets/figures/03-risk-and-position-sizing/effective-bets-light.svg#only-light)

Correlation is not fixed. Measured on calm days it can understate how much stocks fall together on a bad day, so do not treat 0.3 on a quiet month as a promise. A practical rule is to cap risk by group as well as in total: for example, no more than 2% of the account at risk across all positions in one sector, whatever the correlation says.

## In code

Measuring average correlation and effective bets from daily returns. The returns here are seeded random numbers with a shared market factor, so the result repeats.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(5)
n_days = 4000
market = rng.normal(0, 0.01, n_days)
returns = pd.DataFrame(
    {
        name: 0.8 * market + 0.6 * rng.normal(0, 0.01, n_days)
        for name in ["A", "B", "C", "D"]
    }
)

corr = returns.corr().to_numpy()
n = len(corr)
avg_corr = corr[np.triu_indices(n, 1)].mean()
effective = n / (1 + (n - 1) * avg_corr)
print(round(avg_corr, 2), round(effective, 2))
```

The code prints 0.63 and 1.38: four stocks that behave like 1.4 independent ones.

</details>

## Common mistakes

- Checking each trade's risk and never the total. Six 1% trades are 6% at risk.
- Counting positions in the same sector as separate bets. Group them and cap the group.
- Forgetting that a stop moved to break-even still leaves open profit at risk. Count from the current price.

## Try it

1\. Account US$40,000. Open risk to the stops: US$300, US$450, US$520 and US$230. What is the portfolio heat?

<details class="solution" markdown>
<summary>Answer</summary>

Total = 300 + 450 + 520 + 230 = US$1,500. Heat = 1,500 / 40,000 = 3.75%.

</details>

2\. Your cap is 5% of a US$20,000 account, and open risk is US$850. How much risk can a new trade take, and how many shares if entry is US$30.00 and the stop is US$28.50?

<details class="solution" markdown>
<summary>Answer</summary>

The cap is 0.05 x 20,000 = US$1,000. Room = 1,000 - 850 = US$150. Risk per share = 1.50. Shares = 150 / 1.50 = 100. (A normal 1% trade would risk US$200, so the cap cuts the size.)

</details>

3\. Five positions in one sector, average correlation 0.6. How many effective bets, and how does the spread of outcomes compare with one position?

<details class="solution" markdown>
<summary>Answer</summary>

Effective bets = 5 / (1 + 4 x 0.6) = 5 / 3.4 = 1.47. The spread of outcomes is sqrt(5 + 20 x 0.6) = sqrt(17) = 4.12 times one position's spread, against 5 for fully correlated and 2.24 for independent. With 1% risked on each, the spread of outcomes is about 4.1%, near the 5% of fully correlated positions and well above the 2.2% of independent ones.

</details>

4\. You hold 200 shares of Stock A with the price at US$55.00. You raise the stop from US$50.00 to US$53.00. What is the change in open risk?

<details class="solution" markdown>
<summary>Answer</summary>

Before: 200 x (55.00 - 50.00) = US$1,000. After: 200 x (55.00 - 53.00) = US$400. Open risk falls by US$600.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | List your open positions (or three you could hold). For each, write shares, price and stop, and compute the open risk. |
| 3 | Add them up and divide by the account. Write your heat. |
| 3 | Mark which positions are in the same sector. Write the total open risk of that group as a percent of the account. |

</div>

## Key terms

- **Open risk**: the loss on a position from its current price to its stop.
- **Portfolio heat**: total open risk across all positions, as a percent of the account.
- **Correlation**: a number from -1 to +1 for how closely two returns move together.
- **Effective bets**: the number of independent positions that would give the same spread of outcomes.
- **Group risk cap**: a limit on the open risk in one sector or theme.

Next: [Drawdowns and risk of ruin](08-drawdowns-and-risk-of-ruin.md)
