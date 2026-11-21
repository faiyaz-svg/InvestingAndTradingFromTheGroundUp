# Reviewing your trades

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">MIND</span>

After this lesson you can run a 20-minute weekly review, split your results by setup and by plan-following, and say how much a small number of trades can and cannot tell you.

Before this: [The trade journal](04-the-trade-journal.md). You need: a calculator, and your journal if you have one.

## The idea

A journal that nobody reads is a diary. The review is where the entries become decisions: which setup to keep, which rule you keep breaking, what to change next week.

There is one trap to avoid first. [Baron and Hershey (1988)](https://doi.org/10.1037/0022-3514.54.4.569) gave people the same decision made with the same information, and told them different outcomes. People rated the decision better when the outcome was good, and worse when it was bad. That is **outcome bias**: judging a decision by how it turned out instead of by what was known when it was made. A trade that followed the plan and lost was still a good decision. A trade that broke the plan and won was still a bad one, and rewarding it teaches you to repeat it.

So the review judges two things apart: the **process** (did I follow the plan?) and the **outcome** (what was the result in R?).

## How it works

### The weekly review

Do it at a set time, once a week, for about 20 minutes.

1. Check that every trade of the week is in the journal, both stages. Fill gaps now and mark them "late".
2. Count the rule breaks and write the reason for each in a few words.
3. Update the numbers: trade count, win rate, average win and average loss in R, expectancy, total R.
4. Split the results by setup and by "followed the plan".
5. Pick at most one change for next week, written as a rule. Change nothing that the numbers do not point to.

A monthly review adds a longer look: the largest loss, the longest losing streak, the time of day and the market conditions where the setups worked or failed.

### Reading the numbers

The 20 made-up trades below come from two setups, Breakout and Pullback. Look at the bars (each trade in R), the running total, and the four trades marked as plan breaks.

![Bar chart of 20 made-up trades in R with the running total, four trades marked as breaking the plan](../assets/figures/04-psychology-journal-and-paper-trading/r-results-dark.svg#only-dark)
![Bar chart of 20 made-up trades in R with the running total, four trades marked as breaking the plan](../assets/figures/04-psychology-journal-and-paper-trading/r-results-light.svg#only-light)

<div class="example" markdown>

### Worked example: a review of 20 trades

Overall: 20 trades, 10 winners, 10 losers.

1. Win rate = 10 / 20 = 50%.
2. Average win = +1.82R. Average loss = -1.20R (this includes two losses larger than 1R).
3. Expectancy = 0.5 x 1.82 + 0.5 x (-1.20) = +0.31R per trade. Total = 20 x 0.31 = +6.2R.

By setup:

| Setup | Trades | Winners | Total R | Average R |
|---|---|---|---|---|
| Breakout | 10 | 4 | -1.3 | -0.13 |
| Pullback | 10 | 6 | +7.5 | +0.75 |

By process:

| Followed the plan | Trades | Total R | Average R |
|---|---|---|---|
| Yes | 16 | +8.7 | +0.54 |
| No | 4 | -2.5 | -0.63 |

Two findings stand out. The Breakout setup lost money overall while Pullback made most of the profit. And the four trades that broke the plan averaged a loss, two of them larger than 1R.

</div>

Now the limit. With 20 trades the average of +0.31R has a standard deviation of 1.65R, so its standard error (the typical size of the gap between a sample average and the true average) is 1.65 / sqrt(20) = 0.37R. A rough 95% interval is 0.31 plus or minus 1.96 x 0.37, which runs from -0.42R to +1.04R. It includes zero. Ten trades per setup is a smaller sample still, so the Breakout result of -0.13R is not evidence that the setup is bad, and the Pullback result of +0.75R is not evidence that it is good. The math book covers [confidence intervals](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/02-confidence-intervals/) if you want the formula.

What the review can do with a sample this small is find mistakes of process: a stop that moved, an early exit, a trade taken with no setup. Those are visible in a few trades. Whether a setup has an edge needs more trades than a month of journaling gives you, and Part 20 covers testing as a concept (Backtesting concepts and biases<!-- link: ../20-quant-track-in-python/08-backtesting-concepts-and-biases.md -->).

<details class="code" markdown>
<summary>In code</summary>

Download [journal-20-trades.csv](../assets/data/journal-20-trades.csv). The code reproduces the review above.

```python
import pandas as pd

t = pd.read_csv("journal-20-trades.csv")
wins = t[t["r"] > 0]
losses = t[t["r"] < 0]
print(len(t), (t["r"] > 0).mean(), round(wins["r"].mean(), 2), round(losses["r"].mean(), 2), round(t["r"].mean(), 2))
print(t.groupby("setup")["r"].agg(["count", "sum", "mean"]).round(3))
print(t.groupby("followed_plan")["r"].agg(["count", "sum", "mean"]).round(3))

se = t["r"].std(ddof=1) / len(t) ** 0.5
print(round(se, 2), round(t["r"].mean() - 1.96 * se, 2), round(t["r"].mean() + 1.96 * se, 2))
```

The first line prints 20 trades, a 0.5 win rate, +1.82R, -1.2R and +0.31R. The last line prints the standard error 0.37 and the interval -0.42 to 1.04.

</details>

## Common mistakes

- Judging a decision by its result. Ask "did I follow the plan?" first, and look at the R second.
- Changing the plan after every loss. One change a week, based on a pattern in several trades.
- Reading a by-setup table of 10 trades as proof. Treat it as a question to keep testing.

## Try it

1\. In a month you take 12 trades: 5 winners averaging +2.2R and 7 losers averaging -1.0R. What is the expectancy per trade and in total?

<details class="solution" markdown>
<summary>Answer</summary>

Total R = 5 x 2.2 - 7 x 1.0 = 11.0 - 7.0 = +4.0R. Expectancy = 4.0 / 12 = +0.33R per trade. Win rate = 5 / 12 = 41.7%.

</details>

2\. A trade followed the plan and lost 1R. Another broke the plan and won 2R. Which is the better decision, and why?

<details class="solution" markdown>
<summary>Answer</summary>

The first. The plan is your tested set of rules, so following it is the decision you want to repeat whatever the result. The second won by luck of the outcome, and rewarding it makes a plan break more likely next time (outcome bias).

</details>

3\. A setup has 8 trades with a total of +3.2R. What is the average, and why is it weak evidence?

<details class="solution" markdown>
<summary>Answer</summary>

Average = 3.2 / 8 = +0.4R. Eight trades give a wide standard error: if the standard deviation of R is about 1.5R, the standard error is 1.5 / sqrt(8) = 0.53R, which is larger than the average itself.

</details>

4\. In the 20 trades, what is the total R of the four plan-breaking trades, and of the other 16?

<details class="solution" markdown>
<summary>Answer</summary>

The four plan breaks are -1.8, +0.9, -2.2 and +0.6, which add to -2.5R. The other 16 add to 6.2 - (-2.5) = +8.7R, which matches the table. Two of the four lost more than 1R, so the stop was not honoured on those trades.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 6 | Run the five-step weekly review on your journal (or the example data in the [journal workbook](../downloads/trade-journal.xlsx)). Write the one change for next week. |
| 4 | Add a "Followed plan" count to your stats and write the number of trades that broke a rule this week, with a reason for each. |

</div>

## Key terms

- **Outcome bias**: judging a decision by how it turned out instead of by what was known when it was made.
- **Process**: how you made a decision and whether you followed the plan.
- **Weekly review**: a regular check of the journal that ends in at most one change.
- **Standard error**: the typical gap between a sample average and the true average.

Next: [Setting up paper trading](06-paper-trading-setup.md)
