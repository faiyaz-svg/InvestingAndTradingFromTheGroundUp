# Correlation, beta and regression

<span class="tag tag-code">Code</span> <span class="tag tag-part">QUANT</span>

After this lesson you can compute correlation and beta from return series, fit a regression with numpy, read its slope, intercept, standard error and R squared, and say why a beta from a short window is a loose estimate.

Before this: [Portfolio heat and correlation](../03-risk-and-position-sizing/07-portfolio-heat-and-correlation.md), [Diversification and correlation](../13-etfs-portfolios-and-factors/06-diversification-and-correlation.md), [Factor investing](../13-etfs-portfolios-and-factors/09-factor-investing.md), [Returns and volatility in pandas](02-returns-and-volatility.md). The math book has [correlation and linear regression](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/04-correlation-and-linear-regression/) and [regression and econometrics intuition](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/04-more-tools/03-regression-and-econometrics-intuition/). You need: Python with pandas and numpy.

## The idea

Two questions come up when you hold more than one stock. How closely do they move together, and how much does one stock move when the market moves? Correlation answers the first, beta the second, and both come from the same regression of one return series on another.

Parts 3 and 13 used these numbers. This lesson computes them from data and shows how much error they carry.

## How it works

**Correlation** is the covariance of two return series divided by the product of their standard deviations:

\[ \rho = \frac{\operatorname{Cov}(r_s, r_m)}{\sigma_s \, \sigma_m} \]

- \(r_s\) is the stock's return and \(r_m\) the market's, over the same bars.
- \(\sigma_s\) and \(\sigma_m\) are their standard deviations.
- \(\rho\) runs from -1 to 1 and has no unit. It says how tightly the points sit around a line, not how steep the line is.

**Beta** is the slope of the line through those points, from part 13:

\[ \beta = \frac{\operatorname{Cov}(r_s, r_m)}{\operatorname{Var}(r_m)}, \qquad r_s = \alpha + \beta\, r_m + \varepsilon \]

- \(\beta\) is the stock's return per 1 unit of market return. A beta of 1.4 means 1.4% for a 1% market move on average.
- \(\alpha\) is the intercept: the return when the market return is zero. It is the part the market does not explain.
- \(\varepsilon\) is the residual: what is left on each day.

The slope and intercept are the ones that minimise the sum of squared residuals (ordinary least squares, OLS). Two more numbers say how good the fit is. **R squared**, \(R^2\), is the share of the stock's variance the market explains, and for one regressor it equals \(\rho^2\). The **standard error** of \(\beta\) says how far the estimate could be from the true slope: the estimate plus or minus two standard errors is a rough 95% range.

<div class="example" markdown>

### Worked example: five days by hand

Market returns in %: 1, -2, 0, 3, -1 (mean 0.2). Stock returns in %: 2, -3, 1, 5, -2 (mean 0.6).

1. Deviations from the means. Market: 0.8, -2.2, -0.2, 2.8, -1.2. Stock: 1.4, -3.6, 0.4, 4.4, -2.6.
2. Sum of products: 1.12 + 7.92 - 0.08 + 12.32 + 3.12 = 24.40. Sum of squares for the market: 0.64 + 4.84 + 0.04 + 7.84 + 1.44 = 14.80. For the stock: 1.96 + 12.96 + 0.16 + 19.36 + 6.76 = 41.20.
3. Beta = 24.40 / 14.80 = 1.65 (rounded).
4. Alpha = 0.6 - 1.65 x 0.2 = 0.27% a day.
5. Correlation = 24.40 / sqrt(14.80 x 41.20) = 24.40 / 24.69 = 0.99, and \(R^2\) = 0.98.

Five points is too few for any real conclusion. The method is the same for 781.

</div>

Download the files from lesson 2 ([stock-01.csv](../assets/data/stock-01.csv) to [stock-10.csv](../assets/data/stock-10.csv) and [index-x-3y.csv](../assets/data/index-x-3y.csv)). The made-up stocks were built as a multiple of the index return plus their own noise, so we know the true betas: stock-04 was built with a beta of 1.4 and stock-06 with 0.6.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

def load(name):
    return pd.read_csv(f"{name}.csv", parse_dates=["date"], index_col="date")["close"]

prices = pd.DataFrame({f"s{k:02d}": load(f"stock-{k:02d}") for k in range(1, 11)})
prices["index"] = load("index-x-3y")
rets = prices.pct_change().dropna()
corr = rets.corr()
print(corr.loc[["s05", "s10"], "index"].round(2).to_dict())
print(round(corr.loc["s01", "s02"], 2), round(corr.loc["s05", "s10"], 2))
beta = rets.cov()["index"] / rets["index"].var()
print(round(beta["s04"], 3), round(beta["s06"], 3))
```

The correlation with the index is 0.57 for stock-05 and 0.38 for stock-10. Between stocks it is lower: 0.32 for stock-01 and stock-02, and 0.19 for stock-05 and stock-10. The betas are 1.395 for stock-04 and 0.544 for stock-06, close to the 1.4 and 0.6 they were built with.

</details>

The `statsmodels` package gives a full regression table in one call, but it is not installed in this book's environment, so the next snippet does the same arithmetic with numpy. The standard error comes from the formula \(\sqrt{s^2 \,\text{diag}\,(X^\top X)^{-1}}\), where \(s^2\) is the residual variance with \(n - 2\) degrees of freedom and \(X\) holds a column of ones and the market returns.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

def load(name):
    return pd.read_csv(f"{name}.csv", parse_dates=["date"], index_col="date")["close"]

y = load("stock-04").pct_change().dropna()
x = load("index-x-3y").pct_change().dropna()
X = np.column_stack([np.ones(len(x)), x.to_numpy()])
coef, *_ = np.linalg.lstsq(X, y.to_numpy(), rcond=None)
resid = y.to_numpy() - X @ coef
n = len(y)
se = np.sqrt(resid @ resid / (n - 2) * np.diag(np.linalg.inv(X.T @ X)))
r2 = 1 - resid @ resid / ((y - y.mean()) @ (y - y.mean()))
alpha, beta = coef
print(n, round(beta, 3), round(se[1], 3), round(beta / se[1], 1))
print(round(alpha * 252, 3), round(se[0] * 252, 3), round(r2, 3))
print(round(resid.std(ddof=2) * np.sqrt(252), 3), round(beta - 2 * se[1], 2), round(beta + 2 * se[1], 2))
```

