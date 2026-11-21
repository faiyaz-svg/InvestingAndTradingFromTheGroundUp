# Drawdowns and risk of ruin

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">RISK</span>

After this lesson you can measure a drawdown, say what a given risk per trade does to the size and frequency of drawdowns, and read a risk of ruin figure with its assumptions.

Before this: [Risk first: the math of losses](01-risk-first.md), [Win rate, payoff and expectancy](03-win-rate-payoff-and-expectancy.md). You need: a calculator.

## The idea

Two traders have the same strategy: 45% winners at +2R, 55% losers at -1R, which is an expectancy of +0.35R per trade. One risks 1% per trade, another risks 5%. Over 200 trades both are expected to make money. Which one has the harder ride?

Lesson 1 said a deep drawdown is hard to recover. This lesson measures how deep and how often, and why the only difference between the two traders is the size of the bet.

A **drawdown** is the fall in the account from its latest peak. The **maximum drawdown** is the largest such fall over a period.

\[ DD_t = \frac{\text{peak}_t - \text{equity}_t}{\text{peak}_t} \]

- \(\text{equity}_t\) is the account value after trade \(t\), and \(\text{peak}_t\) is the highest value reached up to then, both in US$.
- \(DD_t\) is a fraction. Take its largest value to get the maximum drawdown.

<div class="example" markdown>

### Worked example: a maximum drawdown

An account is worth US$10,000, then US$10,600, US$10,200, US$11,200, US$9,800 and US$10,300 after five trades.

