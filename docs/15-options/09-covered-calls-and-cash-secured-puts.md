# Covered calls and cash-secured puts

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">OPT</span>

After this lesson you can build a covered call and a cash-secured put from the chain, find the breakevens, maximum profit and maximum loss, and size either one against your risk limit.

Before this: [Implied volatility](08-implied-volatility.md), [Theta, vega and rho](07-theta-vega-and-rho.md), [R-multiples](../03-risk-and-position-sizing/02-r-multiples.md). You need: a calculator.

## The idea

These two strategies put you on the seller's side, with the risk limited by something you already own or have set aside. Both collect the premium. One gives up some upside, and the other takes on the obligation to buy.

A **covered call** is 100 shares of a stock plus one short call on it. The shares "cover" the call: if you are assigned, you deliver shares you already hold, so the loss on the call is not unlimited. Buying the shares and selling the call together is also called a buy-write.

A **cash-secured put** is one short put with enough cash in the account to buy 100 shares at the strike. If you are assigned, you pay the strike with the cash you set aside. Both positions are paid a **credit**: the premium you receive when you sell.

We use the lesson 3 chain for Stock A (US$50.20, expiry February 19, 2027, about three months away). You sell at the bid and buy at the ask.

## The construction

| Position | Legs | You trade |
|---|---|---|
| Covered call | Buy 100 shares, sell 1 call at 52.50 | Shares at 50.20, call at the bid 2.10 |
| Cash-secured put | Sell 1 put at 47.50, hold US$4,750 cash | Put at the bid 1.80 |

The covered call's net cost is 50.20 - 2.10 = US$48.10 a share, which is US$4,810 for the 100 shares. The put's credit is 1.80 x 100 = US$180.

Both payoffs at expiry, per share, with \(S\) the stock price at expiry:

\[ \text{covered call} = (S - 50.20) + 2.10 - \max(S - 52.50,\, 0) \]
\[ \text{cash-secured put} = 1.80 - \max(47.50 - S,\, 0) \]

- \(S - 50.20\) is the gain or loss on the shares, bought at 50.20.
- 2.10 and 1.80 are the premiums kept (the credit).
- \(\max(S - 52.50, 0)\) is what the short call costs you at expiry, and \(\max(47.50 - S, 0)\) is what the short put costs you.

| | Covered call | Cash-secured put |
|---|---|---|
| Maximum profit | (52.50 - 48.10) x 100 = US$440, at any \(S\) of 52.50 or more | US$180, at any \(S\) of 47.50 or more |
| Breakeven | 50.20 - 2.10 = 48.10 | 47.50 - 1.80 = 45.70 |
| Maximum loss | US$4,810, if the stock goes to 0 | US$4,570, if the stock goes to 0 |

The curves below show the profit at expiry (solid) and six weeks before expiry (dashed). Look at the right-hand ends: the covered call stops gaining at 52.50, and the dashed curve sits under the solid one there, because the call still has time value you would have to pay to buy it back.

