# Bond ETFs, and rates against stocks

<span class="tag tag-idea">Idea</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">BOND</span>

After this lesson you can read a bond ETF's yield and duration figures, say why it has no maturity date, estimate its first-year return after a rate change, and compare a stock market's earnings yield with a bond yield without over-reading the result.

Before this: [Bond prices and yields](01-bond-prices-and-yields.md), [Duration and convexity](04-duration-and-convexity.md), [Credit spreads and high yield](05-credit-spreads-and-high-yield.md). You need: a calculator.

## The idea

Individual bonds are hard to buy in small amounts and in variety. A **bond ETF** is a fund that holds hundreds or thousands of bonds and sells shares that trade on an exchange like a stock. Part 13 covers how an ETF is built ([How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md)). Here we need only what a bond ETF reports.

### What the fund page tells you

| Figure | What it is | Use it to |
|---|---|---|
| 30-day SEC yield | A standard yield the SEC requires funds to compute: net income per share over the last 30 days, after fund expenses, divided by the share price and annualized | Compare funds on the same basis |
| Distribution yield | The distributions paid over the last 12 months divided by the price | See what the fund paid. It looks backward |
| Yield to maturity | The weighted average yield to maturity of the holdings, as in lesson 1 | See what the portfolio would earn if every bond were held to maturity and none defaulted |
| Effective duration | The duration of the whole portfolio, in years, as in lesson 4 | Estimate the price change for a yield change |
| Average maturity | The weighted average time to maturity of the holdings | Gauge how long the bonds are |
| Expense ratio | The yearly fee, as a percentage of assets | Subtract it from the yield |

The SEC yield formula is set out in [Form N-1A](https://www.sec.gov/files/formn-1a.pdf), the fund registration form. Effective duration allows for bonds that can be repaid early. Here it works like modified duration.

### Why a bond ETF has no maturity date

A single bond comes back to face value on a known date. A bond ETF doesn't. The fund follows an index or a rule, and when a bond nears maturity (many indexes drop bonds with under a year left; check the fund's index rules), the fund sells it and buys another. The portfolio keeps roughly the same duration, and the fund never matures. You cannot wait for par. When you sell, you get the market price, so if yields have risen since you bought, you take the loss unless higher income has made it up.

## How it works

The price move and the income both matter over a holding period. The figures needed are the ETF's yield and effective duration. The estimate for a one-year holding is:

\[ R \approx y - D_{eff} \times \Delta y \]

- \(R\) is the approximate return over the year, as a fraction.
- \(y\) is the yield (use the ETF's yield to maturity or its SEC yield), as a fraction.
- \(D_{eff}\) is the effective duration, in years.
- \(\Delta y\) is the change in yield over the year, as a fraction.

It ignores convexity, spread changes and fees, so it is rough.

<div class="example" markdown>

### Worked example: a rate rise and a bond ETF

Bond Fund X is made up. Its price is US$80.00, its yield is 4.50% and its effective duration is 6.0 years.

1. Yields rise 1.00 percentage point. Price change: -6.0 x 0.01 = -6.0%, or -US$4.80, so the price falls to US$75.20.
2. Income over the year: 4.50% of US$80.00 = US$3.60.
3. Total: -4.80 + 3.60 = -US$1.20, or -1.5% of the starting price.
4. The break-even rise in yield, where income exactly offsets the price loss, is 4.50 / 6.0 = 0.75 percentage points. A smaller rise leaves a positive year, and a larger one a loss.

If yields fall 1.00 point instead, the estimate is +6.0% + 4.5% = +10.5%.

</div>

This is the lesson of 2022, when yields rose quickly and bond funds with long duration fell sharply. Part 21 covers it (The 2022 rate shock<!-- link: ../21-crashes-scams-and-case-studies/07-the-2022-rate-shock.md -->).

### Rates against stocks

Higher bond yields compete with stocks for money and raise the discount rate used to value stocks (part 10). A stock investor expects a higher return than a bond investor. The extra is the **equity risk premium** ([Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md) defines it and says where to find estimates). It can't be observed, only estimated.

A common quick comparison uses the **earnings yield**: a company's (or an index's) earnings divided by its price, which is the inverse of the price-to-earnings ratio.

\[ \text{Earnings yield} = \frac{E}{P} = \frac{1}{P/E} \]

- \(E\) is earnings per share, in US$.
- \(P\) is the price per share, in US$.

<div class="example" markdown>

### Worked example: earnings yield against a bond yield

A made-up stock index trades at a P/E ratio of 20, and the 10-year Treasury yields 4.00% (made up).

1. Earnings yield = 1 / 20 = 5.00%.
2. Gap to the bond yield: 5.00 - 4.00 = 1.00 percentage point.
3. If the index rises so its P/E is 25, the earnings yield is 1 / 25 = 4.00%, and the gap is 0.
4. If the 10-year yield rises to 5.00% with the index unchanged, the gap is also 0.

</div>

The comparison is sometimes called the Fed model, and it has limits that you should know before using it:

- A Treasury pays a fixed amount and returns face value. Earnings are not fixed. They tend to grow, and they fall in recessions. The two yields measure different things, so the gap is not a risk premium.
- Asness (2003), "Fight the Fed Model", *Journal of Portfolio Management* 30(1), 11-24, argues the comparison treats a real earnings yield and a nominal bond yield as the same kind of number, and that it fails as a forecasting tool. Read the paper before relying on the model.
- A gap of zero or less describes a valuation, not a timing signal.

Use the gap as a prompt to ask why stocks are priced as they are. Part 10's equity risk premium estimates and reverse DCF answer that better.

## In code

The yield and duration estimate for a bond fund, and the earnings yield gap.

<details class="code" markdown>
<summary>In code</summary>

```python
price, y, dur = 80.00, 0.045, 6.0
dy = 0.01
price_change = -dur * dy * price
income = y * price
print(round(price_change, 2), round(income, 2), round(price_change + income, 2))  # -4.8 3.6 -1.2
print(round(100 * y / dur, 2))                                                   # break-even rise, 0.75

pe, bond_yield = 20, 0.04
print(round(100 * (1 / pe - bond_yield), 2))                                     # gap, 1.0
```

</details>

## Common mistakes

- Using the distribution yield as the expected return. It looks back.
- Waiting for a bond ETF to return to par like a bond. It has no maturity, so there is no date when its price must come back.
- Reading an earnings yield above the bond yield as proof that stocks are cheap. The two are not the same kind of number.

## Try it

1\. Bond Fund X (price US$80.00, yield 4.50%, effective duration 6.0) sees yields fall 0.50 percentage points over a year. Estimate its return.

<details class="solution" markdown>
<summary>Answer</summary>

Price: +6.0 x 0.005 = +3.0%. Income: 4.5%. Total about +7.5%.

</details>

2\. Why does a bond ETF's 30-day SEC yield suit comparing two funds better than their distribution yields?

<details class="solution" markdown>
<summary>Answer</summary>

Every fund computes it the same way, from the last 30 days of income after expenses. A distribution yield looks back 12 months and can include other payments.

</details>

## Part check

1\. Bond A has a 4% coupon, face value US$1,000 and 10 years to maturity. Its yield rises from 4% to 5%. What happens to the price, and why does it move that way?

<details class="solution" markdown>
<summary>Answer</summary>

It falls from US$1,000.00 to US$922.05 (-7.8%). A higher yield discounts every future payment more, so the present value is lower.

</details>

2\. A 26-week bill with US$10,000 face value sells at a 4.00% discount rate (182 days). What is its price and bond-equivalent yield?

<details class="solution" markdown>
<summary>Answer</summary>

Price = US$9,797.78. Bond-equivalent yield = 4.14%.

</details>

3\. The 10-year yield is 4.92% and the 2-year yield is 4.63%. What is the 2s10s spread, and is the curve inverted at those maturities?

<details class="solution" markdown>
<summary>Answer</summary>

4.92 - 4.63 = 0.29 percentage points. It is positive, so the curve is not inverted there.

</details>

4\. A bond yields 7.00% against a 4.00% Treasury. Its default probability is 1.5% a year and its recovery rate is 40%. What are the spread, the expected loss and the risk premium?

<details class="solution" markdown>
<summary>Answer</summary>

Spread = 3.00 percentage points (300 basis points). Expected loss = 0.015 x 0.60 = 0.90%. Risk premium = 3.00 - 0.90 = 2.10 percentage points.

</details>

5\. Why can a bond ETF's price keep falling with no date when it must recover, while a bond held to maturity returns face value?

<details class="solution" markdown>
<summary>Answer</summary>

The ETF replaces maturing bonds and never matures, so it has no date when its holdings are repaid at par. Its price is the market value of its portfolio.

</details>

6\. A stock index has a P/E of 16 and the 10-year Treasury yields 4.00%. What is the earnings yield and its gap to the bond yield? Name one limit of this gap.

<details class="solution" markdown>
<summary>Answer</summary>

Earnings yield = 1 / 16 = 6.25%. Gap = 2.25 percentage points. One limit: the bond yield is a fixed, nominal payment, while earnings grow and can fall, so the gap is not a risk premium.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Open the fund page of one bond ETF from your broker. Write its 30-day SEC yield, effective duration and expense ratio. Estimate its return if yields rise 0.5 points over a year. |
| 3 | Write the P/E ratio of a broad stock index from its fund page, compute the earnings yield, and compare it with the 10-year Treasury yield. |
| 2 | Journal one sentence ([trade journal](../practice/trade-journal.md)) on which of the two you trust less, and why. |

</div>

## Key terms

- **Bond ETF**: an exchange-traded fund that holds a portfolio of bonds.
- **30-day SEC yield**: the standardized yield funds report, from the last 30 days of income after expenses.
- **Distribution yield**: the last 12 months of distributions divided by the price.
- **Effective duration**: a portfolio's duration, allowing for bonds with early repayment features.
- **Equity risk premium**: the extra return investors expect from stocks over the risk-free rate.
- **Earnings yield**: earnings divided by price, the inverse of the P/E ratio.

Next: [How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md)
