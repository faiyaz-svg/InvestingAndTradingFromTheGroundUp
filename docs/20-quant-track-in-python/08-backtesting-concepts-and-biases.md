# Backtesting concepts and biases

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">QUANT</span>

After this lesson you can say what a backtest is, name the five ways it overstates a rule's results, and spot each one in a short piece of code.

Before this: [Moving averages](../05-reading-charts/05-moving-averages.md), [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md), [Fundamentals from EDGAR](04-fundamentals-from-edgar.md), [Factor sorts](07-factor-sorts.md). You need: Python with pandas for the snippets.

## The idea

You have a rule: buy when the 20-day average crosses above the 50-day average, sell when it crosses back. Before you risk money, you ask what the rule would have earned over the last three years. Answering that by replaying the rule on past prices is a **backtest**.

A backtest is an estimate of the past, made by you, with every choice in your hands. That is why it flatters. This book teaches backtesting as a set of ideas, not as software. It builds no backtester: there is no engine here that you can point at a strategy, because the point of this lesson is to see how the numbers go wrong, and four lines of pandas are enough to show each case.

## How it works

A backtest has three parts: a rule that turns data into a position (long, short or flat), the past returns that position would have earned, and a costing of the trades. Each part has a trap.

### Lookahead bias

**Lookahead bias** is using information that was not available when the decision was made. The commonest form is a one-bar mistake: a rule reads today's close, and the code applies the position to today's return, as if you could trade at a close you have already seen.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

close = pd.read_csv("index-x-3y.csv", parse_dates=["date"], index_col="date")["close"]
ret = close.pct_change().fillna(0)
signal = (ret > 0).astype(int)              # "hold on days the market rises"
cheat = signal * ret                        # uses today's return to decide today's position
honest = signal.shift(1).fillna(0) * ret    # position decided on yesterday's close
print(round((1 + cheat).prod() - 1, 1), round((1 + honest).prod() - 1, 3), round((1 + ret).prod() - 1, 3))
```

Download [index-x-3y.csv](../assets/data/index-x-3y.csv), a made-up index for 782 trading days. The rule "hold on days the market rises" is absurd, and with lookahead it earns 17.7, a gain of 1,770% over three years. Shifting the signal by one bar, so the position comes from yesterday's close, gives -0.057 (-5.7%). Buying and holding the index earned 0.291 (+29.1%).

</details>

The figure shows both lines on a log scale. The only difference between them is `shift(1)`.

![Growth of 1 on a log scale for the same rule with and without lookahead: one line climbs to about 19 and the other stays near 1](../assets/figures/20-quant-track-in-python/lookahead-dark.svg#only-dark)
![Growth of 1 on a log scale for the same rule with and without lookahead: one line climbs to about 19 and the other stays near 1](../assets/figures/20-quant-track-in-python/lookahead-light.svg#only-light)

Lookahead hides in other places. Fundamentals used on the period end instead of the filing date (lesson 4), macro numbers used on the month they describe (lesson 5), an average computed over the whole sample, a high or low from the day's bar used to enter at the open. The test for each is the same: could you have known this value, at that moment, with the tools of the time?

### Survivorship bias

**Survivorship bias** is testing on the stocks that still exist today. Companies that went bankrupt, were delisted or were bought at a loss are missing from many free datasets, and a test on the survivors looks better than the history that investors lived through. Elton, Gruber and Blake (1996) measured the effect for mutual funds, where funds that closed are missing from the databases ([Review of Financial Studies, 9(4), 1097-1120](https://doi.org/10.1093/rfs/9.4.1097)).

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

total = {}
for k in range(1, 11):
    c = pd.read_csv(f"stock-{k:02d}.csv", parse_dates=["date"], index_col="date")["close"]
    total[f"s{k:02d}"] = c.iloc[-1] / c.iloc[0] - 1
total = pd.Series(total)
dropped = total[total < -0.5].index.tolist()      # a vendor that drops stocks that collapse
print(dropped, round(total.mean(), 3), round(total.drop(dropped).mean(), 3))
print(len(total) - len(dropped), round(total.median(), 3))
```

Of the ten made-up stocks ([stock-01.csv](../assets/data/stock-01.csv) to [stock-10.csv](../assets/data/stock-10.csv)), one, `s10`, lost more than half. The average three-year return of all ten is 0.663 (+66.3%). If the dataset has dropped `s10` and holds nine stocks, the average is 0.824 (+82.4%), which is 16 points better for no reason except missing data. The median of all ten is 0.547.

</details>

### Costs

A backtest that ignores costs counts every signal as free. Each trade pays the bid-ask spread and often slippage and commissions (part 3, [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)). A rule that trades often loses much of its edge there.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

