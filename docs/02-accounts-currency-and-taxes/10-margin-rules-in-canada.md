# Margin rules in Canada

<span class="tag tag-canada">Canada</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">ACCT</span>

After this lesson you can say who sets margin requirements for a Canadian broker, find the price at which a margin call comes, include currency in that test, and use the part's rules to choose an account for a trade.

Before this: [Settlement, cash accounts and margin](../01-how-markets-work/07-settlement-cash-and-margin.md), [Tax losses and the superficial loss rule](09-tax-losses-and-superficial-loss.md). You need: a calculator.

## The idea

Lesson 7 of part 1 worked a margin example under US rules. A Canadian broker follows CIRO's margin rules instead, and adds its own on top. The margin requirement depends on the security: Wealthsimple's margin page says the limits are set by CIRO and gives the example that a 30% requirement allows about 3.33 times leverage on available margin (1 / 0.30). It also says the broker can set requirements above CIRO's minimums and can impose borrowing limits or caps on a single security ([Wealthsimple margin](https://www.wealthsimple.com/en-ca/self-directed-investing/margin), as of 2026). Which rate your US stock gets is on your broker's margin page, because I could not read CIRO's list and the broker may be stricter.

A **margin call** happens when your equity falls below the maintenance requirement. Wealthsimple says you must then add cash or eligible securities, or sell positions, and that if you do not, the brokerage can sell securities in your account under your agreements. In Canada, as in lesson 7, do not count on a warning first.

