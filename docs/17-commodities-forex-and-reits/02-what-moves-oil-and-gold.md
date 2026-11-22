# What moves oil and gold

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can list the main forces behind oil and gold prices, read a weekly inventory surprise in barrels, and work out how a stronger US dollar or a higher real yield changes what gold costs to hold.

Before this: [Commodity markets](01-commodity-markets.md), [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md), [Treasuries and TIPS](../12-bonds-and-the-yield-curve/02-treasuries-and-tips.md). You need: a calculator.

## The idea

On Tuesday, September 1, 2026, the made-up oil future closes at US$70.75. On Wednesday it opens at US$73.93, which is 4.5% higher, after a group of producers announces a cut in output. No company changed what it earns, and nothing happened to demand. Supply expectations changed, and the price moved to fit them.

That is the pattern for oil: a price moves when the market's view of supply or demand moves. Gold works differently. It pays nothing, and its price follows what investors want to hold instead of it. This lesson takes oil first, then gold. It does not forecast either one.

```chart
data: 17-commodities-forex-and-reits/oil-daily.json
title: A made-up front-month oil future (US$ per barrel), daily
level: 71.28 | August high
marker: 2026-09-02 | below | Output cut announced (made up)
range: 2026-08-03 to 2026-10-02
caption: The price opened at 73.93 on September 2, above the August high of 71.28, then drifted up to a high of 78.19 on October 1.
```

## What moves oil

Four things do most of the work.

**Supply.** **OPEC+** is a group of oil-exporting countries that sets output targets for its members. Its decisions to raise or cut targets move the price, and so does news about disruptions at a field, a pipeline or a port. Non-members, including the United States, also matter, because they respond to price by drilling more or less.

**Demand.** Oil is burned for transport, heating and industry, so demand follows the economy. A growth scare or a recession pulls the price down. Part 11 covers the data that signals this ([Growth data](../11-macro-and-economic-data/06-growth-data.md)).

**Inventories.** Stored oil is the buffer between supply and demand. The US Energy Information Administration (EIA) publishes the **Weekly Petroleum Status Report**, which lists US crude oil stocks, refinery inputs, gasoline and distillate stocks, imports and exports. It is normally released on Wednesdays at 10:30 a.m. ET. In some holiday weeks it comes out on Thursday at 12:00 p.m. ET instead, and the schedule page lists each date ([EIA, release schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php), as of 2026). A **draw** is a fall in stocks, which means demand and exports exceeded supply. A **build** is a rise.

**The dollar and risk appetite.** Oil is priced in US dollars. When the dollar rises, oil costs more in other currencies, which tends to reduce buying. When investors sell risky assets in a panic, oil often falls with stocks.

### Reading an inventory report

Reports are judged against a **consensus** forecast, as in Part 11 ([How the economy is measured](../11-macro-and-economic-data/01-how-the-economy-is-measured.md)). Only the surprise matters.

<div class="example" markdown>

### Worked example: a weekly inventory surprise

The consensus for US crude stocks is a draw of 1.5 million barrels. At 10:30 a.m. ET the EIA reports a build of 3.2 million barrels. Made-up front-month oil trades at US$74.00 right before the release and US$73.11 ten minutes after.

1. Surprise = actual minus consensus = +3.2 - (-1.5) = 4.7 million barrels more stock than expected.
2. Price change = 73.11 - 74.00 = -US$0.89, which is -0.89 / 74.00 = -1.2%.
3. On one WTI contract of 1,000 barrels, the move is 0.89 x 1,000 = US$890.

The market read more oil in storage than expected as a sign of weaker demand or stronger supply, and the price fell. A report that matches the consensus can leave the price flat even when stocks rise.

</div>

### Oil's curve after a shock

A supply shock moves the front of the curve more than the back, because the shortage is felt now and is expected to fade. The figure uses made-up prices for six contract months.

