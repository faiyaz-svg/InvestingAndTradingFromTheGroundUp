# Payoff diagrams

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">OPT</span>

After this lesson you can work out the profit or loss at expiry of a long or short call or put, find its breakeven, and read the four basic payoff diagrams.

Before this: [Calls and puts](01-calls-and-puts.md). You need: a calculator.

## The idea

Before you buy or sell an option, you want to know one thing: if the stock ends at price X on expiry day, how much do I make or lose? A **payoff diagram** answers that for every X at once. It plots the profit or loss of a position at expiry against the stock price at expiry.

Every strategy in the rest of this part is a combination of the four shapes in this lesson. If you can read these four, you can read any of them.

## How it works

Let \(S_T\) be the stock price at expiry and \(K\) the strike. The **payoff** of an option at expiry is what it is worth then, before counting what you paid.

\[ \text{call payoff} = \max(S_T - K,\ 0) \qquad \text{put payoff} = \max(K - S_T,\ 0) \]

- \(S_T\) is the stock price at expiry, in US$ per share.
- \(K\) is the strike, in US$ per share.
- \(\max(a, b)\) is the larger of the two numbers. A call is worth the amount the stock is above the strike, or nothing. A put is worth the amount the stock is below the strike, or nothing.

The **profit** of the buyer subtracts the premium \(p\) paid, and the profit of the seller is the opposite of the buyer's profit.

\[ \text{long profit} = \text{payoff} - p \qquad \text{short profit} = p - \text{payoff} \]

- \(p\) is the premium in US$ per share. Multiply by 100 for one contract.

The **breakeven** is the expiry price at which profit is zero.

\[ \text{call breakeven} = K + p \qquad \text{put breakeven} = K - p \]

A call buyer needs the stock to rise above the strike by at least the premium. A put buyer needs it to fall below the strike by at least the premium.

<div class="example" markdown>

### Worked example: four positions on one stock

Stock A options, strike US$50. The call premium is 3.25 and the put premium is 2.75 (made-up prices). Per contract, the premium is US$325 for the call and US$275 for the put.

| Stock A at expiry | Long call | Short call | Long put | Short put |
|---|---|---|---|---|
| US$40 | -US$325 | US$325 | US$725 | -US$725 |
| US$45 | -US$325 | US$325 | US$225 | -US$225 |
| US$47.25 | -US$325 | US$325 | US$0 | US$0 |
| US$50 | -US$325 | US$325 | -US$275 | US$275 |
| US$53.25 | US$0 | US$0 | -US$275 | US$275 |
| US$55 | US$175 | -US$175 | -US$275 | US$275 |
| US$60 | US$675 | -US$675 | -US$275 | US$275 |

Check one cell. Long call at US$55: payoff = (55 - 50) x 100 = US$500, minus the US$325 premium = US$175. Short put at US$40: payoff to the holder = (50 - 40) x 100 = US$1,000, and the seller keeps US$275 of premium, so the profit is 275 - 1,000 = -US$725.

Breakevens: the call at 50 + 3.25 = US$53.25, the put at 50 - 2.75 = US$47.25.

</div>

## Reading the diagrams

Look first at the flat part of each line. Each buyer's loss is flat at the premium once the stock is on the wrong side of the strike. Each seller's gain is flat at the premium. The slanted part starts at the strike. The line crosses zero at the breakeven, which is on the far side of the strike by the premium, so the dot is not at the strike.