close = pd.read_csv("index-x-3y.csv", parse_dates=["date"], index_col="date")["close"]
ret = close.pct_change().fillna(0)
fast, slow = close.rolling(20).mean(), close.rolling(50).mean()
position = (fast > slow).astype(int).shift(1).fillna(0)     # decided on yesterday's close
trades = position.diff().abs().fillna(0)
gross = position * ret
net = gross - trades * 0.0010                               # 10 bps (0.10%) per switch, assumed
print(int(trades.sum()), round((1 + gross).prod() - 1, 3), round((1 + net).prod() - 1, 3), round((1 + ret).prod() - 1, 3))
```

An SMA 20 and SMA 50 crossover on the same index switches position 19 times in three years. Before costs it returns 0.060 (+6.0%). After an assumed cost of 10 basis points (0.10%) per switch, it returns 0.040 (+4.0%). Buying and holding earned 0.291. The cost here is small because the rule trades rarely; the bigger finding is that the rule earned less than the index.

</details>

### Selection bias and overfitting

**Selection bias** (also called data snooping) is trying many rules or parameters on the same data and showing only the best one. If you test 50 moving-average lengths, the winner is partly the winner by luck. **Overfitting** is a rule shaped so closely to one stretch of data that it describes noise, not a pattern that repeats. Lesson 9 measures both, and part 5 gave the evidence for moving averages: Sullivan, Timmermann and White (1999) re-tested a large universe of trading rules and corrected for data snooping ([Journal of Finance, 54(5), 1647-1691](https://doi.org/10.1111/0022-1082.00163)).

### Other things that differ from trading

A backtest also assumes fills at the price in the data, no market impact, no halts, and a stable world. Your orders may not fill at the close you saw, a big order moves the price, and the market of 2025 is not the market of 2005.

## Reading a backtest report

When someone gives you a backtest, ask these questions in order. The answers decide whether the number deserves attention.

1. When is the signal computed, and when is the trade assumed to happen?
2. Does the universe include stocks that died?
3. What costs and slippage were applied, and are they realistic for this size?
4. How many rules or parameters were tried before this one?
5. What happened on data the rule never saw (lesson 9)?

## Common mistakes

- Applying a signal to the same bar that produced it. Shift it by one bar and compare.
- Testing on today's index members. The list of members was not known years ago, and it leaves out the failures.
- Reporting a return without costs, or with costs from a different kind of trading.

## Try it

1\. Daily returns are +1%, -2% and +3%. The rule holds on a day when the return is positive. With lookahead, what is the three-day return? Without it (position from the previous day's signal, flat on day 1)?

<details class="solution" markdown>
<summary>Answer</summary>

With lookahead the rule holds on days 1 and 3: 1.01 x 1.03 - 1 = +4.03%. Without it, the position on day 2 comes from day 1's signal (up, so long) and earns -2%; the position on day 3 comes from day 2's signal (down, so flat) and earns 0. The total is 0.98 - 1 = -2.0%.

</details>

2\. A rule switches position 40 times a year, and each switch costs 0.10%. What is the yearly cost, and how much does a 6.0% gross yearly return fall to (subtract the cost)?

<details class="solution" markdown>
<summary>Answer</summary>

40 x 0.10% = 4.0% a year. 6.0% - 4.0% = 2.0% a year after costs.

</details>

3\. Nine surviving stocks averaged +82.4% and a tenth fell 79.0%. What is the average of all ten?

<details class="solution" markdown>
<summary>Answer</summary>

(9 x 82.4 + (-79.0)) / 10 = (741.6 - 79.0) / 10 = 662.6 / 10 = 66.3%. The survivors-only average overstates by 16.1 points.

</details>

4\. A report says "the best of 40 parameter sets returned 18% a year". Which two questions from the list would you ask first?

<details class="solution" markdown>
<summary>Answer</summary>

Question 4, how many rules or parameters were tried (40, so the best is partly luck), and question 5, how it did on data it never saw.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Run the first snippet. Replace `shift(1)` with `shift(2)` and write what the return is. Then explain in one sentence why a shift of 1 is the minimum. |
| 3 | In the cost snippet change the cost to 0.50% per switch and write the net return. |
| 2 | Pick a backtest claim you have seen online and write which of the five questions it does not answer. |

</div>

## Key terms

- **Backtest**: replaying a rule on past data to estimate what it would have earned.
- **Lookahead bias**: using information that was not yet available at the time of the decision.
- **Survivorship bias**: testing only on the companies or funds that still exist.
- **Selection bias (data snooping)**: reporting the best of many tries without counting the tries.
- **Overfitting**: fitting a rule so closely to past data that it describes noise.
- **Basis point (bp)**: one hundredth of a percentage point, 0.01%.

Next: [Overfitting and out-of-sample testing](09-overfitting-and-out-of-sample.md)
