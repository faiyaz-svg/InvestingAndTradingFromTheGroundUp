# Calendars and diagonals

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">OPT</span>

After this lesson you can build a call calendar and a call diagonal, read their profit at the near expiry, say what they gain from, and size one by its debit.

Before this: [Iron condors and butterflies](12-iron-condors-and-butterflies.md), [Theta, vega and rho](07-theta-vega-and-rho.md). You need: a calculator.

## The idea

Time decay is not even (lesson 7). An option with 56 days left loses value faster each day than one with 91 days left. A **calendar spread** uses that gap: you sell a near-dated option and buy a far-dated option of the same type and strike. The near option decays faster than the far one, so the spread widens if the stock stays near the strike.

A **diagonal spread** is the same idea with different strikes as well as different expiries. Buying the far-dated call at a lower strike and selling the near-dated call at a higher strike looks like a covered call with a call in place of the shares.

Both are debits. The near leg is the **short leg** and the far leg is the **long leg**.

## The construction

Take today as November 20, 2026, with Stock A at US$50.20 and the chain's February 19, 2027 expiry as the far leg (91 days, T = 0.25). The near leg expires January 15, 2027, 56 days from today. The chain in lesson 3 has only the far expiry, so the near quotes below are made up: the model price at 31% volatility, with the bid and the ask 0.025 either side of it.

| Position | Trade | Net |
|---|---|---|
| Call calendar at 50 | Sell the January 50 call at the bid 2.65, buy the February 50 call at the ask 3.45 | Debit 3.45 - 2.65 = 0.80, so US$80 |
| Call diagonal | Sell the January 52.50 call at the bid 1.59, buy the February 50 call at the ask 3.45 | Debit 3.45 - 1.59 = 1.86, so US$186 |

You cannot read the profit at expiry off a simple formula, because the far leg has time left when the near leg expires. At the near expiry, 35 days remain on the far leg (\(T = 35/365 = 0.096\) years). Use the Black-Scholes price (lesson 4) for the far leg with the same volatility as today:

\[ \text{profit} = -\max(S - K_s, 0) + V_{far}(S) - D \]

- \(S\) is Stock A's price on January 15.
- \(K_s\) is the short call's strike, 50 for the calendar and 52.50 for the diagonal.
- \(V_{far}(S)\) is the model value of the February call with 35 days left, in US$ per share.
- \(D\) is the debit, 0.80 or 1.86.

| Stock A on January 15 | 44 | 46 | 48 | 50 | 52 | 54 | 56 |
|---|---|---|---|---|---|---|---|
| Calendar profit per contract | -US$60 | -US$29 | +US$29 | +US$119 | +US$42 | -US$7 | -US$34 |
| Diagonal profit per contract | -US$166 | -US$135 | -US$77 | +US$13 | +US$136 | +US$137 | +US$110 |

The calendar's maximum profit is about US$119, at a stock price of 50 when the near leg expires. Its breakevens in the model are about 47.13 and 53.66. Its maximum loss is the US$80 debit, if you close both legs when the near leg expires. The diagonal's breakeven is about 49.75, and its loss is the US$186 debit if the stock falls.

The table is rounded to whole dollars. The tent shape of the calendar is the figure's solid line. The diagonal leans to the right, because its long call at 50 gains when the stock rises, while the short 52.50 call caps the near-term gain.