From 781 daily returns, the beta of stock-04 is 1.395 with a standard error of 0.09, which is a t-statistic of 15.4 (the estimate divided by its standard error). The annualised alpha is 0.281 (28.1% a year) with a standard error of 0.208, so alpha is 1.35 standard errors from zero and cannot be told from zero. \(R^2\) is 0.234: the index explains about 23% of the stock's variance. The residuals have an annualised volatility of 0.365. A rough 95% range for beta is 1.21 to 1.58.

</details>

The scatter shows the 781 points and the fitted line. The cloud is wide, which is what an \(R^2\) of 0.23 looks like.

![Daily returns of a made-up stock plotted against the made-up index, with a fitted line of slope 1.40](../assets/figures/20-quant-track-in-python/beta-scatter-dark.svg#only-dark)
![Daily returns of a made-up stock plotted against the made-up index, with a fitted line of slope 1.40](../assets/figures/20-quant-track-in-python/beta-scatter-light.svg#only-light)

The two parts of a stock's risk show up here. The part the market explains is **systematic** risk, and the residual is **idiosyncratic** risk, as in part 13. With an \(R^2\) of 0.23, most of stock-04's variance is its own.

A beta is not a fixed property. A rolling beta, calculated over the last 60 days, moves a lot:

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

def load(name):
    return pd.read_csv(f"{name}.csv", parse_dates=["date"], index_col="date")["close"]

y = load("stock-04").pct_change().dropna()
x = load("index-x-3y").pct_change().dropna()
roll = y.rolling(60).cov(x) / x.rolling(60).var()
print(round(roll.min(), 2), roll.idxmin().date(), round(roll.max(), 2), roll.idxmax().date())
```

The 60-day beta of stock-04 ranges from 0.67 (on February 9, 2024) to 2.12 (on July 12, 2024), around a true beta of 1.4. Nothing about the stock changed in this made-up data. The swings are estimation error.

</details>

So a beta from a short window can be off by a large amount, and a beta quoted without its window is not a complete number. The factor lesson in part 13 made the same point with 12 monthly returns ([Factor investing](../13-etfs-portfolios-and-factors/09-factor-investing.md)).

## Common mistakes

- Reading correlation as slope. A stock can have a correlation of 0.9 with the market and a beta of 0.5 if it is much less volatile.
- Mixing return frequencies. Betas from daily and from monthly returns differ, so compare like with like.
- Reading a regression result without its standard error. An alpha of 28% a year with a standard error of 21% is not a finding.

## Try it

1\. In the worked example the stock's correlation is 0.99 and its beta 1.65. Why is the beta well above 1 when the correlation is almost 1?

<details class="solution" markdown>
<summary>Answer</summary>

Beta = correlation x (stock volatility / market volatility). The stock's squared deviations (41.20) are larger than the market's (14.80), so its volatility is sqrt(41.20 / 14.80) = 1.67 times the market's. 0.988 x 1.67 = 1.65.

</details>

2\. A stock has beta 1.2 and alpha 0 over a window where the market rises 5%. What return does the regression predict for the stock, and if the market falls 5%?

<details class="solution" markdown>
<summary>Answer</summary>

1.2 x 5% = +6.0%. For a 5% fall: 1.2 x -5% = -6.0%.

</details>

3\. A beta estimate is 1.395 with a standard error of 0.09. Give the rough 95% range.

<details class="solution" markdown>
<summary>Answer</summary>

1.395 - 2 x 0.09 = 1.215 to 1.395 + 2 x 0.09 = 1.575, so about 1.21 to 1.58 with the unrounded numbers.

</details>

4\. \(R^2\) is 0.234. What is the correlation, and what share of the variance is the stock's own?

<details class="solution" markdown>
<summary>Answer</summary>

Correlation = sqrt(0.234) = 0.48 (positive, because the beta is positive). The stock's own share is 1 - 0.234 = 0.766, or 76.6%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Compute the beta of `stock-05` and `stock-10` against the index with the covariance formula. Which is closer to the beta it was built with (0.7 and 1.3)? |
| 3 | Run the 60-day rolling beta for `stock-05` and write down its minimum and maximum. |
| 2 | Write one sentence on how many days of data you would want before trusting a beta. |

</div>

## Key terms

- **Correlation**: the covariance of two series divided by the product of their standard deviations.
- **Beta**: the slope of a stock's returns on the market's returns.
- **Alpha**: the intercept of that regression, the part of return the market does not explain.
- **Residual**: the difference between a stock's return and the regression line.
- **Ordinary least squares (OLS)**: the fit that minimises the sum of squared residuals.
- **R squared**: the share of variance the regression explains.
- **Standard error**: how far an estimate is likely to be from the true value.
- **t-statistic**: an estimate divided by its standard error.

Next: [Factor sorts](07-factor-sorts.md)