![Profit of a covered call and a cash-secured put on Stock A, at expiry and six weeks before](../assets/figures/15-options/covered-call-and-put-dark.svg#only-dark)
![Profit of a covered call and a cash-secured put on Stock A, at expiry and six weeks before](../assets/figures/15-options/covered-call-and-put-light.svg#only-light)

The two have the same shape. Put-call parity (lesson 5) explains why: shares plus a short call is a synthetic short put. The cash-secured put is the cleaner way to hold that shape if you do not own the stock.

## The Greeks of the position

With the chain's own volatilities, the covered call has these Greeks per contract (100 shares):

| Greek | Value | Reading |
|---|---|---|
| Delta | +56.64 | Moves like 56.64 shares: the 100 shares less the call's 43.4 |
| Gamma | -5.40 | A rising stock adds to the call's loss rate |
| Theta | +US$1.78 a day | Time passing helps you |
| Vega | -US$9.87 per volatility point | A rise in IV hurts the short call |

The cash-secured put has delta +31.60, gamma -4.30, theta +US$1.42 a day and vega -US$8.93. You are long the stock's direction a little, short volatility, and paid for time.

## Where it works and where it fails

A covered call fits a stock you already want to hold, in a flat or slowly rising market. It pays you the premium for capping the upside at 52.50. It fails in a sharp rally (you hand the gain above 52.50 to the buyer) and in a fall (the premium of US$2.10 cushions only the first US$2.10 of loss). Selling the call does not protect the shares.

A cash-secured put fits a stock you would buy at 47.50 anyway. If the stock stays above 47.50 you keep US$180. If it falls, you buy at a net 45.70, whatever the price has fallen to. It fails when the stock drops far below the strike, because you own it at a loss.

What tests found: Whaley (Journal of Derivatives, Winter 2002) built the Cboe BuyWrite index of one-month at-the-money covered calls on the S&P 500 and found, for 1988 to 2001, about the same return as the S&P 500 with roughly one-third lower monthly volatility ([abstract](https://www.pm-research.com/content/iijderiv/10/2/35)). Bondarenko's white paper on the Cboe PutWrite index (June 1986 to December 2018) ties its better risk-adjusted record to implied volatility (VIX) averaging 19.3% against 15.1% realized from 1990 to 2018 ([Cboe summary](https://www.cboe.com/insights/posts/white-paper-shows-volatility-risk-premium-facilitated-higher-risk-adjusted-returns-for-put-index)). Both are index results before costs, not tests of single stocks.

## Assignment risk

A covered call can be assigned at any time before expiry, most often when the call is in the money and a dividend is near (lesson 14, [Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md)). Assignment takes your shares at 52.50. That is the maximum profit, so it is not a loss, but you lose the shares and any dividend you hoped to get. A cash-secured put assignment uses your cash to buy 100 shares at 47.50.

## Sizing in R

For a position that can lose almost everything, set 1R at the stop, not at the theoretical maximum loss. We use an account of US$25,000 and 1R = 1% = US$250, as in [fixed fractional sizing](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md).

<div class="example" markdown>

### Worked example: a covered call and a cash-secured put

Commissions are made up: US$0.65 per option contract, charged on opening and on closing. (Wealthsimple lists a US$0 contract fee for US-listed equity options, as of 2026, on its [fees page](https://www.wealthsimple.com/legal/fees/trade), with possible pass-through fees; other brokers charge per contract.) We ignore stock commissions.

1. Covered call: buy 100 shares at 50.20, sell the 52.50 call at the bid 2.10. Net cost 48.10 a share.
2. Stop on the stock at 46.70. Risk per share = 48.10 - 46.70 = 1.40, so US$140. Add option fees 2 x 0.65 = US$1.30: total risk US$141.30, which is 0.57R of the account. One lot fits, but it ties up US$4,810, or 19.2% of the account.
3. Result at 52.50 or more: profit = 440 - 1.30 = US$438.70, which is 1.75R. If the stop is hit, the loss is US$141.30, or 0.57R.
4. Cash-secured put: sell the 47.50 put at the bid 1.80. You reserve US$4,750. If assigned, your cost is 45.70 a share. Put the stock stop at 43.70: risk per share is 2.00, so US$200 plus US$1.30 fees = US$201.30, or 0.81R.
5. Result if the stock stays at or above 47.50: profit = 180 - 1.30 = US$178.70, or 0.71R.

The covered call risks 0.57R for a best case of 1.75R. The put risks 0.81R for a best case of 0.71R, so it pays less than it risks.

</div>

The strategy does not make the stock safer. It changes the shape of the profit, and the stop still defines the loss.

<div class="canada" markdown>

### For Canadians

Wealthsimple says covered calls and cash-secured puts are among the single-leg strategies it offers on Canadian options up to its Level 2, and that you can trade Canadian options in a TFSA and an RRSP (lesson 15 notes limits on puts in registered accounts) ([Wealthsimple CAD options](https://www.wealthsimple.com/en-ca/learn/cad-options-trading), as of 2026). Lesson 15 covers approval levels and the tax questions ([Options in Canadian accounts](15-options-in-canadian-accounts.md)).

</div>

## Common mistakes

- Selling a call on shares you do not want to lose. A rally takes the shares at 52.50.
- Judging a cash-secured put by the premium. The risk is the stock falling, not the US$180.
- Counting premium as profit before the position is closed or expires.

## Try it

1\. A covered call: shares bought at 50.20, call at 52.50 sold for 2.10. What is the profit at expiry if Stock A is at 51.00?

<details class="solution" markdown>
<summary>Answer</summary>

Shares: 51.00 - 50.20 = 0.80. The call expires worthless, so you keep 2.10. Total 2.90 a share, US$290.

</details>

2\. For the cash-secured put (47.50 strike, 1.80 credit), what is the profit at expiry if Stock A is at 44.00?

<details class="solution" markdown>
<summary>Answer</summary>

The put is worth 47.50 - 44.00 = 3.50. Profit = 1.80 - 3.50 = -1.70, so -US$170 (before fees).

</details>

3\. How much cash secures the put, and what is the cost basis if you are assigned?

<details class="solution" markdown>
<summary>Answer</summary>

47.50 x 100 = US$4,750. Cost basis = 47.50 - 1.80 = 45.70 a share.

</details>

4\. The covered call's delta is 56.64. How many dollars does the position gain for a US$1 rise, as a first estimate?

<details class="solution" markdown>
<summary>Answer</summary>

About US$56.64 per contract. The estimate shrinks as the stock nears 52.50, because the call's delta rises.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | On your broker's chain, pick one stock and find a call about 5% above it. Write the bid, the breakeven and the maximum profit of a covered call. |
| 3 | Write the same for a put about 5% below, with the cash needed. |
| 3 | Compute 1R at a stop you choose and say whether one contract fits your limit ([paper trading](../practice/paper-trading.md)). |

</div>

## Key terms

- **Covered call**: 100 shares plus one short call on them.
- **Cash-secured put**: a short put backed by cash equal to the strike times 100.
- **Credit**: the premium received when you open a position by selling.
- **Called away**: the shares are taken from you at the strike because a short call was assigned.

Next: [Vertical spreads](10-vertical-spreads.md)
