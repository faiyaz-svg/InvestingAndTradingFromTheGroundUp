# Buying crypto in Canada

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">CRYPTO</span>

After this lesson you can check whether a platform is registered in Ontario, apply the C$30,000 purchase limit to a series of buys and sells, and work out what a trade costs once the platform's fee and spread are counted.

Before this: [Blockchains, keys and wallets](02-blockchains-keys-and-wallets.md), [Wealthsimple and IBKR](../02-accounts-currency-and-taxes/02-wealthsimple-and-ibkr.md). You need: a calculator.

This lesson is education, not legal advice. Rules change, so each fact here carries its source and "as of 2026". Confirm on the regulator's page before you act.

## The idea

A stock broker in Canada is registered and supervised, and its clients' securities can have investor protection behind them. A crypto platform sits in a different spot. The Canadian Securities Administrators (CSA), the group of provincial regulators, take the view that many crypto trading platforms are dealing in securities or contracts, so they need to register. The Ontario Securities Commission (OSC) is the regulator that matters for an Ontario resident. Many platforms operate under a **pre-registration undertaking**: a commitment to the regulator that holds them to its terms while their registration application is reviewed ([CSA, crypto undertakings](https://www.securities-administrators.ca/crypto-platforms-regulation-and-enforcement-actions/crypto-undertakings/), as of 2026).

The practical rule for you: a platform that the regulator does not list is not one you want to hold money with.

## How it works

### Checking a platform

