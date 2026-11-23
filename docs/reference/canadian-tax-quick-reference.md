# Canadian tax quick reference

This page is education, not tax advice. It summarises what the book's lessons say about Canadian accounts and taxes, and every row links to the lesson and its source. Rules change and have exceptions, and some points could not be confirmed on a CRA page. Where a lesson hedged, the hedge is kept here. Check the CRA's current guide, your broker's pages and, for your own case, an accountant.

## Accounts

The cash and margin accounts are non-registered: they have no special tax status, and every gain and dividend goes on your tax return. The TFSA, RRSP and FHSA are registered accounts. See [Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md).

| Question | Cash or margin (non-registered) | TFSA | RRSP | FHSA |
|---|---|---|---|---|
| Gains taxed | Yes, half of a capital gain is taxable | No | Not until withdrawal | No, if used for a first home |
| Losses claimable | Yes, against capital gains | No | No | No |
| Can borrow (margin) | Yes, at brokers that offer it | No at IBKR Canada | No at IBKR Canada | No at IBKR Canada |
| US dividend withholding | Recoverable as a credit | Not recoverable | Exempt under the treaty | Brokers treat it like a TFSA, check |

The losses row was not found on a CRA page. It comes from adviser guidance such as Raymond James's 2026 tax-loss guide, so confirm it. At IBKR Canada, margin is allowed only in non-registered individual accounts, and short selling needs a margin account ([IBKR Canada individual accounts](https://www.interactivebrokers.ca/en/accounts/individual.php), as of 2026). At Wealthsimple you apply for margin. CIRO sets margin minimums and a broker can set higher ones ([Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md), as of 2026). Check your broker's margin page for the rate your US stock gets.

## Contribution limits for 2026

