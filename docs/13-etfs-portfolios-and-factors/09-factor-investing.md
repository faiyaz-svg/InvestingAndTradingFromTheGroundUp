# Factor investing

<!-- lint-ok: robust (name of a factor, robust minus weak) -->

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">ETF</span>

After this lesson you can estimate a stock's beta, name the main published factors and what each one measures, rank stocks on momentum, and say what research found about how well factor returns last after they are published.

Before this: [Modern portfolio theory](08-modern-portfolio-theory.md), [Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md), [Price multiples](../10-valuation-and-research/01-multiples.md). The math book's [Investing returns and risk](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk/) helps. You need: a calculator.

## The idea

An index fund earns the market's return. Two stocks, one cheap and one expensive by their price multiples, can both be in it, and the market return does not say which one earned more. A **factor** is a characteristic that sorts stocks into groups, such as cheapness or past return, where one group has earned a different return from the other, on average, for long periods. **Factor investing** holds a portfolio tilted toward the group that earned more.

The lesson goes from one factor, the market, to five, and then asks whether factors keep working after people learn about them.

## How it works

### One factor: the market and beta

The capital asset pricing model (CAPM) says a stock's expected excess return (over the risk-free rate) is its beta times the market's:

\[ E[r_i - r_f] = \beta_i \, E[r_m - r_f], \qquad \beta_i = \frac{\text{Cov}(r_i, r_m)}{\text{Var}(r_m)} \]

- \(r_i, r_m, r_f\) are the stock's, the market's and the risk-free return, over the same period.
- \(\beta_i\) is the stock's **beta**: its sensitivity to the market. It is the slope when you regress the stock's excess returns on the market's. A beta of 1.4 means a stock tended to move 1.4% for each 1% market move.

<div class="example" markdown>

### Worked example: a beta from 12 months

Excess returns in %, made up. Market: 2.0, -1.5, 3.0, 0.5, -2.5, 4.0, 1.0, -3.0, 2.5, 0.0, 1.5, -1.0. Stock A: 3.4, -1.9, 4.2, 1.1, -3.2, 5.4, 1.6, -4.0, 3.9, 0.4, 2.0, -1.7.

1. Covariance of the two series = 6.762, variance of the market = 4.884.
2. Beta = 6.762 / 4.884 = 1.38.
3. The regression intercept, called **alpha**, is 0.18% a month: what the stock earned beyond what its beta explains over these 12 months.

Twelve months is a short sample, so the beta and alpha are noisy. Many data sites use 5 years of monthly data, and their betas differ for that reason.

</div>

### More factors

The CAPM's one factor did not explain all the differences in average returns. Fama and French added two more in "Common risk factors in the returns on stocks and bonds" ([Journal of Financial Economics, 1993](https://doi.org/10.1016/0304-405X(93)90023-5)):

\[ r_i - r_f = \alpha + b\,(r_m - r_f) + s\,\text{SMB} + h\,\text{HML} + \varepsilon \]

- SMB ("small minus big") is the return of small-company stocks minus large-company stocks. This is the **size** factor.
- HML ("high minus low") is the return of stocks with a high book-to-market ratio (cheap: the book value of equity is large against its price) minus stocks with a low one. This is the **value** factor.
- \(b, s, h\) are the stock's loadings on each factor, and \(\varepsilon\) is what is left.

