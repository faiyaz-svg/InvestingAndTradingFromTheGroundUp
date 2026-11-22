# Margin, leverage and mark to market

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">FUT</span>

After this lesson you can work out a position's notional value and leverage, follow an account through daily mark to market, and say when a margin call happens and how large it is.

Before this: [What futures are](01-what-futures-are.md), [Settlement, cash accounts and margin](../01-how-markets-work/07-settlement-cash-and-margin.md). You need: a calculator.

## The idea

You are long 2 micro contracts on the made-up Index X, bought at 6,000.00. The multiplier is US$5 per point. The **notional value** of the position is the full value of the exposure:

\[ N = P \times M \times n \]

- \(P\) is the futures price, in index points.
- \(M\) is the multiplier, in US$ per point.
- \(n\) is the number of contracts.

Here N = 6,000 x 5 x 2 = US$60,000. You do not pay that. You post **margin**, a deposit that shows you can cover losses. In futures, margin is not a loan. You borrow nothing and pay no interest on it. The stock-account margin of [lesson 7 of Part 1](../01-how-markets-work/07-settlement-cash-and-margin.md) is a loan against shares, and the two share only a name. The futures deposit is sometimes called a performance bond or good-faith deposit.

Two levels matter, and both are set per contract.

- **Initial margin** is the deposit needed to open a position.
- **Maintenance margin** is the lowest account equity you may hold while the position is open. It is lower than initial margin.

The exchange's clearinghouse sets a minimum for each product (CME Group publishes its margins on its website and changes them with volatility). Your broker may ask for more, and can change its requirement at any time. This lesson uses made-up round numbers: US$2,400 initial and US$2,200 maintenance per contract. For 2 contracts that is US$4,800 initial and US$4,400 maintenance. Look up the current numbers for any real contract before you trade it.

**Leverage** here is notional value divided by the margin posted: 60,000 / 4,800 = 12.5. A 1% move in the index (60 points) moves the position by US$600, which is 12.5% of the US$4,800 margin.

## Mark to market

Futures accounts settle every day. At the end of each session the exchange sets a **settlement price** for each contract. Every position is then **marked to market**: the gain or loss since the last settlement is moved in cash from the losing accounts to the winning ones. The cash moved is called **variation margin**.

\[ E_t = E_{t-1} + (S_t - S_{t-1}) \times M \times n \quad \text{for a long position} \]

- \(E_t\) is account equity at the end of day \(t\), in US$.
- \(S_t\) is the settlement price on day \(t\), in index points.
- \(M\) and \(n\) are the multiplier and the number of contracts, as before.

If equity falls below maintenance margin, the broker issues a **margin call**: you must deposit enough to restore equity to the initial margin level (brokers differ on the exact rule and the deadline, and may liquidate your position without waiting). The figure follows the example below.

<div class="example" markdown>

### Worked example: three days, one margin call

You deposit US$5,500 and buy 2 contracts at 6,000.00, which is also the day 0 settlement price. Settlement prices: day 1, 5,980.00; day 2, 5,880.00; day 3, 5,920.00. One point is worth 5 x 2 = US$10.

1. Day 1: (5,980 - 6,000) x 10 = -US$200. Equity = 5,500 - 200 = US$5,300. It is above the US$4,400 maintenance level.
2. Day 2: (5,880 - 5,980) x 10 = -US$1,000. Equity = 5,300 - 1,000 = US$4,300. This is below US$4,400, so there is a margin call.
3. The call restores equity to US$4,800: 4,800 - 4,300 = US$500 to deposit. Equity is now US$4,800.
4. Day 3: (5,920 - 5,880) x 10 = +US$400. Equity = 4,800 + 400 = US$5,200.

Check: the position is down (5,920 - 6,000) x 10 = -US$800 in total, and 5,500 + 500 - 800 = US$5,200.

</div>

Look at the line crossing the red maintenance line on day 2 and the jump after the deposit.

