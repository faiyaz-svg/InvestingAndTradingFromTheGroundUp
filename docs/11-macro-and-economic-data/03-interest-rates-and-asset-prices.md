# Interest rates and asset prices

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MACRO</span>

After this lesson you can discount a stream of cash flows at two rates, show why higher rates cut the value of far-off cash more than near cash, and name the other routes from rates to stock prices.

Before this: [The Fed and the FOMC](02-the-fed-and-the-fomc.md). The math book has the formula: [present and future value](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/03-time-value-of-money/01-present-and-future-value/) and [present value, NPV and bond prices](https://faiyaz-svg.github.io/MathFromTheGroundUp/07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices/). You need: a calculator.

## The idea

A trader sees the Fed raise rates and Stock B fall 4% while Stock A falls 1%. Both companies are fine. What differs is when each one's cash arrives.

Money today is worth more than the same money later, because today's money can earn interest. If a safe account pays 3% a year, US$100 today becomes US$103 next year. Turned around, US$103 next year is worth US$100 today. The rate used to turn future money into today's value is the **discount rate**, and the result is the **present value** (PV).

The Fed's rate feeds into every discount rate. When the safe rate rises, the discount rate for risky cash flows rises with it (it is the safe rate plus a premium for risk, which Part 10 covers in [Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md)). A higher discount rate lowers the present value of everything, and it lowers the value of late cash more than early cash.

## How it works

The present value of a stream of cash flows is:

\[ PV = \sum_{t=1}^{T} \frac{CF_t}{(1+r)^t} \]

- \(CF_t\) is the cash flow received in year \(t\), in US$ per share.
- \(r\) is the discount rate per year, as a fraction (6% is 0.06).
- \(t\) is the number of years from now, from 1 to \(T\).
- \(PV\) is the value today, in US$ per share.

Each year's cash is divided by \((1+r)^t\), which grows with \(t\). The farther away the cash, the more the divisor bites, and the more a change in \(r\) matters.

<div class="example" markdown>

### Worked example: two made-up companies

Both companies will hand shareholders US$100 per share in total. Stock A pays US$20 a year for years 1 to 5. Stock B pays nothing for nine years and US$100 in year 10, perhaps because it reinvests everything. We discount at 3%, then at 6%, after a rise in rates.

Stock A at 3%: 20/1.03 + 20/1.03^2 + 20/1.03^3 + 20/1.03^4 + 20/1.03^5 = US$91.59.
Stock A at 6%: the same sum at 1.06 = US$84.25.

Stock B at 3%: 100 / 1.03^10 = US$74.41.
Stock B at 6%: 100 / 1.06^10 = US$55.84.

Changes, from 3% to 6%:

1. Stock A: 84.25 / 91.59 - 1 = -8.0%.
2. Stock B: 55.84 / 74.41 - 1 = -25.0%.

The same rate rise cost Stock B about three times as much as Stock A, because its cash is ten years away.

</div>

The bars show present values at both rates. Look at how much shorter the Stock B bars get than the Stock A bars.

![Bars of present value for Stock A and Stock B at 3% and 6% discount rates: Stock B falls much more.](../assets/figures/11-macro-and-economic-data/pv-two-companies-dark.svg#only-dark)
![Bars of present value for Stock A and Stock B at 3% and 6% discount rates: Stock B falls much more.](../assets/figures/11-macro-and-economic-data/pv-two-companies-light.svg#only-light)

Real stocks do not pay fixed cash flows, so this is a model of one channel, not a forecast. It explains why traders say that stocks whose profits sit far in the future, often fast-growing companies, react most to rate news. Bonds have the same property in its purest form. A bond's cash flows are fixed, so its price is a PV, and the sensitivity of price to rates is called duration, which Part 12 teaches (Duration and convexity<!-- link: ../12-bonds-and-the-yield-curve/04-duration-and-convexity.md -->). The yield on a Treasury is the bond market's discount rate for safe cash (Bond prices and yields<!-- link: ../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md -->).

### Other routes from rates to prices

The discount rate is one route. Four more work at the same time.

1. Borrowing costs. Higher rates raise the interest a company pays on floating-rate debt and on new borrowing, which lowers profit. Part 9 covered debt ([Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md)).
2. Customers. Mortgages, car loans and credit cards cost more, so spending on big items can slow.
3. Competition from bonds. When a safe Treasury pays more, stocks must offer more to attract money.
4. The dollar. Higher US rates tend to attract money into dollar assets, which can strengthen the dollar. Lesson 11 and Part 17 cover this.

Rates also change the outlook for profit. If the Fed raises rates because the economy is strong, profit forecasts may rise at the same time as the discount rate. This is why the net effect of a rate change on stocks has no fixed sign. Lesson 8 shows how markets sort it out.

## Common mistakes

- Using the same rate for every cash flow. A rate rise hurts distant cash more. Discount each year on its own.
- Expecting every stock to fall when rates rise. A company with cash due soon, or with profits that rise with the economy, can hold up.
- Mixing nominal and real rates. A 4% rate with 3% inflation is a real rate near 1%. Compare like with like.

## Try it

1\. Discount US$100 due in 5 years at 4%.

<details class="solution" markdown>
<summary>Answer</summary>

PV = 100 / 1.04^5 = US$82.19.

</details>

2\. The same US$100 is due in 5 years, and the discount rate rises to 5%. What is the PV, and what is the percentage change from the answer to exercise 1?

<details class="solution" markdown>
<summary>Answer</summary>

PV = 100 / 1.05^5 = US$78.35. Change = 78.35 / 82.19 - 1 = -4.7% (rounded to one decimal).

</details>

3\. Stock C pays US$50 in year 2 and US$50 in year 4. Discount at 5%.

<details class="solution" markdown>
<summary>Answer</summary>

50 / 1.05^2 + 50 / 1.05^4 = 45.35 + 41.14 = US$86.49.

</details>

4\. Stock B's PV fell 25.0% in the example and Stock A's fell 8.0%. Which one is more sensitive to the discount rate, and why?

<details class="solution" markdown>
<summary>Answer</summary>

Stock B, because its cash comes in year 10. The divisor (1+r)^10 changes more with r than (1+r)^1 to (1+r)^5.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | In a spreadsheet, discount a US$100 payment at 2%, 4%, 6% and 8% for 1, 5 and 10 years. Write the 12 present values in a grid. |
| 3 | Find the largest drop in the grid and say which cell it is. |
| 2 | Log in your [trade journal](../practice/trade-journal.md) one stock you hold or watch, and write whether its profits are mostly near or far away. |

</div>

## Key terms

- **Discount rate**: the yearly rate used to convert future cash into present value.
- **Present value (PV)**: what a future cash flow is worth today at a given discount rate.

Next: [Inflation reports: CPI, PCE and PPI](04-inflation-reports.md)
