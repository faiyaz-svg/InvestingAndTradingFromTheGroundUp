# Crypto market structure: perps, funding and liquidations

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can work out a perpetual future's funding payment, find the liquidation price of a leveraged position, and explain how forced selling can feed on itself.

Before this: [Margin, leverage and mark to market](../14-futures/02-margin-leverage-and-mark-to-market.md), [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md). You need: a calculator.

## The idea

Coin A has no closing bell. The stock market in part 1 has a regular session, a close and an overnight gap. A crypto market trades every hour of every day, on dozens of platforms at once. The same coin has a slightly different price on each, and traders called arbitrageurs buy where it is cheap and sell where it is dear, which keeps the prices close but not equal. There is no single official price, so charts and data vendors build an index from several venues.

The most traded product is not the coin. It is the **perpetual future** (perp): a futures contract with no expiry date. Part 14 explained that a regular future converges to spot at expiry. A perp never expires, so something else must keep its price near spot. That something is the **funding rate**, a payment that passes between longs and shorts at set times.

## How it works

### Funding

At each funding time (every 8 hours on many exchanges, hourly on some), one side pays the other. When the perp trades above the spot index, the funding rate is positive and longs pay shorts. That makes holding the perp costly for longs and attractive for shorts, which pushes the price back down. When the perp trades below spot, the rate is negative and shorts pay longs.

\[ \text{payment} = N \times r \]

- \(N\) is the position's notional value, in US$: units held times the mark price.
- \(r\) is the funding rate for that interval, as a fraction (0.01% is 0.0001).
- A positive payment is paid by longs and received by shorts. Exchanges publish their own formula and interval. This lesson's rates are made up.

<div class="example" markdown>

### Worked example: a day of funding

You are long 1,000 units of the Coin A perp with a mark price of US$22.00, so \(N\) = 1,000 x 22.00 = US$22,000. Three funding times occur in the day, at rates of 0.01%, 0.03% and 0.10%.

1. First payment: 22,000 x 0.0001 = US$2.20.
2. Second payment: 22,000 x 0.0003 = US$6.60.
3. Third payment: 22,000 x 0.0010 = US$22.00.
4. The day's total: US$30.80, paid by you to the shorts.
5. Yearly cost at the first rate alone: 0.0001 x 3 x 365 = 10.95% of notional. At the third rate: 0.0010 x 3 x 365 = 109.5%.

A funding rate that looks small per interval adds up. A high positive rate also tells you that many traders are long and paying to stay there.

</div>

The figure shows the three payments. Look at how the third interval dominates the day.

