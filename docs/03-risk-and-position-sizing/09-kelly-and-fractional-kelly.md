# The Kelly criterion and fractional Kelly

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">RISK</span>

After this lesson you can compute the Kelly fraction for a bet with a known win rate and payoff, read the growth curve, and say why traders use half Kelly or less.

Before this: [Win rate, payoff and expectancy](03-win-rate-payoff-and-expectancy.md), [Drawdowns and risk of ruin](08-drawdowns-and-risk-of-ruin.md). The math book's [logarithms](https://faiyaz-svg.github.io/MathFromTheGroundUp/03-high-school/07-exponentials-and-logarithms/02-logarithms/) lesson covers the natural log used below. You need: a calculator.

## The idea

You have an edge: a 55% chance to win an even-money bet. How much of your account should you bet each time?

Bet nothing and you earn nothing. Bet everything and one loss ends the account. Somewhere between, the account grows fastest over many bets. In 1956 John L. Kelly Jr. showed how to find that fraction ("A New Interpretation of Information Rate", [Bell System Technical Journal 35(4), 917-926](https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf)). It is the **Kelly criterion**, and the fraction is the **Kelly fraction**.

The criterion maximises the long-run growth rate of the account, which is the average of the logarithm of the growth per bet. Maximising growth of the logarithm and maximising the compounded result are the same goal, because lesson 1 showed that gains and losses multiply.

## How it works

For a bet that wins \(b\) times the amount risked with probability \(p\), and loses the amount risked otherwise:

\[ g(f) = p \ln(1 + b f) + (1 - p)\ln(1 - f) \]

- \(f\) is the fraction of the account risked on each bet, between 0 and 1.
- \(b\) is the payoff ratio from lesson 3, and \(p\) is the win rate.
- \(g\) is the average growth of the account per bet, in log terms (multiply by 100 for an approximate percent).

Set the slope to zero to find the top of the curve:

\[ \frac{p\,b}{1 + b f} = \frac{1 - p}{1 - f} \quad\Rightarrow\quad f^{*} = p - \frac{1 - p}{b} \]

The steps are cross-multiplying, collecting the terms in \(f\) on one side, and dividing by \(b\). The result \(f^*\) is the Kelly fraction. If \(f^*\) is zero or negative, the bet has no edge and the answer is not to bet. This is lesson 3's expectancy test in another form: \(f^* > 0\) exactly when \(p\,b - (1 - p) > 0\).

<div class="example" markdown>

### Worked example: a 55% even-money bet

Here \(p = 0.55\) and \(b = 1\).

1. Kelly fraction: f* = 0.55 - 0.45 / 1 = 0.10, or 10% of the account.
2. Growth at f* = 0.10: 0.55 x ln(1.10) + 0.45 x ln(0.90) = 0.55 x 0.09531 - 0.45 x 0.10536 = 0.05242 - 0.04741 = 0.00501, about 0.50% per bet.
3. Half Kelly, f = 0.05: 0.55 x ln(1.05) + 0.45 x ln(0.95) = 0.02683 - 0.02308 = 0.00375, about 0.38% per bet. That is 75% of the full-Kelly growth with half the bet.
4. Twice Kelly, f = 0.20: 0.55 x ln(1.20) + 0.45 x ln(0.80) = 0.10028 - 0.10042 = -0.00014. Growth is slightly negative.

</div>

The figure shows the curve. Betting more than Kelly does not raise growth, and it lowers it. At twice Kelly the account stops growing, even though every bet has an edge.

