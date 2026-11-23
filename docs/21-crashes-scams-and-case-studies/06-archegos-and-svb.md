# Archegos and SVB

<span class="tag tag-case">Case study</span> <span class="tag tag-part">HIST</span>

After this lesson you can explain how a total return swap gave Archegos stock exposure far larger than its capital, and how a bond portfolio's duration and uninsured deposits sank Silicon Valley Bank, with a number for each mechanism.

Before this: [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md), [The 2008 financial crisis](03-the-2008-crisis.md). You need: a calculator.

## The idea

Archegos failed in March 2021 and SVB in March 2023. Archegos was a private investment firm that held large stock positions through derivatives. Silicon Valley Bank (SVB) was a bank that held long-dated bonds funded by deposits it could not keep. One broke on leverage and concentration, the other on duration and funding.

## Archegos, March 2021

Archegos Capital Management was a family office, a firm that manages one family's money, run by Sung Kook (Bill) Hwang. The SEC's complaint, filed April 27, 2022, alleges that from at least March 2020 to March 2021 Hwang bought billions of dollars of **total return swaps** on margin ([SEC press release 2022-70](https://www.sec.gov/newsroom/press-releases/2022-70), as of 2026). The SEC also alleged that Archegos misled its counterparties about its exposure, concentration and liquidity, which kept its trading capacity open. These are allegations in a civil complaint. In the criminal case, a jury convicted Hwang in July 2024 of racketeering conspiracy, securities fraud, market manipulation and wire fraud, and he was sentenced to 18 years in prison ([US Attorney, Southern District of New York](https://www.justice.gov/usao-sdny/pr/founder-and-head-archegos-capital-management-bill-hwang-sentenced-18-years-prison), as of 2026).

### How a total return swap works

In a **total return swap**, a bank agrees to pay a client the gain on a stock (and its dividends) and the client agrees to pay the bank the loss, plus a financing fee. The client never owns the shares. The bank usually buys the shares to hedge, so it holds them on its own books, and the client posts **margin**, a deposit against losses.

For the client this is leverage: a small deposit controls a large stock position. For the market it hides a position: a stock held by the bank does not show as the client's holding, and if several banks hold the same stocks for one client, none sees the total.

The SEC release gives the size: Archegos grew from about US$1.5 billion in value with US$10 billion in exposure in March 2020 to more than US$36 billion in value with US$160 billion in exposure at its peak in March 2021. It says price declines in its most concentrated positions triggered margin calls Archegos could not meet, and its default caused billions of dollars of credit losses at counterparties.

![Archegos value and exposure in March 2020 and March 2021: US$1.5 billion and US$10 billion, then US$36 billion and US$160 billion](../assets/figures/21-crashes-scams-and-case-studies/archegos-exposure-dark.svg#only-dark)
![Archegos value and exposure in March 2020 and March 2021: US$1.5 billion and US$10 billion, then US$36 billion and US$160 billion](../assets/figures/21-crashes-scams-and-case-studies/archegos-exposure-light.svg#only-light)

<div class="example" markdown>

### Worked example: a margin call on a swap

Using the SEC's peak figures: exposure of US$160 billion on US$36 billion of value.

1. Exposure to value is 160 / 36 = 4.4 to 1.
2. A fall in the positions of 36 / 160 = 22.5% removes all the value.

Now a made-up position. A client holds US$100 million of swap exposure with US$20 million of margin, so the margin is 20% of exposure.

1. The stocks fall 10%. Exposure is now US$90 million and the client has lost US$10 million, leaving US$10 million of margin.
2. The bank still requires 20% of US$90 million = US$18 million, so it calls for US$8 million.
3. If the client cannot pay, the bank sells the US$90 million of shares it holds as a hedge. Selling into the same falling market pushes the price down further.
4. With several banks holding the same shares and all selling, the fall is larger than any one expected.

</div>

## SVB, March 2023

The Federal Reserve Board published a review of its supervision of SVB in April 2023, led by Vice Chair for Supervision Michael Barr ([Federal Reserve Board, Review of the Federal Reserve's Supervision and Regulation of Silicon Valley Bank, April 28, 2023](https://www.federalreserve.gov/publications/files/svb-review-20230428.pdf), as of 2026). Its numbers:

- SVB's holding company had about US$212 billion in assets, up from US$71 billion in 2019.
- At the end of 2022, about 94% of its deposits were uninsured, meaning above the US$250,000 limit of deposit insurance.
- It had put a large part of its deposits into long-dated, held-to-maturity (HTM) bonds, mostly agency mortgage-backed securities with maturities of 10 years or more. The HTM portfolio's weighted-average duration was 6.2 years at the end of 2022.
- On March 8, 2023, SVB announced the sale of US$21 billion of available-for-sale securities at a US$1.8 billion after-tax loss, and a plan to raise US$2.25 billion of capital.
- On March 9, depositors withdrew over US$40 billion, and management expected over US$100 billion more the next day. California regulators closed the bank on March 10.

### Duration turns a rate rise into a loss

Part 12 gives the rule: price change is about minus duration times the change in yield. The Treasury's data shows the 10-year yield at 1.52% on December 31, 2021 and 3.88% on December 30, 2022, a rise of 2.36 percentage points ([US Treasury daily par yield curve rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2022), as of 2026).

<div class="example" markdown>

### Worked example: a bank with a duration of 6.2 years

This uses a made-up balance sheet, with SVB's duration. A bank has US$100 of assets: US$60 of securities with a duration of 6.2 years and US$40 of loans. Its equity is US$6.

1. Yields rise 2.36 percentage points. The securities lose about 6.2 x 2.36 = 14.6% of their value.
2. The loss is 60 x 0.146 = US$8.78. That is more than the US$6 of equity.
3. The equity is gone at a rise of 6 / (60 x 6.2 / 100) = 1.61 percentage points.

While the bank holds the bonds, the loss is on paper. If depositors take out 20% of deposits, the bank must sell securities and the loss becomes real. Uninsured depositors who see this have a reason to leave first.

</div>

![Loss on a bond portfolio with a 6.2-year duration against a bank's equity: equity is gone at a 1.61 point rise in yields](../assets/figures/21-crashes-scams-and-case-studies/bank-duration-dark.svg#only-dark)
![Loss on a bond portfolio with a 6.2-year duration against a bank's equity: equity is gone at a 1.61 point rise in yields](../assets/figures/21-crashes-scams-and-case-studies/bank-duration-light.svg#only-light)

## The risk lessons for you

Archegos: exposure matters more than capital, and a derivative position can be larger than your account shows. If you use margin or leveraged products, add up the exposure and divide by the money you could lose.

SVB: a safe bond is safe from default, not from price changes. Check the duration of any bond fund you hold ([Bond ETFs and rates versus stocks](../12-bonds-and-the-yield-curve/06-bond-etfs-and-rates-vs-stocks.md)), and read where your cash is held and who protects it (lesson 9).

## Common mistakes

- Reading allegations as findings. The SEC's complaint is an allegation; the verdict and sentence are the court's findings.
- Calling a bond risk-free because it pays at maturity. It can lose value before then, and a forced sale makes the loss real.
- Counting only the account balance. Exposure divided by capital is the number to know.

## Try it

1\. A fund has US$5 billion of capital and US$30 billion of exposure. What is its leverage, and what fall in the positions removes its capital?

<details class="solution" markdown>
<summary>Answer</summary>

Leverage = 30 / 5 = 6 to 1. A fall of 5 / 30 = 16.7% removes the capital.

</details>

2\. A swap position has US$50 million of exposure and US$10 million of margin. The stocks fall 10%. If the bank requires 20% margin on the new exposure, how much does it call for?

<details class="solution" markdown>
<summary>Answer</summary>

Loss = US$5 million, so US$5 million of margin is left. New exposure is US$45 million, and 20% of that is US$9 million. The call is 9 - 5 = US$4 million.

</details>

3\. A bond portfolio has a duration of 6.2 years and yields rise 1.00 percentage point. What is the approximate fall in value?

<details class="solution" markdown>
<summary>Answer</summary>

6.2 x 1.00 = 6.2%.

</details>

4\. A bank has US$80 of securities with a duration of 5 years and US$4 of equity per US$100 of assets. What rise in yields removes the equity?

<details class="solution" markdown>
<summary>Answer</summary>

The loss per percentage point is 80 x 5 / 100 = US$4.00 per US$100 of assets. The equity of US$4 is gone at a rise of 4 / 4.00 = 1.0 percentage point.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the effective duration of one bond ETF you know on the issuer's page. Work out the fall for a 1 point rise in yields. |
| 4 | Open the Barr report (link above) and read the one-page executive summary. Write what it says about SVB's deposits and its bond portfolio. |
| 2 | In your [trade journal](../practice/trade-journal.md), write your largest total exposure through margin, options or leveraged ETFs, divided by your account value. |

</div>

## Key terms

- **Family office**: a firm that manages the wealth of one family.
- **Total return swap**: a contract where one side pays the price gain and dividends on a stock and the other pays the loss plus a fee.
- **Margin (swap)**: a deposit the client posts against the losses on a swap.
- **Concentration**: holding a large share of a portfolio in a few positions.
- **Held-to-maturity (HTM)**: a bond accounting category carried at cost because the bank intends to hold the bond to maturity.
- **Uninsured deposit**: a deposit above the deposit insurance limit.
- **Bank run**: many depositors withdrawing at once.

Next: [The 2022 rate shock](07-the-2022-rate-shock.md)
