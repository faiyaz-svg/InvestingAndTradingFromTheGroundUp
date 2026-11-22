# Trading forex from Canada

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can say which forex positions you already hold, find the margin rate your Canadian dealer must use for a pair, and work out the leverage, the margin and the pip move that wipes out a small forex position.

Before this: [Forex basics](04-forex-basics.md), [Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md), [Wealthsimple and IBKR compared](../02-accounts-currency-and-taxes/02-wealthsimple-and-ibkr.md). You need: a calculator.

## The idea

You hold US$10,000 in a USD account at IBKR, bought with Canadian dollars when USD/CAD was 1.3650. You have not placed a forex trade, and you do not plan to. Still, you are long USD/CAD: you own US dollars, and their value in Canadian dollars changes with the rate.

| Moment | USD/CAD | Value of US$10,000 in CAD |
|---|---|---|
| When you converted | 1.3650 | C$13,650 |
| Later | 1.3240 | C$13,240 |

The loss is 13,240 - 13,650 = -C$410, which is 1.3240 / 1.3650 - 1 = -3.0%. Nothing was traded. This is the currency risk of Part 2 ([Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)), and it is the same position as a trader who bought USD/CAD on purpose. Holding a foreign currency is a forex position. Trading forex means taking that position deliberately, usually with borrowed money, and in either direction.

## How forex is regulated and sold here

Spot forex for retail clients in Canada is sold by dealers regulated by CIRO, the Canadian Investment Regulatory Organization. CIRO sets minimum margin for unhedged foreign exchange positions in client accounts. It sorts currencies into groups and publishes a list of FX spot risk margin rates for accounts in Canadian and US dollars. The dealer's margin on a pair cannot be lower than the rate on that list. CIRO updates the list as currency volatility changes, so the numbers change ([CIRO, FX spot risk margin rates list](https://www.ciro.ca/rules-and-enforcement/dealer-member-rules/supporting-schedules/list-foreign-exchange-fx-spot-risk-margin-rates-canadian-and-us-base-currency-accounts); the last update seen when this was written was Bulletin 25-0232, released August 8, 2025 and effective August 13, 2025, and later updates may exist). The rules are in sections 5461 to 5469 of CIRO's Investment Dealer and Partially Consolidated Rules.

The book does not print the current percentage for each pair. The list changes, and your broker may require more than CIRO's minimum. Open the list, find the pair, and read its rate. Then check your broker's own margin page for the figure it applies to you.

### Leverage from a margin rate

**Margin** here is the deposit you post to hold a larger forex position, the idea you met for futures in Part 14 ([Margin, leverage and mark to market](../14-futures/02-margin-leverage-and-mark-to-market.md)). The margin rate gives the leverage:

\[ \text{leverage} = \frac{1}{\text{margin rate}} \]

- \(\text{margin rate}\) is the required deposit as a fraction of the position's value (0.02 for 2%).
- \(\text{leverage}\) is the position value divided by the deposit, a multiple.

<div class="example" markdown>

### Worked example: a leveraged USD/CAD position

The margin rate below is made up to show the arithmetic. It is not CIRO's figure for USD/CAD. You buy 20,000 units of USD/CAD at 1.3650 with a made-up margin rate of 2%.

1. Position value: 20,000 x 1.3650 = C$27,300.
2. Margin: 0.02 x 27,300 = C$546.00.
3. Leverage: 1 / 0.02 = 50, or 27,300 / 546 = 50.
4. Value of one pip: 20,000 x 0.0001 = C$2.00. A 100-pip move is 100 x 2.00 = C$200, which is 200 / 546 = 36.6% of the margin.
5. The move that uses up the whole margin: 546 / 20,000 = 0.0273, which is 273 pips, or 0.0273 / 1.3650 = 2.0% of the rate.

A broker closes positions before the loss reaches the full margin, so the real distance to a forced exit is shorter. USD/CAD moved 222 pips from the September 28 close to the October 16 close in lesson 4's made-up series, so a move of this size is ordinary.

</div>