1. The peak after trade 3 is US$11,200. After trade 4 the account is US$9,800.
2. Drawdown = (11,200 - 9,800) / 11,200 = 12.5%. This is the maximum, since the earlier dip from 10,600 to 10,200 was 3.8%.
3. To get back to 11,200 from 9,800 the account needs 11,200 / 9,800 - 1 = 14.3% (lesson 1's formula gives 0.125 / 0.875).

</div>

## How it works

The drawdown you will meet depends on luck as well as on risk, so the best way to see it is to run many versions of the same strategy. A **Monte Carlo simulation** does that: it draws random sequences of wins and losses with the strategy's win rate and payoff, and records what the account does.

The setup here: 45% of trades win +2R and 55% lose -1R, each path has 200 trades, the start is US$10,000 and each trade risks a fixed fraction of the current account. There are 10,000 paths per risk level, with a fixed random seed (2026), and the same random draws at every level. The simulation assumes that every trade is independent, that the win rate and payoffs never change, that every loss is exactly -1R (no slippage or gaps) and that there are no costs. Real trading is rougher than that, so real drawdowns tend to be worse.

The first figure draws one seeded path at three risk levels on a log scale. The line for 5% risk swings the widest.

![One simulated account at 1%, 2% and 5% risk per trade](../assets/figures/03-risk-and-position-sizing/equity-curves-dark.svg#only-dark)
![One simulated account at 1%, 2% and 5% risk per trade](../assets/figures/03-risk-and-position-sizing/equity-curves-light.svg#only-light)

On this single path the three accounts end at US$18,533 (1%), US$32,829 (2%) and US$140,475 (5%), with maximum drawdowns of 6.0%, 12.0% and 29.6%. One path is one story. The table uses all 10,000.

| Risk per trade | Median final account | Median maximum drawdown | Paths with a 30% drawdown | Paths that touch US$5,000 |
|---|---|---|---|---|
| 1% | US$19,674 | 9.0% | 0.00% | 0.00% |
| 2% | US$36,972 | 17.9% | 3.55% | 0.00% |
| 5% | US$188,338 | 40.1% | 91.40% | 1.38% |

Higher risk gives a larger median result and also a much deeper typical drawdown. At 5%, the median path falls 40% from a peak at some point. Lesson 1's table says that fall needs a 66.7% gain to recover. At 5% risk, 91.4% of paths see a drawdown of at least 30%. The edge in this simulation (+0.35R) is large and known exactly, which a real trader never has, so treat the sizes as a shape and not a forecast.

### Risk of ruin

**Risk of ruin** is the probability that the account falls to a level you cannot trade from, called ruin. A classic formula covers the simplest case: even-money bets (win 1 unit or lose 1 unit), a fixed bet size and a constant win probability.

\[ P(\text{ruin}) = \left(\frac{1 - p}{p}\right)^{N} \]

- \(p\) is the win probability, and must be above 0.5.
- \(N\) is the account measured in bet units: the account divided by the amount lost on a loss.
- Ruin means losing the whole account.

With \(p = 0.55\): at 5% per bet, \(N = 20\), and the risk is (0.45 / 0.55)^20 = 1.8%. At 1% per bet, \(N = 100\), and the risk is (0.45 / 0.55)^100, about 1.9 x 10^-9, which is two in a billion. Cutting the bet size by a factor of five cut the risk of ruin by a factor of nearly ten million (seven orders of magnitude).

The assumptions matter more than the formula. If the true \(p\) is 0.50 there is no edge and ruin is certain if you trade long enough. If you estimated 0.55 from 40 trades, the standard error (lesson 3) is about 8 points, so the true value could easily be 0.50 or less. A risk of ruin figure is as good as the win rate you put into it.

## In code

A small Monte Carlo: the same edge at three risk levels, and the median maximum drawdown for each.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

rng = np.random.default_rng(1)
wins = rng.random((2000, 200)) < 0.45            # 2,000 paths of 200 trades
r = np.where(wins, 2.0, -1.0)                    # +2R or -1R

for risk in (0.01, 0.02, 0.05):
    equity = 10_000 * np.cumprod(1 + risk * r, axis=1)
    peak = np.maximum.accumulate(equity, axis=1)
    max_dd = ((peak - equity) / peak).max(axis=1)
    print(risk, round(float(np.median(max_dd)), 3))
```

The code prints median maximum drawdowns of 0.089, 0.174 and 0.401. Another seed gives slightly different numbers, close to the table above.

</details>

## Common mistakes

- Planning for the average drawdown. The median maximum drawdown is the middle case, and half of the paths are worse.
- Quoting a risk of ruin without its assumptions. The formula needs a known win rate, fixed bet size and no change in the edge.
- Raising the risk after a winning run. The edge did not change, but the size of the swings did.

## Try it

1\. An account goes US$20,000, US$22,000, US$19,800, US$21,000, US$17,600. What is the maximum drawdown?

<details class="solution" markdown>
<summary>Answer</summary>

The peak is US$22,000. The low after it is US$17,600. Drawdown = (22,000 - 17,600) / 22,000 = 20.0%.

</details>

2\. Using the table, which risk level gives a median maximum drawdown closest to 18%, and what gain would recover it from the bottom?

<details class="solution" markdown>
<summary>Answer</summary>

2% risk (17.9%). Gain needed = 0.179 / (1 - 0.179) = 21.8%.

</details>

3\. A trader has a 55% win rate on even-money bets and risks 2% per bet. What is the risk of ruin from the formula?

<details class="solution" markdown>
<summary>Answer</summary>

N = 1 / 0.02 = 50. (0.45 / 0.55)^50 = 0.0000439, about 0.004%.

</details>

4\. The same trader finds the true win rate is 52%. What is the risk of ruin now at 2% per bet?

<details class="solution" markdown>
<summary>Answer</summary>

(0.48 / 0.52)^50 = 0.9231^50 = 0.0183, which is 1.8%. A small error in the win rate raises the risk of ruin by a factor of about 416.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Write your account value after each of your last 10 trades (your [trade journal](../practice/trade-journal.md) has them if you keep one), or invent 10. Compute the maximum drawdown. |
| 3 | Write the gain needed to recover from it. |
| 3 | Pick the risk per trade where the median maximum drawdown in the table is the largest you would tolerate. Write it down. |

</div>

## Key terms

- **Drawdown**: the fall in the account from its latest peak, as a fraction of the peak.
- **Maximum drawdown**: the largest drawdown over a period.
- **Monte Carlo simulation**: a method that runs many random versions of a process to see the spread of outcomes.
- **Risk of ruin**: the probability that the account falls to a level you cannot trade from.

Next: [The Kelly criterion and fractional Kelly](09-kelly-and-fractional-kelly.md)
