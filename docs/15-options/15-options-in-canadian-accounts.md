# Options in Canadian accounts

<span class="tag tag-canada">Canada</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">OPT</span>

After this lesson you can say which option strategies a Canadian broker is likely to allow in a TFSA, an RRSP and a margin account, what to confirm before you apply, how the CRA looks at option premiums, and how to run your first block of paper option trades.

Before this: [Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md), [Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md), [Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md). You need: your broker's options page open.

## The idea

The strategies in lessons 9 to 13 assume your account lets you place the trade. In Canada the account type, the broker's approval level and the tax rules each decide that. This lesson lists what we could confirm as of 2026 and marks what we could not.

## What the accounts allow

A broker sets **options approval levels**: you apply, and it grants the highest level you qualify for. Each level opens more strategies, and the levels are the broker's own. Read your broker's risk disclosure and options agreement too.

Wealthsimple's page on Canadian-listed options says they start with single-leg strategies up to its Level 2: long calls, long puts, covered calls and cash-secured puts. It says you can trade Canadian options in a TFSA and an RRSP, with no commission and a regulatory fee of C$0.04 per contract ([Wealthsimple CAD options](https://www.wealthsimple.com/en-ca/learn/cad-options-trading), as of 2026). Its fee schedule lists US-listed equity options at a US$0 contract fee, with possible pass-through fees ([Wealthsimple fees](https://www.wealthsimple.com/legal/fees/trade), as of 2026).