![Oil futures curve in contango before a supply shock and in backwardation after it](../assets/figures/17-commodities-forex-and-reits/oil-curve-shift-dark.svg#only-dark)
![Oil futures curve in contango before a supply shock and in backwardation after it](../assets/figures/17-commodities-forex-and-reits/oil-curve-shift-light.svg#only-light)

The front month rose from US$70.00 to US$78.00 (+US$8.00, +11.4%) and the sixth month rose from US$72.00 to US$73.00 (+US$1.00, +1.4%). The gap between the front month and the sixth month went from -US$2.00 (contango) to +US$5.00 (backwardation). A fund that holds the front contract feels this curve directly, which lesson 3 shows ([Commodity ETFs and roll costs](03-commodity-etfs-and-roll-costs.md)).

## What moves gold

Gold pays no interest and no dividend. Holding an ounce for a year gives you the price change and nothing else. That makes its price sensitive to what you could earn instead.

**Real yields.** A **real yield** is a bond yield after inflation. Part 12 showed it on TIPS, the Treasury bonds that adjust for inflation. When the real yield on a safe bond is high, holding gold means giving up more. With gold at US$2,400 per ounce (made up):

- real yield 1.5%: the cost of not holding the bond is 0.015 x 2,400 = US$36 a year per ounce
- real yield 2.5%: 0.025 x 2,400 = US$60 a year per ounce

A rise in real yields therefore tends to weigh on gold, and a fall tends to help it.

**The dollar.** Gold is priced in US dollars, so a stronger dollar makes it dearer in other currencies. For a Canadian, with USD/CAD at 1.3500, the ounce costs 2,400 x 1.3500 = C$3,240. If USD/CAD rises to 1.4000 and the US dollar price is unchanged, the ounce costs 2,400 x 1.4000 = C$3,360, which is 3.7% more. Buyers in Canada then buy less, which tends to push the US dollar price down.

**Fear and central banks.** Investors sometimes buy gold when they worry about inflation, wars or banks, and central banks hold gold in their reserves. These effects are harder to measure.

Treat each of these as a question to ask when gold moves: did real yields change, did the dollar change, was there a shock? Other forces act at the same time, so none of them is a rule.

<div class="canada" markdown>

### For Canadians

Both prices reach you in US dollars, so your result in CAD depends on USD/CAD as well. A fall in US$ gold of 3% with USD/CAD up 3% leaves your CAD value almost unchanged. Part 2 shows the split of a US-dollar return into asset and exchange-rate parts ([Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)).

</div>

## Common mistakes

- Trading the headline instead of the surprise. An inventory build that was forecast moves little.
- Treating one driver as the answer. Oil can fall on a build and rise on a weaker dollar in the same hour.
- Assuming gold must fall when real yields rise. It is a pressure that other forces can overpower.

## Try it

1\. The consensus for crude stocks is a build of 0.5 million barrels and the report shows a draw of 2.3 million. What is the surprise, and is it a build or a draw relative to expectations?

<details class="solution" markdown>
<summary>Answer</summary>

Surprise = -2.3 - 0.5 = -2.8 million barrels. Stocks fell 2.8 million barrels more than expected, so the report is a larger draw than forecast.

</details>

2\. Made-up oil trades at US$74.00 and falls to US$72.52 after a report. What is the percentage change, and the dollar change on 5 WTI contracts?

<details class="solution" markdown>
<summary>Answer</summary>

Change = 72.52 - 74.00 = -US$1.48, which is -1.48 / 74.00 = -2.0%. On 5 contracts: 1.48 x 1,000 x 5 = US$7,400 (a loss for a long position).

</details>

3\. Gold is US$2,400 per ounce and the real yield on a TIPS rises from 1.5% to 2.0%. By how much does the yearly cost of holding an ounce instead of the bond rise?

<details class="solution" markdown>
<summary>Answer</summary>

At 1.5% the cost is US$36; at 2.0% it is 0.02 x 2,400 = US$48. It rises by US$12 per ounce per year.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Open the [EIA release schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php). Write the next report date and whether it is a normal Wednesday release. |
| 3 | Find the latest weekly report's headline: crude stocks, change from the prior week, and the consensus if your calendar shows it. Compute the surprise. |
| 3 | Open a 10-year TIPS yield and the USD/CAD rate. Write today's values in your [trade journal](../practice/trade-journal.md) as a baseline for gold questions. |

</div>

## Key terms

- **OPEC+**: a group of oil-exporting countries that sets output targets for its members.
- **Weekly Petroleum Status Report**: the EIA's weekly report on US oil stocks, refinery inputs, imports and exports.
- **Draw**: a fall in inventories.
- **Build**: a rise in inventories.
- **Real yield**: a bond yield after inflation.

Next: [Commodity ETFs and roll costs](03-commodity-etfs-and-roll-costs.md)
