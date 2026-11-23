# Vertical spreads

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">OPT</span>

After this lesson you can build a bull call spread and a bull put spread, work out the maximum profit, maximum loss and breakeven from the chain, and size one by its maximum loss.

Before this: [Covered calls and cash-secured puts](09-covered-calls-and-cash-secured-puts.md), [Payoff diagrams](02-payoff-diagrams.md). You need: a calculator.

## The idea

A long call has a loss limited to the premium but a cost that can be high. The 50-strike call on Stock A costs US$345 at the ask. If you think the stock can reach 55 but no further, you are paying for gains above 55 that you do not expect.

A **vertical spread** buys one option and sells another of the same type and expiry at a different strike. The short option pays for part of the long one and caps the gain. You trade the unlimited upside for a lower cost and a defined risk.

The names come from the direction and the type:

| Spread | Legs | Opens with | Wants the stock to |
|---|---|---|---|
| Bull call spread | Buy a lower call, sell a higher call | A **debit** (you pay) | Rise |
| Bear put spread | Buy a higher put, sell a lower put | A debit | Fall |
| Bull put spread | Sell a higher put, buy a lower put | A **credit** (you receive) | Stay up |
| Bear call spread | Sell a lower call, buy a higher call | A credit | Stay down |

The distance between the strikes is the **width**. A debit is the net amount you pay. A credit is the net amount you receive. We work through the first and third, because the other two are their mirror images.

## Two spreads on the chain

Stock A is US$50.20, expiry February 19, 2027. You buy at the ask and sell at the bid.

| Spread | Trade | Net |
|---|---|---|
| Bull call, 50/55 | Buy the 50 call at 3.45, sell the 55 call at 1.30 | Debit 3.45 - 1.30 = 2.15, so US$215 |
| Bull put, 50/45 | Sell the 50 put at 2.65, buy the 45 put at 1.35 | Credit 2.65 - 1.35 = 1.30, so US$130 |

The formulas, with width \(W\), the debit or credit \(D\) per share, and the contract multiplier 100:

\[ \text{debit spread: max profit} = (W - D) \times 100, \quad \text{max loss} = D \times 100 \]
\[ \text{credit spread: max profit} = D \times 100, \quad \text{max loss} = (W - D) \times 100 \]

- \(W\) is the strike difference in US$ per share (5 for both spreads here).
- \(D\) is the net debit or credit in US$ per share.
- For a bull call spread the breakeven is the lower strike plus the debit. For a bull put spread it is the higher strike minus the credit.

| | Bull call 50/55 | Bull put 50/45 |
|---|---|---|
| Maximum profit | (5 - 2.15) x 100 = US$285, if Stock A is at 55 or more | US$130, if Stock A is at 50 or more |
| Maximum loss | US$215, if Stock A is at 50 or less | (5 - 1.30) x 100 = US$370, if Stock A is at 45 or less |
| Breakeven | 50 + 2.15 = 52.15 | 50 - 1.30 = 48.70 |

Both losses are fixed, and neither depends on how far the stock falls beyond the long strike. That is the point: the long leg stops the short leg's loss.