For US options, its pages disagree. The [options page](https://www.wealthsimple.com/en-ca/trade/options) lists covered calls, credit spreads, long calls and long puts for registered accounts and says all other strategies need a margin account. It does not list secured puts for registered accounts. Its help centre says spreads need a margin account with US dollar accounts enabled and are not available in registered accounts ([spreads](https://help.wealthsimple.com/hc/en-ca/articles/43913330243227-Trade-multi-leg-options-spreads), as of 2026). The help pages on spreads and on uncovered short options blocked automated fetching, so we know them from a search summary.

| Strategy (lesson) | TFSA or RRSP | Non-registered margin |
|---|---|---|
| Long call or put (1, 2) | Allowed at Wealthsimple | Allowed |
| Covered call (9) | Allowed at Wealthsimple | Allowed |
| Cash-secured put (9) | Allowed for Canadian options per one page; not listed for US options: ask | Allowed |
| Vertical spread, condor, butterfly, calendar (10 to 13) | Wealthsimple's pages disagree: ask | Allowed with approval and USD enabled |
| Uncovered short option | Not allowed | Highest level only |

IBKR Canada's pages blocked automated fetching, so this book does not state its options permissions for registered accounts. Part 2 notes that IBKR Canada allows margin only in non-registered individual accounts. Ask support in writing which strategies your TFSA and RRSP can use.

## The CRA side

One question is whether the plan may hold the option. The CRA's [Income Tax Folio S3-F10-C1](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-3-property-investments-savings-plans/series-3-property-investments-savings-plan-folio-10-registered-plans-individuals/income-tax-folio-s3-f10-c1-qualified-investments-rrsps-resps-rrifs-rdsps-tfsas.html) says in paragraph 1.16 that listed options generally qualify, except derivatives where the holder's loss can exceed the cost. Paragraph 1.40 says writing an option is generally not subject to the qualified investment rules, though other tax rules may limit it.

The other is whether the activity is a business. In paragraph 1.41 the CRA's view is that writing a covered call does not, by itself, mean the plan carries on a business. Writing an uncovered call, or a put, alone or combined with other positions, may. That wording includes puts that are cash-secured, so a cash-secured put or a spread in a registered plan is a question for your broker and a tax professional (as of 2026). A plan that carries on a business is generally taxable on that income (paragraph 1.41). Part 2 covers the test ([Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md)).

## The tax on option premiums

In a non-registered account, the CRA's old bulletin on securities transactions, IT-479R, is the one that speaks to options. It is archived: the CRA's page says it will not be updated and may be used for reference ([IT-479R, archived](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/it479r/archived-transactions-securities.html), dated 1984). Its paragraphs 23 to 32 say, in outline:

- Capital or income account depends on the facts. The CRA presumes a holder's result follows the holder's share trades, and a covered writer's follows the underlying shares (paragraph 25).
- A naked writer's result is normally income, though consistent capital treatment is accepted.
- On capital account, a writer's premium is generally a gain, less costs. On income account, it is income when the option is exercised, expires or is closed.
- When a written put is assigned, the premium reduces the cost of the shares bought (on capital account, only if your share gains are also on capital account).

Treat this as a map: the page is archived and a current ruling may differ. Keep records as in part 2 ([Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md)), and ask a tax professional about a specific trade.

## Paper block 5

The book sets six paper blocks ([paper trading](../practice/paper-trading.md)). Block 5 is 10 defined-risk option trades, to size by maximum loss and follow each trade to exit or expiry.

- Use only defined-risk strategies: long options and spreads (lessons 10 to 13), and covered calls or cash-secured puts if your account holds them.
- Size by the maximum loss plus fees, with 1R from your plan. If one contract does not fit, record that and pick a cheaper trade.
- Buy at the ask and sell at the bid. Subtract your real broker's fees for every leg, opening and closing.
- Write the exit, the day you will close before expiry, and the assignment risk in the journal before you enter.
- Follow every trade to its exit or expiry, even a loser, and record the R.

## Try it

1\. Your TFSA is at Wealthsimple and you want a bull call spread. According to its help centre, can you place it there?

<details class="solution" markdown>
<summary>Answer</summary>

No, per the help centre: spreads need a margin account with US dollar accounts enabled, and are not available in registered accounts (as of 2026). Its marketing page lists credit spreads for registered accounts, so ask support.

</details>

2\. Name two reasons a covered call in an RRSP is a different question from an uncovered call.

<details class="solution" markdown>
<summary>Answer</summary>

The covered call is backed by shares in the plan, and folio paragraph 1.41 says writing one does not by itself mean a business. Writing an uncovered call may lead the CRA to treat the plan as carrying on a business, and Wealthsimple does not allow it in registered accounts.

</details>

3\. Under IT-479R, what does the CRA presume about a covered writer's gain or loss?

<details class="solution" markdown>
<summary>Answer</summary>

That it follows the treatment of the underlying shares (paragraph 25). The bulletin is archived, so confirm the current position with a professional.

</details>

## Part check

1\. One call has a premium of 3.25. What does one contract cost?

<details class="solution" markdown>
<summary>Answer</summary>

3.25 x 100 = US$325.

</details>

2\. A call with strike 50, three months left, 4% rates and a stock price of 50 is worth 3.2297. Use put-call parity (\(C - P = S - Ke^{-rT}\)) to find the put.

<details class="solution" markdown>
<summary>Answer</summary>

\(Ke^{-rT} = 50 \times e^{-0.01} = 49.5025\). \(C - P = 50 - 49.5025 = 0.4975\). \(P = 3.2297 - 0.4975 = 2.7322\).

</details>

3\. The 50-strike call on the chain has a delta of 0.57. Stock A rises US$1. What is the first estimate of the change in one contract?

<details class="solution" markdown>
<summary>Answer</summary>

About 0.57 x 100 = US$57. Gamma makes the real gain a little larger.

</details>

4\. A US$80 stock has an IV of 30% and three months left. What is the one-standard-deviation expected move?

<details class="solution" markdown>
<summary>Answer</summary>

80 x 0.30 x \(\sqrt{0.25}\) = 80 x 0.30 x 0.5 = US$12.

</details>

5\. Sell the 50 put at 2.65 and buy the 47.50 put at 1.90. What are the credit, maximum loss and breakeven?

<details class="solution" markdown>
<summary>Answer</summary>

Credit = 2.65 - 1.90 = 0.75, so US$75. Maximum loss = (2.50 - 0.75) x 100 = US$175. Breakeven = 50 - 0.75 = 49.25.

</details>

6\. A long straddle costs US$622.60 with fees. Your account is US$25,000 and 1R is 1%. How many contracts, and why?

<details class="solution" markdown>
<summary>Answer</summary>

1R is US$250. The straddle is 622.60 / 250 = 2.49R, so zero contracts: one contract risks more than the limit.

</details>

7\. Which accounts at Wealthsimple can hold a bull call spread, according to its help centre?

<details class="solution" markdown>
<summary>Answer</summary>

A margin account with US dollar accounts enabled. Registered accounts such as a TFSA or RRSP cannot (as of 2026, from the help centre page).

</details>

8\. You are short a covered call that is in the money with 0.05 of time value, and the stock goes ex-dividend tomorrow with a 0.50 dividend. Is assignment likely?

<details class="solution" markdown>
<summary>Answer</summary>

Yes. The dividend 0.50 is larger than the time value 0.05 plus the small interest cost, so the holder gains by exercising before the ex-date, and you would lose the shares and the dividend.

</details>

<div class="practice" markdown>

## Practice today (10 min)

This sets paper block 5 of [paper trading](../practice/paper-trading.md): 10 defined-risk option trades, to size by maximum loss and follow each trade to exit or expiry.

| Minutes | Task |
|---|---|
| 3 | Write into your plan the strategies your account can hold, the approval level you have, and your 1R in dollars. |
| 4 | Place the first paper trade: pick the strategy, buy at the ask and sell at the bid, and size by maximum loss plus fees. |
| 3 | Journal it in both stages ([trade journal](../practice/trade-journal.md)). Repeat daily until 10 trades are done. |

</div>

## Key terms

- **Options approval level**: the set of strategies a broker lets you trade, granted after an application.
- **Qualified investment**: an investment a registered plan such as a TFSA or RRSP may hold under the Income Tax Act.
- **Uncovered option**: a short option with no shares, cash or long option behind it.

Next: [Realized and implied volatility](../16-volatility-and-event-trading/01-realized-vs-implied-volatility.md)
