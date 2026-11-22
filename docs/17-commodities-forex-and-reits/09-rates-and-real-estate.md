# Rates and real estate

<span class="tag tag-idea">Idea</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can explain why REIT prices fall when interest rates rise, work out how a cap rate change moves property value and equity value, and compare a REIT with a rental property on liquidity, leverage, tax and effort.

Before this: [REIT metrics: FFO and cap rates](08-reit-metrics-ffo-and-cap-rates.md), [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md), [Interest rates and asset prices](../11-macro-and-economic-data/03-interest-rates-and-asset-prices.md). You need: a calculator.

## The idea

REIT A, from lessons 7 and 8, closed at US$37.85 on June 26, 2026. Over the next month, in this made-up scenario, the 10-year Treasury yield rises from 3.9% to 4.9%. On July 28 REIT A closes at US$31.50, which is 31.50 / 37.85 - 1 = -16.8%. The buildings and tenants are the same.

```chart
data: 17-commodities-forex-and-reits/reit-daily.json
title: REIT A (made up), daily, in US$
level: 37.85 | June 26 close
level: 31.50 | July 28 close
marker: 2026-06-29 | above | Yields start to rise (made up)
range: 2026-06-01 to 2026-08-13
caption: REIT A closed at 37.85 on June 26 and at 31.50 on July 28, a fall of 16.8%, then traded between 31.23 and 32.12.
```

REITs are among the stocks most sensitive to interest rates, for three reasons.

## Why rates move REITs

### The cap rate follows rates

Part 11 showed that a higher discount rate lowers the present value of future cash ([Interest rates and asset prices](../11-macro-and-economic-data/03-interest-rates-and-asset-prices.md)). A building is a stream of rent, and its price is NOI divided by the cap rate (lesson 8). Buyers compare a building's yield with the Treasury yield, so the cap rate tends to equal a Treasury yield plus a spread for the extra risk. If the Treasury yield rises and the spread holds, the cap rate rises, and the value falls.

<div class="example" markdown>

### Worked example: a cap rate rise and leverage

REIT A has NOI of US$108.0 million and debt of US$720.0 million, with 20 million shares. At a 7.5% cap rate (a 4.0% Treasury yield plus a 3.5 point spread, made up), the properties are worth 108.0 / 0.075 = US$1,440.0 million and NAV is US$720.0 million, or US$36.00 per share.

1. The Treasury yield rises by 1 point and the spread holds, so the cap rate is 8.5%.
2. Property value = 108.0 / 0.085 = US$1,270.6 million, a fall of 1,270.6 / 1,440.0 - 1 = -11.8%.
3. Equity = 1,270.6 - 720.0 = US$550.6 million, or US$27.53 per share, a fall of 550.6 / 720.0 - 1 = -23.5%.
4. If the cap rate fell to 6.5% instead: value = 108.0 / 0.065 = US$1,661.5 million (+15.4%), equity US$941.5 million (+30.8%).

The debt is fixed, so the whole change lands on the equity, which moves about twice as much as the buildings.

</div>

