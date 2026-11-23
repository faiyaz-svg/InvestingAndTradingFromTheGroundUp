# Options strategies

Every strategy from [options](../15-options/index.md), with its legs, whether it opens with a debit or a credit, the profit and loss limits and the breakeven. Let \(S\) be the stock price at expiry, \(K\) a strike, \(p\) a premium per share, \(W\) the strike width, \(D\) the net debit or credit per share and the contract multiplier 100. Each lesson works the numbers on Stock A, a made-up stock, and gives the Greeks for its example.

The formulas are in [Formulas](formulas.md). Greek values are per contract from each lesson's example, at the chain's volatilities. They change with the stock price, time and volatility, so read them as the sign and rough size of each exposure.

## Single options and stock-plus-option positions

| Strategy | Legs | Debit or credit | Max profit | Max loss | Breakeven | Outlook | Main Greeks | Assignment risk | Lesson |
|---|---|---|---|---|---|---|---|---|---|
| Long call | Buy a call | Debit | Unlimited | The premium, \(p \times 100\) | \(K + p\) | Rise | Long delta, long gamma, long vega, short theta | None (you hold the right) | [Payoff diagrams](../15-options/02-payoff-diagrams.md) |
| Long put | Buy a put | Debit | \((K - p) \times 100\), if the stock goes to 0 | The premium, \(p \times 100\) | \(K - p\) | Fall | Short delta, long gamma, long vega, short theta | None | [Payoff diagrams](../15-options/02-payoff-diagrams.md) |
| Covered call | Buy 100 shares, sell 1 call | Credit for the call | Stops at the call strike: for the lesson's example, US$440 at 52.50 or more | The cost of the shares less the credit, if the stock goes to 0 (US$4,810) | Share cost less the credit (48.10) | Flat or slowly rising | Delta +56.64, gamma -5.40, theta +US$1.78 a day, vega -US$9.87 | The call can be assigned any time, most often when it is in the money and a dividend is near; you lose the shares and the dividend | [Covered calls and cash-secured puts](../15-options/09-covered-calls-and-cash-secured-puts.md) |
| Cash-secured put | Sell 1 put, hold cash for 100 shares at the strike | Credit | The credit (US$180) | Strike less the credit, times 100, if the stock goes to 0 (US$4,570) | Strike less the credit (45.70) | You would buy the stock at the strike anyway | Delta +31.60, gamma -4.30, theta +US$1.42 a day, vega -US$8.93 | Assignment uses your cash to buy 100 shares at the strike | [Covered calls and cash-secured puts](../15-options/09-covered-calls-and-cash-secured-puts.md) |

## Vertical spreads

| Strategy | Legs | Debit or credit | Max profit | Max loss | Breakeven | Outlook | Main Greeks | Assignment risk | Lesson |
|---|---|---|---|---|---|---|---|---|---|
| Bull call spread | Buy a lower call, sell a higher call | Debit | \((W - D) \times 100\) | \(D \times 100\) | Lower strike plus the debit | Rise | Example: delta +25.71, gamma +0.21, theta -US$0.39 a day, vega +US$1.02 | The short leg can be assigned early | [Vertical spreads](../15-options/10-vertical-spreads.md) |
| Bear put spread | Buy a higher put, sell a lower put | Debit | \((W - D) \times 100\) | \(D \times 100\) | The mirror image of the bull call spread | Fall | Mirror of the bull call spread | The short leg can be assigned early | [Vertical spreads](../15-options/10-vertical-spreads.md) |
| Bull put spread | Sell a higher put, buy a lower put | Credit | \(D \times 100\) | \((W - D) \times 100\) | Higher strike minus the credit | Stay up | Example: delta +20.70, gamma -1.81, theta +US$0.03 a day, vega -US$2.32 | If the short put is assigned you buy 100 shares and still hold the long put; the broker may need cash or margin | [Vertical spreads](../15-options/10-vertical-spreads.md) |
| Bear call spread | Sell a lower call, buy a higher call | Credit | \(D \times 100\) | \((W - D) \times 100\) | The mirror image of the bull put spread | Stay down | Mirror of the bull put spread | The short leg can be assigned early | [Vertical spreads](../15-options/10-vertical-spreads.md) |

## Volatility and range strategies