![Profit of a call calendar and a call diagonal on Stock A, today and at the near leg's expiry](../assets/figures/15-options/calendar-diagonal-dark.svg#only-dark)
![Profit of a call calendar and a call diagonal on Stock A, today and at the near leg's expiry](../assets/figures/15-options/calendar-diagonal-light.svg#only-light)

The table and figure rest on a model price for the far leg, so treat the numbers as estimates. A real far-dated option will carry its own volatility on January 15, and that moves the answer.

## The Greeks

At the chain's volatilities, per contract, the calendar has delta +0.94, gamma -1.35, theta +US$0.50 a day and vega +US$2.11 per volatility point. The diagonal has delta +16.84, gamma -1.21, theta +US$0.37 and vega +US$2.28. The calendar is nearly delta neutral, is paid for time, and is long volatility. That last part is what separates it from the condor: a rise in IV helps a calendar, because the long far leg has more vega than the short near leg. A fall in IV hurts it, and a five point fall costs about 5 x 2.11 = US$10.55.

## When it works and how it fails

A calendar fits a stock you expect to stay near a strike until the near expiry, with IV not about to drop. It fails when the stock moves away from the strike. It fails when IV falls in the far month (the long leg loses), and around an event inside the near leg's life, where the near option's price jumps and the position is short that jump. Traders often close before the near expiry, to avoid the gamma and the assignment on the short leg in the last days.

A diagonal fits a mildly bullish view. It fails when the stock drops, because the long leg loses, and when it jumps past 52.50 early, because the short call is then deep in the money.

What tests found: we found no good published test of calendars or diagonals on single stocks that accounts for costs, so we quote none.

## Assignment risk

The short near call can be assigned, mostly when it is in the money shortly before a dividend (lesson 14, [Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md)). The long February call does not cover it automatically. If you are assigned, you are short 100 shares until you exercise the February call, which gives up its time value, or close the shares. Close or roll the short leg before the ex-dividend date if it is in the money.

## Sizing in R

The debit is the maximum loss if you close both legs together at the near expiry. We use US$25,000 and 1R = US$250.

<div class="example" markdown>

### Worked example: three calendars and one diagonal

Commissions are made up: US$0.65 per contract per leg, charged on opening and on closing. A two-leg round trip is US$2.60.

1. Calendar: debit 80 + fees 2.60 = US$82.60 per calendar, which is 0.33R. Three calendars risk US$247.80, or 0.99R. Four would risk US$330.40, or 1.32R. Take three.
2. Three calendars at 50 on January 15 (model estimate): profit = 3 x (119 - 2.60) = US$349.20, which is 1.40R.
3. The same three if the stock is at 56: loss = 3 x (34 + 2.60) = US$109.80, or 0.44R. At 44: -3 x (60 + 2.60) = -US$187.80, or 0.75R.
4. Diagonal: debit 186 + 2.60 = US$188.60, which is 0.75R, so one diagonal fits. At 52 on January 15: profit = 136 - 2.60 = US$133.40, or 0.53R. At 44 the loss is 166 + 2.60 = US$168.60, or 0.67R.

If the stock sits at 50 at the near expiry, you could also hold the far call and write another near call. That is a new trade with a new risk, so size it again.

</div>

<div class="canada" markdown>

### For Canadians

Calendars and diagonals are multi-leg spreads, which Wealthsimple's help centre limits to margin accounts (lesson 15 has the sources and a conflict between its pages). IBKR Canada's rules for these were not confirmed for this book, so check your account's permissions.

</div>

## Common mistakes

- Treating the model table as a quote. The far leg's real value depends on the IV that day.
- Holding the short leg through ex-dividend while it is in the money.
- Opening a calendar before an event inside the near leg's life without allowing for the jump.

## Try it

1\. A calendar sells the near call at 2.65 and buys the far call at 3.45. What is the maximum loss in dollars, per contract, and what does it need to be true?

<details class="solution" markdown>
<summary>Answer</summary>

The debit 3.45 - 2.65 = 0.80, so US$80. It holds if you close both legs together at the near expiry.

</details>

2\. Which Greek explains why a fall in IV hurts a calendar?

<details class="solution" markdown>
<summary>Answer</summary>

Vega. The long far leg has more vega than the short near leg, so the net vega is positive (+US$2.11 per point here), and a fall in IV loses money.

</details>

3\. The diagonal's far call is bought at 3.45 and the near 52.50 call is sold at 1.59. Stock A is at 54 on the near expiry and the diagonal is worth US$137 per contract. What is the profit after the US$2.60 of fees?

<details class="solution" markdown>
<summary>Answer</summary>

137 - 2.60 = US$134.40.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On a chain with two expiries, find the same-strike call in each. Write the near bid, the far ask and the debit. |
| 3 | Compare the two implied volatilities. If the near one is higher, say what that does to the spread. |
| 3 | Write the exit rule: the date before the near expiry that you close both legs ([trade journal](../practice/trade-journal.md)). |

</div>

## Key terms

- **Calendar spread**: sell a near-dated option and buy a far-dated option of the same type and strike.
- **Diagonal spread**: a near-dated short option and a far-dated long option of the same type at different strikes.
- **Near leg**: the shorter-dated option in a calendar or diagonal.
- **Far leg**: the longer-dated option.

Next: [Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md)