![Growth per bet against the fraction risked for a 55% even-money bet, with the top at 10%](../assets/figures/03-risk-and-position-sizing/kelly-growth-dark.svg#only-dark)
![Growth per bet against the fraction risked for a 55% even-money bet, with the top at 10%](../assets/figures/03-risk-and-position-sizing/kelly-growth-light.svg#only-light)

### Why traders use half Kelly or less

The formula assumes you know \(p\) and \(b\) exactly. A trader never does. Lesson 3 showed that the win rate from 40 trades has a standard error of about 8 points. Suppose the true win rate is 50%, with no edge, and you measured 55% and bet 10%. The growth is 0.50 x ln(1.10) + 0.50 x ln(0.90) = -0.00503, a loss of about 0.50% per bet. You bet the full Kelly of an edge that was not there.

The curve is not symmetric. Betting less than Kelly gives up a little growth, and betting more risks a lot. This is the reason for **fractional Kelly**: bet a fixed fraction of the Kelly bet, usually one half or less. Edward O. Thorp's chapter on the criterion has a section on this ("The case for fractional Kelly"), and notes that half Kelly gives 3/4 of the growth rate with much less chance of a big loss ([Thorp 2006, "The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market", chapter 9 of the Handbook of Asset and Liability Management, volume 1](https://wayback.archive-it.org/5456/20240920155724/https://www.eecs.harvard.edu/cs286r/courses/fall12/papers/Thorpe_KellyCriterion2007.pdf)).

Drawdowns give a second reason. Use lesson 8's edge: \(p = 0.45\), \(b = 2\). Then f* = 0.45 - 0.55 / 2 = 0.175, so full Kelly risks 17.5% per trade. Half Kelly is 8.75%. The same seeded simulation as lesson 8 (10,000 paths of 200 trades) gives:

| Risk per trade | Median maximum drawdown | Paths that touch half the start |
|---|---|---|
| 5.00% | 40.1% | 1.4% |
| 8.75% (half Kelly) | 61.7% | 11.4% |
| 17.50% (full Kelly) | 89.4% | 45.4% |

At full Kelly the median path loses 89% of its value at some point, and 45% of paths fall to half their starting value. The growth is highest in the long run, but few people can stay with a strategy through that. For this reason Kelly is a ceiling, not a target. The risk of 1% to 2% per trade used in this part is a small fraction of the Kelly bet.

### Limits of the formula

Kelly assumes bets that repeat with the same odds, results that do not depend on each other, and a loss of exactly the amount risked. Trades have stops that slip (lesson 6), results that cluster in time, and edges that change. Use Kelly as a way to see the curve, check your risk per trade against it, and see why more risk is not better. Do not use it to size trades to the decimal.

## In code

The Kelly fraction and the growth at three fractions of it.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def kelly(p, b):
    return p - (1 - p) / b

def growth(p, b, f):
    return p * math.log(1 + b * f) + (1 - p) * math.log(1 - f)

f_star = kelly(0.55, 1)
for label, f in [("half", f_star / 2), ("full", f_star), ("double", f_star * 2)]:
    print(label, round(f, 3), round(growth(0.55, 1, f) * 100, 4))
print(round(kelly(0.45, 2), 3))
```

The code prints growth of 0.3753, 0.5008 and -0.0138 (in percent per bet) at 5%, 10% and 20%, then 0.175 for the lesson 8 edge.

</details>

## Common mistakes

- Treating the Kelly fraction as the right size. It is the peak of a curve built on exact inputs you do not have.
- Using a win rate measured on a small sample. An error of a few points can turn an edge into a loss.
- Betting more than Kelly. Growth falls past the peak and drawdowns get deeper.

## Try it

1\. Compute the Kelly fraction for a bet with p = 0.40 and b = 2.5.

<details class="solution" markdown>
<summary>Answer</summary>

f* = 0.40 - 0.60 / 2.5 = 0.40 - 0.24 = 0.16, so 16%. Half Kelly is 8%.

</details>

2\. A strategy wins 30% of the time with a payoff ratio of 2. What is the Kelly fraction, and what does it mean?

<details class="solution" markdown>
<summary>Answer</summary>

f* = 0.30 - 0.70 / 2 = 0.30 - 0.35 = -0.05. A negative result means no edge, so the answer is not to take the bet. The expectancy is 0.30 x 2 - 0.70 = -0.10R, which agrees.

</details>

3\. For p = 0.60 and b = 1, compute f* and the growth per bet at f*.

<details class="solution" markdown>
<summary>Answer</summary>

f* = 0.60 - 0.40 = 0.20. Growth = 0.60 x ln(1.20) + 0.40 x ln(0.80) = 0.60 x 0.18232 - 0.40 x 0.22314 = 0.10939 - 0.08926 = 0.02014, about 2.0% per bet.

</details>

4\. Your measured edge is p = 0.55 and b = 1, but the true win rate is 0.50. You bet half Kelly (5%). What is the growth per bet?

<details class="solution" markdown>
<summary>Answer</summary>

0.50 x ln(1.05) + 0.50 x ln(0.95) = 0.50 x 0.04879 - 0.50 x 0.05129 = -0.00125, about -0.13% per bet. Half Kelly cuts the loss to a quarter of the -0.50% at full Kelly.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Take your win rate and payoff ratio from [lesson 3](03-win-rate-payoff-and-expectancy.md) (or use 45% and 2.0) and compute f*. |
| 3 | Write what fraction of f* your risk per trade is. If your risk is above half of f*, cut it. |
| 3 | Redo the calculation with the win rate lowered by 5 points. Write how much f* moves. |

</div>

## Key terms

- **Kelly criterion**: the rule that picks the bet size that maximises the long-run growth rate of the account.
- **Kelly fraction**: the fraction of the account to risk each time, \(f^* = p - (1 - p)/b\).
- **Growth rate**: the average log growth of the account per bet.
- **Fractional Kelly**: betting a fixed fraction of the Kelly bet, such as one half.

Next: [Your trading plan](10-your-trading-plan.md)
