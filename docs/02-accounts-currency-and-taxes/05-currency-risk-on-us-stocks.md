# Currency risk on US stocks

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can split your return on a US stock into the stock's move and the exchange-rate move, compute your return in Canadian dollars, and say when a hedge or a USD account changes the risk.

Before this: [Norbert's gambit and CDRs](04-norberts-gambit-and-cdrs.md). You need: a calculator.

## The idea

You buy 100 shares of Stock A at US$50.00 when one US dollar costs C$1.40. The position costs US$5,000, or C$7,000. Later Stock A is at US$55.00, a 10% gain, but one US dollar costs only C$1.33. You sell for US$5,500, which is C$7,315. Your gain in Canadian dollars is C$315, or 4.5%. The stock gained 10% and you gained 4.5%, because the US dollar lost value against the Canadian dollar.

That is **currency risk** (also called exchange-rate risk): the chance that the exchange rate moves against you while you hold a foreign asset. A US stock has two sources of return for a Canadian investor: what the stock does in US dollars, and what the US dollar does against the Canadian dollar.

## How it works

The two returns multiply. If \(r_s\) is the stock's return in US dollars and \(r_x\) is the change in the exchange rate, your return in Canadian dollars is:

\[ 1 + r_c = (1 + r_s)(1 + r_x) \]

- \(r_c\) is your return in C$, as a fraction.
- \(r_s\) is the stock's return in US$, as a fraction.
- \(r_x\) is the change in C$ per US$ over the holding period: \(r_x = R_{\text{end}} / R_{\text{start}} - 1\), where \(R\) is the number of Canadian dollars one US dollar buys.

When \(R\) rises, the US dollar is stronger and a US holding gains in Canadian dollars. When \(R\) falls, it loses.

<div class="example" markdown>

### Worked example: the opening trade

1. Cost: 100 x US$50.00 = US$5,000, at 1.4000 is C$7,000.
2. Sale: 100 x US$55.00 = US$5,500, at 1.3300 is C$7,315.
3. Stock return: 55 / 50 - 1 = 10%.
4. Rate change: 1.3300 / 1.4000 - 1 = -5.0%.
5. Your return: 1.10 x 0.95 - 1 = 4.5%, and 7,315 / 7,000 - 1 = 4.5%.

The cross term matters a little. Adding 10% and -5% gives 5%, but the exact answer is 4.5%, because the -5% applies to a position that grew to 110%.

</div>

The figure puts four made-up cases side by side. The first is the Stock A trade, in the second both moves help, in the third a stock loss is partly offset by the currency, and in the fourth the stock does not move and the currency takes 7%.

![Bars of the stock return in US dollars, the US dollar move and your return in Canadian dollars for four cases](../assets/figures/02-accounts-currency-and-taxes/currency-return-dark.svg#only-dark)
![Bars of the stock return in US dollars, the US dollar move and your return in Canadian dollars for four cases](../assets/figures/02-accounts-currency-and-taxes/currency-return-light.svg#only-light)

## What changes the risk

A USD account does not remove currency risk. It moves the moment you measure it. If you hold US dollars in a USD account and never convert, the exchange rate does not change your US dollar balance, but it changes what that balance is worth in Canadian dollars whenever you spend it or report it for tax (lesson 8). If you spend Canadian dollars, you carry the risk either way.

A **hedge** is a position that offsets a risk. A currency-hedged fund or a CDR (lesson 4) holds the US stock and offsets the exchange-rate move with a currency contract, so the holder's return is close to the stock's US dollar return. The hedge has a cost, built into the fund's fee and returns, and it is not perfect. Check the issuer's page for how it works.

You do not need to hedge to trade. You need to know the exposure: a US$20,000 position changes in value by C$200 for each 0.01 change in the rate (exercise 3).

## Why it matters for a trader

For a swing or day trade lasting hours or days, the exchange rate rarely moves much, and the stock's own move dominates. For a position held for months or years, the currency can be a large part of the result, as the fourth case in the figure shows. It also affects the size you pick: your risk per trade in C$ includes the currency move, a point that part 3 builds on, starting with Risk first<!-- link: ../03-risk-and-position-sizing/01-risk-first.md -->.

<div class="canada" markdown>

### For Canadians

The CRA measures your gain in Canadian dollars. T4037 says to convert the proceeds at the exchange rate in effect when you sell and the cost at the rate in effect when you bought ([CRA T4037 capital gains guide](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html), as of 2026). So a stock that is flat in US dollars can still produce a gain or a loss on your tax return, and the currency part is inside that number. Lesson 8 shows the calculation.

</div>

## Common mistakes

- Adding the stock return and the currency return. They multiply, so use the formula.
- Thinking a USD account means no currency risk. It changes the day you convert, not the exposure.
- Ignoring the currency on a long hold. Over years it can be as large as the stock's move.

## Try it

1\. You buy US$8,000 of Stock A at 1.3600 and sell it for US$8,800 at 1.4000. What is your return in Canadian dollars?

<details class="solution" markdown>
<summary>Answer</summary>

Stock return = 8,800 / 8,000 - 1 = 10%. Rate change = 1.4000 / 1.3600 - 1 = 2.94% (rounded). Your return = 1.10 x 1.0294 - 1 = 13.2% (rounded). In dollars: cost 8,000 x 1.36 = C$10,880, proceeds 8,800 x 1.40 = C$12,320, gain C$1,440, which is 13.2% of C$10,880.

</details>

2\. Stock A is flat in US dollars, and the US dollar falls from 1.4000 to 1.3000 in C$. What is your return in Canadian dollars?

<details class="solution" markdown>
<summary>Answer</summary>

Rate change = 1.3000 / 1.4000 - 1 = -7.1% (rounded). The stock return is 0%, so your return is -7.1%.

</details>

3\. A US$20,000 position and the rate moves from 1.4000 to 1.4100. By how many Canadian dollars does the position's value change?

<details class="solution" markdown>
<summary>Answer</summary>

20,000 x 1.4100 - 20,000 x 1.4000 = 28,200 - 28,000 = C$200.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a US position you hold (or a made-up one). Write its cost in US$, the rate when you bought and the rate today. |
| 3 | Compute the stock return, the rate change and your return in C$. |
| 3 | Write the one number that would tell you the currency effect on a US$10,000 position for a 1 cent move in the rate. |

</div>

## Key terms

- **Currency risk**: the chance that an exchange-rate move changes the value of a foreign holding in your home currency.
- **Hedge**: a position that offsets a risk.
- **Hedged fund**: a fund that offsets the exchange-rate move on its foreign holdings.
- **Exchange-rate return**: the percentage change in the exchange rate over the holding period.

Next: [US withholding tax and the W-8BEN](06-us-withholding-tax-and-w-8ben.md)