| Strategy | Legs | Debit or credit | Max profit | Max loss | Breakeven | Outlook | Main Greeks | Assignment risk | Lesson |
|---|---|---|---|---|---|---|---|---|---|
| Long straddle | Buy a call and a put, same strike and expiry | Debit | Unlimited up; \((K_p - D) \times 100\) down | \(D \times 100\), with \(S\) at the strike | \(K_c + D\) and \(K_p - D\) | A large move in either direction | Example: delta +13.34, gamma +10.25, theta -US$3.31 a day, vega +US$19.75 | None on the long side | [Straddles and strangles](../15-options/11-straddles-and-strangles.md) |
| Long strangle | Buy an out-of-the-money call and put, same expiry | Debit | Unlimited up; \((K_p - D) \times 100\) down | \(D \times 100\), with \(S\) between the strikes | \(K_c + D\) and \(K_p - D\) | A larger move than the straddle needs | Example: delta +11.75, gamma +9.71, theta -US$3.20 a day, vega +US$18.80 | None on the long side | [Straddles and strangles](../15-options/11-straddles-and-strangles.md) |
| Short straddle | Sell a call and a put, same strike | Credit | The credit | Unlimited on the call; up to the strike times 100 less the credit on the put | Not worked in the lesson | A quiet stock | Short volatility | Not defined-risk; highest approval level only, outside the book's paper blocks | [Straddles and strangles](../15-options/11-straddles-and-strangles.md) |
| Iron condor | Bull put spread below the stock plus bear call spread above it (four legs) | Credit | \(C \times 100\), for \(S\) between the short strikes | \((W - C) \times 100\) | Short put strike less \(C\); short call strike plus \(C\) | A range | Example: delta -3.42, gamma -1.48, theta +US$0.30 a day, vega -US$2.40 | Short legs can be assigned; close before the last day if the stock is near a short strike | [Iron condors and butterflies](../15-options/12-iron-condors-and-butterflies.md) |
| Call butterfly | Buy one lower call, sell two middle calls, buy one upper call | Debit | \((W - D) \times 100\), at the middle strike | \(D \times 100\) | Lowest strike plus \(D\); highest strike less \(D\) | The stock pins near the middle strike | Example: delta -1.59, gamma -0.54, theta +US$0.14 a day, vega -US$0.94 | Only the short legs can be assigned | [Iron condors and butterflies](../15-options/12-iron-condors-and-butterflies.md) |

## Time spreads

| Strategy | Legs | Debit or credit | Max profit | Max loss | Breakeven | Outlook | Main Greeks | Assignment risk | Lesson |
|---|---|---|---|---|---|---|---|---|---|
| Call calendar | Sell a near-dated call, buy a far-dated call, same strike | Debit | About US$119 in the lesson's model, with the stock at the strike when the near leg expires | The debit, if you close both legs when the near leg expires | About 47.13 and 53.66 in the lesson's model | The stock stays near the strike | Example: delta +0.94, gamma -1.35, theta +US$0.50 a day, vega +US$2.11 | The short near call can be assigned, mostly shortly before a dividend; you are then short shares until you exercise or close | [Calendars and diagonals](../15-options/13-calendars-and-diagonals.md) |
| Call diagonal | Sell a near-dated call at a higher strike, buy a far-dated call at a lower strike | Debit | Not stated as a single figure; the lesson's model shows it leaning right | The debit, if the stock falls | About 49.75 in the lesson's model | Mildly bullish | Example: delta +16.84, gamma -1.21, theta +US$0.37 a day, vega +US$2.28 | Same as the calendar | [Calendars and diagonals](../15-options/13-calendars-and-diagonals.md) |

The calendar and diagonal figures come from a model price for the far leg, so treat them as estimates. A real far-dated option carries its own volatility on the near expiry date.

## Reading the table

- A defined-risk strategy has a known maximum loss. Size by the maximum loss plus fees, with 1R from your plan. If one contract does not fit, record that and pick a cheaper trade ([Options in Canadian accounts](../15-options/15-options-in-canadian-accounts.md), paper block 5).
- A credit spread usually wins more often than it loses, but each loss is larger than each win. The lesson found no published cost-adjusted test of spreads, condors, butterflies, calendars or diagonals on single stocks.
- Index results for covered calls and put-writing are before costs and are not tests of single stocks ([Covered calls and cash-secured puts](../15-options/09-covered-calls-and-cash-secured-puts.md)).
- What each strategy can do in a TFSA, RRSP or margin account depends on the account and the broker. See the [Canadian tax quick reference](canadian-tax-quick-reference.md) and [Options in Canadian accounts](../15-options/15-options-in-canadian-accounts.md).
- Early exercise and pin risk are in [Assignment, exercise and 0DTE](../15-options/14-assignment-exercise-and-0dte.md).