![Account equity over three days against initial and maintenance margin, with a margin call on day 2](../assets/figures/14-futures/margin-path-dark.svg#only-dark)
![Account equity over three days against initial and maintenance margin, with a margin call on day 2](../assets/figures/14-futures/margin-path-light.svg#only-light)

<div class="warning" markdown>

Futures losses can exceed the margin you posted. Suppose that after the day 2 close, with equity at US$4,300, the index gaps from 5,880 to 5,400 before you can act. The loss on 2 contracts is (5,880 - 5,400) x 10 = US$4,800, so equity becomes 4,300 - 4,800 = -US$500, a debt you owe the broker. Margin limits what the broker asks for, not what the market can take. Size by the loss at your stop, as in [position sizing](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md), not by the margin requirement.

</div>

Leverage also makes a stop matter more. A stop order can fill past its price in a fast market ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

<div class="canada" markdown>

### For Canadians

CME contracts are priced and margined in US dollars. In a Canadian-dollar account, the broker converts, and a US dollar loss after a currency move can cost more Canadian dollars than you expected ([Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)). Wealthsimple's futures page says positions use margin that is returned when the position closes, and that you may get a margin call or have assets liquidated if your balance falls below maintenance ([Wealthsimple futures](https://www.wealthsimple.com/en-ca/trade/futures), as of 2026). Margin rules for stocks are in [Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md).

</div>

## Common mistakes

- Treating margin as the amount at risk. The loss is set by the price move, and it can be larger than the margin.
- Sizing by how many contracts the margin allows. Size by the stop distance.
- Leaving only the initial margin in the account. A small adverse move then triggers a call.

## Try it

1\. One contract has a notional value of US$30,000 and the margin posted is US$2,400. What is the leverage?

<details class="solution" markdown>
<summary>Answer</summary>

30,000 / 2,400 = 12.5.

</details>

2\. You are long 3 contracts (US$5 per point) at 6,000.00 with US$8,000 in the account. The day 1 settlement is 5,950.00. What is the equity?

<details class="solution" markdown>
<summary>Answer</summary>

(5,950 - 6,000) x 5 x 3 = -US$750. Equity = 8,000 - 750 = US$7,250.

</details>

3\. With the made-up margins (US$2,400 initial, US$2,200 maintenance per contract) and 3 contracts, at what equity does a margin call happen, and what is the deposit if equity is US$6,300?

<details class="solution" markdown>
<summary>Answer</summary>

Maintenance = 3 x 2,200 = US$6,600, so a call happens below that. Equity of US$6,300 is below it. Initial = 3 x 2,400 = US$7,200, so the deposit is 7,200 - 6,300 = US$900.

</details>

4\. You are short 2 contracts (US$5 per point) at 6,000.00. The next settlement is 6,030.00. What is the mark to market?

<details class="solution" markdown>
<summary>Answer</summary>

A short loses when the price rises: (6,000 - 6,030) x 5 x 2 = -US$300.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Find the current exchange margin for one micro contract on CME Group's site, and your broker's requirement if it is shown. Write both and the notional value, then the leverage. |
| 5 | Repeat the three-day example with your own settlement prices and find whether a call happens. |

</div>

## Key terms

- **Notional value**: price times multiplier times contracts, the full value of the exposure.
- **Margin (futures)**: a good-faith deposit that covers losses, not a loan.
- **Initial margin**: the deposit needed to open a position.
- **Maintenance margin**: the minimum equity to keep a position open.
- **Leverage**: notional value divided by the margin posted.
- **Settlement price**: the exchange's end-of-day price used to mark positions.
- **Mark to market**: the daily move of gains and losses into or out of the account.
- **Variation margin**: the cash moved each day by mark to market.
- **Margin call**: a demand to restore equity after it falls below maintenance.

Next: [Index futures: ES, MES, NQ and MNQ](03-index-futures.md)
