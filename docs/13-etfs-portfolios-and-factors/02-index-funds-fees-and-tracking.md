# Index funds, fees and tracking

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">ETF</span>

After this lesson you can work out what a fee costs over 30 years, measure how well a fund follows its index with tracking difference and tracking error, and add the spread to the cost of owning an ETF.

Before this: [How ETFs work](01-how-etfs-work.md). The math book's [Index funds, fees and dollar-cost averaging](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/02-index-funds-fees-and-dollar-cost-averaging/) works the fee formula; this lesson uses it and adds tracking and the spread. You need: a calculator.

## The idea

An **index fund** holds the stocks of an index in the index's proportions, so it earns the index's return minus its costs. It makes no forecast. The index (a market-cap-weighted one, from [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md)) sets the holdings, and the fund's job is to copy it. An index ETF is an index fund that trades on an exchange.

If every index fund holds the same stocks, the differences between them are costs and how well each one copies. Those are the three numbers to compare: the fee, the tracking and the spread.

## The fee

The **expense ratio** is the yearly fee as a percentage of the fund's assets, taken out of the fund's returns a little each day, so you never see a bill. In Canada the same number is the **management expense ratio** (MER). Compare two made-up funds that hold the same index, which earns 7% a year before costs. Fund Low charges 0.10%, Fund Mid charges 1.00% and Fund High charges 2.25%. Starting with US$10,000:

\[ V_{30} = V_0 \, (1 + g - f)^{30} \]

- \(V_0\) is the starting amount, US$10,000.
- \(g\) is the yearly return before fees, 0.07.
- \(f\) is the expense ratio as a fraction, for example 0.001 for 0.10%.
- \(V_{30}\) is the value after 30 years, in US$.

<div class="example" markdown>

### Worked example: a fee over 30 years

1. No fee: 10,000 x 1.07^30 = US$76,122.55.
2. Fund Low: 10,000 x 1.069^30 = US$74,016.95. The fee cost US$2,105.61.
3. Fund Mid: 10,000 x 1.06^30 = US$57,434.91. The fee cost US$18,687.64, which is 24.5% of the no-fee ending value.
4. Fund High: 10,000 x 1.0475^30 = US$40,236.57.

A 1.00% fee looks like 1 point out of 7. It takes about a quarter of the final value, because the fee comes out every year and the money it removes would also have compounded.

</div>

The figure shows the three paths. Look at how the gap between them grows faster in the late years, when the balance is largest.

