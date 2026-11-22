# Futures in Canada

<span class="tag tag-canada">Canada</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">FUT</span>

After this lesson you can say where a Canadian can trade futures, cost a round trip in R, read the specs of the Montreal Exchange's S&P/TSX 60 futures, and name the tax question to settle before you trade.

Before this: [Futures hours and sessions](06-futures-hours-and-sessions.md), [Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md). You need: a calculator.

## The idea

You have worked with a made-up micro index future for six lessons. To trade a real one from Toronto, you need a broker that offers futures, a product you can size, and a view on how the gains are taxed. This lesson covers the first two as of 2026, and sets the last one up for a professional.

## Where to trade

**Wealthsimple.** Wealthsimple's futures page says it offers contracts on global indices and commodities in micro, mini and standard sizes, for US$1 per contract with no platform or market data fees, plus exchange and regulatory fees. Its example for the micro S&P 500 is US$0.35 exchange fee and US$0.02 regulatory fee. Hours run from Sunday 6 p.m. to Friday 5 p.m. ET, with a one-hour break ([Wealthsimple futures](https://www.wealthsimple.com/en-ca/trade/futures), as of 2026). Investment Executive reported on May 1, 2026 that futures were in beta and expected to be widely available that summer ([Investment Executive](https://www.investmentexecutive.com/news/product/wealthsimple-announces-futures-contract-launches-benefits-for-active-traders/)). Neither page lists the full set of contracts or says which accounts (TFSA, RRSP, FHSA or non-registered) can hold futures. Check Wealthsimple's help centre for both before you plan a trade.

**IBKR Canada.** This book does not state IBKR Canada's futures access, fees or margin, because they depend on your account. Look at IBKR's futures product page and your account's trading permissions, and check which exchanges (CME and the Montreal Exchange) your account can reach.

**Cost in R.** Using the Wealthsimple example for the micro S&P 500, one contract costs US$1.00 + US$0.35 + US$0.02 = US$1.37. Wealthsimple's page does not say whether the US$1 is charged per side or per round trip, so assume each side, which gives US$2.74 per contract for a round trip. For the 6-contract trade of lesson 3, with 1R = US$240.00, the fees are 6 x 2.74 = US$16.44, which is 16.44 / 240 = 0.07R. Check whether your broker charges per side or per round trip.

## The Montreal Exchange

The Montreal Exchange (M-X, part of TMX Group) lists Canada's index futures. The SXF is the standard S&P/TSX 60 index future: its value is the index level times C$200, and profit and loss is settled in cash every day through the Canadian Derivatives Clearing Corporation. It trades in March, June, September and December, and its outright tick is 0.10 index points, worth C$20 (0.10 x C$200). The final settlement day is the third Friday of the contract month ([Montreal Exchange, SXF](https://www.m-x.ca/en/markets/index-derivatives/sxf), as of 2026). The SXM is the mini version at C$50 per index point ([Montreal Exchange, SXM](https://www.m-x.ca/envoi/produit/sxm_retail_en.html), as of 2026). Margin and the SXM tick size are not covered here, so read the full specifications at [m-x.ca](https://www.m-x.ca) before you size a trade.

<div class="example" markdown>

### Worked example: the value of a point

An S&P/TSX 60 index future moves 5.0 points against you.

1. One SXF: 5.0 x C$200 = C$1,000.
2. One SXM: 5.0 x C$50 = C$250.
3. Two SXF: 2 x C$1,000 = C$2,000.

At an index level of 1,500 (made-up), one SXF has a notional value of 1,500 x 200 = C$300,000, so the contract is large for a small account, and the SXM is a quarter of that, C$75,000.

</div>

The same sizing steps apply: stop distance in points times the multiplier gives risk per contract in Canadian dollars, and you divide your risk amount by it and round down.

<div class="canada" markdown>

### For Canadians

CME contracts are in US dollars and the Montreal Exchange's are in Canadian dollars. Currency risk on a CME contract sits in the P&L and the margin (see [Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)).

Tax is the open question. Whether a futures gain is a capital gain or business income depends on the facts, mainly how often and how you trade. Part 2 explains the test ([Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md)). This book does not state a CRA rule for futures specifically, because the CRA's guidance is general. Ask a tax professional before your first trade, and keep records of every contract in Canadian dollars ([Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md)).

