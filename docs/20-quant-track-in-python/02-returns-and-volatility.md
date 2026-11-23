# Returns and volatility in pandas

<span class="tag tag-code">Code</span> <span class="tag tag-part">QUANT</span>

After this lesson you can compute simple and log returns from a price column, say which one to add and which one to multiply, and turn a daily standard deviation into an annual volatility.

Before this: [Python and pandas for prices](01-python-and-pandas-for-prices.md), [Risk first](../03-risk-and-position-sizing/01-risk-first.md). The math book covers [standard deviation](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/01-descriptive-statistics-and-study-design/) and [continuous compounding and e](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/02-interest-and-growth/04-continuous-compounding-and-e/), which holds the natural logarithm you need. You need: Python with pandas and numpy.

## The idea

A price of 110 means little on its own. The return, the change relative to the starting price, is what you can compare across stocks, years and position sizes. Models in finance work on returns, not prices, because a 10% move means the same thing at a price of 10 or of 1,000.

Take a stock that goes 100, 110, 99. It rises 10% and then falls 10%. The two returns add to zero, yet you ended at 99, a loss of 1%. Returns that you add up this way lie, and this lesson shows which kind of return to add.

## How it works

The **simple return** from one bar to the next is the percentage change, as in lesson 1 of part 1:

\[ r_t = \frac{P_t}{P_{t-1}} - 1 \]

- \(P_t\) is the close at bar \(t\), in US$, and \(P_{t-1}\) the close one bar earlier.
- \(r_t\) is a fraction with no unit (0.10 is 10%).

The **log return** is the natural logarithm of the price ratio:

\[ \ell_t = \ln\frac{P_t}{P_{t-1}} \]

- \(\ln\) is the natural logarithm. \(\ell_t\) has no unit.
- For small moves the two are close, and \(\ell_t = \ln(1 + r_t)\) always.

They combine differently. Over many bars, simple returns multiply: \((1 + r_1)(1 + r_2)\cdots - 1\). Log returns add: the sum of the \(\ell_t\) is \(\ln(P_T / P_0)\), the log of the whole move. So use log returns to add across time. Use simple returns to add across assets on one day, because a portfolio's simple return is the weighted sum of its holdings' simple returns.

<div class="example" markdown>

### Worked example: 100, 110, 99

1. Simple returns: 110 / 100 - 1 = +10.0%, then 99 / 110 - 1 = -10.0%. Their sum is 0.0%, and the true change is 99 / 100 - 1 = -1.0%.
2. Compounded: 1.10 x 0.90 = 0.99, so -1.0%. Multiplying gives the right answer.
3. Log returns: ln(1.10) = 0.0953 and ln(0.90) = -0.1054. The sum is -0.0101, and ln(0.99) = -0.0101. Adding works.
4. Convert back: e^(-0.0101) - 1 = -1.0%.

</div>

### Volatility and annualising

**Volatility** is the standard deviation of returns: how widely the returns spread around their average. A daily volatility of 1.9% says a typical day moves about 1.9% up or down. To compare stocks and to compare with a yearly number, we scale to a year. If daily returns are independent, their variances add over days, so the standard deviation over \(N\) days is \(\sqrt{N}\) times the daily one:

\[ \sigma_{\text{annual}} = \sigma_{\text{daily}} \times \sqrt{252} \]

- \(\sigma_{\text{daily}}\) is the standard deviation of daily returns (a fraction).
- 252 is the usual count of US trading days in a year, a convention, not a law. Some desks use 250 or 260.
- To annualise a weekly standard deviation use \(\sqrt{52}\), and a monthly one \(\sqrt{12}\).

The \(\sqrt{N}\) rule assumes returns are independent from day to day. With trends or reversals it is only an approximation. Also, the annual average return scales by \(252\), not \(\sqrt{252}\), which is why risk grows more slowly than return as you hold longer.

Download [stock-01.csv](../assets/data/stock-01.csv) through [stock-10.csv](../assets/data/stock-10.csv) and [index-x-3y.csv](../assets/data/index-x-3y.csv). They are made up: ten stocks and an index over the same 782 days, built so that each stock moves partly with the index.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