| Account | 2026 limit | Source |
|---|---|---|
| TFSA | $7,000 for 2026; unused room carries forward | [CRA limits table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| RRSP | Dollar limit $33,810 for 2026 (your room also depends on your earned income) | Same table |
| FHSA | $8,000 a year, $40,000 lifetime; unused room carries forward up to $8,000 | [CRA FHSA definitions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/definitions.html) |

Going over your room is an excess contribution and the CRA can tax it, so track your room in CRA My Account. TFSA room returns on January 1 of the year after a withdrawal, so putting money back in the same year can over-contribute. The FHSA can stay open until the earliest of 15 years after you open your first FHSA, the year you turn 71, or the year after your first qualifying withdrawal. See [Account types for trading](../02-accounts-currency-and-taxes/01-account-types-for-trading.md).

## US dividend withholding

The default US rate for a Canadian resident is 30%. The Canada-US treaty lowers it to 15% on dividends if you have given your broker a W-8BEN. The lesson could not read the IRS treaty table's text, so check the Canada row ([IRS tax treaty tables](https://www.irs.gov/individuals/international-taxpayers/tax-treaty-tables)). A W-8BEN is valid from the date you sign it until the end of the third calendar year after, and you must send a new one within 30 days if something on it changes ([IRS instructions](https://www.irs.gov/instructions/iw8ben), as of 2026).

| Account | Withholding on a US dividend | Can you get it back? |
|---|---|---|
| Cash or margin (non-registered) | 15% with a W-8BEN, 30% without | Usually as a foreign tax credit on your return |
| RRSP | 0%, the treaty exempts retirement accounts such as an RRSP | Nothing to recover |
| TFSA | 15% | No |
| FHSA | 15% by broker practice, check | No; no CRA or IRS page was found that says so |

In a non-registered account you report the full dividend before withholding, in Canadian dollars, and claim a foreign tax credit (Form T2209, and T2036 outside Quebec), converting at the Bank of Canada rate for the day ([CRA foreign tax credit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40500-federal-foreign-tax-credit.html), as of 2026). See [US withholding tax and the W-8BEN](../02-accounts-currency-and-taxes/06-us-withholding-tax-and-w-8ben.md).

## Withholding by fund structure

This table comes from a 2016 Canadian analysis ([Canadian Couch Potato, July 11, 2016](https://canadiancouchpotato.com/2016/07/11/foreign-withholding-taxes-revisited/)) and is the most recent one the lesson could read in full. Treaty rules and fund structures may have changed, so confirm with the issuer and the fund's tax page. The FHSA row was not found on a CRA page, so treat it as the TFSA's.

| Structure | RRSP | TFSA or FHSA | Non-registered |
|---|---|---|---|
| US-listed ETF of US stocks | 0% withheld | 15% withheld, not recoverable | 15% withheld, recoverable as a foreign tax credit |
| Canadian-listed ETF holding US stocks directly | 15% withheld in the fund, not recoverable | 15%, not recoverable | 15%, and the fund reports the tax so you can usually claim a credit |
| Canadian-listed ETF holding a US-listed ETF | 15% withheld on what the US ETF pays the fund, not recoverable | Same | Same |

The RRSP advantage applies only to US stocks, not to international stocks. A US-listed ETF also costs a currency conversion: Wealthsimple charges a 1.5% fee on the conversion for a US-listed security in a CAD account (as of 2026). See [US-listed or Canadian-listed ETFs](../13-etfs-portfolios-and-factors/03-us-vs-canadian-listed-etfs.md) and [USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md).

## Capital gains or business income

A capital gain is the profit from selling capital property. Only half of it is taxable: the CRA's guide T4037 gives the inclusion rate as one-half for 2001 through 2025. The proposed increase to two-thirds was delayed to 2026 and then cancelled in March 2025, so the book uses one-half for 2026. Check the current guide before you file ([CRA T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). Business income is profit from carrying on a business of trading securities. All of it is taxable and the expenses are deductible.

There is no single test. The CRA's archived bulletin IT-479R lists factors, including how often you trade, how long you hold, your experience, the time you spend on research, whether you finance with margin or debt, and whether shares are speculative ([IT-479R](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/it479r/archived-transactions-securities.html)). No one factor is usually decisive. The section 39(4) election (Form T123) covers Canadian securities only, not US stocks, and does not apply to traders or dealers. A TFSA does not shelter business income: in Canadian Western Trust Co. (Ahamed TFSA) v. King, 2024 FCA 108, a TFSA trust was taxed on business income from trading. The lesson did not research later changes to the liability rules. Keep your trade journal as your record. See [Capital gains or business income](../02-accounts-currency-and-taxes/07-capital-gains-vs-business-income.md).

## Cost base in CAD

The adjusted cost base (ACB) is what you paid, in Canadian dollars, including commissions, averaged across identical shares ([CRA T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html), as of 2026).

1. Convert proceeds at the rate in effect at the sale, the ACB at the rate in effect when you acquired the shares, and expenses at the rate when they were incurred.
2. Recalculate the average cost after each purchase of identical shares: total cost divided by total shares.
3. A sale does not change the average cost of the shares you still hold.

Use the Bank of Canada rate for the transaction day, or another source that is widely available, verifiable and used consistently from year to year. Pick one and use it every year. See [Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md).

## Losses and the superficial loss rule

A capital loss in a non-registered account offsets taxable capital gains. A net capital loss can generally be applied only against taxable capital gains, carried back three years (Form T1A) and carried forward with no time limit (Schedule 3). A loss is superficial, and denied, when you or an affiliated person buy the same or identical shares from 30 days before to 30 days after the sale and still own them 30 days after the sale. The window is 61 days. The denied loss can usually be added to the ACB of the replacement shares. A buyback in your own TFSA or RRSP is a hedged point: adviser guides say the loss is then denied for good, a few say otherwise, and the lesson could not read the CRA's text, so treat the loss as lost and ask a tax professional. Whether two ETFs that track the same index are identical is also a question for a tax professional. See [Tax losses and the superficial loss rule](../02-accounts-currency-and-taxes/09-tax-losses-and-superficial-loss.md).

## Foreign property reporting (T1135)

If the total cost of your specified foreign property was more than C$100,000 at any time in the year, you file Form T1135. The test uses cost, generally the ACB, not market value. Shares of non-resident corporations count even when a Canadian broker holds them, and so does a US-listed ETF. Between C$100,000 and C$250,000 throughout the year you can use the simplified Part A, and at C$250,000 or more you complete Part B. Property held in an RRSP or TFSA is excluded ([CRA T1135 questions and answers](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html), as of 2026). See [Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md).

## Options

Account rules depend on the broker, and Wealthsimple's pages disagree on spreads in registered accounts, so ask support in writing. IBKR Canada's pages could not be read, so the lesson states no options permissions for it ([Options in Canadian accounts](../15-options/15-options-in-canadian-accounts.md), as of 2026).

| Question | What the lesson says |
|---|---|
| May a registered plan hold an option? | CRA Income Tax Folio S3-F10-C1: listed options generally qualify, except derivatives where the holder's loss can exceed the cost (paragraph 1.16). Writing an option is generally not subject to the qualified investment rules, though other tax rules may limit it (paragraph 1.40) |
| Is writing options a business? | The CRA's view is that writing a covered call does not by itself mean the plan carries on a business. Writing an uncovered call, or a put, alone or combined with other positions, may (paragraph 1.41). That wording includes cash-secured puts, so ask your broker and a tax professional |
| Premiums in a non-registered account | The archived IT-479R (1984) says capital or income account depends on the facts. A naked writer's result is normally income, though consistent capital treatment is accepted. A written put that is assigned reduces the cost of the shares bought. Treat this as a map: the page is archived and a current ruling may differ |

## Crypto

The CRA treats crypto generally like a commodity. These events are dispositions: selling for Canadian or foreign currency, trading one crypto-asset for another, paying for goods or services with crypto, and gifting or donating it. Moving coins between your own wallets is not ([CRA, Reporting income from crypto-asset transactions](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/income-crypto-transactions.html), as of 2026). The capital gains and business income tests are the same as for stocks. Use fair market value in CAD with a reasonable method applied consistently. The ACB is usually the weighted average cost. The superficial loss rule is a general rule for capital property, and the CRA's crypto pages do not mention it, so a repurchase of the same coin fits its pattern. Keep records of each transaction for at least six years from the end of the last tax year they relate to ([CRA, Keeping books and records](https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/cryptocurrency-guide/books-records-crypto.html)). Whether a crypto ETF is allowed in a TFSA, RRSP or FHSA is a question for the fund's prospectus and your broker. Wealthsimple Crypto is offered in non-registered accounts, with no registered options listed. See [Crypto taxes and position sizing](../18-crypto/09-crypto-taxes-and-sizing.md), [Crypto ETFs](../18-crypto/05-crypto-etfs.md) and [Buying crypto in Canada](../18-crypto/04-buying-crypto-in-canada.md).

## Futures

Whether a futures gain is a capital gain or business income depends on the facts, mainly how often and how you trade. The lessons state no CRA rule for futures specifically. Ask a tax professional before your first trade, and record every contract in Canadian dollars ([Futures in Canada](../14-futures/07-futures-in-canada.md)).
