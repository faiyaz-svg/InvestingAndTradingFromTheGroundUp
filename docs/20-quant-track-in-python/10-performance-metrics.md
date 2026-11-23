# Performance metrics

<span class="tag tag-code">Code</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">QUANT</span>

After this lesson you can compute CAGR, annualised volatility, the Sharpe and Sortino ratios, maximum drawdown, the Calmar ratio and the hit rate from a series of returns, and say what each one hides.

Before this: [Returns and volatility in pandas](02-returns-and-volatility.md), [Drawdowns and risk of ruin](../03-risk-and-position-sizing/08-drawdowns-and-risk-of-ruin.md), [Modern portfolio theory](../13-etfs-portfolios-and-factors/08-modern-portfolio-theory.md), [Overfitting and out-of-sample testing](09-overfitting-and-out-of-sample.md). You need: Python with pandas and numpy.

## The idea

A strategy, a stock or a fund leaves behind a series of returns. A handful of numbers describe it: how fast it grew, how bumpy the ride was, what you earned for the bumps, and how deep the worst fall was.

This lesson computes the standard set on the daily returns of the made-up stock-04, then closes the part with a check.

## How it works

Take returns \(r_1, \ldots, r_n\) (simple, per day), the equity curve \(E_t = \prod_{i \le t}(1 + r_i)\) starting at 1, the number of years \(y = n/252\), and a risk-free rate \(r_f\) per year (assumed 2% here, a made-up round number).

**CAGR**, the compound annual growth rate, is the constant yearly return that gives the same total growth:

\[ \text{CAGR} = E_n^{1/y} - 1 \]

- \(E_n\) is the final value of the equity curve, a multiple of the starting value.
- \(y\) is in years.

**Annualised volatility** is \(\sigma\sqrt{252}\), from lesson 2, where \(\sigma\) is the standard deviation of daily returns.

The **Sharpe ratio** is the return above the risk-free rate per unit of volatility (part 13):

\[ \text{Sharpe} = \frac{\bar{r} - r_f/252}{\sigma}\sqrt{252} \]

- \(\bar{r}\) is the mean daily return, and \(r_f/252\) the daily risk-free rate.

The **Sortino ratio** replaces the standard deviation with the **downside deviation**, which counts only returns below a target (here the daily risk-free rate), so upside swings are not punished. Returns above the target count as 0, and the mean runs over all periods:

\[ \text{Sortino} = \frac{(\bar{r} - r_f/252)\times 252}{\sqrt{\operatorname{mean}\big(\min(r_t - r_f/252,\,0)^2\big)}\,\sqrt{252}} \]

The **maximum drawdown** is the worst fall from a previous peak, from part 3:

\[ D_t = \frac{E_t}{\max_{s \le t} E_s} - 1, \qquad \text{MaxDD} = \min_t D_t \]

The **Calmar ratio** is CAGR divided by the size of the maximum drawdown, \(\text{CAGR}/|\text{MaxDD}|\). Calmar is usually measured over three years and MAR over the whole history, but sources mix the names, so state the window. The **hit rate** is the share of periods with a positive return, \(\operatorname{mean}(r_t > 0)\).

<div class="example" markdown>

### Worked example: six months of returns

Monthly returns: +5%, -10%, +8%, +2%, -4%, +6%, with \(r_f = 0\). Annualising monthly data uses 12 periods and \(\sqrt{12}\).

1. Equity curve: 1.0500, 0.9450, 1.0206, 1.0410, 0.9994, 1.0593. Total return is 5.93%.
2. CAGR over 0.5 years: 1.0593^2 - 1 = 12.2%.
3. Mean monthly return 1.167%, standard deviation 6.88%. Annualised volatility = 6.88% x sqrt(12) = 23.8%.
4. Sharpe = (1.167 / 6.882) x sqrt(12) = 0.59.
5. Downside deviation: the negative months are -10% and -4%, so mean of squares over all 6 months = (0.01 + 0.0016) / 6 = 0.001933, root 4.40%, annualised 15.2%. Sortino = (1.167% x 12) / 15.2% = 0.92.
6. Maximum drawdown: the curve peaks at 1.05, then falls to 0.945, which is -10.0%. A later fall from 1.0410 to 0.9994 is -4.0%. So MaxDD = -10.0%.
7. Calmar = 12.2% / 10.0% = 1.22. Hit rate = 4 positive months out of 6 = 66.7%.