close = pd.read_csv("stock-01.csv", parse_dates=["date"], index_col="date")["close"]
simple = close.pct_change()
log = np.log(close).diff()
print(round(simple.iloc[1], 4), round(log.iloc[1], 4))
print(round(close.iloc[-1] / close.iloc[0] - 1, 3), round((1 + simple).prod() - 1, 3), round(np.expm1(log.sum()), 3))
print(round(simple.sum(), 3), round(log.sum(), 3))
print(round(simple.mean(), 6), round(log.mean(), 6), round(simple.mean() - simple.std() ** 2 / 2, 6))
```

The first day's return is -0.0408 as a simple return and -0.0416 as a log return. The whole three-year move is 0.577 (+57.7%) three ways: from the first and last close, by multiplying the simple returns, and by adding the log returns and converting back. Adding the simple returns gives 0.601, which is wrong; adding the log returns gives 0.456, which is the log of the whole move. The last line shows that the mean log return (0.000583 a day) is below the mean simple return (0.000769) by about half the variance, \(\sigma^2/2\).

</details>

The gap between those two averages is called volatility drag. A stock that is volatile loses growth even when its average simple return is fixed, which is why part 3 says that big losses cost more than their size ([Risk first](../03-risk-and-position-sizing/01-risk-first.md)).

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

names = [f"stock-{k:02d}" for k in range(1, 11)] + ["index-x-3y"]
prices = pd.DataFrame({n: pd.read_csv(f"{n}.csv", parse_dates=["date"], index_col="date")["close"] for n in names})
rets = prices.pct_change().dropna()
annual = rets.std() * np.sqrt(252)
print(annual.sort_values().round(3).iloc[[0, -1]].to_dict())
r = rets["stock-01"]
print(round(r.std(), 4), round(r.std() * np.sqrt(252), 3))
roll = r.rolling(20).std() * np.sqrt(252)
print(roll.idxmin().date(), round(roll.min(), 3), roll.idxmax().date(), round(roll.max(), 3))
```

The least volatile series is the index at 0.145 (14.5% a year) and the most volatile is stock-10 at 0.484. For stock-01 the daily standard deviation is 0.0193 and the annual one is 0.306. The 20-day rolling volatility of stock-01 ranges from 0.152 on January 10, 2024 to 0.438 on March 12, 2024, which is what the figure shows.

</details>

The next figure draws the 20-day rolling volatility of stock-01 and of the index. Look at how it rises together in the early-2024 sell-off and how it is never constant.

![The 20-day annualised volatility of a made-up stock and a made-up index, with both rising in early 2024](../assets/figures/20-quant-track-in-python/rolling-volatility-dark.svg#only-dark)
![The 20-day annualised volatility of a made-up stock and a made-up index, with both rising in early 2024](../assets/figures/20-quant-track-in-python/rolling-volatility-light.svg#only-light)

A single annual volatility number hides this. Volatility tends to come in clusters, so part 16 treats it as something that moves (see Realized and implied volatility<!-- link: ../16-volatility-and-event-trading/01-realized-vs-implied-volatility.md -->).

## Common mistakes

- Adding simple returns across time. Compound them (multiply), or add log returns.
- Annualising with the wrong count. A daily series uses \(\sqrt{252}\); a weekly series uses \(\sqrt{52}\). Using 252 on a weekly series overstates volatility by more than twice.
- Comparing a volatility from 20 days with one from 3 years. The window changes the answer, so say how many days you used.

## Try it

1\. A stock goes 50.00, 55.00, 52.25. Find the two simple returns, their sum, and the true total return.

<details class="solution" markdown>
<summary>Answer</summary>

55 / 50 - 1 = +10.0%; 52.25 / 55 - 1 = -5.0%. The sum is +5.0%. The true total is 52.25 / 50 - 1 = +4.5%, so adding overstates by 0.5 points.

</details>

2\. For the same prices, find the two log returns and show that their sum matches the total.

<details class="solution" markdown>
<summary>Answer</summary>

ln(1.10) = 0.0953 and ln(0.95) = -0.0513. The sum is 0.0440. ln(52.25 / 50) = ln(1.045) = 0.0440. They match, and e^0.0440 - 1 = 4.5%.

</details>

3\. Daily volatility is 1.5%. What is the annual volatility? What is the weekly one?

<details class="solution" markdown>
<summary>Answer</summary>

Annual: 1.5% x sqrt(252) = 1.5% x 15.87 = 23.8%. Weekly: 1.5% x sqrt(5) = 3.35%, using 5 trading days in a week.

</details>

4\. A stock has an annual volatility of 30%. What daily move is one standard deviation, and how many days in 252 would you expect beyond it if returns were normal?

<details class="solution" markdown>
<summary>Answer</summary>

Daily volatility = 30% / sqrt(252) = 1.89%. For a normal distribution about 31.7% of days fall beyond one standard deviation (either way), so about 0.317 x 252 = 80 days.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Load `stock-05.csv` and `stock-10.csv`. Print each one's annual volatility and its three-year simple return. |
| 4 | Print the 60-day rolling annual volatility of `stock-05` and find its highest value and date. |
| 2 | Write one line on why you would not compare these two numbers from windows of different lengths. |

</div>

## Key terms

- **Simple return**: the percentage change in price, \(P_t / P_{t-1} - 1\).
- **Log return**: the natural log of the price ratio; it adds across time.
- **Volatility**: the standard deviation of returns.
- **Annualise**: scale a per-period volatility to a year, by \(\sqrt{252}\) for daily data.
- **Rolling window**: a calculation repeated over the last N bars as the window moves forward.
- **Volatility drag**: the gap between the average simple return and the average log return, about half the variance.

Next: [Indicators in pandas](03-indicators-in-pandas.md)
