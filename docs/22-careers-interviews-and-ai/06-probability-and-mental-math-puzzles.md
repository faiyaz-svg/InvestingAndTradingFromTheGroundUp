# Probability and mental math puzzles

<span class="tag tag-career">Career</span> <span class="tag tag-part">CAREER</span>

After this lesson you can solve the standard expected value, conditional probability, Bayes, coin and dice puzzles, explain a market-making game, and do quick arithmetic by hand.

Before this: [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md) and [Base rates, calibration and forecast logs](../19-data-flows-and-forecasting/07-base-rates-calibration-and-forecast-logs.md). The math book has the background: [sample spaces and events](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/01-sample-spaces-events-and-axioms/), [conditional probability and Bayes](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/02-conditional-probability-and-bayes/) and [discrete random variables](https://faiyaz-svg.github.io/MathFromTheGroundUp/05-university-core/07-probability/03-discrete-random-variables/). You need from them: counting outcomes, the conditional probability formula and expected value. A calculator, or none.

## The idea

A trading firm asks: "I roll a die and pay you the number in dollars. You may roll once more and keep the second result instead. What would you pay to play?" Firms that trade use puzzles like this because a trader prices uncertain payoffs all day. The interviewer wants a method you can say aloud: list the outcomes, find the probabilities, take the weighted average, and check that the answer is reasonable.

## How it works

### Expected value

The **expected value** is each outcome times its probability, added up:

\[ E[X] = \sum_i x_i \, p_i \]

- \(x_i\) is a possible payoff, in dollars.
- \(p_i\) is its probability, and the \(p_i\) add to 1.

<div class="example" markdown>

### Worked example: the die you may roll again

1. One roll is worth E = (1 + 2 + 3 + 4 + 5 + 6) / 6 = 3.5.
2. Work backward from the second roll. After the first roll, keep it if it beats the 3.5 you expect from rerolling: keep 4, 5 or 6 and reroll 1, 2 or 3.
3. Value = (4 + 5 + 6) / 6 + (3 / 6) x 3.5 = 2.5 + 1.75 = US$4.25.

Pay at most US$4.25. Working backward from the last decision is the standard method for any "you may stop" game.

</div>

### Conditional probability and base rates

**Conditional probability** is the chance of A given that B happened: \(P(A \mid B) = P(A \cap B) / P(B)\). **Bayes' rule** reverses it:

\[ P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)} \]

- \(P(A)\) is the base rate of A before you see B.
- \(P(B \mid A)\) is how often B appears when A is true.
- \(P(B)\) is how often B appears overall.

<div class="example" markdown>

### Worked example: two puzzles

Two dice, at least one is a six. What is the chance the sum is 10 or more?

1. Outcomes with at least one six: 36 - 25 = 11.
2. Of those, the sum is 10 or more for (6,4), (4,6), (6,5), (5,6) and (6,6): 5.
3. Answer: 5 / 11 = 45.5%.

A signal fires on 90% of profitable setups and on 9% of unprofitable ones. 1% of setups are profitable. The signal fires. How likely is the setup to be profitable?

1. Fires and profitable: 0.01 x 0.90 = 0.009.
2. Fires and unprofitable: 0.99 x 0.09 = 0.0891.
3. P = 0.009 / (0.009 + 0.0891) = 0.009 / 0.0981 = 9.2%.

The base rate dominates: a signal that looks strong still leaves the setup unlikely to work.

</div>

### Coin puzzles

On a fair coin, the expected number of flips until the first head is 2. To see HH (two heads in a row) takes 6 flips on average, and to see HT takes 4. The two differ although both patterns have probability 1/4 at any spot, because after a failed HH attempt you restart, but after the first H of HT you stay close to success. Solve it with a short system: let \(a\) be the expected flips from the start, and \(h\) from having a head as the last flip. For HT, \(a = 1 + 0.5a + 0.5h\) and \(h = 1 + 0.5h\) (a tail finishes, so 0.5 of the time \(h\) continues), giving \(h = 2\) and \(a = 4\).

### A market-making game

A market maker quotes two prices at once: a **bid**, where they will buy, and an **ask**, where they will sell. A typical interview game asks you to make a market on the sum of two dice, with the payoff equal to the sum.

The fair value is 7. You quote 6 bid and 8 ask. If the other side buys one unit from you at 8, your expected profit is 8 - 7 = US$1. If they sell to you at 6, your expected profit is 7 - 6 = US$1.

