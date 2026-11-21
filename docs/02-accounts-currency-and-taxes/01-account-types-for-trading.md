# Account types for trading

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can say what each Canadian account type allows for trading, work out your contribution room, and pick the account for a given kind of trade.

Before this: [Settlement, cash accounts and margin](../01-how-markets-work/07-settlement-cash-and-margin.md). The math book covers the basics in [Retirement accounts](https://faiyaz-svg.github.io/MathFromTheGroundUp/08-financial-math/06-investing-and-retirement/03-retirement-accounts/). You need: a calculator.

## The idea

You can hold the same US stock in five kinds of account, and the account decides three things: how the gains are taxed, what you may do (borrow, short, trade options) and what happens to a loss. Part 1 introduced the cash account and the margin account. Those two are **non-registered** accounts: they have no special tax status, and every gain and dividend goes on your tax return. The other three are **registered** accounts, which the government has approved for special tax treatment: the TFSA, the RRSP and the FHSA.

The **TFSA** (Tax-Free Savings Account) is funded with after-tax money. Growth and withdrawals are not taxed. The **RRSP** (Registered Retirement Savings Plan) is funded with money you deduct from your income, and withdrawals are taxed as income. The **FHSA** (First Home Savings Account) has a tax deduction on contributions like an RRSP, and a withdrawal to buy a first home is tax-free.

## Limits as of 2026

Each account has a **contribution room**: the most you may put in. Going over it is an excess contribution and the CRA can tax it, so track your room in CRA My Account.

| Account | 2026 limit | Source |
|---|---|---|
| TFSA | $7,000 for 2026; unused room carries forward | [CRA limits table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| RRSP | dollar limit $33,810 for 2026 (your room also depends on your earned income) | same table |
| FHSA | $8,000 a year, $40,000 lifetime, unused room carries forward up to $8,000 | [CRA FHSA definitions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/definitions.html) |

The TFSA room adds up. Someone who was 18 or older and resident in Canada in every year from 2009 to 2026 has had 5,000 + 5,000 + 5,000 + 5,000 + 5,500 + 5,500 + 10,000 + 5,500 + 5,500 + 5,500 + 6,000 + 6,000 + 6,000 + 6,000 + 6,500 + 7,000 + 7,000 + 7,000 = $109,000 in total, using the yearly limits on the CRA table. Your own total is lower if you turned 18 or arrived later. The FHSA also has a time limit: the account can stay open until the earliest of 15 years after you open your first FHSA, the year you turn 71, or the year after your first qualifying withdrawal (same CRA page).

## What you can do in each account

Registered accounts hold qualified investments, which include listed stocks and ETFs. Your broker narrows the list of what you can do. At IBKR Canada, margin is allowed only in non-registered individual accounts ([IBKR Canada individual accounts](https://www.interactivebrokers.ca/en/accounts/individual.php), as of 2026), and short selling needs a margin account ([Short selling](../01-how-markets-work/08-short-selling.md)). So a TFSA, RRSP or FHSA works like a cash account: you buy and sell, you do not borrow or short.

| Question | Cash or margin (non-registered) | TFSA | RRSP | FHSA |
|---|---|---|---|---|
| Gains taxed | Yes, half of a capital gain is taxable (lesson 7) | No | Not until withdrawal | No, if used for a first home |
| Losses claimable | Yes, against capital gains | No | No | No |
| Can borrow (margin) | Yes, at brokers that offer it | No at IBKR Canada | No at IBKR Canada | No at IBKR Canada |
| US dividend withholding | Recoverable as a credit | Not recoverable | Exempt under the treaty | Brokers treat it like a TFSA, check |

I could not find the losses row on a CRA page. It comes from adviser guidance such as [Raymond James's 2026 tax-loss guide](https://www.raymondjames.ca/commentary-and-insights/tax-planning/2026/07/13/tax-loss-harvesting-canada-2026-guide), so confirm it with the CRA or an accountant. The withholding row is explained in [US withholding tax and the W-8BEN](06-us-withholding-tax-and-w-8ben.md).

## One more rule: business income in a TFSA

If the CRA decides that you trade as a business, the income from that trading is business income, and a TFSA does not shelter it. The CRA's TFSA page says that income taxable in the TFSA trust is a specified distribution and creates no new room ([CRA TFSA page](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account.html)). Lesson 7, [Capital gains or business income](07-capital-gains-vs-business-income.md), covers how that decision is made.

<div class="example" markdown>

### Worked example: TFSA room after a withdrawal

You have used all your room. In 2026 you withdraw $4,000 from your TFSA. The room comes back on January 1 of the next year, so your 2027 room is the 2027 limit plus the $4,000 withdrawn.

Suppose the 2027 limit is $7,000 (made up here; the CRA sets it each year). Room on January 1, 2027 is 7,000 + 4,000 = $11,000. If you put $4,000 back in December 2026, before that room returns, you have over-contributed by $4,000.

</div>

<div class="canada" markdown>

### For Canadians

Wealthsimple's margin page describes linking a TFSA to a margin account and says this does not affect TFSA contribution room ([Wealthsimple margin](https://www.wealthsimple.com/en-ca/self-directed-investing/margin), as of 2026). Read the page and your agreement before you do it, because linked assets can be sold to cover a margin call. CIPF protects the assets if the broker fails; lesson 2 has the limits.

</div>

## Common mistakes

- Trading very often in a TFSA without knowing that the CRA can treat frequent trading as business income.
- Counting on a loss inside a TFSA, RRSP or FHSA to offset gains elsewhere. It does not.
- Withdrawing from a TFSA and putting the money back in the same year. The room returns only on January 1.

## Try it

1\. Someone has never contributed to a TFSA and has been resident since turning 18 in 2014. What is the total room at the start of 2026, before the 2026 limit is added? (Use the CRA table.)

<details class="solution" markdown>
<summary>Answer</summary>

Room for 2014 to 2025: 5,500 + 10,000 + 5,500 + 5,500 + 5,500 + 6,000 + 6,000 + 6,000 + 6,000 + 6,500 + 7,000 + 7,000 = $76,500. Adding the 2026 limit gives $83,500.

</details>

2\. You open an FHSA in 2026 and contribute $8,000. In 2027 you contribute nothing. What is the most you can contribute in 2028?

<details class="solution" markdown>
<summary>Answer</summary>

The 2028 limit is $8,000 plus a carry-forward of up to $8,000 of unused room from 2027, so $16,000. The lifetime limit of $40,000 is not a problem yet, because you have used only $8,000.

</details>

3\. Which account would you use to borrow and buy shares at IBKR Canada, and why?

<details class="solution" markdown>
<summary>Answer</summary>

A non-registered margin account. IBKR Canada allows margin only in non-registered individual accounts.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Log in to CRA My Account and write down your TFSA, RRSP and FHSA room (or note that you have no access yet). |
| 3 | List every account you hold at Wealthsimple or IBKR, and whether margin is on or off. |
| 3 | Open [the trade journal page](../practice/trade-journal.md) and add an "account" field to your journal template. |

</div>

## Key terms

- **Non-registered account**: a cash or margin account with no special tax status.
- **Registered account**: an account the government approves for tax treatment (TFSA, RRSP, FHSA).
- **TFSA**: a savings account funded with after-tax money, where growth and withdrawals are not taxed.
- **RRSP**: a retirement account where contributions are deductible and withdrawals are taxed.
- **FHSA**: a first-home account with deductible contributions and tax-free qualifying withdrawals.
- **Contribution room**: the most you may add to a registered account.
- **Qualified investment**: an asset a registered account may hold.

Next: [Wealthsimple and IBKR compared](02-wealthsimple-and-ibkr.md)
