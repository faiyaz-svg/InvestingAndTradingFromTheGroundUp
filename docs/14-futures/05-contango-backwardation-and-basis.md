# Contango, backwardation and basis

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">FUT</span>

After this lesson you can work out a futures contract's fair value from the spot price, say whether a curve is in contango or backwardation, and see why a futures price falls toward spot at expiry.

Before this: [Expiry and rolling](04-expiry-and-rolling.md), [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md). You need: a calculator.

## The idea

On a day when the made-up Index X is at 6,000.00 (the **spot** price, the price of the index itself), the December contract trades at 6,040.50, three months before it expires. Why would a contract on the same index cost 40.50 points more? Nobody expects the index to rise exactly 40.50 points. The difference comes from the cost of holding the index until December.

Suppose you wanted the index exposure for three months, and you had two ways to get it. You could buy the stocks in the index, which costs US$6,000 per unit of index, financed with borrowed money at 4.00% a year. Or you could buy the future. In three months the stocks have cost you interest, and they have paid dividends (at 1.30% a year, a made-up yield).

- Interest: 6,000 x 0.04 x 0.25 = 60.00 points.
- Dividends received: 6,000 x 0.013 x 0.25 = 19.50 points.
- Net cost of carrying the stocks: 60.00 - 19.50 = 40.50 points.

The future must be priced so both routes cost the same, or a trader could earn a risk-free profit. That cost of holding the asset is the **cost of carry**.

## How it works

\[ F = S \times \bigl(1 + (r - d) \times T\bigr) \]

- \(F\) is the fair value of the futures price, in index points.
- \(S\) is the spot price, in index points.
- \(r\) is the annual interest rate for borrowing, as a fraction (0.04 for 4.00%). See the [bond lesson](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md) for why rates are quoted per year.
- \(d\) is the annual dividend yield of the index, as a fraction.
- \(T\) is the time to expiry in years (0.25 for three months).

This is the usual simple form. Real pricing uses exact day counts and compounding, so a live price differs by a small amount.

<div class="example" markdown>

### Worked example: fair value and convergence

\(S\) = 6,000.00, \(r\) = 4.00%, \(d\) = 1.30%, \(T\) = 0.25.

1. \(r - d\) = 0.04 - 0.013 = 0.027.
2. F = 6,000 x (1 + 0.027 x 0.25) = 6,000 x 1.00675 = 6,040.50.
3. The **basis** is spot minus futures: 6,000.00 - 6,040.50 = -40.50. Some sources define it as futures minus spot, so check the sign convention before you compare numbers.
4. Two months later, with spot still at 6,000.00, T = 1/12 = 0.0833. F = 6,000 x (1 + 0.027 x 0.0833) = 6,013.50. The futures price fell 27.00 points while spot did not move.
5. At expiry T = 0 and F = 6,000.00. The futures price equals spot, which is **convergence**.

A long holder of one micro contract lost 27.00 x 5 = US$135.00 between steps 2 and 4 with a flat index, but a holder of the stocks would have paid the same cost in interest, less dividends. The future's price moves in step with the carry.

</div>

If the actual price were 6,080.00, above fair value of 6,040.50, a trader could sell the future, buy the stocks and borrow to pay for them, and lock in 39.50 points before trading costs. Such trades push the price back to fair value. That is why index futures stay close to their formula.

## Contango and backwardation

When the futures price is above spot, and later contracts cost more than earlier ones, the market is in **contango**. When later contracts cost less, it is in **backwardation**. The set of futures prices across expiry months is the **futures curve**, or term structure. The figure shows both on made-up numbers.

