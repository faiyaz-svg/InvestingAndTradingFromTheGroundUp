# Capital gains or business income

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can compare the tax on a trading profit treated as a capital gain and as business income, list the factors the CRA looks at, and say which facts of your own trading to track.

Before this: [US withholding tax and the W-8BEN](06-us-withholding-tax-and-w-8ben.md). The math book's [Taxes on investment income](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/08-starting-your-career/02-taxes-on-investment-income/) and [Side gigs and self-employment](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/08-starting-your-career/03-side-gigs-and-self-employment/) help. You need: a calculator.

This lesson is education, not tax advice. Which treatment applies to you depends on facts, and only you, your accountant and the CRA can settle it.

## The idea

Profit from selling a stock in a non-registered account is taxed in one of two ways. A **capital gain** is the profit from selling capital property, such as shares held as an investment. Only half of it is taxable: the CRA's capital gains guide gives the inclusion rate, the fraction of the gain that you add to income, as one-half for 2001 through 2025 ([CRA T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). The proposed increase to two-thirds was first delayed to 2026 ([CRA update](https://www.canada.ca/en/revenue-agency/news/newsroom/tax-tips/tax-tips-2025/update-cra-administration-proposed-capital-gains-taxation-changes.html)) and then cancelled in March 2025, so one-half is the rate used in this book for 2026. Check the current guide before you file. **Business income** is profit from carrying on a business of trading securities. All of it is taxable, and the expenses of earning it are deductible.

The inclusion rate is why the question matters. For the same profit, the tax is very different.

<div class="example" markdown>

### Worked example: one profit, two treatments

Your profit from trading Stock A and similar names is C$10,000 in the year. Your marginal tax rate is 40% (made up; look up yours in the math book's [tax brackets](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective/) lesson).

1. As a capital gain: taxable amount = 10,000 x 1/2 = C$5,000. Tax = 5,000 x 40% = C$2,000.
2. As business income: taxable amount = C$10,000. Tax = 10,000 x 40% = C$4,000.

The difference is C$2,000, or 20% of the profit. The treatment also works the other way for a loss: a business loss can be deducted against other income, while a capital loss can be applied only against capital gains (lesson 9).

</div>

## How the CRA decides

There is no single test. The CRA's archived bulletin IT-479R lists factors, and the CRA says no one of them is usually decisive, but a combination can indicate a business ([IT-479R](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/it479r/archived-transactions-securities.html)). The factors include:

1. How often you buy and sell, and how fast your holdings turn over.
2. How long you typically hold a security.
3. Your knowledge of and experience in securities markets.
4. Whether trading is part of your ordinary business.
5. How much time you spend studying the markets and researching your purchases.
6. Whether you finance purchases mainly on margin or other debt.
7. Whether you advertise or otherwise signal that you will buy securities.
8. For shares, whether they are speculative or non-dividend-paying.

An intention to sell at a profit is not enough on its own. A single transaction can also count as business if the course of conduct points that way.

A swing trader holding a few days or weeks, trading often, with study time and margin, matches several of these. A long-term investor who buys an index fund once a month and holds for years matches few. Most people are in between, and that is when the CRA looks at the whole picture.

## Two rules that interact

**The section 39(4) election.** A taxpayer who has sold a Canadian security in a year can elect, on that year's return, to treat all Canadian securities owned that year and later years as capital property. It cannot be undone, it covers Canadian securities (not US stocks), and it does not apply to traders or dealers, banks and some other groups. The form is T123 (same IT-479R page). For a trader of US stocks it does not settle the question.

**A TFSA is not a shield for a business.** In Canadian Western Trust Co. (Ahamed TFSA) v. King, 2024 FCA 108, the Federal Court of Appeal dismissed an appeal in a case where a TFSA trust was taxed on business income from trading ([the decision](https://decision.tcc-cci.gc.ca/fca-caf/decisions/en/521420/1/document.do), June 11, 2024). If your trading in a TFSA is a business, the income can be taxed in the TFSA. I did not research later changes to the liability rules, so check the CRA's TFSA page.

## What to keep track of

Whatever your situation, keep the facts that the factors ask for: a log of each trade with its date, your holding periods, how much of the capital is borrowed, and the time you spend on research. The [trade journal](../practice/trade-journal.md) already holds most of this, so it doubles as your record if the CRA ever asks.

<div class="canada" markdown>

### For Canadians

Wealthsimple and IBKR do not decide for you. Their tax slips report proceeds and amounts, and you choose how to report them on your return. If you file a capital gain one year, a switch to business income in a later year (or the reverse) needs a reason. Many traders consult an accountant at the point where trading becomes frequent, large or borrowed.

</div>

## Common mistakes

- Assuming that holding for more than a year makes a gain a capital gain. Holding period is one factor, not a rule.
- Assuming a TFSA ends the question. The CRA can tax business income in a TFSA.
- Picking the treatment each year by whichever costs less. The CRA looks at the pattern of your activity, and a switch needs a reason.

## Try it

1\. Profit of C$20,000 at a 35% marginal rate. What is the tax as a capital gain and as business income?

<details class="solution" markdown>
<summary>Answer</summary>

Capital gain: 20,000 x 1/2 = 10,000 taxable, tax = 10,000 x 35% = C$3,500. Business income: 20,000 x 35% = C$7,000.

</details>

2\. A trader makes 300 trades a year, holds for 2 days on average, uses margin for most purchases and spends 25 hours a week on research. Which treatment do the factors point toward, and is that final?

<details class="solution" markdown>
<summary>Answer</summary>

Toward business income: high frequency, short holding period, margin financing and heavy research time. It is not final, because the CRA weighs the whole picture and the result depends on the facts.

</details>

3\. Two investors each earn C$6,000 profit on shares of Stock C and pay a 30% marginal rate. One is an investor who bought once and held for five years. The other trades the stock weekly. What is each tax if the CRA accepts the capital treatment for the first and the business treatment for the second?

<details class="solution" markdown>
<summary>Answer</summary>

First investor: 6,000 x 1/2 = 3,000 taxable, tax = 3,000 x 30% = C$900. Second investor: 6,000 x 30% = C$1,800.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Count your trades and your average holding time for the last 3 months, from your broker's statements. |
| 3 | Go through the eight factors above and mark the ones that describe you. |
| 3 | Add "date", "holding period" and "borrowed or not" columns to your [trade journal](../practice/trade-journal.md). |

</div>

## Key terms

- **Capital gain**: profit from selling capital property.
- **Inclusion rate**: the fraction of a capital gain added to your taxable income, one-half (2001 to 2025 in the CRA's guide, and still one-half for 2026).
- **Business income**: profit from carrying on a business, fully taxable with expenses deductible.
- **Capital property**: property bought as an investment rather than to resell in a business.
- **Section 39(4) election**: a choice to treat Canadian securities as capital property.

Next: [Cost base in CAD and keeping records](08-cost-base-in-cad-and-records.md)
