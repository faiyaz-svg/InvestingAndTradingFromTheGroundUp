# Win rate, payoff and expectancy

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">RISK</span>

After this lesson you can compute a strategy's expectancy in R and in dollars, find the win rate it needs to break even, and say how many trades you need before a win rate means anything.

Before this: [R-multiples](02-r-multiples.md). The math book's [discrete random variables](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/03-discrete-random-variables/) lesson defines expected value, the average result over many repeats. You need: a calculator.

## The idea

Trader P wins 70% of her trades. Trader Q wins 40%. Who makes more money?

You cannot tell yet. If P's winners are small and her losers are full stops, she can lose money while winning most of the time. Q can profit while losing most of the time if his winners are large. Two numbers decide it: how often you win and how much you win compared with how much you lose.

The **win rate** is the share of trades that make money. The **payoff ratio** is the average win divided by the average loss, both in R. Together they give the **expectancy**: the average result of one trade, in R, if the next trades look like the past ones.

## How it works

\[ p = \frac{\text{winners}}{\text{trades}} \qquad b = \frac{W}{L} \qquad E = p\,W - (1 - p)\,L \]

- \(p\) is the win rate, a fraction between 0 and 1.
- \(W\) is the average winning trade in R (a positive number), and \(L\) the average losing trade in R (also positive, so a loss of 0.9R has \(L = 0.9\)).
- \(b\) is the payoff ratio, with no unit.
- \(E\) is the expectancy, in R per trade. Multiply by the dollar value of R for dollars per trade.

The first term is the average gained per trade from winners, and the second is the average lost per trade from losers.

The break-even win rate is the \(p\) where \(E = 0\). Setting \(p\,W = (1 - p)\,L\) and solving gives:

\[ p_{\text{break-even}} = \frac{1}{1 + b} \]

| Payoff ratio b | Break-even win rate |
|---|---|
| 0.5 | 66.7% |
| 1.0 | 50.0% |
| 1.5 | 40.0% |
| 2.0 | 33.3% |
| 3.0 | 25.0% |

The lines show expectancy in R against win rate for three payoff ratios. Each line crosses zero at the dot, which is the break-even win rate from the table.