</div>

## Common mistakes

- Assuming your account type can hold futures. Confirm it in writing from the broker.
- Quoting a fee per contract when the broker charges per side. Double it in the cost in R until you know.
- Using a US multiplier for a Canadian contract. SXF is C$200, not US$.

## Try it

1\. One Montreal SXF contract and a 3.5-point move. What is the P&L in C$?

<details class="solution" markdown>
<summary>Answer</summary>

3.5 x C$200 = C$700 (a gain for a long position if the index rose).

</details>

2\. Fees are US$1.37 per contract per side. What is the round trip for 4 contracts, and what share of 1R = US$160?

<details class="solution" markdown>
<summary>Answer</summary>

4 x 1.37 x 2 = US$10.96. 10.96 / 160 = 0.0685, so 0.07R.

</details>

3\. A micro trade risks US$240 and fees are 0.07R. The target is 2R. What is the reward after fees?

<details class="solution" markdown>
<summary>Answer</summary>

2.00R - 0.07R = 1.93R, about US$463.20 (1.93 x 240).

</details>

## Part check

1\. You are long 4 contracts of a micro future (US$5 per point) at 5,990.00 and sell at 6,012.50. What is the P&L?

<details class="solution" markdown>
<summary>Answer</summary>

(6,012.50 - 5,990.00) x 5 x 4 = 22.50 x 20 = US$450.00.

</details>

2\. Three micro contracts at 6,000.00 (US$5 per point) with US$7,200 of margin. What are the notional and the leverage?

<details class="solution" markdown>
<summary>Answer</summary>

Notional = 6,000 x 5 x 3 = US$90,000. Leverage = 90,000 / 7,200 = 12.5.

</details>

3\. Account US$40,000, risk 0.5%, MES entry 6,100.00, stop 6,090.00. How many contracts?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = US$200.00. 10.00 points = 40 ticks x US$1.25 = US$50.00 per contract. 200 / 50 = 4 contracts.

</details>

4\. You are short 2 micro contracts at 6,000.00. Settlements: 5,990.00, then 6,015.00. What is the account change over the two days?

<details class="solution" markdown>
<summary>Answer</summary>

Day 1: (6,000 - 5,990) x 10 = +US$100. Day 2: (5,990 - 6,015) x 10 = -US$250. Total = -US$150.

</details>

5\. You roll from September at 6,010.00 to December at 6,050.51. Your September stop is 5,985.00. What is the December stop?

<details class="solution" markdown>
<summary>Answer</summary>

5,985.00 + 40.51 = 6,025.51.

</details>

6\. \(S\) = 6,000, \(r\) = 3.5%, \(d\) = 1.5%, \(T\) = 0.5. What is fair value, and is the market in contango or backwardation?

<details class="solution" markdown>
<summary>Answer</summary>

F = 6,000 x (1 + 0.02 x 0.5) = 6,060.00. The future is above spot, so contango.

</details>

7\. Can futures losses exceed the margin you post?

<details class="solution" markdown>
<summary>Answer</summary>

Yes. Margin is a deposit, not a limit on loss. A fast move or a gap can take equity below zero, and you owe the difference.

</details>

<div class="practice" markdown>

## Practice today (10 min)

This sets paper block 4 of [paper trading](../practice/paper-trading.md): 10 micro futures trades, to check tick value, margin and sizing before real contracts.

| Minutes | Task |
|---|---|
| 3 | Write the contract, tick value, margin and fees for your paper account in your plan. |
| 4 | Place the first paper trade with the sizing steps of lesson 3 and the realism rules on that page. |
| 3 | Journal it in both stages ([trade journal](../practice/trade-journal.md)). Repeat daily until 10 trades are done. |

</div>

## Key terms

- **Montreal Exchange**: the Canadian derivatives exchange, part of TMX Group.
- **SXF**: the standard S&P/TSX 60 index future, worth C$200 per index point.
- **SXM**: the mini S&P/TSX 60 index future, worth C$50 per index point.
- **Canadian Derivatives Clearing Corporation**: the clearinghouse for Montreal Exchange contracts.

Next: Calls and puts<!-- link: ../15-options/01-calls-and-puts.md -->
