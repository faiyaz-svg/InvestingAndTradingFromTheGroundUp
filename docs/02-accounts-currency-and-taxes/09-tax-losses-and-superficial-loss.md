# Tax losses and the superficial loss rule

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can say how a capital loss is used on a Canadian return, test a sale for the superficial loss rule, and work out the new cost base when a loss is denied.

Before this: [Cost base in CAD and keeping records](08-cost-base-in-cad-and-records.md). You need: a calculator and a calendar.

This lesson is education, not tax advice. The CRA's rules have exceptions, so check the source before you rely on a result.

## The idea

You sold shares for less than your adjusted cost base. That is a **capital loss**, and in a non-registered account it has a use: it can reduce the tax on capital gains. The rules are in the CRA's guide T4037 ([CRA T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html), as of 2026).

Your allowable capital losses for the year first offset your taxable capital gains. If losses are larger, the rest is a **net capital loss**. A net capital loss of another year can generally be applied only against taxable capital gains. The guide says it can be carried back three years and carried forward with no time limit. To carry it back you use Form T1A, and to carry either way you complete Schedule 3.

A loss inside a TFSA, RRSP or FHSA is a different case. The sources I found say it cannot be claimed against gains elsewhere, such as [Raymond James's 2026 tax-loss guide](https://www.raymondjames.ca/commentary-and-insights/tax-planning/2026/07/13/tax-loss-harvesting-canada-2026-guide), but I did not find a CRA page for it.

## The superficial loss rule

A trader who sells at a loss and buys the same stock back the next day has changed nothing about their position, and the CRA does not allow the loss. This is the **superficial loss** rule. A loss is superficial when both of these are true:

1. You, or an affiliated person, bought (or has a right to buy) the same or identical shares in the period from 30 calendar days before the sale to 30 calendar days after it.
2. You, or an affiliated person, still own those shares (or the right to buy them) 30 days after the sale.

Affiliated persons include your spouse or common-law partner, a corporation you or your spouse control, and certain partnerships and trusts. A superficial loss cannot be deducted in that year. If you acquired the replacement shares, the denied loss can usually be added to their ACB, so you recover it when you sell them (T4037, same page). Some events, such as emigration or death, are exceptions.

The window is 61 days long: 30 days before, the sale day, and 30 days after.

<div class="example" markdown>

### Worked example: a loss and a quick buyback

You hold 100 shares of Stock A with a total ACB of C$7,000. On March 10, 2026, you sell them for C$5,500.

1. Loss: 7,000 - 5,500 = C$1,500. Allowable (half): C$750.
2. The window runs from February 8, 2026 (30 days before) to April 9, 2026 (30 days after).
3. You buy 100 shares of Stock A back on March 20 for C$5,600 and still hold them on April 9. The loss is superficial and denied.
4. New ACB = 5,600 + 1,500 = C$7,100.
5. Later you sell those shares for C$6,800 on May 15, outside the window. Loss = 7,100 - 6,800 = C$300, and the allowable part is C$150.

The deferral returned most of the denied loss, because the new cost base carries it. Compare the case where you do not buy back. If you also had C$4,000 of capital gains that year, the C$1,500 loss would cut the taxable gain by C$750. At a made-up 40% marginal rate, that saves 750 x 40% = C$300 of tax.

</div>

## Staying clear of the rule

You can wait 31 days to buy back, so the buyback falls outside the 30-day window. You can also buy a different stock or fund. Whether two funds are "identical" depends on facts, so a swap between two ETFs that track the same index is a question for a tax professional, and I did not find a CRA ruling to cite.

The rule also catches purchases you do not think of as buybacks:

- A dividend reinvestment plan (DRIP) that buys shares inside the window.
- An automatic purchase in the same or another account you control.
- A buyback in your own TFSA or RRSP. Adviser guides say the loss is then denied for good, because a registered plan has no cost base to take it, though a few sources say otherwise. I could not read the CRA's own text on this, so treat the loss as lost and ask a tax professional.
- A purchase by your spouse or common-law partner.

## Currency and the loss

The loss is calculated in Canadian dollars, with the ACB and proceeds converted at their own dates (lesson 8). A US stock can fall 3% in US dollars and produce a bigger or smaller loss in C$. Test the rule on your Canadian numbers.

<div class="canada" markdown>

### For Canadians

Tax-loss selling is often done late in the year. A loss counts for the year of the sale, and with T+1 settlement a trade made on the last trading days of December can settle in January. I did not find a CRA page that says which date counts, so ask your accountant before you cut it close. A December sale also puts the 30-day window into January, so a buyback in early January is inside it.

</div>

## Common mistakes

- Selling at a loss in a cash account and buying the same stock in your TFSA or RRSP. The loss is generally treated as denied, with no sure way to recover it.
- Forgetting the 30 days before the sale. A purchase on March 5 and a sale on March 10 can be superficial.
- Leaving a DRIP on in an account that holds the stock you sold.

## Try it

1\. You sell on June 15, 2026. What are the first and last days of the superficial loss window?

<details class="solution" markdown>
<summary>Answer</summary>

30 days before June 15 is May 16. 30 days after is July 15. The window is May 16, 2026 to July 15, 2026.

</details>

2\. You buy 100 shares on March 5, buy another 100 on March 8 and sell 100 at a loss on March 10, and you still hold 100 shares on April 9. Is the loss superficial?

<details class="solution" markdown>
<summary>Answer</summary>

Yes. You bought identical shares within 30 days before the sale, and you still hold identical shares 30 days after it.

</details>

3\. You had a C$3,000 capital loss and C$1,000 of capital gains in the same year. What is the net capital loss?

<details class="solution" markdown>
<summary>Answer</summary>

Allowable loss = 3,000 x 1/2 = C$1,500. Taxable gain = 1,000 x 1/2 = C$500. Net capital loss = 1,500 - 500 = C$1,000, which carries back three years or forward with no limit, against taxable capital gains.

</details>

4\. A superficial loss of C$900 is denied, and you hold the replacement shares with a cost of C$4,000. What is their new ACB?

<details class="solution" markdown>
<summary>Answer</summary>

4,000 + 900 = C$4,900.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | List any positions you hold at a loss in a non-registered account, with ACB and current value in C$. |
| 3 | For one of them, write the 61-day window if you sold today. |
| 3 | Check whether a DRIP or automatic purchase is on in any account that holds it. |

</div>

## Key terms

- **Capital loss**: the loss from selling capital property for less than its ACB.
- **Allowable capital loss**: the part of a capital loss, one-half, that offsets taxable capital gains.
- **Net capital loss**: allowable losses in excess of taxable capital gains for the year.
- **Superficial loss**: a loss on a sale where identical shares are bought in the 61-day window and still held 30 days after.
- **Affiliated person**: a person or entity the CRA treats as the same party for this rule, including a spouse.

Next: [Margin rules in Canada](10-margin-rules-in-canada.md)
