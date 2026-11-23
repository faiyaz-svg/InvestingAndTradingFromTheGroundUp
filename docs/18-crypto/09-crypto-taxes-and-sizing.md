# Crypto taxes and position sizing

<span class="tag tag-canada">Canada</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can say which crypto transactions the CRA treats as dispositions, work out a gain in Canadian dollars, apply the superficial loss rule to a coin, and size a position in a coin that moves much more than a stock.

Before this: [Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md), [Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md), [Tax losses and the superficial loss rule](../02-accounts-currency-and-taxes/09-tax-losses-and-superficial-loss.md), [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md). You need: a calculator.

This lesson is education, not tax advice. Your treatment depends on your facts, so check the CRA pages and ask a tax professional.

## The idea

You swap Coin A for Coin B on a platform. No dollars touch your bank account, but for the CRA it is a sale of Coin A at the market value of Coin B, and it can create a gain.

The CRA's crypto pages list the events that count as a disposition: selling for Canadian or foreign currency, trading one crypto-asset for another, paying for goods or services with crypto (treated as barter), and gifting or donating it. Moving coins between wallets you own is not a disposition ([CRA, Reporting income from crypto-asset transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html), as of 2026). The CRA's [guide for cryptocurrency users](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/digital-currency/cryptocurrency-guide.html) says it generally treats cryptocurrency like a commodity for the purposes of the Income Tax Act, and that trading one cryptocurrency for another is a barter transaction and a disposition. For a coin held as an investment, the capital gains rules from part 2 apply.

## How it works

### Capital or business

The same two treatments apply as for stocks. A gain from activity that is not a business is a capital gain, and half is taxable. If it is business income, all of it is income. The CRA considers factors such as how often you trade and how long you hold.

### Amounts in CAD

Everything is in Canadian dollars at fair market value, the price a willing buyer and a willing seller would agree on. The CRA says to use a reasonable method and apply it consistently from year to year ([CRA, Determining the value of crypto-assets](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/value-crypto.html), as of 2026). A coin you receive in a trade has a cost base equal to its fair market value that day. For identical coins bought at different prices, the CRA's tax tip on [reporting capital gains as a crypto-asset user](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2024/reporting-your-capital-gains-as-crypto-asset-user.html) says the adjusted cost base is usually the weighted average cost, which is part 2's average-cost method.

<div class="example" markdown>

### Worked example: a swap and a quick buyback

All prices are in C$ and made up.

1. Buy 100 Coin A at C$20.00 (C$2,000) and 50 at C$26.00 (C$1,300). ACB = 3,300 / 150 = C$22.00 per coin.
2. Swap 60 Coin A for Coin B worth C$1,800. ACB of the 60 = 60 x 22.00 = C$1,320. Gain = 1,800 - 1,320 = C$480.
3. Half is taxable: C$240. At a made-up 40% rate the tax is C$96. Coin B has an ACB of C$1,800.
4. You hold 90 Coin A with an ACB of 1,980. You sell 40 at C$15.00 for C$600. ACB of those 40 = C$880, so the loss is C$280.
5. Ten days later you buy 40 Coin A at C$15.50 (C$620) and still hold them 30 days after the sale. The loss is superficial and denied.
6. The C$280 is added to the cost of the new purchase. ACB of your 90 coins = 50 x 22.00 + 620 + 280 = C$2,000, or C$22.22 per coin.

</div>

### The superficial loss rule

