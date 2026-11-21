# Risk first: the math of losses

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">RISK</span>

After this lesson you can work out the gain needed to recover from any loss, and say why a trader sets the size of the loss before thinking about the size of the profit.

Before this: [Order types](../01-how-markets-work/05-order-types.md). For percentage changes, see [percent change](https://faiyaz-svg.github.io/MathFromTheGroundUp/02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications/) in the math book. You need: a calculator.

## The idea

You have US$10,000. You take four trades and each one loses 10% of the account. How much have you lost?

Not 40%. The first loss takes 10% of US$10,000 and leaves US$9,000. The second takes 10% of US$9,000 and leaves US$8,100. After four losses the account is 10,000 x 0.90 x 0.90 x 0.90 x 0.90 = US$6,561, which is a 34.39% loss. Each loss is taken from a smaller account, so the total loss is a bit less than the sum.

Now the part that matters. To get from US$6,561 back to US$10,000 you need a gain of (10,000 - 6,561) / 6,561 = 52.4%. The gain is bigger than the loss because it works on a smaller base.

A drop from the highest value your account has reached is a **drawdown**. Lesson 8 measures drawdowns in full ([Drawdowns and risk of ruin](08-drawdowns-and-risk-of-ruin.md)). This lesson only needs the idea: the deeper the drawdown, the harder the climb back.

## How it works

Say the account loses a fraction \(L\) from its peak. What gain \(G\) brings it back?

\[ (1 - L)(1 + G) = 1 \quad\Rightarrow\quad G = \frac{L}{1 - L} \]

- \(L\) is the loss from the peak as a fraction (0.50 for a 50% loss).
- \(G\) is the gain needed on what is left, as a fraction.
- \((1 - L)\) is the share of the account that remains after the loss.

The first equation says: what is left, grown by \(G\), must equal the starting value (1). Solving for \(G\) gives the second.

| Loss from peak | Gain needed to recover |
|---|---|
| 5% | 5.3% |
| 10% | 11.1% |
| 20% | 25.0% |
| 25% | 33.3% |
| 30% | 42.9% |
| 40% | 66.7% |
| 50% | 100.0% |
| 60% | 150.0% |
| 75% | 300.0% |
| 90% | 900.0% |

The curve bends upward slowly at first and then steeply. Look at where the red dots sit: a 10% loss needs 11.1%, a 50% loss needs 100%, and a 75% loss needs 300%.

![Gain needed to recover from a loss, which rises slowly at first and then steeply](../assets/figures/03-risk-and-position-sizing/loss-recovery-dark.svg#only-dark)
![Gain needed to recover from a loss, which rises slowly at first and then steeply](../assets/figures/03-risk-and-position-sizing/loss-recovery-light.svg#only-light)

<div class="example" markdown>

### Worked example: ten losses in a row

Two traders each lose ten trades in a row from a US$10,000 account. Trader X risks 1% of the account on each trade. Trader Y risks 10%.

1. Trader X: 10,000 x 0.99^10 = 10,000 x 0.9044 = US$9,043.82. The account is down 9.56%.
2. Gain X needs to recover: 1 / 0.9044 - 1 = 10.6%.
3. Trader Y: 10,000 x 0.90^10 = 10,000 x 0.3487 = US$3,486.78. The account is down 65.13%.
4. Gain Y needs to recover: 1 / 0.3487 - 1 = 186.8%.

The same ten losses are a bad stretch for X and a drawdown of more than 65% for Y. The only difference is the size of each bet.

</div>

### Why risk comes first

You control three things in a trade: whether to enter, how much to lose if you are wrong, and how much to make if you are right. You control the second one completely, because you choose the stop (lesson 5) and the size (lesson 4). You do not control the third, because the market decides it.

So the order of work is: decide the loss you will accept, size the trade to that loss, and only then look at the possible profit. The rest of this part builds each step with numbers.

## Common mistakes

- Adding losses instead of compounding them. Four 10% losses are 34.39%, and the gain needed is 52.4%, not 40%.
- Judging a loss by its size alone. A 20% loss needs a 25% gain, and a 50% loss needs a 100% gain: twice the loss, four times the climb.
- Thinking a high-risk trade can be "made up" later. The deeper the hole, the more the account has to earn on a smaller base.

## Try it

1\. Your account falls 20% from its peak. What gain brings it back?

<details class="solution" markdown>
<summary>Answer</summary>

G = 0.20 / (1 - 0.20) = 0.20 / 0.80 = 0.25, so 25%.

</details>

2\. An account of US$20,000 loses 30%. How much is left, and what gain is needed to get back to US$20,000 (in dollars and in percent)?

<details class="solution" markdown>
<summary>Answer</summary>

Left: 20,000 x 0.70 = US$14,000. Gain needed: 6,000 / 14,000 = 42.9%, which matches 0.30 / 0.70.

</details>

3\. You need a gain of 100% to recover. What loss did you take?

<details class="solution" markdown>
<summary>Answer</summary>

Solve G = L / (1 - L) with G = 1: 1 - L = L, so L = 0.50. You lost 50%.

</details>

4\. Five losses in a row, each 2% of the current account, from US$10,000. What is the account worth, and what gain recovers it?

<details class="solution" markdown>
<summary>Answer</summary>

10,000 x 0.98^5 = 10,000 x 0.9039 = US$9,039.21. That is a 9.61% loss. Gain needed: 1 / 0.9039 - 1 = 10.6%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Open your broker's history. Find your largest drop from a peak in the last year, in percent, and use the formula to write the gain it needed. |
| 4 | Extend the table: compute the gain needed for losses of 15%, 35% and 65%. |
| 2 | Write one sentence: the most you would accept losing on a single trade, as a percent of your account. |

</div>

## Key terms

- **Drawdown**: a fall in account value from its highest point.
- **Gain needed to recover**: the percentage gain on what is left that returns the account to its peak, \(L / (1 - L)\).
- **Compounding of losses**: each loss applies to the smaller balance left by the one before, so percentage losses do not add.

Next: [R-multiples](02-r-multiples.md)