1. Go to the OSC's [crypto businesses](https://www.osc.ca/en/industry/registration-and-compliance/crypto-businesses) page, which lists registered crypto asset trading platforms, and look for the legal name of the company, not the brand.
2. Note whether it is listed as registered or as holding a pre-registration undertaking, and read the date.
3. Check the CSA's list of [crypto platforms authorized to do business with Canadians](https://www.securities-administrators.ca/crypto-platforms-regulation-and-enforcement-actions/crypto-platforms-authorized-to-do-business-with-canadians/) and the OSC's [investor warnings](https://www.osc.ca/en/investors/investor-warnings-and-alerts). Then run the company's name through the CSA's National Registration Search, which is linked from the CSA site.
4. Check who holds the coins (lesson 2) and whether the platform says its holdings have investor protection.

These lists change often. Open them yourself and write down what they say on the day you check.

### The purchase limit

On December 10, 2024 the OSC published the results of a review of crypto platforms ([OSC Staff Notice 33-757](https://www.osc.ca/en/securities-law/instruments-rules-policies/3/33-757/osc-staff-notice-33-757-review-restricted-dealer-crypto-asset-trading-platforms-compliance-account), as of 2026). Law-firm summaries of it, such as [BLG's](https://www.blg.com/en/insights/2025/01/best-practices-from-the-ontario-securities-commission-crypto-asset-trading-platforms), state the investment limit this way: for platforms that are not required to run a suitability check on each trade, a client who is not an "eligible crypto investor" may not go above a net acquisition cost of C$30,000 over the preceding 12 months, calculated on a net basis and never below C$0. Bitcoin, Ether, Bitcoin Cash, Litecoin and compliant "value-referenced" crypto assets (certain stablecoins) are excluded from that limit, as of the date of the notice.

The OSC's own pages were not readable by the book's tools, so the wording above rests on those summaries. Confirm the exact wording, the definition of an eligible crypto investor and any exceptions in the notice before you rely on it.

<div class="example" markdown>

### Worked example: applying the limit

You trade only Coin A, a made-up coin that is not one of the excluded assets, on a platform that applies the limit. The figures are net acquisition cost: purchases less sales, not below zero.

1. Buy C$20,000 of Coin A. Net cost: C$20,000. Room left: 30,000 - 20,000 = C$10,000.
2. Sell C$5,000 of Coin A. Net cost: 20,000 - 5,000 = C$15,000. Room left: C$15,000.
3. Buy C$18,000 more. That takes net cost to 33,000, which is above C$30,000, so the platform should refuse part of it. The most you can buy is C$15,000.

Bitcoin and Ether would not count toward this limit as of the notice date.

</div>

### What a trade costs

Platforms charge in two places: a visible fee, and a **spread**, the gap between the price you pay and the mid price. Wealthsimple Crypto's page lists a flat 0.5% fee plus a spread that varies by asset and order size, no spread on limit orders, and a $1 surcharge on orders under $100 ([Wealthsimple Crypto](https://www.wealthsimple.com/en-ca/product/crypto), as of 2026). The page also says the service is offered through Wealthsimple Investments Inc., a member of CIRO, that holdings are not covered by CIPF or CDIC, and that crypto is offered in non-registered accounts, with no registered account options listed. The page does not mention OSC or CSA registration, so check the OSC list for the exact entity.

\[ \text{round-trip cost} = 1 - (1 - f)(1 - f) \]

- \(f\) is the cost of one trade as a fraction of the amount, fee and spread together.
- The result is the share of your money lost to costs if the price does not move between buying and selling.

<div class="example" markdown>

### Worked example: the cost of one round trip

Use a fee of 0.5% and a made-up spread of 0.4%, so \(f\) = 0.9%.

1. Buy C$5,000: you receive coins worth 5,000 x (1 - 0.009) = C$4,955.
2. Sell the same coins at an unchanged price: 4,955 x (1 - 0.009) = C$4,910.41 (4,910.405 before rounding).
3. Round-trip cost: 5,000 - 4,910.405 = C$89.60 (rounded), or 1 - 0.991 x 0.991 = 1.8%.

Part 3 explains why costs like these change what a trade is worth ([Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md)).

</div>

<div class="canada" markdown>

### For Canadians

Crypto bought at a Canadian platform is taxed under the CRA rules in lesson 9. Wealthsimple's page lists crypto only for non-registered accounts, so any gain is reported on your return, and the cost base and records of every crypto trade are yours to keep. Canadian bitcoin and ether ETFs offer another route that holds coins inside a fund (lesson 5).

</div>

## Common mistakes

- Checking the brand name instead of the legal entity on the regulator's list.
- Treating a platform's app store rating as a safety check.
- Forgetting the spread. A "zero fee" trade can still cost you through a wide spread.

## Try it

1\. You buy C$12,000 of Coin A, sell C$3,000, and buy C$9,000. What is your net acquisition cost, and how much room is left under C$30,000?

<details class="solution" markdown>
<summary>Answer</summary>

Net cost = 12,000 - 3,000 + 9,000 = C$18,000. Room left = 30,000 - 18,000 = C$12,000.

</details>

2\. Fee 0.5% and spread 0.2% per trade. What is the round-trip cost on C$8,000?

<details class="solution" markdown>
<summary>Answer</summary>

f = 0.7%. After buying: 8,000 x 0.993 = 7,944. After selling: 7,944 x 0.993 = 7,888.39. Cost = 8,000 - 7,888.39 = C$111.61 (1.4%).

</details>

3\. A platform appears in a search but not on the OSC's list. What do you do?

<details class="solution" markdown>
<summary>Answer</summary>

Do not send money. Check the legal name again and look at the CSA's lists of authorized and banned platforms. If it is still unlisted, treat it as unregistered.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick one platform. Find its legal entity name in its terms, then look for it on the OSC's registered crypto asset trading platforms page. Write the date you checked. |
| 3 | Find its fee page. Write the fee, whether a spread applies, and the minimum order. Work out the round-trip cost on C$1,000. |
| 2 | Write in your [trade journal](../practice/trade-journal.md) what a platform failure would cost you, in C$. |

</div>

## Key terms

- **Crypto trading platform (CTP)**: a business that lets clients buy and sell crypto assets.
- **Pre-registration undertaking**: a platform's commitment to its regulator while its registration is under review.
- **Eligible crypto investor**: an investor class that the OSC's rules treat differently from a non-eligible investor, with a higher limit (the OSC defines who qualifies).
- **Net acquisition cost**: purchases less sales of crypto assets over a period, not below zero.
- **Spread**: the gap between the price you pay and the mid price.
- **Round-trip cost**: the share of your money lost to costs from buying and selling at an unchanged price.

Next: [Crypto ETFs](05-crypto-etfs.md)
