# LTCM and the dot-com bubble

<span class="tag tag-case">Case study</span> <span class="tag tag-part">HIST</span>

After this lesson you can show how leverage turns a small spread move into a large equity loss, say what the 1998 LTCM rescue did and did not involve, and test a high valuation by working out the growth it needs.

Before this: [1929 and 1987](01-1929-and-1987.md), [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md). You need: a calculator.

## The idea

Long-Term Capital Management (LTCM) was a US hedge fund, a private fund for wealthy and institutional investors. In 1998 it lost almost 90% of its capital in nine months and was recapitalized by its lenders. The dot-com bubble, a few years later, is a different kind of failure: prices that needed years of growth that did not come, and research that was not independent. Together they show two risks: borrowed money, and a price that assumes too much.

## LTCM, 1998

The numbers below come from the US Government Accountability Office report on LTCM, written for Congress in 1999 ([GAO-00-3](https://www.govinfo.gov/content/pkg/GAOREPORTS-GGD-00-3/html/GAOREPORTS-GGD-00-3.htm), as of 2026).

- It lost US$1.8 billion in August 1998 alone, and between January and September 1998 lost almost 90% of its capital.
- Its simple balance sheet leverage, assets divided by capital, was about 28 to 1 in its year-end 1997 statement. GAO's table shows large investment banks at the time between 22 to 1 and 34 to 1, so the ratio alone was not unusual for a bank, though it was for a hedge fund.
- It also held about US$1.4 trillion of derivatives contracts (by notional, the face amount the contract refers to) off its balance sheet. GAO says notional is not a measure of actual risk.
- Most of the balance sheet was government bonds of major countries. LTCM also used repurchase agreements, short sales and loans, and negotiated terms such as zero initial margin with its lenders.

The trades were mostly **convergence trades**: buy a cheaper bond, sell short a similar, more expensive one, and wait for the gap to close. Each trade earns little, so a fund needs leverage to make it worthwhile. That also makes it fragile.

<div class="example" markdown>

### Worked example: a spread widens

This uses made-up numbers. A fund has US$100 million of equity. It buys US$2,000 million of Bond X and sells short US$2,000 million of Bond Y, a similar bond. Both have a duration of 10 years (lesson 4 of part 12: a 1 basis point change in yield changes the price by about 10 x 0.01%). The yield gap, or **spread**, between X and Y is 20 basis points, and the fund expects it to close to 0.

1. The long side is US$2,000 million on US$100 million of equity, so leverage is 20 to 1.
2. Each 1 basis point change in the spread is worth about 2,000 million x 10 x 0.0001 = US$2.0 million.
3. If the spread closes by 20 basis points, the fund makes about US$40 million, which is 40% of its equity.
4. If instead it widens 15 basis points to 35, the fund loses about US$30 million, which is 30% of its equity.
5. At 28 to 1, a 1% fall in asset value costs 28% of equity, and a 3.57% fall (100 / 2,800) removes all of it.

A move that is small on an unleveraged portfolio is a large loss here.

</div>

The figure shows loss of equity against the fall in asset value for four leverage levels. Look at where each line reaches 100%.

![Loss of equity against the fall in asset value for 1, 10, 28 and 40 to 1 leverage: the 28 to 1 line reaches 100% at a 3.6% fall](../assets/figures/21-crashes-scams-and-case-studies/ltcm-leverage-dark.svg#only-dark)
![Loss of equity against the fall in asset value for 1, 10, 28 and 40 to 1 leverage: the 28 to 1 line reaches 100% at a 3.6% fall](../assets/figures/21-crashes-scams-and-case-studies/ltcm-leverage-light.svg#only-light)

### The rescue

By mid-September 1998 LTCM was close to failure. The Federal Reserve decided that a rapid sale of its positions, and of related positions at other firms, in already unsettled markets might cause some markets to stop working for a while, so it helped arrange a rescue. On September 23, 1998, 14 banks and brokerage firms agreed to put US$3.625 billion into the fund in exchange for 90% of its ownership. The Federal Reserve Bank of New York brought the firms together but did not put its own money in; creditors supplied the capital ([Federal Reserve History, Near Failure of Long-Term Capital Management](https://www.federalreservehistory.org/essays/ltcm-near-failure), as of 2026).

GAO's main finding was about the lenders: LTCM's leverage grew mainly because its creditors did not enforce their own risk standards, and regulators had relied on them to police the fund.

## The dot-com bubble

In the late 1990s, prices of internet and technology companies rose far above what their profits supported, and many new companies sold shares to the public for the first time in **initial public offerings** (IPOs). The risk here is not leverage. It is paying a price that needs years of fast growth to be worth paying.

<div class="example" markdown>

### Worked example: what a price needs

Stock B (made-up) has revenue of US$100 million and a market cap of US$5,000 million, which is 50 times its sales ([Price multiples](../10-valuation-and-research/01-multiples.md)). Suppose that, at maturity, the company earns a 20% net margin and the market then pays 15 times earnings.

1. For the market cap to still be US$5,000 million at maturity, net income must be 5,000 / 15 = US$333.3 million.
2. At a 20% margin, that needs revenue of 333.3 / 0.20 = US$1,666.7 million, which is 16.7 times today's revenue.
3. At 25% revenue growth a year, 16.7 times takes ln(16.67) / ln(1.25) = 12.6 years.

This ignores the time value of money, which makes the answer worse. Even if everything goes right, a buyer who pays US$5,000 million today owns a company worth US$5,000 million after 12.6 years, with no gain. Part 10 turns this into a full test ([Reverse DCF and expectations](../10-valuation-and-research/06-reverse-dcf-and-expectations.md)).

</div>

### Research and the IPO market

On April 28, 2003, the SEC, the NYSE, the NASD, the New York Attorney General and state regulators announced settlements with ten firms. Regulators alleged that from about mid-1999 through mid-2001 the firms let investment banking influence their research analysts, without managing the resulting conflicts. Some firms were also alleged to have issued fraudulent research, and two to have misallocated shares in hot IPOs. The firms neither admitted nor denied the allegations. The payments totalled about US$1.4 billion: US$487.5 million in penalties, US$387.5 million in disgorgement, US$432.5 million to fund independent research and US$80 million for investor education ([SEC press release 2003-54](https://www.sec.gov/news/press/2003-54.htm), as of 2026).

## The risk lesson for you

Leverage is a bet on how big a move you can survive, not on direction. Before using margin or a leveraged product, work out the fall that wipes you out. For valuation, ask what the price assumes about growth, and who is paid when you buy: a research note from a firm that also sells the shares is not independent.

## Common mistakes

- Judging risk from a convergence trade's average return. Small steady gains hide a rare large loss.
- Reading "the Fed rescued LTCM" as a taxpayer bailout. The Fed's role was convening the lenders, who supplied the capital.
- Buying more because a high multiple keeps rising. The multiple is the thing to explain.

## Try it

1\. A fund has US$50 million of equity and US$1,000 million of assets. What is its leverage, and what fall in assets removes its equity?

<details class="solution" markdown>
<summary>Answer</summary>

Leverage = 1,000 / 50 = 20 to 1. A fall of 50 / 1,000 = 5% removes the equity.

</details>

2\. In the worked example, the spread widens 8 basis points. What is the loss?

<details class="solution" markdown>
<summary>Answer</summary>

2,000 million x 10 x 0.0008 = US$16 million, which is 16% of US$100 million.

</details>

3\. GAO says LTCM lost almost 90% of its capital between January and September 1998. Taking exactly 90%, what gain on the remaining capital gets back to the start?

<details class="solution" markdown>
<summary>Answer</summary>

The remaining capital is 10% of the start. The gain needed is 1 / 0.10 - 1 = 9, which is 900%.

</details>

4\. Stock B in the example grows revenue at 40% a year instead of 25%. How many years to reach 16.7 times today's revenue?

<details class="solution" markdown>
<summary>Answer</summary>

ln(16.67) / ln(1.40) = 2.814 / 0.3365 = 8.4 years.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a US stock you follow. Find its market cap and last-year revenue, then work out the price-to-sales ratio and the growth years it needs to reach a 15 times earnings price at a 20% margin. |
| 4 | Open GAO-00-3 (link above) and read the first two pages of the Results in Brief. Write one sentence on who GAO says should have limited LTCM's leverage. |
| 2 | In your [trade journal](../practice/trade-journal.md), write the largest loss you could take today if every position fell 4%, and whether you could survive it. |

</div>

## Key terms

- **Hedge fund**: a private investment fund open to wealthy and institutional investors, with fewer restrictions than a mutual fund.
- **Convergence trade**: a long and a short position in similar assets, betting that their price gap will close.
- **Spread**: the gap between two yields, in basis points.
- **Notional**: the face amount a derivatives contract refers to, which is not the amount at risk.
- **Initial public offering (IPO)**: a company's first sale of shares to the public.
- **Disgorgement**: repayment of profits made from conduct a regulator found wrongful.

Next: [The 2008 financial crisis](03-the-2008-crisis.md)
