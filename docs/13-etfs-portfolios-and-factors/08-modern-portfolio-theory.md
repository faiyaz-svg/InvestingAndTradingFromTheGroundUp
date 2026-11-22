# Modern portfolio theory

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">ETF</span>

After this lesson you can find the lowest-risk mix of two assets, compute a Sharpe ratio, read an efficient frontier, and say where portfolio optimization breaks.

Before this: [Diversification and correlation](06-diversification-and-correlation.md). The math book's [Investing returns and risk](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk/) covers expected return and volatility. You need: a calculator.

## The idea

Lesson 6 showed that mixing two assets with a correlation below 1 gives less risk than the average of the two. Harry Markowitz asked the next question: out of all possible mixes of many assets, which ones give the most expected return for each level of risk? His answer, in "Portfolio Selection" ([Journal of Finance, 1952](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)), started **modern portfolio theory** (MPT). It treats an investor as caring about two numbers for the whole portfolio: expected return and standard deviation of return. Assets are judged by how they change the portfolio's pair, not by their own numbers alone.

## How it works

For weights \(w_i\) on \(n\) assets, the portfolio's expected return and variance are

\[ \mu_p = \sum_i w_i \mu_i, \qquad \sigma_p^2 = \sum_i \sum_j w_i w_j \sigma_i \sigma_j \rho_{ij} \]

- \(\mu_i\) is asset \(i\)'s expected yearly return, as a fraction.
- \(\sigma_i\) is its standard deviation, and \(\rho_{ij}\) the correlation of assets \(i\) and \(j\) (with \(\rho_{ii} = 1\)).
- The double sum is lesson 6's two-asset formula for any number of assets.

### The minimum-variance mix

For two assets A and B, the weight in A that gives the lowest portfolio volatility is

\[ w_A = \frac{\sigma_B^2 - \rho \sigma_A \sigma_B}{\sigma_A^2 + \sigma_B^2 - 2 \rho \sigma_A \sigma_B} \]

<div class="example" markdown>

### Worked example: the lowest-risk mix of a stock and a bond fund

Asset A (stocks, made up): expected return 8%, volatility 16%. Asset B (bonds): 3%, 5%. Correlation 0.1.

1. Numerator: 0.05^2 - 0.1 x 0.16 x 0.05 = 0.0025 - 0.0008 = 0.0017.
2. Denominator: 0.16^2 + 0.05^2 - 2 x 0.1 x 0.16 x 0.05 = 0.0256 + 0.0025 - 0.0016 = 0.0265.
3. \(w_A\) = 0.0017 / 0.0265 = 6.4%. The lowest-risk mix is 6.4% A and 93.6% B.

</div>

### The Sharpe ratio

Risk alone is not the goal. Return per unit of risk is closer. The **Sharpe ratio**, from William Sharpe ("Mutual Fund Performance", Journal of Business, 1966), measures the extra return over a risk-free rate for each unit of volatility:

\[ S = \frac{\mu_p - r_f}{\sigma_p} \]

- \(\mu_p\) is the portfolio's expected return and \(r_f\) the risk-free rate (the return on a safe asset such as a short government bill), both as fractions.
- \(\sigma_p\) is the portfolio's standard deviation.
- \(S\) has no unit. A higher value means more return per unit of risk.

With \(r_f = 2\%\), asset A alone has \(S\) = (8 - 2) / 16 = 0.375, and B alone has (3 - 2) / 5 = 0.20. Mixes of the two:

| Weight in A | Expected return | Volatility | Sharpe ratio |
|---|---|---|---|
| 0% | 3.0% | 5.00% | 0.200 |
| 20% | 4.0% | 5.37% | 0.373 |
| 40% | 5.0% | 7.33% | 0.409 |
| 60% | 6.0% | 10.00% | 0.400 |
| 100% | 8.0% | 16.00% | 0.375 |

A 40 / 60 mix beats both assets alone on the Sharpe ratio, which is the gain from diversification in return-per-risk terms.

### The efficient frontier and the tangency portfolio

Add a third asset C: expected return 6.5%, volatility 15%, with correlations 0.6 to A and 0.1 to B. Every mix of the three has a point (volatility, expected return). For each level of risk, some mix has the highest return, and the line through those best points is the **efficient frontier**. Any mix below it is dominated: another mix gives more return for the same risk. The frontier starts at the minimum-variance portfolio and rises to the highest-return asset.

If you can also hold the risk-free asset, the best risky mix is the one with the highest Sharpe ratio: the **tangency portfolio**, where a line from \(r_f\) touches the frontier at one point. Its weights are proportional to \(\Sigma^{-1}(\mu - r_f)\), where \(\Sigma\) is the matrix of covariances. For these three assets the tangency mix is 32.0% A, 55.6% B and 12.4% C, with expected return 5.04%, volatility 7.26% and a Sharpe ratio of 0.418. You then choose your risk by mixing the tangency portfolio with cash: half in each gives a return of 0.5 x 5.04 + 0.5 x 2 = 3.52% and volatility of 0.5 x 7.26 = 3.63%. The dashed line in the figure, the capital allocation line, shows all such blends.