Now the trap. Suppose the other side has seen one die. If it shows 6, the sum averages 6 + 3.5 = 9.5. They buy from you at 8 and you lose 9.5 - 8 = US$1.5 on average. This is **adverse selection**: the people who trade with you know more than you do. Interviewers watch for what you do next: widen the spread, ask for a smaller size, or move the quote after a trade.

![Bars for the probability of each sum of two dice, with a bid of 6, fair value 7 and ask 8 marked](../assets/figures/22-careers-interviews-and-ai/two-dice-dark.svg#only-dark)
![Bars for the probability of each sum of two dice, with a bid of 6, fair value 7 and ask 8 marked](../assets/figures/22-careers-interviews-and-ai/two-dice-light.svg#only-light)

### Mental math

Practise a few tricks until they are automatic.

| Trick | Example |
|---|---|
| Times 11: add the digits and put the sum between them | 47 x 11 = 4(4+7)7 = 4(11)7, carry the 1: 517 |
| Square a number ending in 5: n x (n+1), then 25 | 35 squared = 3 x 4 = 12, then 25: 1,225 |
| Percent: find 10%, then scale | 15% of 84 = 8.4 + 4.2 = 12.6 |
| Times 99: times 100 minus the number | 99 x 37 = 3,700 - 37 = 3,663 |
| Rule of 72: years to double = 72 / the rate in percent | 8% a year: 72 / 8 = 9 years |
| Difference of squares | 17 x 13 = 15 squared - 2 squared = 225 - 4 = 221 |

## In code

You can check any puzzle by simulation or by counting.

<details class="code" markdown>
<summary>In code</summary>

```python
import itertools
import random

# at least one six, sum of 10 or more
rolls = [r for r in itertools.product(range(1, 7), repeat=2) if 6 in r]
print(sum(1 for r in rolls if sum(r) >= 10), "of", len(rolls))

# the die you may roll again
random.seed(1)
total = 0
for _ in range(200_000):
    x = random.randint(1, 6)
    total += x if x >= 4 else random.randint(1, 6)
print(round(total / 200_000, 2))
```

</details>

## Common mistakes

- Answering before listing the outcomes. Write down the sample space first.
- Using the base rate wrongly in a Bayes puzzle. A good test on a rare event gives mostly false alarms.
- Quoting a market with no thought for who trades against you.

## Try it

1\. How many rolls of a fair die does it take on average to see the first six?

<details class="solution" markdown>
<summary>Answer</summary>

The first-success time has mean 1 / p = 1 / (1/6) = 6 rolls.

</details>

2\. Repeat the Bayes puzzle with 2% of setups profitable.

<details class="solution" markdown>
<summary>Answer</summary>

0.02 x 0.90 = 0.018 and 0.98 x 0.09 = 0.0882. P = 0.018 / (0.018 + 0.0882) = 0.018 / 0.1062 = 16.9%.

</details>

3\. You quote 6 bid and 8 ask on the sum of two dice. A buyer who has seen one die showing 5 buys at 8. What is your expected profit?

<details class="solution" markdown>
<summary>Answer</summary>

The sum averages 5 + 3.5 = 8.5. You sold at 8, so you expect 8 - 8.5 = -US$0.50.

</details>

4\. Work out 23 x 11, 65 squared and 15% of 240 by hand.

<details class="solution" markdown>
<summary>Answer</summary>

23 x 11 = 2(2+3)3 = 253. 65 squared = 6 x 7 = 42, then 25: 4,225. 15% of 240 = 24 + 12 = 36.

</details>

5\. The die game, but you may reroll twice (up to three rolls total). What is it worth?

<details class="solution" markdown>
<summary>Answer</summary>

With two rolls left the value is 4.25, so after the first roll keep 5 or 6 and reroll 1 to 4. Value = (5 + 6) / 6 + (4 / 6) x 4.25 = 1.8333 + 2.8333 = US$4.67.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Do four mental-math problems (an 11, a square ending in 5, a percentage, a 99) with a timer. |
| 5 | Solve one new puzzle from the exercises aloud, with the sample space, the method and a sanity check. |

</div>

## Key terms

- **Expected value**: the probability-weighted average of the possible payoffs.
- **Conditional probability**: the chance of an event given that another happened.
- **Bayes' rule**: the formula that turns \(P(B \mid A)\) into \(P(A \mid B)\) using the base rate.
- **Market maker**: a trader who quotes a bid and an ask at the same time.
- **Bid and ask (in a game)**: the prices at which the maker will buy and sell.
- **Adverse selection**: losing on trades because the other side knows more.

Next: [Quant interviews](07-quant-interviews.md)
