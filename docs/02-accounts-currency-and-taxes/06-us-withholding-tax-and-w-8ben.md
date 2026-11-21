# US withholding tax and the W-8BEN

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can say how much US tax is taken from a US dividend in each account type, explain what the W-8BEN does, and work out the net dividend and the Canadian foreign tax credit.

Before this: [Currency risk on US stocks](05-currency-risk-on-us-stocks.md), [Dividends, splits and corporate actions](../01-how-markets-work/09-dividends-splits-and-corporate-actions.md). The math book's [Taxes on investment income](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/08-starting-your-career/02-taxes-on-investment-income/) helps. You need: a calculator.

## The idea

A US company pays its dividend, and the US taxes the part paid to someone who is not a US person. This is **withholding tax**: the payer holds back a percentage and sends it to the tax authority, and you receive the rest. For a Canadian resident, the default US rate is 30%, and the Canada-US tax treaty lowers it to 15% on dividends if you have told the US that you are a Canadian resident. You tell it with a form, the **W-8BEN**, a certificate of foreign status that you sign for your broker. The rates are listed in Table 1 of the IRS treaty tables ([IRS tax treaty tables](https://www.irs.gov/individuals/international-taxpayers/tax-treaty-tables)); I could not read the table's text, so check the Canada row yourself.

The W-8BEN is valid from the date you sign it until the end of the third calendar year after that. A form signed on September 30, 2026 stays valid through December 31, 2029. You must give your broker a new one within 30 days if something on it changes, such as moving to the US ([IRS instructions for Form W-8BEN](https://www.irs.gov/instructions/iw8ben), as of 2026). Your broker collects the form when you open an account; check your account settings for its date.

## What each account type does

The treaty makes one exception that matters to you. Brokers and tax guides apply it as follows (the treaty text itself is the source, and I could not read it, so confirm with your broker's tax page and the IRS table above).

| Account | Withholding on a US dividend | Can you get it back? |
|---|---|---|
| Cash or margin (non-registered) | 15% with a W-8BEN, 30% without | Usually as a foreign tax credit on your return |
| RRSP | 0%, the treaty exempts retirement accounts such as an RRSP | Nothing to recover |
| TFSA | 15% | No. Canada does not tax a TFSA, so there is no Canadian tax to credit against |
| FHSA | 15% by broker practice, check | No. Brokers treat it like a TFSA, and I found no CRA or IRS page that says so |

So a US dividend stock can lose 15% of its dividend in a TFSA and none in an RRSP. That does not mean you should move all of them: the RRSP's other rules (withdrawals taxed as income, room) matter too, and the dividend is only part of the return. US-listed ETFs and Canadian-listed ETFs that hold US stocks can have an extra layer of withholding inside the fund; the fund's tax page says how.

## How the credit works

In a non-registered account, you report the full dividend before withholding as income, in Canadian dollars. You then claim a **foreign tax credit** for the US tax paid, which reduces your Canadian tax. The CRA says you generally claim the lesser of the foreign tax you paid and the Canadian tax otherwise payable on that income, on Form T2209 (and Form T2036 for the province outside Quebec). You convert both the income and the tax to Canadian dollars at the Bank of Canada rate for the day the amounts arose ([CRA foreign tax credit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40500-federal-foreign-tax-credit.html), as of 2026).

<div class="example" markdown>

### Worked example: one dividend in each account

You own 200 shares of Stock A, which pays US$0.50 a share. The Bank of Canada rate on the payment day is 1.3800. You have a W-8BEN on file. Your marginal tax rate is 30% (made up for the example).

1. Gross dividend: 200 x 0.50 = US$100.00, which is C$138.00.
2. TFSA: 15% is withheld, US$15.00. You receive US$85.00, or C$117.30. Canadian tax is 0. Total tax is 15%.
3. RRSP: nothing is withheld. You receive US$100.00, or C$138.00.
4. Cash account: US$15.00 is withheld, so you receive US$85.00. You report C$138.00 of income. Canadian tax at 30% is C$41.40. The foreign tax is 15.00 x 1.38 = C$20.70, which is below C$41.40, so the credit is C$20.70. You pay C$20.70 in Canadian tax. Total tax is 20.70 + 20.70 = C$41.40, which is 30%.
5. Without a W-8BEN in the TFSA: 30% is withheld, US$30.00, so you receive US$70.00.

In the cash account the credit brings the total tax up to your normal rate, not above it. In the TFSA, the 15% is a cost.

</div>

<div class="canada" markdown>

### For Canadians

Check three things at your broker: that a W-8BEN is on file and not expired, which account types it applies to, and how its tax slips show foreign tax paid. Compare your broker's tax page with the table above and with your first dividend's statement. If your statement shows more than the rate above, ask support before filing.

</div>

## Common mistakes

- Skipping the W-8BEN or letting it expire, which can leave 30% withheld instead of 15%.
- Forgetting that US dividends in a TFSA or FHSA carry a cost that never comes back.
- Reporting only the net dividend in a cash account. You report the gross amount and claim the credit.

## Try it

1\. You hold 500 shares of Stock B, which pays US$0.20 a share, in a TFSA with a W-8BEN. How much US tax is withheld and how much do you receive?

<details class="solution" markdown>
<summary>Answer</summary>

Gross = 500 x 0.20 = US$100.00. Withholding = 15% of 100 = US$15.00. You receive US$85.00.

</details>

2\. The same dividend is paid into a cash account on a day when the Bank of Canada rate is 1.4000, and your marginal rate is 25% (made up). What is your net Canadian tax after the credit?

<details class="solution" markdown>
<summary>Answer</summary>

Income = 100 x 1.40 = C$140.00. Canadian tax at 25% = C$35.00. Foreign tax = 15 x 1.40 = C$21.00. The credit is the lesser of 21.00 and 35.00, so C$21.00. Canadian tax after credit = 35.00 - 21.00 = C$14.00.

</details>

3\. A W-8BEN is signed on March 3, 2026. Through what date is it valid?

<details class="solution" markdown>
<summary>Answer</summary>

Through December 31, 2029, the end of the third calendar year after 2026.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the date of your W-8BEN at each broker, and write the date it expires. |
| 3 | Find your last US dividend in each account type. Write the gross, the amount withheld and the percentage. |
| 3 | Compare that percentage with the table above. Note any account where it differs. |

</div>

## Key terms

- **Withholding tax**: tax held back by the payer and sent to the tax authority before you are paid.
- **W-8BEN**: the form that certifies you are a non-US person and claims treaty rates.
- **Treaty rate**: the lower withholding rate set by a tax treaty, 15% on US dividends for Canadian residents.
- **Foreign tax credit**: a reduction in Canadian tax for foreign income tax already paid.
- **Gross dividend**: the dividend before withholding.

Next: [Capital gains or business income](07-capital-gains-vs-business-income.md)