Part 2, lesson 9 gives the rule: a loss is denied if you or an affiliated person buy the same or an identical property within 30 days before or after the sale and still hold it 30 days after ([CRA, T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). The CRA's crypto pages do not mention the rule, and it is a general rule for capital property, so a repurchase of the same coin fits its pattern. A swap into a different coin does not. Whether two forms of the same coin are identical is a question for a tax professional.

### Records

The CRA expects, for each transaction, the amount and type of coin, the date and time, the value in CAD, a description with the other party, and the wallet addresses. Export platform ledgers regularly. Keep everything at least six years from the end of the last tax year it relates to ([CRA, Keeping books and records](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html), as of 2026).

### Sizing a volatile coin

Part 3's method is unchanged: risk amount divided by risk per unit. What changes is that the **average true range** (ATR) is a larger share of the price.

\[ S = E - k \times ATR \qquad \text{units} = \left\lfloor \frac{f \times A}{E - S} \right\rfloor \]

- \(E\) is the entry price and \(S\) the stop, in C$ per coin.
- \(k\) is the ATR multiple (2 here) and \(ATR\) is in C$ per coin.
- \(f\) is the share of the account risked and \(A\) is the account in C$.

<div class="example" markdown>

### Worked example: sizing a coin

Account C$20,000, risk 1% (C$200). On June 2, 2026 the made-up Coin A closes at C$22.17 with a 14-day ATR of C$1.22 (1.2243 before rounding), which is 5.5% of the price. Spot only, no leverage.

1. Stop: 22.17 - 2 x 1.2243 = C$19.72.
2. Risk per coin: C$2.45 (2.4486 before rounding).
3. Units: 200 / 2.4486 = 81.7, so 81 coins.
4. Position: 81 x 22.17 = C$1,795.77, which is 9.0% of the account.
5. If the price gaps through the stop and fills at C$18.00 (as on the cascade day in lesson 6), the loss is 81 x (22.17 - 18.00) = C$337.77, or 1.7% of the account, not 1%.

With leverage (lesson 6), keep the stop above the liquidation price.

</div>

The chart shows the ATR in its own panel and the stop as a level.

```chart
data: 18-crypto/coin-a-cascade.json
title: Coin A, daily (weekdays only): ATR in its own panel
show: atr 14
level: 19.72 | ATR stop
range: 2026-04-27 to 2026-06-02
caption: On June 2 the close was 22.17, the 14-day ATR was 1.22 and the stop was 19.72.
```

## In code

The sample file is [coin-a-daily.csv](../assets/data/coin-a-daily.csv), the same made-up bars as the chart.

<details class="code" markdown>
<summary>In code</summary>

```python
import pandas as pd

bars = pd.read_csv("coin-a-daily.csv", parse_dates=["date"])
prev = bars["close"].shift()
tr = pd.concat([bars["high"] - bars["low"],
                (bars["high"] - prev).abs(),
                (bars["low"] - prev).abs()], axis=1).max(axis=1)
atr = tr.rolling(14).mean().iloc[-1]
entry = bars["close"].iloc[-1]
stop = entry - 2 * atr
units = int(0.01 * 20_000 / (entry - stop))
print(round(atr, 4), round(stop, 2), units)
```

It prints 1.2243, 19.72 and 81.

</details>

## Common mistakes

- Treating a coin-to-coin swap as tax-free. It is a disposition at fair market value.
- Not recording the CAD value of each trade on the day.
- Sizing a coin like a stock. A wide ATR means the same C$200 risk buys few coins.

## Try it

1\. You bought 100 coins at C$30 and 100 at C$50, and sell 50 for C$60 each. What is the taxable capital gain?

<details class="solution" markdown>
<summary>Answer</summary>

ACB = (3,000 + 5,000) / 200 = C$40. Gain = 50 x (60 - 40) = C$1,000. Half is taxable: C$500.

</details>

2\. Account C$10,000, risk 1%, entry C$20.00, stop C$17.00. How many coins?

<details class="solution" markdown>
<summary>Answer</summary>

Risk = C$100. Risk per coin = C$3.00. 100 / 3 = 33.3, so 33 coins.

</details>

## Part check

1\. After the second halving period, how many BTC have been issued?

<details class="solution" markdown>
<summary>Answer</summary>

210,000 x (50 + 25) = 15,750,000 BTC.

</details>

2\. You hold C$5,000 at an exchange. Who holds the private keys?

<details class="solution" markdown>
<summary>Answer</summary>

The exchange. Your balance is a claim on it (lesson 8).

</details>

3\. A long perp has entry US$50.00, 5x leverage and 0.5% maintenance. Liquidation price?

<details class="solution" markdown>
<summary>Answer</summary>

50.00 x (1 - 1/5) / (1 - 0.005) = 40.00 / 0.995 = US$40.20.

</details>

4\. Under the C$30,000 limit you buy C$10,000, buy C$15,000 and sell C$4,000 of Coin A. Room left?

<details class="solution" markdown>
<summary>Answer</summary>

Net cost = 21,000, so C$9,000 is left, if the limit applies to this coin.

</details>

5\. A spot ETF charges 0.50% a year. What is C$10,000 worth after 2 years if the coin does not move?

<details class="solution" markdown>
<summary>Answer</summary>

10,000 x 0.995^2 = C$9,900.25.

</details>

6\. Long 2,000 perp units at US$10.00, funding 0.01% per interval. One payment, and who pays?

<details class="solution" markdown>
<summary>Answer</summary>

20,000 x 0.0001 = US$2.00, paid by longs to shorts.

</details>

7\. Why can four halving cycles not prove halvings drive the price?

<details class="solution" markdown>
<summary>Answer</summary>

Four observations give a wide interval (t value 3.18 against 1.96), and other events overlap each cycle.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Set up a record sheet with the CRA's fields: date and time, coin and amount, CAD value, other party, wallet address. Enter three real or made-up transactions. |
| 3 | Compute the ACB per coin for those entries and the gain if you sold one. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) the largest daily move you would plan for in a coin, and the units that follow from a 1% risk. |

</div>

## Key terms

- **Disposition**: a sale, trade, payment or gift of property that triggers a gain or loss for tax.
- **Fair market value**: the price a willing buyer and a willing seller would agree on in an open market.
- **Barter transaction**: paying with crypto for goods or services, which is a disposition.
- **Adjusted cost base (crypto)**: the average Canadian-dollar cost of your coins of one kind.
- **ATR stop**: a stop set a multiple of the average true range from the entry.

Next: [Free data sources and their licences](../19-data-flows-and-forecasting/01-free-data-sources.md)
