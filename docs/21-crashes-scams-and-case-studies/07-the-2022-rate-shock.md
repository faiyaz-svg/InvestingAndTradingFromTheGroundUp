# The 2022 rate shock

<span class="tag tag-case">Case study</span> <span class="tag tag-part">HIST</span>

After this lesson you can describe how fast US interest rates rose in 2022, work out the price fall of a bond for a given rise in yields using duration and convexity, and say why higher rates also lower the value of stocks that pay far in the future.

Before this: [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md), [Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md). You need: a calculator.

## The idea

After 2008 the Federal Reserve held short-term rates near zero for years (lesson 3), and it cut them to zero again in March 2020 (lesson 4). In 2022 inflation rose, and the Fed raised its target range from 0 to 1/4 percent to 4 1/4 to 4 1/2 percent between March and December. Existing bonds, which pay fixed coupons, fell in price. The mechanism is the same duration arithmetic as in part 12, applied to the whole market.

## What happened

| Item | Number | Source |
|---|---|---|
| 12-month CPI inflation, June 2022 | 9.1%, the largest 12-month increase since the period ending November 1981 | [BLS CPI release, July 13, 2022](https://www.bls.gov/news.release/archives/cpi_07132022.htm) |
| Fed target range, March 16, 2022 | raised to 1/4 to 1/2 percent | [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm) |
| Fed target range, December 14, 2022 | raised to 4 1/4 to 4 1/2 percent | [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm) |
| 3-month Treasury yield | 0.06% on Dec 31, 2021; 4.42% on Dec 30, 2022 | US Treasury |
| 2-year Treasury yield | 0.73% to 4.41% | US Treasury |
| 10-year Treasury yield | 1.52% to 3.88% | US Treasury |

The Treasury figures are from its daily par yield curve rates ([US Treasury](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2022), as of 2026). The figure draws them for 2022.

![US Treasury 3-month, 2-year and 10-year yields through 2022: the 3-month rises from 0.06% to 4.42%, the 2-year from 0.73% to 4.41% and the 10-year from 1.52% to 3.88%](../assets/figures/21-crashes-scams-and-case-studies/treasury-2022-dark.svg#only-dark)
![US Treasury 3-month, 2-year and 10-year yields through 2022: the 3-month rises from 0.06% to 4.42%, the 2-year from 0.73% to 4.41% and the 10-year from 1.52% to 3.88%](../assets/figures/21-crashes-scams-and-case-studies/treasury-2022-light.svg#only-light)

Source: US Treasury, daily par yield curve rates, downloaded November 21, 2026 (US public domain). Look at the order: the short end rose first and furthest. The 10-year yield peaked at 4.25% on October 24 and the 2-year at 4.72% on November 7. By December 30 the 2-year yield (4.41%) was above the 10-year (3.88%), an inverted curve ([The yield curve](../12-bonds-and-the-yield-curve/03-the-yield-curve.md)).

## How a rate rise hits a bond

The price of a bond is the present value of its payments, so a higher yield means a lower price. Part 12 shows the estimate

\[ \frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \tfrac{1}{2}\, C\, (\Delta y)^2 \]

- \(\Delta P / P\) is the percent change in price, as a fraction.
- \(D_{mod}\) is modified duration, in years.
- \(\Delta y\) is the change in yield, as a fraction (2.36 percentage points is 0.0236).
- \(C\) is convexity, in years squared.

<div class="example" markdown>

### Worked example: a 10-year bond through 2022

Bond B (made-up) is a 10-year bond with a 1.52% coupon, paid twice a year, priced at par (US$100) when the market yield is 1.52%. Over the year the yield rises to 3.88%, a rise of 2.36 percentage points.

1. Repricing at 3.88%: the price is US$80.59, a fall of 19.4%.
2. Its modified duration is 9.24 years and convexity is 94.0. The duration-only estimate is -9.24 x 0.0236 = -21.8%.
3. Adding convexity: +0.5 x 94.0 x 0.0236^2 = +2.6%, which gives -19.2%, close to the exact -19.4%.

The coupon paid US$1.52 a year, so over the year the holder gets about 1.5% back, and the total loss is still about 18%. A holder who sells at the low locks it in. A holder who keeps the bond gets US$100 at maturity, and meanwhile earns a low coupon while new bonds pay 3.88%.

</div>

Duration is the reason longer bonds fell more. A 2-year bond has a duration near 2, so the same 2.36 point rise would cost about 4.7%, not 21.8%. SVB (lesson 6) held a portfolio with a duration of 6.2 years.

## How it hits a stock

A stock's value is the present value of its future cash. Part 10 covers the discount rate. A higher rate lowers the value of cash far in the future more than cash soon.

<div class="example" markdown>

### Worked example: a stock and its discount rate

Stock A (made-up) is expected to pay US$3.00 next year, growing 4% a year forever. The value is next year's cash divided by (r - g), where r is the discount rate and g the growth rate.

1. At r = 7%: 3.00 / (0.07 - 0.04) = US$100.
2. At r = 9%: 3.00 / (0.09 - 0.04) = US$60.
3. A rise of 2 percentage points in the discount rate cuts the value by 40%, with no change in the company's cash.

A company that pays most of its cash soon is less affected. This is a model, so the real fall also depends on what investors expect for growth, and the discount rate does not rise one for one with Treasury yields. It shows the direction and the size of the sensitivity.

</div>

## What else changed

Margin interest and borrowing costs rose with the Fed's rate, so a leveraged position cost more to hold. Cash also paid: a 3-month Treasury bill yielded 4.42% on December 30, 2022, against 0.06% a year earlier, so holding cash was no longer free of return.

## The risk lesson for you

Rates are a risk factor in every portfolio, and bonds are one part of it. List what in your accounts is sensitive: long-duration bonds and bond ETFs, stocks priced for growth far ahead, leveraged positions with floating borrowing costs, and cash plans. Part 12 gives you the tool: look up a bond fund's duration and multiply by a rate move you can imagine, such as 2 percentage points.

## Common mistakes

- Treating a rise in yield as a gain because new bonds pay more. The price fall is immediate; the extra income arrives over years.
- Using the 10-year yield for every bond. A 2-year and a 10-year bond move by different amounts for the same yield change.
- Assuming a bond fund has no price risk because the bonds are government bonds. Default risk is low; duration risk is not.

## Try it

1\. A bond fund has a modified duration of 6 years. Yields rise 1.5 percentage points. What is the approximate price fall?

<details class="solution" markdown>
<summary>Answer</summary>

6 x 1.5 = 9%.

</details>

2\. Bond B's yield instead rises from 1.52% to 2.52% (1 percentage point). What is the duration-only estimate of its price change?

<details class="solution" markdown>
<summary>Answer</summary>

-9.24 x 0.01 = -9.2%. With convexity, +0.5 x 94.0 x 0.01^2 = +0.47%, so about -8.8%.

</details>

3\. The 10-year yield rose from 1.52% to 3.88%. How many basis points?

<details class="solution" markdown>
<summary>Answer</summary>

3.88 - 1.52 = 2.36 percentage points, which is 236 basis points.

</details>

4\. In the stock example, the discount rate is 8%. What is the value, and the fall from US$100?

<details class="solution" markdown>
<summary>Answer</summary>

3.00 / (0.08 - 0.04) = US$75, a fall of 25%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Look up today's 2-year and 10-year Treasury yields on the Treasury's site. Write the spread and whether the curve is inverted. |
| 4 | Find the effective duration of a bond ETF you know. Write the price change for a 1 point rise and a 1 point fall. |
| 2 | In your [trade journal](../practice/trade-journal.md), write which of your holdings would lose value if the 10-year yield rose 1 point. |

</div>

## Key terms

- **Inflation**: a general rise in prices, measured here by the consumer price index (CPI).
- **Federal funds target range**: the range the Fed sets for its overnight lending rate between banks.
- **Rate shock**: a fast, large change in interest rates.
- **Inverted yield curve**: short-term yields above long-term yields.
- **Discount rate**: the rate used to turn future cash into a present value.

Next: [Pump and dumps, finfluencers and signal groups](08-pump-and-dumps-finfluencers-and-signal-groups.md)
