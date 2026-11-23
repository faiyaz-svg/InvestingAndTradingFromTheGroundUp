# Iron condors and butterflies

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">OPT</span>

After this lesson you can build an iron condor and a call butterfly from the chain, find their breakevens, maximum profit and maximum loss, and size them so the worst case is within your limit.

Before this: [Vertical spreads](10-vertical-spreads.md), [Straddles and strangles](11-straddles-and-strangles.md). You need: a calculator.

## The idea

The last lesson bought volatility. These two strategies do the reverse: they profit when the stock stays in a range. Each is built from vertical spreads, so the loss is defined.

An **iron condor** is two credit spreads at once: a bull put spread below the stock and a bear call spread above it. You collect two credits and keep them all if the stock ends between the two short strikes. A **butterfly** buys one option at a lower strike, sells two at a middle strike, and buys one at an upper strike, all of the same type and expiry. It pays most if the stock ends at the middle strike.

## The construction

Stock A is US$50.20, expiry February 19, 2027. You buy at the ask and sell at the bid.

| Position | Trade | Net |
|---|---|---|
| Iron condor | Buy the 45 put at 1.35, sell the 47.50 put at 1.80, sell the 52.50 call at 2.10, buy the 55 call at 1.35 | Credit 1.80 - 1.35 + 2.10 - 1.35 = 1.20, so US$120 |
| Call butterfly, 47.50 / 50 / 52.50 | Buy the 47.50 call at 5.10, sell two 50 calls at 3.35, buy the 52.50 call at 2.20 | Debit 5.10 + 2.20 - 6.70 = 0.60, so US$60 |

With the credit \(C\), the debit \(D\) and the wing width \(W\) (2.50 in both):

\[ \text{condor: max profit} = C \times 100, \quad \text{max loss} = (W - C) \times 100 \]
\[ \text{butterfly: max profit} = (W - D) \times 100, \quad \text{max loss} = D \times 100 \]

- \(W\) is the gap between adjacent strikes, in US$ per share.
- The condor's two wings are the same width, so only one side can lose at expiry.
- The condor's breakevens are the short put strike less \(C\) and the short call strike plus \(C\).
- The butterfly's breakevens are the lowest strike plus \(D\) and the highest strike less \(D\).

| | Iron condor | Call butterfly |
|---|---|---|
| Maximum profit | US$120, for \(S\) from 47.50 to 52.50 | (2.50 - 0.60) x 100 = US$190, at \(S = 50\) |
| Maximum loss | (2.50 - 1.20) x 100 = US$130, at \(S\) of 45 or less, or 55 or more | US$60, at \(S\) of 47.50 or less, or 52.50 or more |
| Breakevens | 47.50 - 1.20 = 46.30 and 52.50 + 1.20 = 53.70 | 47.50 + 0.60 = 48.10 and 52.50 - 0.60 = 51.90 |

The solid lines show the profit at expiry. The flat top of the condor and the single peak of the butterfly are the two shapes to remember. The dashed lines show six weeks before expiry: both are low and wide, and they rise toward the solid shape only as time passes.

