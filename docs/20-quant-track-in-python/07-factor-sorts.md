# Factor sorts

<span class="tag tag-code">Code</span> <span class="tag tag-part">QUANT</span>

After this lesson you can rank a universe of stocks on a signal each month, split it into groups, compare the next month's returns across the groups, and say how much a result from 23 months of 10 stocks is worth.

Before this: [Factor investing](../13-etfs-portfolios-and-factors/09-factor-investing.md), [Market regime filters](../07-swing-trading/03-market-regime-filters.md), [Returns and volatility in pandas](02-returns-and-volatility.md). You need: Python with pandas and numpy.

## The idea

Part 13 described factors as characteristics that sort stocks into groups with different average returns. Researchers test a factor with a **sort**: at the end of each month, rank all stocks on the characteristic, split the ranking into equal groups, hold each group for the next month and compare the groups' returns. If the top group beats the bottom group month after month, the characteristic may carry a premium.

The sort is the same one the academic papers run on thousands of stocks, shrunk to ten made-up stocks over three years so you can see every step. The size of the sample is the main lesson of the end of this page.

## How it works

1. Get month-end prices and monthly returns. `resample("ME").last()` takes the last close of each month.
2. Compute the signal for each stock at each month end, using only data up to that date. For 12-1 momentum, from part 13, it is the return from 12 months ago to one month ago, \(P_{t-1}/P_{t-12} - 1\). The latest month is skipped because very recent returns partly reverse.
3. Rank the stocks within each month, and cut the ranks into groups. With 10 stocks and 5 groups (quintiles), each group has 2 stocks.
4. Line up each stock's return for the following month. In pandas, `ret.shift(-1)` moves next month's return onto this month's row.
5. Average the next-month return inside each group, and average over months. The difference between the top group and the bottom group is the **spread**.
6. Say how sure you are. For the monthly spreads \(s_1, \ldots, s_T\) the t-statistic is
\[ t = \frac{\bar{s}}{\operatorname{sd}(s)/\sqrt{T}} \]
where \(\bar{s}\) is the average spread, \(\operatorname{sd}(s)\) its standard deviation and \(T\) the number of months. A t-statistic above about 2 is the usual bar, and for a new factor researchers argue for a higher one (lesson 9).

<div class="example" markdown>

### Worked example: one month, September 30, 2024

The 12-1 signal for each stock at that date, sorted, with the group and the return in October 2024:

| Stock | Signal | Group | Next month |
|---|---|---|---|
| s10 | -0.514 | 1 | -21.2% |
| s05 | 0.045 | 1 | +6.2% |
| s08 | 0.060 | 2 | -3.3% |
| s06 | 0.084 | 2 | -0.7% |
| s07 | 0.140 | 3 | -19.8% |
| s01 | 0.145 | 3 | -3.4% |
| s09 | 0.350 | 4 | -3.8% |
| s02 | 0.582 | 4 | +3.4% |
| s04 | 0.691 | 5 | -4.9% |
| s03 | 1.103 | 5 | -5.2% |

1. Top group (s04, s03): (-4.9 - 5.2) / 2 = -5.05%, which the code prints more exactly as -5.08%.
2. Bottom group (s10, s05): (-21.2 + 6.2) / 2 = -7.5%, printed as -7.47%.
3. Spread: -5.08 - (-7.47) = +2.39 points. The winners fell, but by less than the losers.

One month with 2 stocks per group is noise. The sort only means something over many months.

</div>

Download the ten stock files from lesson 2 if you have not already ([stock-01.csv](../assets/data/stock-01.csv) to [stock-10.csv](../assets/data/stock-10.csv)).

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

prices = pd.DataFrame({f"s{k:02d}": pd.read_csv(f"stock-{k:02d}.csv", parse_dates=["date"], index_col="date")["close"] for k in range(1, 11)})
month = prices.resample("ME").last()
ret = month.pct_change()
signal = month.shift(1) / month.shift(12) - 1       # 12-1 momentum, known at month end
nxt = ret.shift(-1)                                 # the following month's return
print(month.shape, len(signal.dropna(how="all")), signal.dropna(how="all").index[0].date())
d = pd.Timestamp("2024-09-30")
group = np.ceil(signal.loc[d].rank(method="first") / 2).astype(int)   # 10 stocks, 2 per group
print(pd.DataFrame({"signal": signal.loc[d].round(3), "group": group, "next": nxt.loc[d].round(3)}).sort_values("signal").to_string())
print(round(nxt.loc[d][group == 5].mean(), 4), round(nxt.loc[d][group == 1].mean(), 4))
```

There are 36 month ends, and the signal exists for 24 of them, starting at January 31, 2024. The table is the one in the worked example, and the last line prints the group averages -0.0508 (top) and -0.0747 (bottom).

</details>

Now the whole sort, for two signals. Low volatility ranks stocks by the negative of their 12-month standard deviation of monthly returns, so the calmest stocks are in group 5. The function skips months where a signal or next-month return is missing, which leaves 23 months.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import pandas as pd

prices = pd.DataFrame({f"s{k:02d}": pd.read_csv(f"stock-{k:02d}.csv", parse_dates=["date"], index_col="date")["close"] for k in range(1, 11)})
month = prices.resample("ME").last()
ret = month.pct_change()
nxt = ret.shift(-1)
mom = month.shift(1) / month.shift(12) - 1
lowvol = -ret.rolling(12).std()                     # higher score = calmer stock

def sort_report(signal):
    ok = signal.notna().all(axis=1) & nxt.notna().all(axis=1)
    g = np.ceil(signal[ok].rank(axis=1, method="first") / 2)
    by_group = [round(float(nxt[ok][g == q].stack().mean()), 4) for q in (1, 2, 3, 4, 5)]
    spread = nxt[ok][g == 5].mean(axis=1) - nxt[ok][g == 1].mean(axis=1)
    t = spread.mean() / (spread.std() / np.sqrt(len(spread)))
    return len(spread), by_group, round(float(spread.mean()), 4), round(float(t), 2), round(float((spread > 0).mean()), 2)

print(sort_report(mom))
print(sort_report(lowvol))
```