Carhart added a fourth in "On Persistence in Mutual Fund Performance" ([Journal of Finance, 1997](https://doi.org/10.1111/j.1540-6261.1997.tb03808.x)): WML, winners minus losers, the **momentum** factor, which Jegadeesh and Titman had documented in 1993 (Journal of Finance). Fama and French's five-factor model, "A five-factor asset pricing model" ([Journal of Financial Economics, 2015](https://doi.org/10.1016/j.jfineco.2014.10.010)), added profitability (RMW, robust minus weak operating profit) and investment (CMA, conservative minus aggressive asset growth). Profitability is a measure of **quality**; part 9 shows how to read it in [Returns on capital](../09-company-financials/07-returns-on-capital.md). A fifth idea, **low volatility**, holds stocks with low beta or low volatility. Frazzini and Pedersen found that a portfolio long low-beta and short high-beta assets earned positive risk-adjusted returns ([Journal of Financial Economics, 2014](https://doi.org/10.1016/j.jfineco.2013.10.005)).

| Factor | Holds more of | Measured by |
|---|---|---|
| Value | cheap stocks | book-to-market, earnings yield |
| Size | small companies | market cap |
| Momentum | recent winners | return over the prior 12 months, skipping the latest month |
| Quality | profitable, stable companies | operating profitability |
| Low volatility | low-risk stocks | beta or past volatility |

### A momentum rule, step by step

1. Each month, compute each stock's return from 12 months ago to one month ago. The latest month is skipped because very recent returns tend to partly reverse.
2. Rank the stocks and take the top group (for example, the top tenth) as winners.
3. Hold the winners for a month, then repeat. A rule needs no stop level or price target.

<div class="example" markdown>

### Worked example: ranking ten made-up stocks

Prior 12-1 month return and next month's return, in %:

| Stock | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Prior return | 45 | 38 | 31 | 22 | 12 | 4 | -6 | -14 | -25 | -38 |
| Next month | 3.1 | 2.2 | 1.0 | 1.4 | 0.2 | -0.3 | 0.5 | -1.2 | -0.8 | -2.4 |

1. Top 3 (S1 to S3): average next month = (3.1 + 2.2 + 1.0) / 3 = 2.10%.
2. Bottom 3 (S8 to S10): (-1.2 - 0.8 - 2.4) / 3 = -1.47%.
3. Winners minus losers = 2.10 - (-1.47) = 3.57%.

This is one invented month built to show the arithmetic. Real momentum spreads are noisy, positive on average over many months in published studies, and negative in some months.

</div>

## When it fails

Factor returns are averages over long periods, and a single factor can lag the market for years. Momentum has crashed: Daniel and Moskowitz found that it loses heavily in "panic" states, after market declines and in high volatility, when losers rebound ([Journal of Financial Economics, 2016](https://doi.org/10.1016/j.jfineco.2015.12.002)). Kenneth French's data library publishes the monthly factor series, so you can compute rolling 10-year averages yourself.

The bigger question is whether the premium survives publication. McLean and Pontiff studied 97 return-predicting variables: returns were 26% lower out of sample, and 58% lower after the papers were published. They read the first number as an upper bound on data mining, and the gap to 58% as the effect of investors trading on what they read ([Journal of Finance, 2016](https://doi.org/10.1111/jofi.12365)).

<div class="example" markdown>

### Worked example: what a tilt is worth after decay

Suppose a factor earned 2.0% a year over the sample. You move 20% of your stock money into a fund that holds it.

1. At the sample premium: 0.20 x 2.0 = 0.40 percentage points a year.
2. After a 58% decay: premium = 2.0 x 0.42 = 0.84%, so the tilt adds 0.20 x 0.84 = 0.17 points.
3. If the fund's returns differ from the market's by about 6% a year (its tracking error), the tilt changes your yearly result by about 0.20 x 6 = 1.2 points either way, which is far bigger than 0.17.

The tilt adds noise much faster than it adds expected return, and a higher fee than an index fund subtracts from the 0.17.

</div>

Factor ETFs follow these rules in a fund. This book names no product. Read how the fund defines the factor, and compare its fee and tracking difference with a plain index fund; two "value" funds can hold different stocks.

<div class="canada" markdown>

### For Canadians

Factor funds exist in Canadian-listed and US-listed forms. The tax and currency points of lesson 3 apply to them, and so does the placement in lesson 10. A factor tilt is a choice about the risk of looking different from the market, so size it by the 1.2-point style of number above.

</div>

## In code

Estimate the beta and alpha from the 12 months above.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

m = np.array([2.0, -1.5, 3.0, 0.5, -2.5, 4.0, 1.0, -3.0, 2.5, 0.0, 1.5, -1.0])
s = np.array([3.4, -1.9, 4.2, 1.1, -3.2, 5.4, 1.6, -4.0, 3.9, 0.4, 2.0, -1.7])
beta, alpha = np.polyfit(m, s, 1)
print(round(beta, 2), round(alpha, 2))
```

</details>

## Common mistakes

- Reading a high backtested factor return as a forecast. The research above shows returns are lower after publication.
- Tilting heavily on one factor after a good run. Factors have long cold stretches.
- Comparing a factor fund with the market over one or two years. The difference needs far longer to tell from luck.

## Try it

1\. A stock's returns have a covariance of 8.4 with the market's, and the market's variance is 6.0. What is its beta?

<details class="solution" markdown>
<summary>Answer</summary>

8.4 / 6.0 = 1.4.

</details>

2\. With a beta of 1.4, a risk-free rate of 2% and an expected market excess return of 5%, what does CAPM give as the stock's expected return?

<details class="solution" markdown>
<summary>Answer</summary>

Excess = 1.4 x 5 = 7%. Expected return = 2 + 7 = 9%.

</details>

3\. In the ranking example, what do winners minus losers become if S3's next month were -1.0 instead of 1.0?

<details class="solution" markdown>
<summary>Answer</summary>

Top 3 = (3.1 + 2.2 - 1.0) / 3 = 1.43%. Spread = 1.43 - (-1.47) = 2.90%.

</details>

4\. A factor earned 3.0% a year in the sample. After 58% decay, what is the premium, and what does a 25% tilt add?

<details class="solution" markdown>
<summary>Answer</summary>

Premium = 3.0 x 0.42 = 1.26%. The tilt adds 0.25 x 1.26 = 0.315, about 0.32 percentage points.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Look up a stock you hold on a data site. Write its beta and the window it uses. Compare it with a second site. |
| 3 | Find a factor fund's index rule on the issuer's page. Write how it defines the factor. |
| 2 | Write the fund's fee next to a plain index fund's fee, and the difference over 30 years using lesson 2's formula. |

</div>

## Key terms

- **Factor**: a stock characteristic that sorts stocks into groups with different average returns.
- **Factor investing**: holding a portfolio tilted toward a factor.
- **Beta**: a stock's sensitivity to the market's return.
- **Alpha**: the part of a return not explained by the factors in the model.
- **Size**: the factor of small companies minus large ones.
- **Value**: the factor of cheap stocks minus expensive ones.
- **Momentum**: the factor of recent winners minus recent losers.
- **Quality**: the factor of profitable, stable companies.
- **Low volatility**: the factor of low-risk stocks.

Next: [A long-term portfolio](10-a-long-term-portfolio.md)
