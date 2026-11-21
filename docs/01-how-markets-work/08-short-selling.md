# Short selling

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">MKT</span>

After this lesson you can work out the profit or loss on a short sale including its costs, say why the loss on a short has no upper limit, and explain a short squeeze.

Before this: [Settlement, cash accounts and margin](07-settlement-cash-and-margin.md). You need: a calculator.

## The idea

Buying a stock profits when the price rises. **Short selling** profits when the price falls. You sell shares you do not own, then buy them back later and return them. If you sell at US$50 and buy back at US$45, you keep US$5 a share.

The shares have to come from somewhere. Your broker **borrows** them from another client's account, or from a lender, and delivers them to the buyer. This is why shorting needs a margin account (lesson 7): the broker holds your collateral against the borrowed shares. Closing the position by buying the shares back is called **covering**.

The steps:

1. **Locate.** Before a short sale, the broker must have reasonable grounds to believe the shares can be borrowed, and must document that first. This is the locate rule in the SEC's Regulation SHO ([SEC on Regulation SHO](https://www.sec.gov/investor/pubs/regsho.htm)). If your broker cannot find shares to borrow, you cannot short that stock.
2. **Sell short.** The shares are sold at the market. The proceeds sit in your account as collateral and you owe the lender the shares.
3. **Cover.** Later you buy the same number of shares and return them. Your profit or loss is the sale price minus the buyback price, times the shares, less costs.

## How it works

For a short position:

\[ \text{Profit} = (P_0 - P_1) \times N - C \]

- \(P_0\) is the price you sold at, in US$.
- \(P_1\) is the price you covered at, in US$.
- \(N\) is the number of shares.
- \(C\) is the costs, in US$: borrow fee, dividends owed and commissions.

A short pays costs that a long does not:

- **Borrow fee.** The lender charges a yearly rate on the value of the shares, which the broker passes on. It varies with the stock: easy-to-borrow stocks cost little, and a stock many people want to short can cost far more. Check your broker's rate for the stock before shorting.
- **Dividends.** If the stock pays a dividend while you are short, you owe that amount to the lender (lesson 9 explains dividends).
- **Margin interest** on any borrowed cash, as in lesson 7.

<div class="example" markdown>

### Worked example: a short for 30 days

You short 100 shares of Stock A at US$50.00 (made-up) and hold for 30 days. The borrow fee is 3% a year (made-up). Stock A pays a US$0.50 dividend during the hold.

1. Proceeds: 100 x 50.00 = US$5,000.00.
2. Borrow fee: 5,000 x 0.03 x 30 / 365 = US$12.33.
3. Dividend owed: 100 x 0.50 = US$50.00. Costs C = 12.33 + 50.00 = US$62.33.
4. Cover at US$45.00: profit = (50.00 - 45.00) x 100 - 62.33 = 500 - 62.33 = US$437.67.
5. Cover at US$60.00 instead: loss = (50.00 - 60.00) x 100 - 62.33 = -1,000 - 62.33 = -US$1,062.33.

Prices of 45 and 60 are 10% down and 20% up, and the loss is more than twice the gain.

</div>

## Why the risk is different

A long position can lose at most what you paid, because a stock cannot go below zero. A short position can lose more than you put in, because a price has no ceiling. The figure shows 100 shares bought at US$50 and 100 shares sold short at US$50.

![Profit and loss of 100 shares bought and 100 shares sold short at US$50: the long loss is limited to US$5,000 and the short loss has no limit](../assets/figures/01-how-markets-work/short-vs-long-dark.svg#only-dark)
![Profit and loss of 100 shares bought and 100 shares sold short at US$50: the long loss is limited to US$5,000 and the short loss has no limit](../assets/figures/01-how-markets-work/short-vs-long-light.svg#only-light)

The short's best case is US$5,000 (the price goes to zero), but its loss line keeps going.

A **short squeeze** happens when a rising price forces shorts to cover. Covering is a purchase, and many purchases at once push the price up further, which forces more covering. **Short interest** is the number of shares sold short; dividing it by the stock's average daily volume gives **days to cover**, a rough measure of how long it would take shorts to exit. Part 19 covers the data (Short interest and borrow<!-- link: ../19-data-flows-and-forecasting/04-short-interest-and-borrow.md -->).

### Rules that limit shorting

Under SEC Rule 201 (the alternative uptick rule), a stock that falls 10% in one day is subject to a short-sale price test for the rest of that day and the next day ([SEC on Regulation SHO](https://www.sec.gov/investor/pubs/regsho.htm)). The test stops short sales from pushing a price that is already falling.

<div class="canada" markdown>

### For Canadians

Short selling is not allowed in registered accounts (TFSA, RRSP, RESP, RRIF); it needs a non-registered margin account. Wealthsimple states this on its [short selling page](https://www.wealthsimple.com/en-ca/learn/what-is-short-selling), and so does [National Bank Direct Brokerage](https://nbdb.ca/learning-centre/investment-strategies/growing-portfolio/how-to-short-sell-shares.html), as of 2026. Whether your broker offers short-sale order entry, and at what borrow fees, changes over time, so check its own pages before you plan a short.

</div>

## Common mistakes

- Sizing a short like a long. A 50% rise costs 50% of the proceeds, and a short has no cap, so size it by the stop you can honour.
- Ignoring the borrow fee. On a hard-to-borrow stock the fee can exceed the move you expect.
- Shorting into a crowded trade. A high days to cover means a rise can force the exit of many shorts at once.

## Try it

1\. You short 200 shares of Stock B at US$30.00 and cover at US$27.50. There are no costs. What is the profit?

<details class="solution" markdown>
<summary>Answer</summary>

(30.00 - 27.50) x 200 = US$500.00.

</details>

2\. You short 100 shares of Stock A at US$50.00 and the price rises 50%. What is the loss, and what percentage of the sale proceeds is it?

<details class="solution" markdown>
<summary>Answer</summary>

New price = 75.00. Loss = (50.00 - 75.00) x 100 = -US$2,500.00, which is 50% of the US$5,000 proceeds.

</details>

3\. Stock A has 2,000,000 shares sold short and trades 500,000 shares a day on average. What are the days to cover?

<details class="solution" markdown>
<summary>Answer</summary>

2,000,000 / 500,000 = 4 days.

</details>

4\. You short 100 shares at US$50.00 for 60 days, with a 4% yearly borrow fee, and cover at US$48.00. There is no dividend. What is the profit after the borrow fee?

<details class="solution" markdown>
<summary>Answer</summary>

Gross profit = (50.00 - 48.00) x 100 = US$200.00. Fee = 5,000 x 0.04 x 60 / 365 = US$32.88. Profit = 200 - 32.88 = US$167.12.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | On your broker or on its help pages, find whether it lets you short, and in which account types. Write the answer and the page. |
| 5 | Pick a past gap down on any chart ([chart drills](../practice/chart-drills.md)) and write what a short from the prior close would have made, before costs. |

</div>

## Key terms

- **Short selling**: selling borrowed shares to profit if the price falls.
- **Borrow**: shares lent to the short seller by a lender through the broker.
- **Locate**: the broker's check that shares can be borrowed before a short sale.
- **Covering**: buying shares back to close a short.
- **Borrow fee**: the yearly rate the lender charges for the borrowed shares.
- **Short squeeze**: a rise that forces shorts to cover, pushing the price higher.
- **Short interest**: the number of shares currently sold short.
- **Days to cover**: short interest divided by average daily volume.

Next: [Dividends, splits and corporate actions](09-dividends-splits-and-corporate-actions.md)