Margin is only for non-registered accounts at IBKR Canada ([IBKR Canada individual accounts](https://www.interactivebrokers.ca/en/accounts/individual.php), as of 2026), and you need to apply for it at Wealthsimple. Wealthsimple's rates run from 3.24% to 5.70% in Canadian dollars and from 4.50% to 8.00% in US dollars by amount borrowed, set off a prime rate of 4.70% (C$) and 7.00% (US$) as its page showed in November 2026. Interest accrues daily and is charged monthly (same page).

## How it works

Let \(V_0\) be the starting value of the position, \(L\) the loan and \(m\) the maintenance requirement as a fraction of the position. Equity is \(V - L\), and the call comes when \(V - L < mV\), so at

\[ V_{\text{call}} = \frac{L}{1 - m} \]

- \(V_{\text{call}}\) is the position value at which the call is triggered, in C$.
- \(L\) is the loan, in C$. It does not change when the price does (before interest).
- \(m\) is the maintenance requirement, such as 0.30. It is a made-up value in these examples.

The fall that triggers the call is \(1 - V_{\text{call}} / V_0\).

<div class="example" markdown>

### Worked example: a 3 times position in a US stock

You have C$20,000 and borrow C$40,000 to hold C$60,000 of Stock A, a US stock. The requirement is 30% and the loan rate is 5% (both made up, the rate is inside the Wealthsimple range for C$).

1. Equity ratio at the start: (60,000 - 40,000) / 60,000 = 33.3%.
2. Call value: 40,000 / (1 - 0.30) = C$57,142.86.
3. Fall that triggers the call: 1 - 57,142.86 / 60,000 = 4.76%.
4. At the call your equity is 57,142.86 - 40,000 = C$17,142.86, a loss of C$2,857.14, or 14.3% of your C$20,000.
5. Currency counts. Stock A falls 2% in US dollars and the US dollar falls 3% against the Canadian dollar. The position is worth 60,000 x 0.98 x 0.97 = C$57,036.00, a fall of 4.94%. Equity ratio = (57,036 - 40,000) / 57,036 = 29.9%, below 30%, so a call comes even though the stock fell only 2%.
6. Interest for 30 days on C$40,000 at 5%: 40,000 x 0.05 x 30 / 365 = C$164.38.

A 4.76% fall costs you 14.3% of your cash. Interest and currency make the real cushion thinner.

</div>

The figure shows four loan sizes. Look at where each line crosses the dashed 30% line: the larger the loan, the sooner it crosses.

![Equity as a share of the position against the fall in value, with calls at 4.8% and 28.6% falls for the two larger loans](../assets/figures/02-accounts-currency-and-taxes/margin-call-dark.svg#only-dark)
![Equity as a share of the position against the fall in value, with calls at 4.8% and 28.6% falls for the two larger loans](../assets/figures/02-accounts-currency-and-taxes/margin-call-light.svg#only-light)

## Choosing an account

The part's rules give a way to choose:

1. Long-term holding, no borrowing: a TFSA or RRSP (lesson 1), keeping the dividend withholding in mind (lesson 6).
2. Frequent trading with borrowing or shorting: a non-registered margin account, with the tax consequences of lessons 7 and 9.
3. Converting a large amount: the tiers or the gambit (lessons 3 and 4).
4. A first-home goal: an FHSA, subject to its limits.

<div class="canada" markdown>

### For Canadians

FINRA's day-trading changes in part 1 are US rules. IBKR's own pages for Canadian clients have shown different day-trading text, and I could not confirm how the changes apply to an IBKR Canada account, so read the broker's current day-trading and margin pages. Day-trading margin for Canadian dealers falls under CIRO's rules, whose text I did not read.

</div>

## Common mistakes

- Sizing the loan by what the broker allows. The call comes much sooner than a full fall in the position.
- Leaving out the exchange rate when the position is a US stock.
- Assuming a margin call gives you time to deposit funds.

## Try it

1\. You hold C$30,000 of Stock A with a C$18,000 loan and a 30% requirement. At what position value does a call come, and what fall is that?

<details class="solution" markdown>
<summary>Answer</summary>

V_call = 18,000 / 0.70 = C$25,714.29. Fall = 1 - 25,714.29 / 30,000 = 14.29%.

</details>

2\. A C$10,000 loan at 6% for 45 days. What is the interest?

<details class="solution" markdown>
<summary>Answer</summary>

10,000 x 0.06 x 45 / 365 = C$73.97.

</details>

3\. Using the worked example, the stock rises 5% in US dollars and the dollar is unchanged. What is your return on the C$20,000, before interest?

<details class="solution" markdown>
<summary>Answer</summary>

The position is 60,000 x 1.05 = C$63,000. Equity = 63,000 - 40,000 = C$23,000. Return = 3,000 / 20,000 = 15%.

</details>

## Part check

1\. Which account types does IBKR Canada allow margin in?

<details class="solution" markdown>
<summary>Answer</summary>

Non-registered individual accounts only, not a TFSA, RRSP or FHSA.

</details>

2\. A CAD account has a 1.5% conversion fee on each fill and a flat rate of 1.3500. You buy and sell US$10,000 at the same price. What does the round trip cost in C$?

<details class="solution" markdown>
<summary>Answer</summary>

Buy: 10,000 x 1.35 x 1.015 = C$13,702.50. Sell: 10,000 x 1.35 x 0.985 = C$13,297.50. Cost = C$405.00.

</details>

3\. A stock rises 6% in US dollars and the rate moves from 1.4000 to 1.3600. What is your return in C$?

<details class="solution" markdown>
<summary>Answer</summary>

Rate change = 1.36 / 1.40 - 1 = -2.86% (rounded). Return = 1.06 x 0.9714 - 1 = 2.97% (rounded).

</details>

4\. A US$400 dividend is paid into a TFSA and into an RRSP, with a W-8BEN on file. How much is withheld in each?

<details class="solution" markdown>
<summary>Answer</summary>

TFSA: 15% of 400 = US$60.00 (you receive US$340.00). RRSP: US$0.00.

</details>

5\. You hold 100 shares with a C$40.00 cost and add 100 with a C$50.00 cost. You sell 50 shares at C$60.00. What is the gain?

<details class="solution" markdown>
<summary>Answer</summary>

ACB per share = (4,000 + 5,000) / 200 = C$45.00. Gain = 50 x 60.00 - 50 x 45.00 = 3,000 - 2,250 = C$750.00.

</details>

6\. You sell at a loss on November 20, 2026. What is the last day of the superficial loss window, and is a buyback on December 15 that you hold into January a problem?

<details class="solution" markdown>
<summary>Answer</summary>

30 days after November 20 is December 20, 2026. A buyback on December 15 is inside the window and you still hold it 30 days after the sale, so the loss is superficial.

</details>

7\. A profit of C$8,000 at a 30% marginal rate. What is the tax as a capital gain and as business income?

<details class="solution" markdown>
<summary>Answer</summary>

Capital gain: 8,000 x 1/2 x 30% = C$1,200. Business income: 8,000 x 30% = C$2,400.

</details>

8\. A C$12,000 account borrows C$18,000 for a C$30,000 position with a 30% requirement. Which fall triggers a call?

<details class="solution" markdown>
<summary>Answer</summary>

V_call = 18,000 / 0.70 = C$25,714.29, a fall of 14.29%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find your broker's margin page. Write the requirement for one US stock you follow and the loan rate. |
| 4 | Compute the call price for a made-up position at that requirement. |
| 2 | Add a line to your [trade journal](../practice/trade-journal.md) template: account type, currency and loan size for each trade. |

</div>

## Key terms

- **Margin requirement**: the share of a position that must be your own equity.
- **Maintenance requirement**: the minimum equity share you must keep, below which a margin call comes.
- **Call value**: the position value at which equity equals the requirement.
- **CIRO margin rules**: the rules that set the minimum margin Canadian investment dealers require.

Next: [Risk first: the math of losses](../03-risk-and-position-sizing/01-risk-first.md)