![Growth of US$10,000 over 30 years at 7% before fees, with fees of 0%, 0.10%, 1.00% and 2.25%](../assets/figures/13-etfs-portfolios-and-factors/fee-drag-dark.svg#only-dark)
![Growth of US$10,000 over 30 years at 7% before fees, with fees of 0%, 0.10%, 1.00% and 2.25%](../assets/figures/13-etfs-portfolios-and-factors/fee-drag-light.svg#only-light)

The 7% is made up. The point holds for any return: a fee is a certain cost, and a return is not.

## Tracking

A fund does not earn exactly the index's return. It pays its fee, holds a little cash, buys and sells to follow changes in the index, and may hold a sample of the index instead of every stock. Two numbers describe this.

**Tracking difference** is the fund's return minus the index's return over a period, usually a year. It is the cost you actually got, and it is roughly the fee (a little less if the fund earns income from lending its securities, or more if its trading costs are high).

**Tracking error** is the standard deviation of the fund's return minus the index's return, measured on shorter periods (monthly or daily) and scaled to a year. It says how steady the gap is. A fund can have a tracking difference of -0.20% every year with a tiny tracking error, which is a consistent fee, or a tracking difference near 0 that comes from big gaps that cancel, which is a large tracking error.

\[ TE = \sqrt{12} \times \text{sd}\left(r_{\text{fund},m} - r_{\text{index},m}\right) \]

- \(r_{\text{fund},m}\) and \(r_{\text{index},m}\) are the monthly returns in %.
- sd is the sample standard deviation of the 12 monthly differences, in percentage points.
- \(\sqrt{12}\) scales monthly to yearly, assuming the monthly gaps are independent.

<div class="example" markdown>

### Worked example: tracking difference and error

Fund Z (made up) has a 0.20% expense ratio. Its monthly returns and its index's, in %:

| Month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Index | 1.20 | -0.80 | 2.10 | 0.50 | -1.50 | 1.90 | 0.70 | -0.30 | 1.10 | 2.40 | -2.00 | 0.90 |
| Fund Z | 1.18 | -0.81 | 2.07 | 0.50 | -1.52 | 1.89 | 0.66 | -0.31 | 1.08 | 2.40 | -2.03 | 0.89 |

1. Compound each series. The index returns 6.26% and the fund returns 6.05%.
2. Tracking difference = 6.05 - 6.26 = -0.21%. This is close to the 0.20% fee.
3. The monthly differences are -0.02, -0.01, -0.03, 0.00, and so on. Their standard deviation is 0.0123 percentage points.
4. Tracking error = 0.0123 x sqrt(12) = 0.04% a year.

The fund follows its index closely and steadily. A fund with the same -0.21% but a tracking error of 0.5% would be surprising you each month.

</div>

## The spread

You also pay when you trade. The ETF has a bid and an ask ([Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)). If you buy at the ask and sell at the bid, a round trip costs the whole **bid-ask spread**. A made-up ETF is quoted US$40.00 bid and US$40.04 ask. The spread is US$0.04, and the midpoint is US$40.02, so the spread is 0.04 / 40.02 = 0.10% of the price. On US$10,000 a round trip costs about US$10.00.

Over 30 years, a single round trip is small next to the fee. Trading 12 round trips a year is 12 x 0.10% = 1.2% a year, which is more than the fee of most index ETFs. Large ETFs of liquid stocks often have spreads of a cent or two, but the spread is a number you can see at the moment you trade, so look at it each time.

<div class="canada" markdown>

### For Canadians

A Canadian fund's MER includes its management fee, its operating costs and sales tax (GST or HST), as a percentage of assets. Its trading costs are reported separately as a trading expense ratio, so the full cost of owning is a little above the MER. Fund fact sheets define both numbers; read them. For real funds, quote the figure only from the issuer's page with the date (as of 2026), and compare tracking difference over several years, which is the cost you actually paid.

</div>

## In code

Compute the tracking difference and error from two lists of monthly returns.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

index = np.array([1.2, -0.8, 2.1, 0.5, -1.5, 1.9, 0.7, -0.3, 1.1, 2.4, -2.0, 0.9])
fund = np.array([1.18, -0.81, 2.07, 0.5, -1.52, 1.89, 0.66, -0.31, 1.08, 2.4, -2.03, 0.89])

annual = lambda r: np.prod(1 + r / 100) - 1
print("tracking difference %", round(100 * (annual(fund) - annual(index)), 2))
print("tracking error %", round(np.std(fund - index, ddof=1) * 12 ** 0.5, 2))
```

</details>

## Common mistakes

- Comparing the MER alone. The spread, the tracking and the currency cost (lesson 3) can matter as much.
- Judging tracking from one year. A fund can be ahead or behind its index by luck of timing, so compare several years.
- Reading a low tracking error as a low cost. Tracking error says the gap is steady, and the tracking difference says how big it is.

## Try it

1\. An index returns 6% a year before costs. A fund charges 0.25%. What is US$20,000 worth after 20 years? Round to the dollar.

<details class="solution" markdown>
<summary>Answer</summary>

20,000 x (1 + 0.06 - 0.0025)^20 = 20,000 x 1.0575^20 = US$61,184 (rounded).

</details>

2\. The same index at no fee gives 20,000 x 1.06^20. How much did the fee cost?

<details class="solution" markdown>
<summary>Answer</summary>

20,000 x 1.06^20 = US$64,142.71. The fee cost 64,143 - 61,184 = US$2,959 (the unrounded values give the same).

</details>

3\. A fund returned 9.40% and its index returned 9.65% over a year. What is the tracking difference?

<details class="solution" markdown>
<summary>Answer</summary>

9.40 - 9.65 = -0.25%.

</details>

4\. An ETF is quoted US$25.10 bid and US$25.14 ask. What is the spread as a percentage of the midpoint, and what does a round trip on US$5,000 cost?

<details class="solution" markdown>
<summary>Answer</summary>

Spread = 0.04. Midpoint = 25.12. Spread % = 0.04 / 25.12 = 0.16%. On US$5,000 a round trip costs 5,000 x 0.0016 = about US$8.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick an index ETF you know. On the issuer's page, write its expense ratio or MER and its 5-year fund and index returns. Compute the 5-year tracking difference. |
| 3 | Write the live bid and ask of that ETF and compute the spread as a percentage. |
| 3 | Compute what a 1% fee would cost on your own portfolio over 30 years using the formula above. |

</div>

## Key terms

- **Index fund**: a fund that holds an index's stocks in the index's proportions.
- **Expense ratio**: the yearly fund fee as a percentage of assets.
- **Management expense ratio (MER)**: the Canadian name for the expense ratio, which includes sales tax.
- **Tracking difference**: the fund's return minus its index's return over a period.
- **Tracking error**: the standard deviation of the fund's return minus the index's return, scaled to a year.
- **Bid-ask spread**: the ask price minus the bid price, which a round trip costs.

Next: [US-listed or Canadian-listed ETFs](03-us-vs-canadian-listed-etfs.md)
