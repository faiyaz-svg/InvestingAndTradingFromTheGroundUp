# US-listed or Canadian-listed ETFs

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ETF</span>

After this lesson you can compare a US-listed and a Canadian-listed ETF for the same exposure by counting the withholding tax in each account type and the cost of converting currency, and say what an all-in-one ETF is.

Before this: [Index funds, fees and tracking](02-index-funds-fees-and-tracking.md), [US withholding tax and the W-8BEN](../02-accounts-currency-and-taxes/06-us-withholding-tax-and-w-8ben.md), [Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md). You need: a calculator.

## The idea

You want a fund of US large companies. A US-listed ETF trades in US$ on a US exchange. A Canadian-listed ETF trades in C$ on the TSX, and holds the same US stocks. They look alike, but they differ in two costs: how much foreign tax is taken from the dividends, and what it costs to move between Canadian and US dollars.

This lesson is education, not tax advice. The structures below come from Canadian analyses, and a fund's own tax page and your accountant decide your case. The main source is a 2016 article by Dan Bortolotti on the white paper *Foreign Withholding Taxes*, which he wrote with Justin Bender ([Canadian Couch Potato, July 11, 2016](https://canadiancouchpotato.com/2016/07/11/foreign-withholding-taxes-revisited/)). It is the most recent Canadian analysis I could read in full; the treaty rules and fund structures may have changed since, so confirm with the issuer.

## Where the tax is taken

Lesson 6 of part 2 explained that a US dividend paid to a Canadian loses 15% under the treaty, and that an RRSP is exempt. With a fund there can be a layer at the fund, and a layer at you. For US stocks:

| Structure | RRSP | TFSA or FHSA | Non-registered |
|---|---|---|---|
| US-listed ETF of US stocks | 0% withheld | 15% withheld, not recoverable | 15% withheld, recoverable as a foreign tax credit |
| Canadian-listed ETF holding US stocks directly | 15% withheld in the fund, not recoverable | 15%, not recoverable | 15%, and the fund reports the tax so you can usually claim a credit |
| Canadian-listed ETF holding a US-listed ETF | 15% withheld on what the US ETF pays the fund, not recoverable | same | same |

The article's conclusion is that in an RRSP, a US-listed ETF of US stocks avoids the withholding, which it estimated at 0.30% a year for a 2% dividend yield (15% of 2%). In a TFSA or a taxable account, a Canadian-listed ETF is generally the better choice, and the US-listed one has little or no tax advantage ([same article](https://canadiancouchpotato.com/2016/07/11/foreign-withholding-taxes-revisited/)). I could not find a CRA page that states the FHSA row, so treat it as the TFSA's, as part 2 does.

For international stocks (not US), the picture changes. A Canadian-listed fund that holds a US-listed international ETF suffers withholding twice: the foreign country takes its share inside the US fund, then the US takes 15% when the US fund pays the Canadian fund. The same article estimated a drag of 0.26% a year for a Canadian-listed fund holding international stocks directly (in an RRSP or TFSA) and 0.59% for one holding a US-listed ETF, and the second layer is not recoverable. These are 2016 estimates for two example funds, not current fees. A US-listed international ETF in an RRSP does not escape the foreign layer, so the RRSP advantage is only for US stocks.

<div class="example" markdown>

### Worked example: the withholding on one holding

You hold C$50,000 of a US stock fund (made up) with a 1.5% dividend yield.

1. Dividends in a year: 50,000 x 0.015 = C$750.
2. 15% withheld: 750 x 0.15 = C$112.50, which is 112.50 / 50,000 = 0.225% of the holding.
3. In an RRSP with a US-listed ETF: C$0 lost. With a Canadian-listed ETF that holds US stocks: C$112.50 lost a year.
4. In a TFSA, either structure loses C$112.50 a year, for a US ETF or a Canadian ETF.

</div>

## The currency cost