![Expectancy in R against win rate for payoff ratios of 1, 2 and 3](../assets/figures/03-risk-and-position-sizing/expectancy-dark.svg#only-dark)
![Expectancy in R against win rate for payoff ratios of 1, 2 and 3](../assets/figures/03-risk-and-position-sizing/expectancy-light.svg#only-light)

<div class="example" markdown>

### Worked example: expectancy of 40 trades

A made-up journal holds 40 trades. 18 were winners, averaging +1.8R. 22 were losers, averaging -0.9R. One R is US$250.

1. Win rate: p = 18 / 40 = 0.45, or 45%.
2. Payoff ratio: b = 1.8 / 0.9 = 2.0.
3. Expectancy: E = 0.45 x 1.8 - 0.55 x 0.9 = 0.810 - 0.495 = +0.315R per trade.
4. In dollars: 0.315 x 250 = US$78.75 per trade, or 40 x 78.75 = US$3,150 over the 40 trades.
5. Break-even win rate: 1 / (1 + 2.0) = 33.3%. At 45% there is a margin of 11.7 percentage points.

Check against the totals: 18 x 1.8 = 32.4R won and 22 x 0.9 = 19.8R lost, so the net is 12.6R. Divide by 40 trades: 0.315R.

</div>

A high win rate alone says nothing. A strategy that wins 70% of the time with an average win of 0.3R and an average loss of 1.0R has E = 0.70 x 0.3 - 0.30 x 1.0 = 0.21 - 0.30 = -0.09R per trade. It wins often and loses money.

### How sure is a win rate?

A win rate measured on few trades is noisy. The standard error of a proportion is

\[ SE = \sqrt{\frac{p\,(1 - p)}{n}} \]

where \(n\) is the number of trades. For the journal above, SE = sqrt(0.45 x 0.55 / 40) = 0.0787, or 7.9 percentage points. A 95% confidence interval is about the win rate plus or minus 1.96 standard errors: 45% plus or minus 15.4 points, from 29.6% to 60.4%. That range includes the 33.3% break-even rate. Forty trades cannot tell you that the edge is real. The math book covers the idea in [confidence intervals](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/08-statistics/02-confidence-intervals/).

Expectancy also assumes the future looks like the past. A strategy that worked in a calm market can change its win rate and payoff when volatility changes. Treat expectancy as an estimate with error bars, not as a fact. Part 20 returns to how tests mislead ([Backtesting concepts and biases](../20-quant-track-in-python/08-backtesting-concepts-and-biases.md)).

## In code

Computing win rate, payoff ratio and expectancy from a list of results in R.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

r = np.array([2.0, -1.0, -0.5, 0.3, 3.1, 1.4, -1.0, -1.0])
wins = r[r > 0]
losses = -r[r < 0]

p = len(wins) / len(r)
b = wins.mean() / losses.mean()
expectancy = p * wins.mean() - (1 - p) * losses.mean()

print(round(p, 3), round(b, 2), round(expectancy, 4))
print(round(r.mean(), 4))
```

The two expectancy figures match: the formula and the plain average of all results are the same number (0.4125R here, from 4 winners and 4 losers).

</details>

## Common mistakes

- Reading a win rate without the payoff ratio. A 70% win rate with small winners can lose money.
- Trusting an expectancy from 15 or 20 trades. The error bar is wider than the edge.
- Mixing R and dollars. Compute expectancy in R, then convert with the dollar value of one R.

## Try it

1\. A strategy wins 40% of the time. The average win is +2.4R and the average loss is -1.0R. What is the expectancy?

<details class="solution" markdown>
<summary>Answer</summary>

E = 0.40 x 2.4 - 0.60 x 1.0 = 0.96 - 0.60 = +0.36R per trade.

</details>

2\. A strategy has a payoff ratio of 1.5. What win rate does it need to break even? What is the expectancy at a 45% win rate, with an average loss of 1R?

<details class="solution" markdown>
<summary>Answer</summary>

Break-even: 1 / (1 + 1.5) = 40.0%. At 45%: W = 1.5 x 1.0 = 1.5R, so E = 0.45 x 1.5 - 0.55 x 1.0 = 0.675 - 0.55 = +0.125R.

</details>

3\. With R = US$200 and an expectancy of +0.125R, how much does the strategy make on average over 100 trades?

<details class="solution" markdown>
<summary>Answer</summary>

0.125 x 200 = US$25.00 per trade, so 100 x 25.00 = US$2,500 on average. The real total varies around that.

</details>

4\. A day trader wins 62% of 25 trades. What is the standard error of the win rate?

<details class="solution" markdown>
<summary>Answer</summary>

SE = sqrt(0.62 x 0.38 / 25) = sqrt(0.009424) = 0.0971, or 9.7 percentage points.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | List your last 10 to 20 trades with the result in R, in your [trade journal](../practice/trade-journal.md) if you keep one (use [R-multiples](02-r-multiples.md) for any you cannot score). Compute win rate, average win, average loss and expectancy. |
| 3 | Compute the break-even win rate for your payoff ratio. Write the gap to your actual win rate. |
| 2 | Compute the standard error of your win rate and write the 95% range. |

</div>

## Key terms

- **Win rate**: the share of trades that make money.
- **Payoff ratio**: the average win divided by the average loss.
- **Expectancy**: the average result of one trade, in R, from the win rate and the average win and loss.
- **Break-even win rate**: the win rate at which expectancy is zero, \(1 / (1 + b)\).
- **Standard error**: the typical size of the error in an estimate such as a win rate.

Next: [Position sizing with fixed fractional risk](04-fixed-fractional-sizing.md)