![Profit of a bull call spread and a bull put spread on Stock A, at expiry and six weeks before](../assets/figures/15-options/vertical-spreads-dark.svg#only-dark)
![Profit of a bull call spread and a bull put spread on Stock A, at expiry and six weeks before](../assets/figures/15-options/vertical-spreads-light.svg#only-light)

Look at where the dashed line (six weeks before expiry) sits against the solid one. It is smoother and passes closer to zero. Before expiry the spread is worth less than its maximum at the high strike, and the gap closes only as expiry approaches.

## The Greeks

At the chain's volatilities, per contract, the bull call spread has delta +25.71, gamma +0.21, theta -US$0.39 a day and vega +US$1.02. That is a small net of two large numbers: the long 50 call and the short 55 call mostly cancel. The bull put spread has delta +20.70, gamma -1.81, theta +US$0.03 a day and vega -US$2.32.

The debit spread is a bet on direction with little decay and little volatility exposure, and that is why traders use it instead of a plain call when the implied volatility is high. The credit spread is paid for the stock holding up, and it is short volatility.

## When it works and how it fails

A debit spread works when you have a target for the stock and the spread is cheap against the move you expect. It fails when the stock moves slowly: the position gains only by expiry, so a fast rise early adds little. It fails when the stock overshoots, because the gain stops at 55.

A credit spread works when the stock stays above the short strike. It fails on a sharp fall, where one move takes you from a small gain to the full loss, and the loss is larger than the gain (US$370 against US$130 here). A credit spread usually wins more often than it loses, because the stock only has to stay above the short strike, but each loss is larger than each win.

What tests found: we found no published test of vertical spreads on single stocks that accounts for costs, so we quote none.

## Assignment risk

The short leg can be assigned early. If the short 50 put in the bull put spread is assigned, you buy 100 shares at 50 and still hold the 45 put. The 45 put caps the loss, but you now hold shares worth about US$5,000, and the broker may need cash or margin for them until you sell. Many brokers close or restrict a spread near expiry. Lesson 14 covers this ([Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md)).

## Sizing in R

The maximum loss is known, so 1R can be the maximum loss, or a fraction of it. We use an account of US$25,000 with 1R = 1% = US$250.

<div class="example" markdown>

### Worked example: sizing and trading the bull call spread

Commissions are made up: US$0.65 per contract per leg, charged on opening and on closing. The spread has two legs, so a round trip costs 2 x 2 x 0.65 = US$2.60.

1. Debit 2.15 x 100 = US$215. Maximum loss with fees = 215 + 2.60 = US$217.60, which is 0.87R. One spread fits. Two would risk US$435.20, or 1.74R.
2. Maximum profit = 285 - 2.60 = US$282.40, which is 1.13R. The reward to risk is 282.40 / 217.60 = 1.30.
3. At expiry with Stock A at 58: both legs are in the money, the spread is worth 5.00, and the profit is US$282.40. At 52.15 you break even before fees. At 50 or less you lose US$217.60.
4. The credit spread of the table does not fit the limit. Its maximum loss with fees is 370 + 2.60 = US$372.60, which is 1.49R, so zero contracts at 1%. A narrower spread does fit: sell the 47.50 put at 1.80 and buy the 45 put at 1.35 for a credit of 0.45 (US$45). Its maximum loss is (2.50 - 0.45) x 100 = US$205, which is US$207.60 with fees, or 0.83R, and its breakeven is 47.05.

</div>

Part 3 gives the rule: size from the loss, not from the account balance or from how likely the win seems. A credit spread's high chance of winning does not change its 1.49R worst case. A credit spread also needs collateral: your broker holds the width less the credit (US$370 for the first spread) until it closes.

<div class="canada" markdown>

### For Canadians

Wealthsimple's help centre says spreads need a margin account with USD accounts enabled and cannot be traded in registered accounts such as a TFSA or RRSP ([Wealthsimple spreads](https://help.wealthsimple.com/hc/en-ca/articles/43913330243227-Trade-multi-leg-options-spreads), as of 2026; the page blocks automated fetching, so this comes from a search summary). Wealthsimple's options marketing page lists credit spreads for registered accounts, so its pages disagree. Ask support in writing before you plan a spread. Lesson 15 covers account rules.

</div>

## Common mistakes

- Calling a credit spread "safe" because it usually wins. The worst case is larger than the best case.
- Sizing by the credit. The risk is the width less the credit.
- Choosing strikes by price alone. A wide spread near the money is a different bet from a narrow one far away.

## Try it

1\. Buy the 52.50 call at the ask 2.20 and sell the 55 call at the bid 1.30. What are the debit, maximum profit, maximum loss and breakeven?

<details class="solution" markdown>
<summary>Answer</summary>

Debit = 2.20 - 1.30 = 0.90, US$90. Width 2.50. Maximum profit = (2.50 - 0.90) x 100 = US$160. Maximum loss = US$90. Breakeven = 52.50 + 0.90 = 53.40.

</details>

2\. For the bull put 50/45 (credit 1.30), what is the profit at expiry if Stock A is at 47?

<details class="solution" markdown>
<summary>Answer</summary>

The short 50 put is worth 3.00 and the long 45 put is worth 0. Profit = 1.30 - 3.00 = -1.70, so -US$170 before fees.

</details>

3\. A spread has a maximum loss of US$217.60 with fees and your 1R is US$300. How many contracts fit?

<details class="solution" markdown>
<summary>Answer</summary>

300 / 217.60 = 1.38, so 1 contract. Round down.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On a chain, build a bull call spread: write the ask of the lower call, the bid of the higher call, the debit and the breakeven. |
| 3 | Write the maximum loss with fees from your own broker's schedule, and the number of contracts that fit your 1R. |
| 3 | Journal it as a paper trade idea ([trade journal](../practice/trade-journal.md)): the plan, size and exit before the open. |

</div>

## Key terms

- **Vertical spread**: a long and a short option of the same type and expiry at different strikes.
- **Width**: the difference between the two strikes.
- **Debit**: the net premium you pay to open a position.
- **Bull call spread**: buy a lower call, sell a higher call.
- **Bull put spread**: sell a higher put, buy a lower put.

Next: [Straddles and strangles](11-straddles-and-strangles.md)