![Profit of an iron condor and a call butterfly on Stock A, at expiry and six weeks before](../assets/figures/15-options/condor-butterfly-dark.svg#only-dark)
![Profit of an iron condor and a call butterfly on Stock A, at expiry and six weeks before](../assets/figures/15-options/condor-butterfly-light.svg#only-light)

The condor has the bigger profit zone (46.30 to 53.70) and a smaller peak. The butterfly pays more than three times what it risks at its peak, 190 against 60, but only if the stock finishes within about 1.90 of 50.

## The Greeks

At the chain's volatilities, per contract, the condor has delta -3.42, gamma -1.48, theta +US$0.30 a day and vega -US$2.40. The butterfly has delta -1.59, gamma -0.54, theta +US$0.14 a day and vega -US$0.94. Both are close to delta neutral, collect a little time decay, are short gamma and short volatility. The Greeks are small because the long and short legs cancel, so the profit is small too. A rise in IV hurts both, and a quiet stock helps.

## When it works and how it fails

A condor fits a stock you expect to stay in a range, after a volatility spike when IV is high. It fails on a break out of the range: one side loses US$130 while the other side's credit is already kept, so the loss is capped but is larger than the profit (130 against 120). It fails on a second day of news and on gaps, which skip your stop and land past a long strike.

A butterfly fits a view that the stock will pin near one price, such as a round number into expiry. Its hit rate is low, because the profit zone is narrow, and it pays for that with a large payoff. It fails whenever the stock drifts. Both need a liquid chain, because each trade has four legs and four spreads to cross. On the chain, the four condor legs cross about 0.05 to 0.10 each; that is why you place the whole order at the middle between the bid and ask.

What tests found: we found no good published test of iron condors or butterflies on single stocks with costs, so we quote none. The closest evidence is index put-writing, which shows that short-volatility positions earned a premium in the past (lesson 9) and is a reminder that the loss comes in the left tail.

## Assignment risk

Only the short legs can be assigned. A short 47.50 put or short 52.50 call that finishes in the money at expiry is likely to be assigned, and then you hold shares or a short stock position until the long leg is exercised or you close it. Close the position before the last day if the stock is near a short strike. Lesson 14 covers pin risk ([Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md)).

## Sizing in R

Both have a known maximum loss. Use the maximum loss plus fees as 1R, or a fraction of it. We use US$25,000 and 1R = US$250.

<div class="example" markdown>

### Worked example: sizing the condor and the butterfly

Commissions are made up: US$0.65 per contract per leg, charged on opening and on closing. Four contracts make one round trip of 4 x 2 x 0.65 = US$5.20, for either position.

1. Condor: maximum loss = 130 + 5.20 = US$135.20, which is 0.54R. Two condors would risk US$270.40, or 1.08R, so one condor fits.
2. Condor maximum profit = 120 - 5.20 = US$114.80, or 0.46R. The reward to risk is 114.80 / 135.20 = 0.85.
3. Butterfly: maximum loss = 60 + 5.20 = US$65.20 per butterfly, or 0.26R. Three butterflies risk US$195.60 (0.78R). Four risk US$260.80 (1.04R), so three fit.
4. Three butterflies at 50 at expiry: profit = 3 x (190 - 5.20) = US$554.40, or 2.22R. At 52.50 or more: -US$195.60.
5. Stock A at 53 at expiry: the condor's call spread is worth 0.50 against its 52.50/55 strikes. Condor profit = 120 - 50 - 5.20 = US$64.80.

</div>

The size is set by the loss, as in part 3. A condor whose best case is smaller than its worst case needs a high win rate: break-even odds are 135.20 / (135.20 + 114.80) = 54%, ignoring partial outcomes.

<div class="canada" markdown>

### For Canadians

Wealthsimple's help centre says multi-leg spreads need a margin account and are not offered in registered accounts, but its marketing page lists credit spreads for them (lesson 15 has the sources). Confirm in writing before you try these in a TFSA or RRSP. Use a non-registered margin account, with the tax treatment in part 2.

</div>

## Common mistakes

- Selling a condor for the credit and placing no exit. Decide the loss level before you enter.
- Choosing a very narrow butterfly and expecting to hit it. The zone is about 3.80 wide at the money.
- Holding a condor into the last day with a short strike near the stock.

## Try it

1\. An iron condor collects a credit of 1.00 with wings 2.50 wide. What are the maximum profit and maximum loss?

<details class="solution" markdown>
<summary>Answer</summary>

Maximum profit US$100. Maximum loss (2.50 - 1.00) x 100 = US$150.

</details>

2\. A butterfly 45 / 50 / 55 costs 1.50. What are the maximum profit and the breakevens?

<details class="solution" markdown>
<summary>Answer</summary>

Width 5. Maximum profit (5 - 1.50) x 100 = US$350, at 50. Breakevens 45 + 1.50 = 46.50 and 55 - 1.50 = 53.50.

</details>

3\. The condor (credit 1.20, short strikes 47.50 and 52.50) ends at 46 at expiry. What is the profit before fees?

<details class="solution" markdown>
<summary>Answer</summary>

The 47.50 put is worth 1.50 and the 45 put is worth 0. The put spread costs 1.50. Profit = 1.20 - 1.50 = -0.30, so -US$30.

</details>

4\. A condor risks US$135.20 per contract and your 1R is US$250. How many fit?

<details class="solution" markdown>
<summary>Answer</summary>

250 / 135.20 = 1.85, so 1 condor.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On a chain, build an iron condor with 2.50 or 5 wings and write the credit, both breakevens and the maximum loss. |
| 3 | Add fees from your broker's schedule and write the loss as a fraction of your 1R. |
| 3 | Write the exit rule (a loss level and a day before expiry) in your journal ([trade journal](../practice/trade-journal.md)). |

</div>

## Key terms

- **Iron condor**: a bull put spread below the stock plus a bear call spread above it, opened for a credit.
- **Butterfly**: one option bought at a lower strike, two sold at the middle strike, one bought at an upper strike.
- **Wing**: the long option that caps the loss on one side of a condor or butterfly.

Next: [Calendars and diagonals](13-calendars-and-diagonals.md)
