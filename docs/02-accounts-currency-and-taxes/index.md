# Part 2: Accounts, currency and taxes

Trading US stocks from Canada: which account, USD or CAD, withholding tax, CRA rules and records.

Before this part: Part 1. The math book's lessons on RRSP, TFSA and FHSA and on taxes on investment income help.

<!-- lessons:start -->
## Lessons

1. [Account types for trading](01-account-types-for-trading.md) (canada)
2. [Wealthsimple and IBKR compared](02-wealthsimple-and-ibkr.md) (canada)
3. [USD or CAD, and currency conversion fees](03-usd-vs-cad-and-fx-fees.md) (canada)
4. [Norbert's gambit and CDRs](04-norberts-gambit-and-cdrs.md) (canada)
5. [Currency risk on US stocks](05-currency-risk-on-us-stocks.md) (canada)
6. [US withholding tax and the W-8BEN](06-us-withholding-tax-and-w-8ben.md) (canada)
7. [Capital gains or business income](07-capital-gains-vs-business-income.md) (canada)
8. [Cost base in CAD and keeping records](08-cost-base-in-cad-and-records.md) (canada)
9. [Tax losses and the superficial loss rule](09-tax-losses-and-superficial-loss.md) (canada)
10. [Margin rules in Canada](10-margin-rules-in-canada.md) (canada, review)

<!-- lessons:end -->

## Cheat sheet

Facts marked 2026 come from the CRA, the brokers or CIPF pages linked in the lessons. Check them again before you rely on them.

### Accounts

| Account | Tax treatment | 2026 limit | Margin at IBKR Canada |
|---|---|---|---|
| Cash or margin | Gains and dividends on your return | none | Margin in non-registered only |
| TFSA | Growth and withdrawals not taxed | $7,000 | No |
| RRSP | Deduct contributions, tax on withdrawal | $33,810 dollar limit | No |
| FHSA | Deduct contributions, tax-free home withdrawal | $8,000 a year, $40,000 lifetime | No |

### Currency

| Rule | Formula or value |
|---|---|
| Return in C$ | \( 1 + r_c = (1 + r_s)(1 + r_x) \) |
| Conversion cost | \( (R_b - R_m) / R_m \) |
| Wealthsimple tiers (as of 2026) | 1.5% under $10,000, 1.0%, 0.5% from $25,000, 0% from $100,000 |
| CAD account US trade (Wealthsimple) | 1.5% on each fill, no fee in a USD account |
| Norbert's gambit | two commissions, journal fee, spreads, rate risk while in transit |

### Tax

| Rule | Value |
|---|---|
| US dividend withholding | 15% with a W-8BEN, 30% without; RRSP 0%; TFSA 15% lost; cash account 15% with credit |
| W-8BEN validity | to the end of the third calendar year after signing |
| Capital gain inclusion | one-half (CRA guide through 2025; the planned increase was cancelled) |
| ACB | average cost in C$, each leg at its own day's rate; sales do not change the average |
| Superficial loss | identical shares bought in the 61-day window and held 30 days after the sale: loss denied, added to ACB |
| Net capital loss | back 3 years, forward without limit, against taxable capital gains |
| T1135 | total foreign property cost above C$100,000 at any time in the year (not RRSP or TFSA) |

### Margin

\( V_{\text{call}} = L / (1 - m) \), where \( L \) is the loan and \( m \) the maintenance requirement. Margin interest is \( L \times \text{rate} \times \text{days} / 365 \).

### Checklist before you trade

1. Which account, and does its rules allow this trade (borrow, short, options)?
2. Which currency, and what will the conversion cost?
3. Is a W-8BEN on file and in date?
4. Where will the trade be recorded, in C$, with the day's rate?
5. For a loss, is any identical stock bought or held in the 61-day window, in any account?