A US-listed ETF costs US$. If you buy it from a C$ balance, you convert. At Wealthsimple, a trade of a US-listed security in a CAD account carries a 1.5% fee on the conversion, and a USD account avoids that fee ([Wealthsimple trade fees](https://www.wealthsimple.com/legal/fees/trade), as of 2026). Part 2 has ways around the fee, such as a USD account, and [Norbert's gambit and CDRs](../02-accounts-currency-and-taxes/04-norberts-gambit-and-cdrs.md) for large amounts. A Canadian-listed ETF has no conversion at the trade. It still has currency risk: the stocks inside are priced in US$, so a fall in the US dollar lowers your C$ return unless the fund is a **hedged** version, which offsets the currency move at a cost.

<div class="example" markdown>

### Worked example: is the RRSP saving worth the conversion?

You put C$20,000 in an RRSP. The US fund yields 1.5%. Assume a flat balance for simplicity, and a 1.5% conversion fee both ways.

1. Withholding saved by the US-listed ETF: 20,000 x 0.015 x 0.15 = C$45 a year.
2. Conversion on the way in: 20,000 x 0.015 = C$300. On the way out: another C$300 (more if the balance grew).
3. Break-even for the buy alone: 300 / 45 = 6.7 years. For both legs: 600 / 45 = 13.3 years.

With a lower conversion cost, the break-even is shorter. With a conversion fee, the C$45 gain is small against the C$300 you pay up front, so the saving is not automatic.

</div>

## All-in-one ETFs

An **asset allocation ETF** (an all-in-one ETF) holds several other ETFs, for example global stocks and bonds, at a set mix such as 60% stocks and 40% bonds, and rebalances them for you. You pay one fee, and the fund's holdings carry the same withholding as the funds inside. Canada has many, usually Canadian-listed in C$. The lesson to take is to look through the wrapper: which funds does it hold, are any of them US-listed wrappers for international stocks, what does the whole stack cost, and what mix does it hold. This book does not name a product; lesson 10 builds the same mix from parts.

<div class="canada" markdown>

### For Canadians

Foreign property held at a Canadian broker can need Form T1135 if its cost passes C$100,000 ([CRA T1135 Q&A](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html), as of 2026). A US-listed ETF is foreign property; [Cost base in CAD and records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md) explains the form, and the CRA's guide says which units count. Check your own case before you rely on either listing.

</div>

## Common mistakes

- Buying a US-listed ETF in a TFSA to "avoid withholding". The TFSA gets no treaty exemption, so the 15% is lost.
- Counting the RRSP saving without the conversion cost. Add both before you choose.
- Assuming a Canadian-listed ETF has no currency risk. It holds US$ stocks unless it is hedged.

## Try it

1\. You hold C$30,000 of a US stock fund in a TFSA. It yields 2.0%. How much withholding a year, in C$?

<details class="solution" markdown>
<summary>Answer</summary>

Dividends = 30,000 x 0.02 = C$600. Withholding = 600 x 0.15 = C$90, whichever listing holds the US stocks.

</details>

2\. The same C$30,000 sits in an RRSP in a US-listed ETF. How much is withheld?

<details class="solution" markdown>
<summary>Answer</summary>

C$0 at the US layer, because the RRSP is exempt under the treaty. The same fund in a Canadian-listed ETF would lose C$90.

</details>

3\. You convert C$30,000 at a 1.5% fee to buy that US-listed ETF, and keep it for 5 years with no growth. Does the RRSP saving cover the fee on the way in?

<details class="solution" markdown>
<summary>Answer</summary>

Fee = 30,000 x 0.015 = C$450. Saving = C$90 a year x 5 = C$450. They are equal at 5 years for the buy leg only, so after the sale fee you are behind.

</details>

4\. A Canadian ETF holds a US-listed ETF of international stocks. How many layers of foreign withholding does it face, and is the second one recoverable in a TFSA?

<details class="solution" markdown>
<summary>Answer</summary>

Two: the foreign country's tax inside the US ETF, then 15% US tax on the payment to the Canadian fund. The second is not recoverable.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the tax page of one Canadian-listed ETF you might hold. Write whether it holds stocks directly or through a US-listed ETF. |
| 3 | For the same exposure, find a US-listed ETF. Write its dividend yield from the issuer's page. |
| 3 | Compute the yearly withholding for C$10,000 in each, for one account type you use. |

</div>

## Key terms

- **US-listed ETF**: an ETF that trades on a US exchange in US dollars.
- **Canadian-listed ETF**: an ETF that trades on a Canadian exchange in Canadian dollars.
- **Hedged ETF**: an ETF that offsets the exchange-rate move on its foreign holdings.
- **Asset allocation ETF (all-in-one ETF)**: an ETF that holds several other ETFs at a fixed mix and rebalances them.

Next: [Leveraged and inverse ETFs](04-leveraged-and-inverse-etfs.md)