![Three funding payments paid by a long position in one day: US$2.20, US$6.60 and US$22.00](../assets/figures/18-crypto/funding-dark.svg#only-dark)
![Three funding payments paid by a long position in one day: US$2.20, US$6.60 and US$22.00](../assets/figures/18-crypto/funding-light.svg#only-light)

### Leverage and liquidation

Perps let you hold a position larger than your cash. The deposit you put up is **collateral**, and **leverage** is the notional value divided by the collateral, as in part 14. If losses cut your equity down to the **maintenance margin** (a set share of the notional), the exchange closes the position by force. That is a **liquidation**, and the price at which it happens is the **liquidation price**.

For a long with entry price \(E\), leverage \(L\), and maintenance margin rate \(m\) (a fraction of notional):

\[ P_{\text{liq}} = \frac{E \, (1 - 1/L)}{1 - m} \]

- \(E\) is the entry price, in US$.
- \(L\) is leverage, a number such as 10.
- \(m\) is the maintenance margin as a fraction of the position's current value. This example uses 0.5%, made up.
- The formula ignores fees and funding, and it applies to an isolated position backed by its own collateral.

It comes from setting equity equal to the maintenance requirement: collateral + units x (P - E) = m x units x P, with collateral = units x E / L.

<div class="example" markdown>

### Worked example: where a 10x long is liquidated

You buy 1,000 units of the Coin A perp at US$20.00 with US$2,000 of collateral. The notional is US$20,000, so \(L\) is 10.

1. Liquidation price: 20.00 x (1 - 0.1) / (1 - 0.005) = 18.00 / 0.995 = US$18.09.
2. Check: at 18.09 the equity is 2,000 + 1,000 x (18.09 - 20.00) = about US$90, and maintenance is 0.005 x 18,090 = about US$90.
3. The fall that wipes you out: (20.00 - 18.09) / 20.00 = 9.5%.
4. At 2x leverage the same formula gives 20.00 x 0.5 / 0.995 = US$10.05, a fall of 49.7%.

Ten times leverage turns a 9.5% move into a total loss of the collateral. A daily bar in crypto often moves more than that.

</div>

![Equity of a 10x long falling to the maintenance margin line at US$18.09](../assets/figures/18-crypto/liquidation-dark.svg#only-dark)
![Equity of a 10x long falling to the maintenance margin line at US$18.09](../assets/figures/18-crypto/liquidation-light.svg#only-light)

### Liquidation cascades

A liquidation is a market order: the exchange sells your position into the book, whatever the price. If many positions sit near the same price, the first liquidations push the price down, which pushes the next group below its liquidation price, and so on. This chain is a **liquidation cascade**. Thin order books make it worse, because the forced sells land on few buyers.

The chart is made-up data in which Coin A rises to 27.50 and then falls in one day. The generator draws weekdays only, while a real crypto market has weekend bars as well.

```chart
data: 18-crypto/coin-a-cascade.json
title: Coin A, daily (weekdays only): a one-day cascade
show: volume
marker: 2026-04-16 | above | Cascade day
level: 27.50 | April 15 close
range: 2026-03-30 to 2026-05-15
caption: On April 16 the price opened at 27.50, fell to 22.83 and closed at 23.65, on about four times the median daily volume.
```

Test two longs entered at the April 15 close of 27.50. The 10x position has \(P_{\text{liq}}\) = 27.50 x 0.9 / 0.995 = US$24.87, and the day's low of 22.83 passed through it. The 5x position has 27.50 x 0.8 / 0.995 = US$22.11, which the low did not reach, so it survived. On the day's close the price was down 14.0%, which is a 70% loss of the 5x position's collateral. Leverage alone decided who stayed in. Part 3 covers sizing for exactly this reason ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

<div class="canada" markdown>

### For Canadians

Whether a Canadian resident can trade perpetual futures depends on the platform and on securities rules for derivatives. Which platforms serve Canadians changes, so check the platform's terms, the CSA's lists from lesson 4, and the margin and tax rules before you open an account. Treat the formulas here as concepts. Lesson 9 covers the CRA's general rules for crypto gains and losses, and does not settle how a derivative is taxed, so ask a tax professional.

</div>

## Common mistakes

- Setting a stop beyond the liquidation price. The exchange closes you out first.
- Reading the funding rate per interval as the full cost of holding. Multiply it by the intervals in your holding period.
- Using one venue's price as "the" price. Check the index and the mark price the exchange uses for liquidations.

## Try it

1\. Long 500 units, mark price US$40.00, funding rate 0.02% for the interval. What do you pay?

<details class="solution" markdown>
<summary>Answer</summary>

N = 500 x 40.00 = US$20,000. Payment = 20,000 x 0.0002 = US$4.00, paid by you because the rate is positive and you are long.

</details>

2\. A short holds the same position. Does it pay or receive at that rate?

<details class="solution" markdown>
<summary>Answer</summary>

It receives US$4.00. When the rate is positive, shorts are paid by longs.

</details>

3\. Entry US$50.00, 4x leverage, maintenance 0.5%. Find the liquidation price and the fall that triggers it.

<details class="solution" markdown>
<summary>Answer</summary>

P_liq = 50.00 x (1 - 0.25) / 0.995 = 37.50 / 0.995 = US$37.69. The fall is (50.00 - 37.69) / 50.00 = 24.6%.

</details>

4\. Funding is 0.01% every 8 hours on US$10,000 of notional. What is the cost over 30 days?

<details class="solution" markdown>
<summary>Answer</summary>

10,000 x 0.0001 = US$1.00 per interval. 3 x 30 = 90 intervals, so US$90.00, or 0.9% of notional.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Look up the current funding rate for one perp on a public exchange page. Compute the cost for one day on US$1,000 of notional. |
| 3 | Pick a leverage of 3x, 5x and 10x. Compute the liquidation price for an entry of 100, with maintenance at 0.5%. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) the largest daily fall you would accept on a leveraged position, and the leverage that survives it. |

</div>

## Key terms

- **Perpetual future (perp)**: a futures contract with no expiry date.
- **Funding rate**: the periodic payment between longs and shorts that keeps a perp near the spot price.
- **Collateral**: the deposit that backs a leveraged position.
- **Maintenance margin (perp)**: the equity a position must keep, as a share of its notional.
- **Liquidation price**: the price at which the exchange closes a position by force.
- **Liquidation cascade**: a chain of forced sales that pushes the price down and triggers more of them.

Next: [On-chain data and crypto cycles](07-on-chain-data-and-cycles.md)
