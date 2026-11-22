# Commodity ETFs and roll costs

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can say how a futures-based commodity ETF holds its exposure, work out what a year of rolling costs in contango, and explain why the April 2020 WTI price went below zero.

Before this: [Expiry and rolling](../14-futures/04-expiry-and-rolling.md), [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md), [How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md). You need: a calculator.

## The idea

Fund A is a made-up oil ETF. The price of oil on the spot market is US$80.00 a barrel and does not move for a whole year. A reader who buys Fund A expects to get back what they put in. After 12 months the fund is down 8.6%. Nothing is wrong with the fund. It did what it says it does, and the cost sits in how it holds oil.

A fund cannot store barrels in a warehouse, so most oil ETFs hold futures contracts. A futures contract expires, so the fund must sell the one it holds and buy the next one: the **roll** from Part 14 ([Expiry and rolling](../14-futures/04-expiry-and-rolling.md)). If the next contract costs more than the one it replaces, each roll costs the fund money.

## How it works

### What the fund holds

A **futures-based ETF** holds futures contracts for the commodity and keeps the rest of its cash in short-term Treasury bills. A fund with US$10 million and a WTI price of US$80.00 holds about 10,000,000 / (80.00 x 1,000) = 125 contracts, one contract being 1,000 barrels. Each fund has its own roll schedule in its prospectus: some roll over a few days before expiry, and some hold other months. Read it before you buy.

Other commodity funds avoid the roll. A **physically backed ETF** holds the metal itself (gold bars in vaults, as its prospectus describes) and has no futures to roll. A fund of producer stocks holds companies instead, with the stock risk of Part 10. Each choice gives a different exposure to the price.

### Roll yield

**Roll yield** is the gain or loss from rolling. In contango (later contracts cost more than earlier ones) the fund sells a cheap contract and buys a dearer one, then watches the dearer one fall toward spot as it ages: negative roll yield. In backwardation (later contracts cost less) it earns a positive roll yield. [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md) showed the cause.

\[ V_{12} = V_0 \times \frac{S_{12}}{S_0} \times \left(\frac{1}{1+c}\right)^{12} \]

- \(V_0\) and \(V_{12}\) are the fund's value at the start and after 12 months, in US$.
- \(S_0\) and \(S_{12}\) are the spot price at the start and after 12 months, in US$ per barrel.
- \(c\) is the contango per month: how much dearer the next contract is than the front one, as a fraction (0.0075 for 0.75%).
- The last factor is the roll cost compounded over 12 monthly rolls. This is a simplified model with a fixed \(c\). Real curves change from month to month.

<div class="example" markdown>

### Worked example: a year in contango

Spot is US$80.00. Each month the next contract is 0.75% above the front one, so \(c\) = 0.0075. The fund starts at US$10,000,000.

1. One monthly roll: the fund buys a contract at 80.00 x 1.0075 = 80.60. If spot does not move, that contract falls to 80.00 by the next roll, which is a loss of 0.60 per barrel, or 1 / 1.0075 = 0.99256 of its value, a 0.74% fall.
2. After 12 rolls: 0.99256^12 = 0.9142. With spot flat, \(V_{12}\) = 10,000,000 x 0.9142 = US$9,142,000, a loss of 8.6%.
3. If spot rises 5% to US$84.00: 10,000,000 x 1.05 x 0.9142 = US$9,600,000, a loss of 4.0%, even though oil rose. (Values are rounded to the nearest US$1,000.)

In backwardation, with each next contract 0.75% below the front one, the same arithmetic gives (1 / 0.9925)^12 = 1.0945, a gain of about 9.5% a year from rolling alone.

</div>

The figure shows the flat-spot case and the case where spot rises 5%.