![A futures curve rising with expiry in contango and falling in backwardation, around a flat spot price of 100](../assets/figures/14-futures/contango-backwardation-dark.svg#only-dark)
![A futures curve rising with expiry in contango and falling in backwardation, around a flat spot price of 100](../assets/figures/14-futures/contango-backwardation-light.svg#only-light)

For an index, \(r\) is usually larger than \(d\), so the curve usually rises (contango). If \(d\) exceeded \(r\), it would slope down.

For commodities, carry includes storage and insurance costs, and a benefit of holding the physical good, the **convenience yield**. The formula becomes \(F = S \times (1 + (r + u - y) \times T)\), where \(u\) is the storage cost and \(y\) is the convenience yield, all per year. With \(S\) = 80.00 (made-up units), \(r\) = 4%, \(u\) = 3% and \(y\) = 0, three-month fair value is 80 x (1 + 0.07 x 0.25) = 81.40. With a convenience yield of 9% (scarce supply, users who need the goods now) the result is 80 x (1 + (0.04 + 0.03 - 0.09) x 0.25) = 79.60, which is backwardation.

## Why it matters when you hold

Convergence has a cost for long holders in contango. Suppose a fund holds the three-month contract at 81.40, spot stays at 80.00, and it rolls each quarter. Each roll gives up 1.40, which is 1.40 / 80.00 = 1.75% of price. Four rolls cost about 7.0% in a year (1.75% x 4), even if spot never moves. This is **roll yield** (negative in contango, positive in backwardation). It matters for commodity funds, covered in Part 17 ([Commodity markets](../17-commodities-forex-and-reits/01-commodity-markets.md), [Commodity ETFs and roll costs](../17-commodities-forex-and-reits/03-commodity-etfs-and-roll-costs.md)). For an index future the carry is the net of interest and dividends, which was 2.7% a year in this lesson's example, so the drag is smaller than the commodity case above.

<div class="canada" markdown>

### For Canadians

When you size a contract in US dollars from a Canadian account, \(r\) in the formula is the US rate, because the contract is priced against US dollar funding. Your own cost of borrowing does not enter the price. Part 11 covers where rates come from ([Interest rates and asset prices](../11-macro-and-economic-data/03-interest-rates-and-asset-prices.md)).

</div>

## Common mistakes

- Reading contango as a forecast that prices will rise. It is the cost of carry, not an expectation.
- Ignoring the basis when comparing a future with the index. A 40.50-point difference is not an arbitrage.
- Mixing the sign convention for basis. Write which one you use.

## Try it

1\. \(S\) = 5,000.00, \(r\) = 5.00%, \(d\) = 1.50%, \(T\) = 0.5. What is fair value?

<details class="solution" markdown>
<summary>Answer</summary>

F = 5,000 x (1 + (0.05 - 0.015) x 0.5) = 5,000 x 1.0175 = 5,087.50.

</details>

2\. In exercise 1, the future trades at 5,100.00. Is it rich or cheap against fair value, and by how many points?

<details class="solution" markdown>
<summary>Answer</summary>

It is rich: 5,100.00 - 5,087.50 = 12.50 points above fair value.

</details>

3\. A commodity has \(S\) = 80.00, \(r\) = 4%, \(u\) = 3%, \(y\) = 0, and \(T\) = 0.5. What is the six-month fair value?

<details class="solution" markdown>
<summary>Answer</summary>

F = 80 x (1 + 0.07 x 0.5) = 80 x 1.035 = 82.80.

</details>

4\. Is a curve with spot 100, three-month 99.20 and six-month 98.50 in contango or backwardation?

<details class="solution" markdown>
<summary>Answer</summary>

Backwardation: later contracts cost less than spot.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the front two months of one index future. Compute the spread and compare it with the formula using a current short-term rate and a dividend yield you look up. |
| 5 | Write in your own words why the spread shrinks every day, and check it tomorrow. |

</div>

## Key terms

- **Spot**: the price of the underlying for immediate delivery or, for an index, the index level.
- **Cost of carry**: the net cost of holding the underlying until expiry.
- **Fair value**: the futures price that matches the cost of carry.
- **Basis**: spot minus futures (sign conventions vary).
- **Convergence**: the futures price moving to the spot price as expiry nears.
- **Contango**: a curve where later contracts cost more.
- **Backwardation**: a curve where later contracts cost less.
- **Futures curve**: futures prices across expiry months.
- **Convenience yield**: the benefit of holding the physical good, per year.
- **Roll yield**: the gain or loss from rolling along the curve.

Next: [Futures hours and sessions](06-futures-hours-and-sessions.md)
