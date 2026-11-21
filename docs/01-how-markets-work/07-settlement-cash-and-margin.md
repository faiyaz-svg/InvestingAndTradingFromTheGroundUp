# Settlement, cash accounts and margin

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MKT</span>

After this lesson you can find a trade's settlement date, say what a cash account lets you do, and work out how margin changes your gains, your losses and the price at which you get a margin call.

Before this: [Who is on the other side of your trade](06-who-is-on-the-other-side.md). You need: a calculator.

## The idea

When your order fills, the trade is agreed, but the shares and the cash have not yet changed hands. **Settlement** is the step where the buyer's cash is delivered to the seller and the shares are delivered to the buyer. The time between the trade and settlement is the **settlement cycle**.

The US moved to a one-business-day cycle, written **T+1**, on May 28, 2024, and Canada moved to T+1 on May 27, 2024 ([CIRO notice on the move to T+1](https://www.ciro.ca/news-room/publications/amendments-umir-and-idpc-rules-facilitate-investment-industrys-move-t1-settlement)). \(T\) is the trade date. A trade on Thursday settles on Friday. A trade on Friday settles on the next Monday, because settlement counts business days only.

The figure shows both cases.

![A calendar strip showing a Thursday trade settling Friday and a Friday trade settling the next Monday](../assets/figures/01-how-markets-work/settlement-t1-dark.svg#only-dark)
![A calendar strip showing a Thursday trade settling Friday and a Friday trade settling the next Monday](../assets/figures/01-how-markets-work/settlement-t1-light.svg#only-light)

You do not wait for settlement to sell. You own the shares from the trade date for practical purposes, and you can sell them the same day. Settlement matters for three things: when withdrawn cash is really yours, when you can use proceeds in some account types, and which day counts for dividends (lesson 9, [Dividends, splits and corporate actions](09-dividends-splits-and-corporate-actions.md)).

## Cash accounts and margin accounts

A **cash account** lets you buy only with cash you already have. You cannot borrow, and the rules around using sale proceeds before they settle vary by broker, so check how yours treats unsettled funds. A **margin account** lets you borrow from the broker against the stocks you hold. **Margin** is that borrowed money, and the stocks in the account are the **collateral**, the assets that secure the loan.

Borrowing gives you **leverage**: a position larger than your own cash. In the US, Regulation T lets a broker lend up to 50% of the purchase price of a stock on new purchases ([FINRA on margin accounts](https://www.finra.org/rules-guidance/key-topics/margin-accounts)). That 50% is the **initial margin**. Afterwards the broker needs your equity to stay above a **maintenance margin**, a minimum share of the position's value that you own outright. FINRA Rule 4210 sets a floor, and brokers often set a higher house rate. If your equity falls below it you get a **margin call**: you must add cash or securities, or sell, and the broker can sell your positions without asking if you do not.

\[ \text{Equity ratio} = \frac{V - L}{V} \]

- \(V\) is the market value of the position, in US$.
- \(L\) is the loan from the broker, in US$.
- \(V - L\) is your equity, and the ratio is a fraction of the position's value.

The broker charges **margin interest** on the loan, which accrues daily; at IBKR it is posted monthly ([IBKR margin rates](https://www.interactivebrokers.ca/en/trading/margin-rates.php), as of 2026).

<div class="example" markdown>

### Worked example: margin on 400 shares

You have US$10,000 in cash and buy 400 shares of Stock A at US$50.00, a US$20,000 position. You borrow US$10,000, which is 50% of the purchase price. Assume a house maintenance requirement of 30% (made up for this example) and a margin rate of 6% a year (also made up).

1. Equity ratio at purchase: (20,000 - 10,000) / 20,000 = 50%.
2. The price falls 20% to US$40.00. Position = 400 x 40 = US$16,000. Equity = 16,000 - 10,000 = US$6,000.
3. Your account fell 6,000 / 10,000 - 1 = -40%, double the stock's fall.
4. Equity ratio = 6,000 / 16,000 = 37.5%, still above 30%.
5. The margin call price \(P\) solves (400P - 10,000) / (400P) = 0.30, so 400P - 10,000 = 120P, 280P = 10,000, P = US$35.71 (rounded). That is a 28.6% fall from US$50. The position is then worth 400 x 35.7143 = US$14,285.71 and your equity is US$4,285.71, a loss of 57.1% of your cash.
6. Interest for 30 days: 10,000 x 0.06 x 30 / 365 = US$49.32.

A 20% fall in the stock became a 40% fall in your account. The same leverage doubles gains too.

</div>

## Day-trading rules

For years, FINRA's pattern day trader rule required US$25,000 in equity for a margin account that made four or more day trades in five business days. FINRA's Regulatory Notice 26-10 replaced it with intraday margin standards effective June 4, 2026, which remove the day-trade count and the US$25,000 minimum; firms may phase the change in until October 20, 2027 ([FINRA Regulatory Notice 26-10](https://www.finra.org/rules-guidance/notices/26-10)). Under the new standards a broker computes an intraday margin deficit, which must be met promptly, and repeated failures can bring a 90-day restriction. Which version your broker applies today depends on the broker, so read its day-trading page.

<div class="canada" markdown>

### For Canadians

Canadian brokers follow CIRO's margin rules, not Regulation T, and the rates and eligible securities are set by CIRO's lists with broker-specific limits on top. Part 2 covers them ([Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md)). IBKR Canada does not allow margin trading in registered accounts such as a TFSA or RRSP, so margin means a non-registered account ([IBKR Canada registered account information](https://www.interactivebrokers.ca/en/accounts/rsp_tfsa_information.php), as of 2026; check the page for the FHSA). Shorting (lesson 8) also needs a margin account.

</div>

## Common mistakes

- Sizing by buying power. Margin allows a larger position than your risk plan does, and a bigger position loses faster.
- Forgetting interest. It accrues each day you hold the loan, so holding a leveraged position for months costs real money.
- Assuming you get a warning before a forced sale. A broker may sell without calling first when equity is below the requirement.

## Try it

1\. A stock is bought on Friday, November 20, 2026. When does the trade settle under T+1?

<details class="solution" markdown>
<summary>Answer</summary>

Monday, November 23, 2026, the next business day after Friday.

</details>

2\. A stock is bought on Wednesday, November 25, 2026. NYSE is closed Thursday, November 26. When does it settle?

<details class="solution" markdown>
<summary>Answer</summary>

Friday, November 27, 2026. The first business day after the trade is Friday, because Thursday is a holiday.

</details>

3\. You have US$5,000, buy US$10,000 of Stock A using a 50% margin loan, and the price rises 10%. What is your return on the US$5,000?

<details class="solution" markdown>
<summary>Answer</summary>

The position is worth 10,000 x 1.10 = US$11,000, so the gain is US$1,000. Return = 1,000 / 5,000 = 20%, before interest.

</details>

4\. Same account. The price falls 25%. What is your equity and what share of your own money did you lose?

<details class="solution" markdown>
<summary>Answer</summary>

Position = 10,000 x 0.75 = US$7,500. Equity = 7,500 - 5,000 = US$2,500. You lost 2,500 of your 5,000, which is 50%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find your broker's page on settlement and unsettled funds. Write what you can do with sale proceeds before they settle. |
| 3 | In your account, find whether it is cash or margin and write the margin rate or the reason margin is off. |
| 3 | Pick any day in next month's NYSE calendar that sits next to a holiday and write the settlement date for a trade that day. |

</div>

## Key terms

- **Settlement**: the exchange of cash for shares after a trade.
- **T+1**: settlement one business day after the trade date.
- **Cash account**: an account that can buy only with the cash it holds.
- **Margin account**: an account that can borrow from the broker.
- **Margin**: money borrowed from the broker against your holdings.
- **Collateral**: the assets that secure a loan.
- **Leverage**: a position larger than your own cash.
- **Initial margin**: the share of a purchase you must fund yourself.
- **Maintenance margin**: the minimum equity you must keep as a share of the position's value.
- **Margin call**: a demand to add funds or sell when equity falls below maintenance.

Next: [Short selling](08-short-selling.md)