![Property value and equity value of REIT A at cap rates of 6.5%, 7.5% and 8.5%](../assets/figures/17-commodities-forex-and-reits/cap-rate-leverage-dark.svg#only-dark)
![Property value and equity value of REIT A at cap rates of 6.5%, 7.5% and 8.5%](../assets/figures/17-commodities-forex-and-reits/cap-rate-leverage-light.svg#only-light)

The spread does not always hold. If rates rise because the economy is strong, rents may rise too, which softens the fall.

### Debt costs rise

A REIT refinances loans as they mature. Suppose US$200.0 million of REIT A's debt matures and is refinanced at 6.5% instead of 4.0%. Extra interest = 200.0 x 0.025 = US$5.0 million. FFO falls from 60.0 to 55.0, or US$2.75 per share from US$3.00, a fall of 8.3%. The dividend, which was 63.0% of FFO, is now 1.89 / 2.75 = 68.7% of it.

### The competing yield

An investor can hold a Treasury instead. REIT A's AFFO yield is 6.67% against a 4.0% Treasury, a gap of 2.67 points. If the Treasury yield rises to 5.0% and investors want the same gap, the AFFO yield must reach 7.67%. The price that gives it is 2.10 / 0.0767 = US$27.38, a fall of 13.1% from US$31.50, with no change in the REIT's cash flow.

## REITs and rental property

The other way to hold real estate is to own a building. The table compares the two.

| | REIT | Rental property you own |
|---|---|---|
| Liquidity | Sell in seconds at the market price | Weeks or months, with selling costs |
| Leverage | Inside the REIT; you owe nothing beyond your units | Your own mortgage, which you guarantee |
| Diversification | Many buildings in one unit | One building, one street |
| Effort | None beyond watching the holding | Tenants, repairs, vacancies, bookkeeping |
| Minimum cost | One unit | A down payment and closing costs |
| Control | None | Full: rent, upgrades, when to sell |
| Tax | Distributions taxed as income, return of capital or gains (lesson 7) | Net rent is income; half of a capital gain is taxable (CRA, [T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html), as of 2026) |

<div class="example" markdown>

### Worked example: leverage you own

A rental property costs C$500,000, with C$100,000 down and a C$400,000 loan at 5.0%, interest only to keep the arithmetic short (made up). NOI is C$25,000, so the cap rate is 25,000 / 500,000 = 5.0%.

1. Interest = 0.05 x 400,000 = C$20,000. Cash flow before tax = 25,000 - 20,000 = C$5,000, which is 5.0% of the C$100,000 down payment.
2. If the property's value falls 10% to C$450,000, equity = 450,000 - 400,000 = C$50,000, a fall of 50%.
3. C$100,000 in a REIT that falls 10% loses C$10,000. The REIT has its own debt, so its price can move more than its buildings, as REIT A showed, but your loss is limited to what you paid.

The property's leverage is 5 to 1 on your own cash, and you carry the loan.

</div>

<div class="canada" markdown>

### For Canadians

Canadian REIT debt costs follow Canadian bond yields and the Bank of Canada's path ([The Bank of Canada and a macro week](../11-macro-and-economic-data/11-the-bank-of-canada-and-a-macro-week.md)). A US REIT in a TFSA faces US withholding that depends on the account, as Part 2 explains ([US withholding tax and the W-8BEN](../02-accounts-currency-and-taxes/06-us-withholding-tax-and-w-8ben.md)).

</div>

## Common mistakes

- Assuming a REIT always falls when yields rise. The cause of the rise matters, as the economy and rents also move.

## Try it

1\. NOI is US$50.0 million. What is the property value at a 6.5% cap rate, and at 7.5%? What is the percentage change?

<details class="solution" markdown>
<summary>Answer</summary>

50.0 / 0.065 = US$769.2 million. 50.0 / 0.075 = US$666.7 million. Change = 666.7 / 769.2 - 1 = -13.3%.

</details>

2\. A REIT has property of US$1,000.0 million and debt of US$400.0 million. Property value falls 10%. What is the percentage fall in equity?

<details class="solution" markdown>
<summary>Answer</summary>

Equity before = 600.0. After: 900.0 - 400.0 = 500.0. Change = 500.0 / 600.0 - 1 = -16.7%.

</details>

## Part check

1\. Producer B will sell 40,000 barrels next month and sells 40 contracts at US$68.00. Oil ends at US$72.00. What price per barrel does it lock in?

<details class="solution" markdown>
<summary>Answer</summary>

Physical sale: 72.00 x 40,000 = US$2,880,000. Futures loss: (72.00 - 68.00) x 40,000 = -US$160,000. Total US$2,720,000, which is US$68.00 per barrel.

</details>

2\. When does the EIA normally release its weekly petroleum report, and what is the surprise if the consensus is a draw of 2.0 million barrels and the report shows a draw of 0.5 million?

<details class="solution" markdown>
<summary>Answer</summary>

Wednesdays at 10:30 a.m. ET (Thursday at 12:00 p.m. ET after a federal holiday). Surprise = -0.5 - (-2.0) = +1.5 million barrels: stocks fell less than expected.

</details>

3\. A commodity fund rolls monthly in a 1.0% contango and spot is flat for a year. What is the fund's change?

<details class="solution" markdown>
<summary>Answer</summary>

(1 / 1.01)^12 = 0.8874, a fall of 11.3%.

</details>

4\. You hold 30,000 units of USD/CAD, bought at 1.3650. The rate falls to 1.3620. What is the loss in pips and in CAD?

<details class="solution" markdown>
<summary>Answer</summary>

30 pips. Pip value = 30,000 x 0.0001 = C$3.00. Loss = 30 x 3.00 = C$90.00.

</details>

5\. Spot USD/CAD is 1.3400, the one-year US rate is 3.50% and the Canadian rate is 2.00%. What is the one-year forward rate?

<details class="solution" markdown>
<summary>Answer</summary>

F = 1.3400 x 1.02 / 1.035 = 1.3206.

</details>

6\. A margin rate of 2.5% (made up) applies to 20,000 units of USD/CAD at 1.3650. What are the leverage and the margin?

<details class="solution" markdown>
<summary>Answer</summary>

Leverage = 1 / 0.025 = 40. Position value = 20,000 x 1.3650 = C$27,300. Margin = 0.025 x 27,300 = C$682.50.

</details>

7\. A REIT has net income US$20.0 million, real estate depreciation US$35.0 million and a gain on a sale of US$5.0 million. It has 25 million shares and pays US$1.60. What is the payout ratio on FFO?

<details class="solution" markdown>
<summary>Answer</summary>

FFO = 20.0 + 35.0 - 5.0 = US$50.0 million, or US$2.00 per share. Payout = 1.60 / 2.00 = 80.0%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a REIT ETF. On a chart of the last two years, mark the dates the 10-year yield rose most and write the ETF's move over each (see [chart drills](../practice/chart-drills.md)). |
| 4 | Take the REIT from lesson 8's practice. Compute the change in its NAV per share for a 1 point rise in the cap rate. |
| 2 | Write in your [journal](../practice/trade-journal.md) one reason rates could rise that would help a REIT and one that would hurt it. |

</div>

## Key terms

- **Cap rate spread**: the cap rate minus a Treasury yield of similar term.
- **Refinancing**: replacing maturing debt with new debt at the current rate.
- **Leverage (real estate)**: the use of borrowed money so that equity is a small share of a property's value.

Next: What bitcoin is<!-- link: ../18-crypto/01-what-bitcoin-is.md -->