</div>

Download [stock-04.csv](../assets/data/stock-04.csv) if you do not have it.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

r = pd.read_csv("stock-04.csv", parse_dates=["date"], index_col="date")["close"].pct_change().dropna()
rf = 0.02                                              # assumed risk-free rate, per year
years = len(r) / 252
equity = (1 + r).cumprod()

cagr = equity.iloc[-1] ** (1 / years) - 1
vol = r.std() * np.sqrt(252)
sharpe = (r.mean() - rf / 252) / r.std() * np.sqrt(252)
downside = np.sqrt((np.minimum(r - rf / 252, 0) ** 2).mean()) * np.sqrt(252)
sortino = (r.mean() - rf / 252) * 252 / downside
drawdown = equity / equity.cummax() - 1
max_dd = drawdown.min()
calmar = cagr / abs(max_dd)
hit = (r > 0).mean()
print(round(years, 2), round(equity.iloc[-1] - 1, 3), round(cagr, 3), round(vol, 3))
print(round(sharpe, 2), round(sortino, 2), round(max_dd, 3), round(calmar, 2), round(hit, 3))
print(drawdown.idxmin().date(), equity.loc[:drawdown.idxmin()].idxmax().date())
```

The series has 781 returns, which is 3.1 years. The total return is 1.725 (+172.5%), the CAGR is 0.382 (38.2% a year) and the annualised volatility is 0.417. The Sharpe ratio is 0.94 and the Sortino ratio 1.37. The maximum drawdown is -0.294 (-29.4%), the Calmar ratio 1.3, and the hit rate 0.531 (53.1% of days up). The worst fall ran from the peak on February 23, 2024 to the trough on April 12, 2024.

</details>

The figure shows the drawdown curve: how far below its previous peak the stock stood on each day. Look at how long it spends below zero as well as how deep it goes.

![Drawdown curve of a made-up stock, spending most of three years below its previous peak, with a maximum drawdown of 29.4% in April 2024](../assets/figures/20-quant-track-in-python/drawdown-dark.svg#only-dark)
![Drawdown curve of a made-up stock, spending most of three years below its previous peak, with a maximum drawdown of 29.4% in April 2024](../assets/figures/20-quant-track-in-python/drawdown-light.svg#only-light)

### What each number hides

CAGR hides the path: two series with the same CAGR can have very different falls on the way. Volatility treats up and down moves the same. The Sharpe ratio suits roughly symmetric returns, and a strategy with small gains and rare large losses can show a high Sharpe until the loss arrives (part 13 made this point). The Sortino ratio fixes only the symmetry. Maximum drawdown is one path, and a longer history usually contains a worse fall. The hit rate says nothing about size: a rule that wins 90% of the time can still lose money ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)).

A metric from a backtest also carries the biases of lessons 8 and 9. A Sharpe ratio of 2 from the best of 100 variants is a different statement from a Sharpe ratio of 2 from one rule chosen in advance and tested on new data.

## Common mistakes

- Annualising a monthly series with 252. Use 12 and \(\sqrt{12}\) for monthly data.
- Comparing CAGRs without the drawdowns. Pair every return number with a risk number.

## Try it

1\. Monthly returns +4%, -2%, +3%. What is the total return and the hit rate?

<details class="solution" markdown>
<summary>Answer</summary>

1.04 x 0.98 x 1.03 = 1.0498, so +4.98%. Two of three months are positive, a hit rate of 66.7%.

</details>

2\. An equity curve goes 1.00, 1.20, 0.90, 1.10. What is the maximum drawdown?

<details class="solution" markdown>
<summary>Answer</summary>

The peak is 1.20 and the next low is 0.90: 0.90 / 1.20 - 1 = -25.0%.

</details>

3\. A series has an annual mean return of 15%, an annual volatility of 25% and a risk-free rate of 3%. Find the Sharpe ratio. If its downside deviation (annualised) is 15%, find the Sortino ratio.

<details class="solution" markdown>
<summary>Answer</summary>

Sharpe = (15 - 3) / 25 = 0.48. Sortino = (15 - 3) / 15 = 0.80.

</details>

## Part check

1\. A stock goes through a 2-for-1 split on a day when its raw close falls from 100.00 to 51.00. Which close do you use for the day's return, and what is the return if the adjusted closes are 50.00 and 51.00?

<details class="solution" markdown>
<summary>Answer</summary>

The adjusted close. The return is 51.00 / 50.00 - 1 = +2.0%. The raw close would show 51 / 100 - 1 = -49.0%, which is the split, not a loss.

</details>

2\. A stock has a daily standard deviation of 1.2%. What is the annual volatility?

<details class="solution" markdown>
<summary>Answer</summary>

1.2% x sqrt(252) = 1.2% x 15.87 = 19.05%, about 19.0%.

</details>

3\. A company's FY revenue is 400 million and its three quarterly 10-Q figures are 90, 95 and 100 million. What is Q4 revenue? A monthly CPI report for May is released on June 11. Which month's CPI should a backtest hold on June 5?

<details class="solution" markdown>
<summary>Answer</summary>

Q4 = 400 - (90 + 95 + 100) = 400 - 285 = 115 million. On June 5 the May report is not out, so the backtest holds April's CPI.

</details>

4\. A stock's correlation with the market is 0.5, its volatility is 30% and the market's is 15%. What is its beta?

<details class="solution" markdown>
<summary>Answer</summary>

Beta = correlation x (stock volatility / market volatility) = 0.5 x 30 / 15 = 1.0.

</details>

5\. A momentum sort over 36 months has an average monthly spread of 0.8% with a standard deviation of 3.0%. What is the t-statistic, and does it reach 2?

<details class="solution" markdown>
<summary>Answer</summary>

t = 0.8 / (3.0 / sqrt(36)) = 0.8 / 0.5 = 1.6. It does not reach 2.

</details>

6\. A test uses today's S&P 500 members for the whole of 2000 to 2025. Which bias is this, and does it raise or lower the result?

<details class="solution" markdown>
<summary>Answer</summary>

Survivorship bias. It raises the result, because companies that failed or were dropped from the index are missing.

</details>

7\. You test 50 rules with no skill and each has a 5% chance of passing a test at the 5% level. What is the chance that at least one passes?

<details class="solution" markdown>
<summary>Answer</summary>

1 - 0.95^50 = 1 - 0.077 = 0.923, about 92%.

</details>

8\. A strategy earns 12% a year with a volatility of 20%, and the risk-free rate is 2%. Its worst drawdown is 25%. What are its Sharpe ratio and its Calmar ratio?

<details class="solution" markdown>
<summary>Answer</summary>

Sharpe = (12 - 2) / 20 = 0.50. Calmar = 12 / 25 = 0.48.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the snippet on `stock-05.csv` and `index-x-3y.csv`. Write the CAGR, Sharpe and maximum drawdown of each. |
| 3 | Write which of the two you would rather hold and which number decided it. |
| 2 | Write which of the biases from lesson 8 or 9 would most change these numbers if they came from a backtest. |

</div>

## Key terms

- **CAGR**: the constant yearly return that gives the same total growth.
- **Equity curve**: the value of one unit of money invested at the start, over time.
- **Sharpe ratio**: the return above the risk-free rate per unit of volatility.
- **Downside deviation**: the root of the average squared shortfall below a target.
- **Sortino ratio**: excess return per unit of downside deviation.
- **Maximum drawdown**: the largest fall from a previous peak to a later low.
- **Calmar ratio**: CAGR divided by the size of the maximum drawdown.
- **Hit rate**: the share of periods with a positive return.

Next: [1929 and 1987](../21-crashes-scams-and-case-studies/01-1929-and-1987.md)