The example shows why the leverage figure alone does not describe the risk. Size the position from the loss you accept, as Part 3 does ([Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md)), and treat margin as a limit, not a target. A stop at 50 pips on this position risks C$100.

## Where you can trade it

**IBKR.** Interactive Brokers Canada lets you trade currency pairs in its accounts, and a currency conversion at IBKR is itself a forex trade. IBKR publishes a spot currency commission schedule and minimum order sizes, and orders below the size minimum on its main forex venue can be routed to an odd-lot book at slightly worse prices ([IBKR Canada, spot currency commissions](https://www.interactivebrokers.ca/en/pricing/commissions-spot-currencies.php), [minimum and maximum order sizes](https://interactivebrokers.ca/en/index.php?f=5479), as of 2026; check both pages for the current numbers). Part 2 compared IBKR's conversion costs with Wealthsimple's ([USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md)).

**Other brokers.** Spot forex is not offered at every Canadian broker. Look at your broker's products page or ask support whether it offers currency pairs, in which account types, and at what margin. Do not assume that a broker that offers futures or stocks also offers forex.

**Account type.** Leveraged forex needs a margin account. Part 2 covers what registered accounts allow ([Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md)).

**Checking the firm.** Forex advertising is common and the firms vary. Confirm that the firm is registered in Canada and a CIRO member before you deposit money.

## Costs and taxes

The spread is the main cost, as lesson 4's trade showed: 2 pips on 20,000 units was C$4.00. Add commissions, and the financing charge or credit for holding a position overnight, which comes from the interest rate gap in lesson 5. A position held for a month carries the gap between the two rates for the days held.

For tax, the CRA decides whether gains and losses on currency trades are capital or business income, from facts such as how often and how long you trade. Part 2 covers that test ([Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md)) and the records you need ([Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md)).

## Common mistakes

- Reading leverage as the maximum safe size. A 50-times position moves 50 times as fast against you.
- Quoting a leverage figure from an advertisement. The binding numbers are CIRO's list and your broker's margin page.
- Forgetting that your USD cash is already a position, and adding a forex trade in the same direction.

## Try it

1\. You hold US$25,000 at USD/CAD 1.3500. The rate moves to 1.3800. What is the change in your CAD value?

<details class="solution" markdown>
<summary>Answer</summary>

Before: 25,000 x 1.3500 = C$33,750. After: 25,000 x 1.3800 = C$34,500. Change = +C$750, which is +2.2%.

</details>

2\. A margin rate of 3.3% (made up). What leverage does it give, to one decimal?

<details class="solution" markdown>
<summary>Answer</summary>

1 / 0.033 = 30.3.

</details>

3\. You buy 10,000 units of USD/CAD at 1.3650 with a 2% margin rate (made up). What is the margin in CAD, and the pip move that equals half of it?

<details class="solution" markdown>
<summary>Answer</summary>

Value = 10,000 x 1.3650 = C$13,650. Margin = 0.02 x 13,650 = C$273.00. Pip value = C$1.00. Half of the margin is C$136.50, which is 136.5 pips.

</details>

4\. You would risk C$150 on 20,000 units of USD/CAD. How many pips can your stop be from entry?

<details class="solution" markdown>
<summary>Answer</summary>

Pip value = 20,000 x 0.0001 = C$2.00. Stop distance = 150 / 2.00 = 75 pips.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open CIRO's FX spot risk margin list. Find the group and rate for USD/CAD and write it with the bulletin number and date. |
| 3 | Open your broker's forex or currency page. Write whether it offers pairs, the account types and the margin rate it states. |
| 2 | In your [paper trading](../practice/paper-trading.md) notes, write the size of a USD/CAD trade that risks C$100 with a 40-pip stop. |

</div>

## Key terms

- **Margin (forex)**: the deposit posted to hold a larger forex position.
- **Margin rate**: the deposit as a fraction of the position's value.
- **FX spot risk margin rate**: the minimum margin rate CIRO sets for a currency, by currency group.
- **Odd lot (forex)**: an order below the minimum size of the main forex venue.

Next: [REITs explained](07-reits-explained.md)