The figure uses made-up numbers. Look for the three assets as squares, the cloud of random long-only mixes (no short selling), and the orange frontier along its upper edge.

![Efficient frontier of three made-up assets, the tangency portfolio and the capital allocation line from the risk-free rate](../assets/figures/13-etfs-portfolios-and-factors/frontier-dark.svg#only-dark)
![Efficient frontier of three made-up assets, the tangency portfolio and the capital allocation line from the risk-free rate](../assets/figures/13-etfs-portfolios-and-factors/frontier-light.svg#only-light)

### Where it breaks

The mathematics is exact; the inputs are not. The expected returns, volatilities and correlations are estimates from past data, and the optimizer amplifies their errors, since it loads on whichever asset looks best by a small, noisy margin. DeMiguel, Garlappi and Uppal compared 14 optimized strategies with the plain 1/N rule (equal weights) and found that out of sample the gains from optimal diversification were often offset by estimation error ([Review of Financial Studies, 2009](https://doi.org/10.1093/rfs/hhm075)). That does not prove equal weights are right. It says a good-looking optimized portfolio can be an artefact of noisy inputs.

Other limits: standard deviation counts upside and downside swings the same; correlations change, rising in crashes (lesson 6); the model has one period and ignores taxes, fees and your own liabilities. Use it for the ideas it gives (diversify across low-correlation assets, judge risk at the portfolio level) and not as a source of exact weights.

<div class="canada" markdown>

### For Canadians

The risk-free rate for a Canadian is a C$ rate, such as a Government of Canada treasury bill or a high-interest savings rate. The mix you pick has to be placed into accounts (lesson 10), and currency adds a risk the model above does not include, which is one more reason to treat the weights as approximate.

</div>

## In code

Find the tangency weights and the Sharpe ratio for the three assets above.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

mu = np.array([0.08, 0.03, 0.065])
sd = np.array([0.16, 0.05, 0.15])
corr = np.array([[1, 0.1, 0.6], [0.1, 1, 0.1], [0.6, 0.1, 1]])
cov = np.outer(sd, sd) * corr
rf = 0.02

x = np.linalg.solve(cov, mu - rf)
w = x / x.sum()
ret, vol = w @ mu, (w @ cov @ w) ** 0.5
print(np.round(100 * w, 1), round(100 * ret, 2), round(100 * vol, 2), round((ret - rf) / vol, 3))
```

</details>

## Common mistakes

- Trusting the optimizer's weights. Small changes in the expected returns move them a lot.
- Treating the Sharpe ratio as a full measure of risk for assets with rare large losses. Standard deviation understates that risk.
- Forgetting the risk-free rate in the Sharpe ratio. Return divided by risk without it rewards an asset for earning the safe rate. Cash with a 2% return and almost no risk would score very high.

## Try it

1\. Stocks have a return of 9% and volatility of 18%. The risk-free rate is 2%. What is the Sharpe ratio?

<details class="solution" markdown>
<summary>Answer</summary>

(9 - 2) / 18 = 0.389.

</details>

2\. Using the lesson's A and B (correlation 0.1), what is the volatility of a 20 / 80 mix?

<details class="solution" markdown>
<summary>Answer</summary>

Variance = 0.04 x 0.0256 + 0.64 x 0.0025 + 2 x 0.2 x 0.8 x 0.1 x 0.16 x 0.05 = 0.001024 + 0.0016 + 0.000256 = 0.00288. Volatility = 5.37%.

</details>

3\. The tangency portfolio returns 5.04% with volatility 7.26%. You hold 70% of it and 30% cash at 2%. What are your expected return and volatility?

<details class="solution" markdown>
<summary>Answer</summary>

Return = 0.7 x 5.04 + 0.3 x 2 = 3.528 + 0.6 = 4.13%. Volatility = 0.7 x 7.26 = 5.08%.

</details>

4\. Name two reasons an optimized portfolio can do worse out of sample than an equal-weight one.

<details class="solution" markdown>
<summary>Answer</summary>

The inputs are estimates with error, and the optimizer puts the biggest weights where the error is most favourable. Correlations also change, so the past estimate may not hold.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the In code box. Change the expected return of asset A from 8% to 7% and note how the tangency weights move. |
| 3 | Compute the Sharpe ratio of a fund you hold, from its 5-year return, volatility and the current 1-year government bill rate. |
| 2 | Write one line on why the weights moved more than the input did. |

</div>

## Key terms

- **Modern portfolio theory (MPT)**: Markowitz's framework for judging a portfolio by its expected return and its volatility.
- **Efficient frontier**: the set of portfolios with the highest expected return for each level of risk.
- **Sharpe ratio**: the excess return over the risk-free rate divided by volatility.
- **Risk-free rate**: the return on an asset with no default or price risk over the holding period.
- **Tangency portfolio**: the risky mix with the highest Sharpe ratio.
- **Capital allocation line**: the line of blends of the tangency portfolio and the risk-free asset.

Next: [Factor investing](09-factor-investing.md)
