# The VIX and the term structure

<span class="tag tag-data">Data</span> <span class="tag tag-part">VOL</span>

After this lesson you can say what the VIX measures, turn a VIX level into an expected move, read a curve of VIX futures in contango or backwardation, and work out the roll cost that eats into volatility products.

Before this: [Realized and implied volatility](01-realized-vs-implied-volatility.md), [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md), [Leveraged and inverse ETFs](../13-etfs-portfolios-and-factors/04-leveraged-and-inverse-etfs.md). You need: a calculator.

## The idea

A news site says the VIX is 20. Is that high? What does it say about tomorrow? We need to know what the number is made from.

The **VIX** is an index published by Cboe. Cboe describes it as a measure of market expectations of near-term volatility conveyed by S&P 500 option prices ([Cboe, VIX](https://www.cboe.com/tradable_products/vix/), as of 2026). Its methodology targets the 30-day expected volatility of the S&P 500, and it uses out-of-the-money SPX calls and puts with more than 23 and fewer than 37 days to expiry ([Cboe VIX methodology](https://cdn.cboe.com/resources/vix/VIX_Methodology.pdf), as of 2026). It is quoted in volatility points per year, the same unit as the implied volatility of part 15.

It is not the implied volatility of one option. It combines options across many strikes, so it prices the whole distribution of outcomes, including the tails.

## How it works

### What goes into the number

For each of the two expiries around 30 days, Cboe computes a variance from a weighted sum of out-of-the-money option prices, then blends the two to a constant 30 days.

\[ \sigma^2 = \frac{2}{T} \sum_i \frac{\Delta K_i}{K_i^2}\, e^{RT}\, Q(K_i) - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2, \qquad \text{VIX} = 100 \times \sqrt{\sigma^2} \]

- \( T \) is the time to expiry in years, \( R \) is the risk-free rate, and \( F \) is the forward index level.
- \( K_i \) is the strike of the \( i \)th out-of-the-money option (puts below \( K_0 \), calls above), \( \Delta K_i \) is the gap to its neighbouring strikes, and \( K_0 \) is the first strike below \( F \).
- \( Q(K_i) \) is the midpoint of that option's bid and ask, in index points.
- The sum is over all strikes with a valid quote. The result is a variance, and the square root turns it into a volatility. The blend of the two expiries is in Cboe's methodology.

You will not compute this by hand. What matters is that it is a weighted average of option prices, with far out-of-the-money puts included, which is why it rises when investors pay more for protection.

### From a VIX level to a move

Treat the VIX like any IV. The one-standard-deviation move over 30 days is \( \text{VIX} \times \sqrt{30/365} \), and over one day it is \( \text{VIX} / \sqrt{252} \).

| VIX | One-standard-deviation move over 30 days | Per day |
|---|---|---|
| 14.5 | 4.16% | 0.91% |
| 20 | 5.73% | 1.26% |
| 31 | 8.89% | 1.95% |

The VIX gives a size, not a direction. A 20 says the options market is pricing roughly a 5.7% one-standard-deviation range for the S&P 500 over the next 30 days, in either direction.

### The VIX is not tradable

You cannot buy the VIX itself. FINRA says volatility-linked products track indexes of VIX futures rather than the VIX, which is not directly investable ([FINRA, Know Before You Invest](https://syndication.finra.org/node/282), October 26, 2017). Cboe lists **VIX futures**, introduced in 2004, and options on the VIX ([Cboe, VIX](https://www.cboe.com/tradable_products/vix/), as of 2026). A VIX future is a contract on the VIX's value at its expiry. Its price today is the market's price for the VIX on that date, not the VIX now.

### The term structure

The prices of VIX futures across expiries form a **volatility term structure**: a curve of the market's price for volatility at different dates. The figure shows two made-up curves, drawn like the curves in part 14 ([Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md)).

![Two made-up VIX futures curves: contango with the VIX at 14.5 and futures rising to 18.6, backwardation with the VIX at 31.0 and futures falling to 23.6](../assets/figures/16-volatility-and-event-trading/vix-term-structure-dark.svg#only-dark)
![Two made-up VIX futures curves: contango with the VIX at 14.5 and futures rising to 18.6, backwardation with the VIX at 31.0 and futures falling to 23.6](../assets/figures/16-volatility-and-event-trading/vix-term-structure-light.svg#only-light)

On the left the VIX is 14.5 and later futures cost more: **contango**. Calm markets usually look like this. On the right the VIX is 31.0 and later futures cost less: **backwardation**. Stress usually looks like this, because the market expects volatility to fall back.

### The roll cost

A volatility exchange-traded product (ETP) holds VIX futures and keeps a steady maturity, so it sells the near contract and buys a later one as time passes. In contango the near contract converges down to the VIX as it expires. FINRA's notice says that when later contracts cost more, as in contango, this rolling produces a negative roll yield and a loss on the trade, and that some of these products had lost more than 90% of their value since launch ([FINRA Regulatory Notice 17-32](https://www.finra.org/rules-guidance/notices/17-32), October 16, 2017).

<div class="example" markdown>

### Worked example: the cost of contango with the VIX unchanged

Use the contango curve: the VIX is 14.50 and the one-month future is 15.80. A product holds the one-month future. Suppose the VIX stays at 14.50.

1. The future converges to the VIX at expiry: from 15.80 to 14.50.
2. The loss is (14.50 - 15.80) / 15.80 = -0.0823, so -8.2% in a month.
3. If the curve kept this shape every month, twelve months of it compound to (1 - 0.0823)^12 - 1 = -0.643, so -64.3%.

This is a simplified model: real curves move, the VIX does not stay flat, and the product holds a blend of contracts. It shows the mechanism. In backwardation the sign flips, but volatility spikes tend to fade, and leveraged and inverse versions reset daily, so holding them is a different problem from timing one ([Leveraged and inverse ETFs](../13-etfs-portfolios-and-factors/04-leveraged-and-inverse-etfs.md)).

</div>

FINRA also says volatility-linked ETNs are unsecured debt, so holders carry the issuer's credit risk, and that most of these products are short-term trading tools, not long-term hedges ([FINRA, Know Before You Invest](https://syndication.finra.org/node/282)).

## Common mistakes

- Reading a VIX level as a forecast of direction. It prices the size of moves, up or down.
- Assuming a volatility ETP follows the VIX. It follows futures, and the roll cost separates them.
- Holding a volatility product as a long-term hedge. The sources above say it is built for short holding periods.

## Try it

1\. The VIX is 25. What is the one-standard-deviation move over 30 days, and over one day?

<details class="solution" markdown>
<summary>Answer</summary>

30 days: 25 x \( \sqrt{30/365} \) = 25 x 0.2867 = 7.17%. One day: 25 / 15.8745 = 1.57%.

</details>

2\. The VIX is 31.0 and the one-month future is 28.9. Contango or backwardation, and by how many points?

<details class="solution" markdown>
<summary>Answer</summary>

Backwardation, because the future is below the VIX. The gap is 31.0 - 28.9 = 2.1 points.

</details>

3\. A product holds a one-month future at 19.40 while the VIX sits at 18.00. If the VIX does not move, what is the one-month result?

<details class="solution" markdown>
<summary>Answer</summary>

(18.00 - 19.40) / 19.40 = -0.0722, so -7.2%.

</details>

4\. A friend says "VIX 20 means the S&P 500 will fall 5.7%". What is wrong?

<details class="solution" markdown>
<summary>Answer</summary>

The 5.7% is one standard deviation of the move in either direction over 30 days. It says nothing about the sign, and the index can move more or less.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Look up today's VIX on Cboe's site and compute its 30-day and one-day one-standard-deviation moves. |
| 3 | Find the VIX futures curve on Cboe's site. Write the first four expiries and call it contango or backwardation. |
| 3 | For the first two expiries, compute the one-month roll cost if the VIX stays where it is. |

</div>

## Key terms

- **VIX**: Cboe's index of the 30-day expected volatility of the S&P 500, built from SPX option prices.
- **VIX futures**: contracts on the VIX's value at a future date; the VIX itself cannot be bought.
- **Volatility term structure**: the curve of VIX futures prices across expiries.
- **Volatility exchange-traded product (ETP)**: a fund or note that holds VIX futures and so carries their roll cost.

Next: [Volatility regimes](03-volatility-regimes.md)
