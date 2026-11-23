# Part 20: Quant track in Python

pandas for prices and fundamentals, returns and volatility, regression, factor sorts and how backtests mislead.

Before this part: Parts 5, 9 and 19. The CS book's Python basics lessons.

<!-- lessons:start -->
## Lessons

1. [Python and pandas for prices](01-python-and-pandas-for-prices.md) (code)
2. [Returns and volatility in pandas](02-returns-and-volatility.md) (code)
3. [Indicators in pandas](03-indicators-in-pandas.md) (code)
4. [Fundamentals from EDGAR](04-fundamentals-from-edgar.md) (code)
5. [Macro data from FRED and Treasury](05-macro-data-from-fred-and-treasury.md) (code)
6. [Correlation, beta and regression](06-correlation-beta-and-regression.md) (code)
7. [Factor sorts](07-factor-sorts.md) (code)
8. [Backtesting concepts and biases](08-backtesting-concepts-and-biases.md) (idea)
9. [Overfitting and out-of-sample testing](09-overfitting-and-out-of-sample.md) (idea)
10. [Performance metrics](10-performance-metrics.md) (code, review)

<!-- lessons:end -->

## Cheat sheet

### Formulas

| Quantity | Formula | pandas |
|---|---|---|
| Simple return | \(P_t/P_{t-1} - 1\) | `close.pct_change()` |
| Log return | \(\ln(P_t/P_{t-1})\) | `np.log(close).diff()` |
| Annual volatility | \(\sigma_{\text{daily}}\sqrt{252}\) (weekly \(\sqrt{52}\), monthly \(\sqrt{12}\)) | `r.std() * np.sqrt(252)` |
| SMA \(N\) | mean of the last \(N\) closes | `close.rolling(N).mean()` |
| EMA \(N\) | \(k = 2/(N+1)\), seeded with the SMA (charts) | `ewm(alpha=k, adjust=False)` after seeding, or `ewm(span=N, adjust=False)` (seeded with the first close) |
| Wilder average | \(k = 1/N\), seeded with the plain mean of the first \(N\) | `ewm(alpha=1/N, adjust=False)` after seeding |
| RSI | \(100 - 100/(1 + \bar G/\bar L)\) | Wilder averages of gains and losses |
| ATR | Wilder average of true range | `max(high-low, abs(high-prev), abs(low-prev))` |
| Beta | \(\operatorname{Cov}(r_s, r_m)/\operatorname{Var}(r_m)\) | `rets.cov()["m"] / rets["m"].var()` |
| t-statistic | estimate / standard error | `mean / (std / np.sqrt(n))` |
| CAGR | \(E_n^{1/y} - 1\) | `equity.iloc[-1] ** (252 / n) - 1` |
| Sharpe | \((\bar r - r_f/252)/\sigma \cdot \sqrt{252}\) | `(r.mean() - rf/252) / r.std() * np.sqrt(252)` |
| Max drawdown | \(\min_t (E_t / \max_{s\le t} E_s - 1)\) | `(equity / equity.cummax() - 1).min()` |
| Calmar | CAGR / abs(max drawdown) | `cagr / abs(max_dd)` |
| Expected best Sharpe of \(N\) no-skill trials | \(\sigma_{SR}[(1-\gamma)Z^{-1}(1-1/N) + \gamma Z^{-1}(1-1/(Ne))]\) | `statistics.NormalDist().inv_cdf` |

### Data rules

| Data | Rule |
|---|---|
| Prices | `read_csv(..., parse_dates=["date"], index_col="date")`; use the adjusted close for returns, the raw close for the price on the day |
| Weekly bars | `resample("W-FRI")`: open first, high max, low min, close last, volume sum |
| EDGAR facts | keep the latest `filed` for each `end`; length of period from `start` and `end`; Q4 = FY - (Q1 + Q2 + Q3); join on `filed`, not `end` |
| EDGAR requests | real contact in the User-Agent, at most 10 requests a second |
| FRED | your own free API key; "." is a missing value |
| Treasury CSV | dates are `%m/%d/%Y`, newest row first: sort the index |
| Monthly macro with daily prices | `merge_asof` on the release date |

### Before you trust a backtest

1. Signal on yesterday's close, trade after it (`shift(1)`).
2. The universe includes the stocks that died.
3. Costs and slippage are in.
4. The number of trials is counted, and a deflated Sharpe ratio or a t-statistic above about 3 is used for the best of many.
5. A test period the rule never saw, looked at once.
6. Metrics come in pairs: a return with a drawdown, a Sharpe ratio with its error (about 1 for one year of daily data).