![Profit at expiry of a long call and a short call, strike 50](../assets/figures/15-options/calls-payoff-dark.svg#only-dark)
![Profit at expiry of a long call and a short call, strike 50](../assets/figures/15-options/calls-payoff-light.svg#only-light)

The long call has a loss of at most US$325 and an unlimited gain. The short call is its mirror: a gain of at most US$325 and a loss with no limit. The two lines are mirror images because every dollar the buyer makes is a dollar the seller loses (the premium moves from buyer to seller, and the diagram ignores fees).

![Profit at expiry of a long put and a short put, strike 50](../assets/figures/15-options/puts-payoff-dark.svg#only-dark)
![Profit at expiry of a long put and a short put, strike 50](../assets/figures/15-options/puts-payoff-light.svg#only-light)

The puts slope the other way. The long put gains as the stock falls, up to a limit: the stock cannot go below 0, so the best case is (50 - 0) x 100 - 275 = US$4,725. The short put loses that same amount at worst.

Three limits of the diagram:

1. It shows expiry only. Before expiry the line is a smooth curve above this one, because time still has value (lesson 4, [What sets an option's price](04-what-sets-an-option-price.md)).
2. It ignores commissions and the bid-ask spread.
3. It does not say how likely each price is. A strategy that wins in many places can still lose money on average.

Compare an option with 100 shares. The shares' payoff is a straight line through the purchase price. The option bends it: it removes the losses on one side, and the premium is the price of that bend.

## In code

A short function that builds any of the four, so you can test a strike and premium before using them.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

def profit(S, K, premium, kind="call", side="long"):
    """Profit per share at expiry. S can be a number or an array."""
    payoff = np.maximum(S - K, 0) if kind == "call" else np.maximum(K - S, 0)
    return payoff - premium if side == "long" else premium - payoff

prices = np.array([40, 45, 47.25, 50, 53.25, 55, 60])
print(profit(prices, 50, 3.25, "call", "long") * 100)
print(profit(prices, 50, 2.75, "put", "short") * 100)
```

</details>

## Common mistakes

- Putting the breakeven at the strike. The premium moves it: a call's breakeven is above the strike, a put's below.
- Forgetting the 100. The diagram's units are US$ per share. Multiply by 100 for a contract.
- Treating a short option's maximum gain as the goal. The seller's best case is small and capped, and the worst case is large. Part 3's R and expectancy lessons apply here as well ([Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md)).

## Try it

1\. A put on Stock A has strike 60 and premium 4.10. What is the breakeven, and what is the profit per contract if the stock ends at US$52?

<details class="solution" markdown>
<summary>Answer</summary>

Breakeven = 60 - 4.10 = US$55.90. At US$52 the payoff is (60 - 52) x 100 = US$800, minus 410 = US$390.

</details>

2\. You sold a call with strike 55 for a premium of 1.30. Stock A ends at US$57. What is your result per contract?

<details class="solution" markdown>
<summary>Answer</summary>

The holder's payoff is (57 - 55) x 100 = US$200. You received US$130. Result = 130 - 200 = -US$70.

</details>

3\. For the call in the worked example (strike 50, premium 3.25), where must the stock end for the buyer to double the money paid?

<details class="solution" markdown>
<summary>Answer</summary>

Doubling means a profit of US$325, so the payoff must be 325 + 325 = US$650, which is 6.50 per share. The stock must end at 50 + 6.50 = US$56.50.

</details>

4\. A short put (strike 50, premium 2.75) and a long put (strike 50, premium 2.75) are held by two traders. The stock ends at US$46. What is each result?

<details class="solution" markdown>
<summary>Answer</summary>

The payoff is (50 - 46) x 100 = US$400. The long put gains 400 - 275 = US$125. The short put loses US$125, the same amount.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a call from your broker's chain. Write its strike and ask, then compute the breakeven and the profit at three prices you choose. |
| 4 | Sketch the payoff of the matching put from the same chain on paper, with the breakeven marked. |
| 2 | Run the code above with your numbers and compare it with the paper sketch. |

</div>

## Key terms

- **Payoff diagram**: a plot of profit or loss at expiry against the stock price at expiry.
- **Payoff**: what an option is worth at expiry, before subtracting the premium.
- **Profit**: for a buyer, the payoff minus the premium paid; for a seller, the premium received minus the payoff.
- **Breakeven**: the expiry price at which profit is zero.

Next: [The options chain and moneyness](03-the-chain-and-moneyness.md)