For momentum there are 23 months. The average next-month returns for groups 1 to 5 are -1.08%, 1.83%, 0.16%, 3.83% and 1.18%. The spread averages 2.26% a month, its t-statistic is 1.12, and the spread is positive in 57% of the months. For low volatility the spread averages 2.01% a month with a t-statistic of 1.05, positive in 65% of the months.

</details>

The bars show the momentum result. The groups are not in a neat staircase: group 4 beats group 5.

![Average next-month return for five momentum groups of ten made-up stocks, which does not rise steadily from group 1 to group 5](../assets/figures/20-quant-track-in-python/momentum-groups-dark.svg#only-dark)
![Average next-month return for five momentum groups of ten made-up stocks, which does not rise steadily from group 1 to group 5](../assets/figures/20-quant-track-in-python/momentum-groups-light.svg#only-light)

## How much to believe it

A spread of 2.26% a month looks large. A t-statistic of 1.12 says it is not: with 23 months and a spread that swings by about 10 points either way, luck gives a number like this often. Neither sort passes the usual bar of 2. The made-up stocks were built with different, persistent drifts, so some momentum is really there, but 23 months cannot show it.

The caveats that apply to this toy apply, in smaller form, to a real sort:

- Only 10 stocks and 2 per group. Real tests use thousands of stocks and groups of hundreds.
- A fixed list of stocks. The universe here is the ten that exist at the end, so the sort never sees a stock that dropped out, which is survivorship (lesson 8).
- No costs. Rebalancing every month means many trades, and each one pays the spread and slippage.
- Equal weights, no limits on size or liquidity. Small, thinly traded stocks drive many published results and are costly to trade.
- The signal uses the shift described in step 2. Without the shift, the sort would peek at the month it is trying to predict.

Published studies find real factor premiums on large samples and also find that they shrink after publication: McLean and Pontiff (2016, [Journal of Finance](https://doi.org/10.1111/jofi.12365)) put the drop at 58% after the papers appeared, as part 13 reports.

## Common mistakes

- Ranking on information that was not yet known at the month end, such as a number from a filing made later (lesson 4).
- Forgetting to shift the return. Group returns for the same month as the signal are partly the signal's own cause.
- Reading a spread without its t-statistic or its number of months.

## Try it

1\. Five stocks have signals 0.30, -0.10, 0.05, 0.60 and 0.20. Rank them from the lowest signal (rank 1) and name the top-ranked stock's signal.

<details class="solution" markdown>
<summary>Answer</summary>

Sorted: -0.10 (rank 1), 0.05 (2), 0.20 (3), 0.30 (4), 0.60 (5). The top-ranked stock has signal 0.60.

</details>

2\. Ten stocks and five groups: which two ranks form group 3? Use `np.ceil(rank / 2)`.

<details class="solution" markdown>
<summary>Answer</summary>

ceil(5 / 2) = 3 and ceil(6 / 2) = 3. Ranks 5 and 6, the two middle stocks, form group 3.

</details>

3\. Monthly spreads over 4 months are +2%, -1%, +3% and 0%. What are the mean, the standard deviation (sample, divide by 3) and the t-statistic?

<details class="solution" markdown>
<summary>Answer</summary>

Mean = 4 / 4 = 1.0%. Deviations: 1, -2, 2, -1, squares 1, 4, 4, 1, sum 10. Variance = 10 / 3 = 3.33, standard deviation = 1.826%. t = 1.0 / (1.826 / sqrt(4)) = 1.0 / 0.913 = 1.10.

</details>

4\. A group of stocks earns 2.26% a month more than the bottom group with a t-statistic of 1.12 over 23 months. What would the t-statistic be with the same mean and standard deviation over 92 months?

<details class="solution" markdown>
<summary>Answer</summary>

The t-statistic grows with the square root of the number of months. 92 / 23 = 4, and sqrt(4) = 2, so t = 1.12 x 2 = 2.24. The same average spread would pass the usual bar of 2 with four times as much data.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Change the momentum signal to a 6-1 month signal (`shift(1) / shift(6) - 1`) and run the sort. Write the spread and t-statistic. |
| 3 | Run it again with 3 groups instead of 5 (use `np.ceil(rank / (10 / 3))`) and write whether the spread got bigger. |
| 2 | Write which of the five caveats above would change the result most for a real sort, and why. |

</div>

## Key terms

- **Sort**: ranking stocks on a signal and grouping them to compare later returns.
- **Signal**: the number a sort ranks on.
- **Quintile**: one fifth of a ranked list.
- **Spread (of a sort)**: the average return of the top group minus the bottom group.
- **Universe**: the list of stocks a test covers.
- **Rebalance (a sort)**: forming the groups again at each month end.

Next: [Backtesting concepts and biases](08-backtesting-concepts-and-biases.md)