![A commodity fund in contango loses value over 12 months even when the spot price is flat or rises 5%](../assets/figures/17-commodities-forex-and-reits/roll-yield-dark.svg#only-dark)
![A commodity fund in contango loses value over 12 months even when the spot price is flat or rises 5%](../assets/figures/17-commodities-forex-and-reits/roll-yield-light.svg#only-light)

Roll costs are not a fee that shows in the expense ratio, and they are not constant. They depend on the shape of the curve when the fund rolls, which can change from contango to backwardation within months (lesson 2 showed it after a shock). A fund that tracks the front contract can trail spot by a lot over years, and a fund's price chart over a long period is not the price of oil.

## April 2020: a negative price

On April 20, 2020, the May 2020 WTI contract, one day before it expired, settled at -US$37.63 per barrel. It was the first negative settlement in the contract's history. The CFTC's staff report on the event describes an oversupplied market, and the contract had little storage to receive physical oil for delivery ([CFTC, interim staff report on trading in NYMEX WTI crude oil, 2020](https://cftc.gov/media/5296/InterimStaffReportNYMEX_WTICrudeOil/download)). A holder of a long contract at expiry owes payment for barrels it must take, and with no place to put them, holders paid to be rid of the position. The lesson is that a futures price is a claim on delivery, and the front contract near expiry can behave differently from later months.

<div class="canada" markdown>

### For Canadians

Commodity ETFs come in US-listed and Canadian-listed versions. A Canadian-listed one is priced in CAD and may hedge the currency, as in [US-listed or Canadian-listed ETFs](../13-etfs-portfolios-and-factors/03-us-vs-canadian-listed-etfs.md). Whether a given fund is available at Wealthsimple or IBKR, and how it is taxed, depends on its structure. Read the prospectus and the broker's product page, and ask a tax professional if the structure is unclear. Part 13 covers leveraged funds, which add a daily reset on top of the roll ([Leveraged and inverse ETFs](../13-etfs-portfolios-and-factors/04-leveraged-and-inverse-etfs.md)).

</div>

## Common mistakes

- Judging a commodity ETF by the spot price. Compare it with the fund's own history, and check the curve for roll costs.
- Assuming a gold ETF and an oil ETF work the same way. One may hold metal, the other futures.
- Holding a futures contract into the last days of its life without a plan. Roll or close before the delivery process starts.

## Try it

1\. Spot is US$80.00 and the next contract is US$80.40. What is the contango per month, and the roll loss on a fund holding 200 contracts with spot flat until the next roll?

<details class="solution" markdown>
<summary>Answer</summary>

Contango = 0.40 / 80.00 = 0.5%. The held contract falls 0.40 per barrel: 0.40 x 1,000 x 200 = US$80,000.

</details>

2\. Using the lesson's model with \(c\) = 0.005, what is the value after 12 months of US$10,000 if spot is flat?

<details class="solution" markdown>
<summary>Answer</summary>

(1 / 1.005)^12 = 0.9419. 10,000 x 0.9419 = US$9,419, a loss of 5.8%.

</details>

3\. How far must spot rise over 12 months, with \(c\) = 0.0075, for the fund to break even?

<details class="solution" markdown>
<summary>Answer</summary>

The roll factor is 0.9142, so spot must rise by 1 / 0.9142 - 1 = 0.0938, which is 9.4%.

</details>

4\. Why can a futures price turn negative when a share price cannot?

<details class="solution" markdown>
<summary>Answer</summary>

A share carries no obligation beyond its price, so the worst outcome is zero. A futures holder at expiry must take delivery, with storage and handling costs. If nobody has room for the barrels, the holder pays to be rid of them, and the price goes below zero.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the page of one commodity ETF (any issuer). Find what it holds (futures or metal), its roll schedule or custody note, and its expense ratio. |
| 3 | Write what shape you expect its curve to have, and how you would check it on a futures quote page. |
| 2 | Write one sentence on whether a long-term holder or a short-term trader is more exposed to roll costs. |

</div>

## Key terms

- **Futures-based ETF**: a fund that holds futures contracts and short-term Treasury bills.
- **Physically backed ETF**: a fund that holds the metal itself.
- **Roll yield**: the gain or loss from selling an expiring contract and buying the next one.

Next: [Forex basics](04-forex-basics.md)
