# Biases that cost traders money

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MIND</span>

After this lesson you can name five thinking habits that distort trading decisions, say what research found about each, and spot the one that is at work in a specific trade.

Before this: [Order types](../01-how-markets-work/05-order-types.md). You need: a calculator.

## The idea

You buy 100 shares of Stock A at US$50.40 with a stop at US$49.40. The stock falls through the stop and keeps going. Three weeks later it trades at US$44.50, and you still hold it. The plan said you would lose US$100. You have lost US$590.

Nothing in the plan was hard. The trouble is that a person looking at a loss does not think the way a spreadsheet does. A **cognitive bias** is a regular, predictable error in how people judge or decide. The errors are not random, so you can learn their shapes and set up the trade so they have less room to act.

The sections below cover five biases. Each has a published study behind it, and each has a fix that is a rule, not a promise to try harder.

## How it works

### Loss aversion and the value function

**Prospect theory** ([Kahneman and Tversky, 1979](https://doi.org/10.2307/1914185)) describes how people value gains and losses measured from a **reference point**, usually what they paid or where they started the day. Two findings matter here. Losses weigh more than equal gains, which is called **loss aversion**. And the effect of each extra dollar shrinks as the amount grows. [Tversky and Kahneman (1992)](https://doi.org/10.1007/BF00122574) fitted a curve and reported median estimates of 0.88 for the shrinking and 2.25 for the loss weight.

\[ v(x) = x^{0.88} \text{ for } x \ge 0, \qquad v(x) = -2.25\,(-x)^{0.88} \text{ for } x < 0 \]

- \(x\) is the gain or loss from the reference point, in US$.
- \(v(x)\) is how the outcome feels, in arbitrary units.
- 0.88 is the shrinking exponent and 2.25 is the loss weight. Both are median estimates from one set of experiments, not constants of nature.

The figure shows the curve. Look at how much steeper the loss side is.

![The prospect theory value function: a loss of 100 feels about 2.25 times as large as a gain of 100](../assets/figures/04-psychology-journal-and-paper-trading/value-function-dark.svg#only-dark)
![The prospect theory value function: a loss of 100 feels about 2.25 times as large as a gain of 100](../assets/figures/04-psychology-journal-and-paper-trading/value-function-light.svg#only-light)

<div class="example" markdown>

### Worked example: a good bet that feels bad

A coin-flip trade wins US$150 or loses US$100 with equal odds. Its expected value is 0.5 x 150 - 0.5 x 100 = +US$25.

1. A US$150 gain feels like 150^0.88 = 82.2.
2. A US$100 loss feels like -2.25 x 100^0.88 = -129.5.
3. The felt value of the bet is 0.5 x 82.2 + 0.5 x (-129.5) = -23.6.

The bet has a positive expected value and a negative felt value. A trader who skips it, or who exits winners early to avoid giving a gain back, is acting on that second number.

</div>

### The disposition effect

[Shefrin and Statman (1985)](https://doi.org/10.1111/j.1540-6261.1985.tb05002.x) named the **disposition effect**: the urge to sell winners too early and hold losers too long. Selling a loser means accepting the loss, and loss aversion makes that hurt. [Odean (1998)](https://doi.org/10.1111/0022-1082.00072) tested it on trades from 10,000 accounts at one US discount broker. Investors sold 14.8% of the gains they could have realized and 9.8% of the losses. That is the pattern in the opening example.

### Sunk cost

A **sunk cost** is money already spent that you cannot get back. It should not affect a decision about what to do next, but it does. [Arkes and Blumer (1985)](https://doi.org/10.1016/0749-5978(85)90049-4) sold theatre season tickets at random prices. Buyers who paid full price attended more plays than buyers who got a discount, though the price did not change how good the plays were.

In trading, the sunk cost is your entry price. The market does not know it. The only question is whether you would open this position now, at today's price, with today's stop.

```chart
data: 04-psychology-journal-and-paper-trading/loser-held.json
title: Stock A, daily: a stop that was moved
level: 50.40 | Entry 50.40
level: 49.40 | Planned stop 49.40
marker: 2026-03-17 | below | Stop hit
marker: 2026-04-10 | below | Exit 44.50
range: 2026-03-02 to 2026-04-10
caption: Stock A traded down through the planned stop on March 17 (low 49.27). The exit came on April 10 at 44.50, which is 5.9 times the planned loss.
```

### Anchoring and confirmation bias

[Tversky and Kahneman (1974)](https://doi.org/10.1126/science.185.4157.1124) described **anchoring**: a number you saw first pulls later estimates toward it, even when the number is arbitrary. Your entry price is a strong anchor. "I'll sell when it gets back to 50.40" is a plan built on your history, not on the chart.

**Confirmation bias** is the habit of looking for evidence that agrees with what you already think and discounting evidence that does not ([Nickerson 1998](https://doi.org/10.1037/1089-2680.2.2.175), a review of the research). After you buy, you read the bullish comments and skip the bearish ones.

## Fixes that work as rules

1. Set the stop before you enter, and write it down ([Rules and checklists](03-rules-and-checklists.md)).
2. Ask the sunk cost question: "If I held cash, would I open this trade now?" If no, exit.
3. Look for one reason the trade is wrong before you enter, and write it in the journal ([The trade journal](04-the-trade-journal.md)).
4. Measure results in R (a multiple of your planned risk), so a loss beyond 1R shows as a broken rule (see [R-multiples](../03-risk-and-position-sizing/02-r-multiples.md)).

## Common mistakes

- Treating "I know about this bias" as protection. Knowing the name does not change the feeling. Only a rule you set before the trade does.
- Moving the stop a little while the trade is open. The stop was set when you were calm, so it is the better number.
- Calling a held loser a long-term investment. If you would not buy it today as an investment, you are holding it because of the sunk cost.

## Try it

1\. A loss of US$200 feels how large under the 1992 estimates, and what gain feels the same size?

<details class="solution" markdown>
<summary>Answer</summary>

Felt value of the loss = -2.25 x 200^0.88 = -2.25 x 105.9 = -238.3. A gain of g feels the same size when g^0.88 = 238.3, so g = 200 x 2.25^(1/0.88) = 200 x 2.513 = US$503 (rounded). A loss of US$200 weighs like a gain of about US$503 in this model.

</details>

2\. You bought 100 shares of Stock A at US$50.40 with a stop at US$49.40. You exit at US$44.50. What is the loss in dollars and in R?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = (50.40 - 44.50) x 100 = US$590. One R = (50.40 - 49.40) x 100 = US$100. The loss is 590 / 100 = 5.9R.

</details>

3\. In Odean's data, 14.8% of gains and 9.8% of losses were realized. How many times more likely was a gain to be sold than a loss?

<details class="solution" markdown>
<summary>Answer</summary>

14.8 / 9.8 = 1.51, so about 1.5 times as likely.

</details>

4\. Which bias is at work in this thought: "I bought at 50.40, so I will wait until it is back at 50.40 to sell"?

<details class="solution" markdown>
<summary>Answer</summary>

Anchoring on the entry price and the disposition effect (holding a loser to avoid realizing it). Sunk cost is also present, because the entry price is money already spent.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick the last trade you closed, or a position you hold. Write the entry, the stop and what you did. Mark which of the five biases, if any, shaped one decision. |
| 3 | Write the sunk cost question where you see it before you place an order (a sticky note or your trading notes). |
| 2 | Check the stop on every open position: is it where the plan put it? |

</div>

## Key terms

- **Cognitive bias**: a regular, predictable error in judgment or decision making.
- **Prospect theory**: a description of how people value gains and losses from a reference point.
- **Reference point**: the level against which a gain or loss is measured, often your entry price.
- **Loss aversion**: the tendency for a loss to weigh more than an equal gain.
- **Disposition effect**: selling winners too early and holding losers too long.
- **Sunk cost**: money already spent that cannot be recovered and should not affect the next decision.
- **Anchoring**: letting an early number pull later estimates toward it.
- **Confirmation bias**: favouring evidence that agrees with what you already believe.

Next: [Tilt, revenge trading and FOMO](02-tilt-revenge-and-fomo.md)
