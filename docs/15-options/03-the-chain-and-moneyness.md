# The options chain and moneyness

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">OPT</span>

After this lesson you can read an options chain, say whether a contract is in, at or out of the money, split its price into intrinsic and time value, and decode an option symbol.

Before this: [Payoff diagrams](02-payoff-diagrams.md), [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md), [Tickers and symbols](../00-start-here/tickers-and-symbols.md). You need: a calculator.

## The idea

A stock has one price. A stock's options have dozens: every expiry has a row for each strike, and each row has a call and a put. A broker shows them in a table called an **options chain**. You pick the contract from the chain, so you need to read it quickly.

Below is a made-up chain for Stock A, which last traded at US$50.20. It shows one expiry about three months away (we use T = 0.25 years for the math) and five strikes. Calls first.

| Strike | Bid | Ask | Last | Volume | Open interest | IV | Delta |
|---|---|---|---|---|---|---|---|
| 45.00 | 6.90 | 7.00 | 6.95 | 120 | 1,840 | 36.1% | 0.77 |
| 47.50 | 4.95 | 5.10 | 5.00 | 310 | 2,210 | 33.0% | 0.68 |
| 50.00 | 3.35 | 3.45 | 3.40 | 1,850 | 6,420 | 30.6% | 0.57 |
| 52.50 | 2.10 | 2.20 | 2.15 | 940 | 3,980 | 29.0% | 0.43 |
| 55.00 | 1.30 | 1.35 | 1.30 | 610 | 5,120 | 28.6% | 0.31 |

Then puts, same expiry:

| Strike | Bid | Ask | Last | Volume | Open interest | IV | Delta |
|---|---|---|---|---|---|---|---|
| 45.00 | 1.25 | 1.35 | 1.30 | 260 | 3,120 | 36.1% | -0.23 |
| 47.50 | 1.80 | 1.90 | 1.85 | 780 | 4,050 | 32.9% | -0.32 |
| 50.00 | 2.65 | 2.75 | 2.70 | 1,210 | 5,210 | 30.6% | -0.43 |
| 52.50 | 3.85 | 4.00 | 3.95 | 430 | 2,060 | 29.0% | -0.57 |
| 55.00 | 5.50 | 5.65 | 5.60 | 150 | 1,480 | 28.6% | -0.69 |

## What the columns mean

The bid, ask and last work as they do for a stock (lesson 4 of part 1, [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md)). All three are per share, so the 50-strike call costs 3.45 x 100 = US$345 to buy at the ask. The midpoint is the average of bid and ask. For the 50-strike call it is (3.35 + 3.45) / 2 = 3.40.

**Volume** is the number of contracts traded today. **Open interest** is the number of contracts that exist and have not been closed or exercised. A contract opened and closed on the same day adds to volume only. Open interest usually updates once a day, so it lags. High open interest and a tight spread are the signs of a liquid contract.

The spread is a larger cost for options than for stocks. The 50-strike call has a spread of 0.10, which is 0.10 / 3.40 = 2.9% of the mid. The 55-strike call has a spread of 0.05, which is 0.05 / 1.325 = 3.8% of its mid. Buying at the ask and selling straight back at the bid loses that spread. Placing a limit order near the midpoint is the usual habit, and part 1's order-types lesson explains why ([Order types](../01-how-markets-work/05-order-types.md)).

The last two columns appear in most chains too. **IV**, implied volatility, is the volatility the market price implies; lesson 8 explains it. **Delta** is how much the option's price changes when the stock moves US$1; lesson 6 explains it. Take both as labels for now.

## Moneyness

**Moneyness** says where the strike sits against the stock price.

| | Call | Put |
|---|---|---|
| In the money (**ITM**) | Strike below the stock | Strike above the stock |
| At the money (**ATM**) | Strike at or nearest the stock | Strike at or nearest the stock |
| Out of the money (**OTM**) | Strike above the stock | Strike below the stock |

With Stock A at US$50.20, the 47.50 call is ITM (you could buy at 47.50 and the stock is worth 50.20), the 50 strike is ATM, and the 52.50 call is OTM. For puts it flips: the 52.50 put is ITM, the 47.50 put is OTM.

## Intrinsic value and time value

An option's price has two parts.

\[ \text{premium} = \text{intrinsic value} + \text{time value} \]

- **Intrinsic value** is what the option would be worth if exercised right now: \(\max(S - K, 0)\) for a call and \(\max(K - S, 0)\) for a put, where \(S\) is the stock price now. It is never negative.
- **Time value** (also called extrinsic value) is the rest: the premium minus the intrinsic value. It pays for the chance that the stock moves in your favour before expiry. An OTM option is all time value.

<div class="example" markdown>

### Worked example: splitting four prices

Stock A is at US$50.20. Use each contract's midpoint from the chain.

| Contract | Mid | Intrinsic | Time value |
|---|---|---|---|
| 47.50 call (ITM) | 5.025 | 50.20 - 47.50 = 2.70 | 5.025 - 2.70 = 2.325 |
| 50.00 call (ATM) | 3.40 | 50.20 - 50 = 0.20 | 3.40 - 0.20 = 3.20 |
| 52.50 call (OTM) | 2.15 | 0 | 2.15 |
| 52.50 put (ITM) | 3.925 | 52.50 - 50.20 = 2.30 | 3.925 - 2.30 = 1.625 |

The ATM call has the most time value, US$3.20 per share (US$320 per contract). The deeper ITM call has more intrinsic value and less time value. Time value is largest near the money and falls on both sides.

</div>

The bars show a model price for calls across strikes (volatility 30%, three months left): the blue part is intrinsic and the orange part is time value.

![Call value split into intrinsic value and time value by strike, Stock A at 50.20](../assets/figures/15-options/time-value-by-strike-dark.svg#only-dark)
![Call value split into intrinsic value and time value by strike, Stock A at 50.20](../assets/figures/15-options/time-value-by-strike-light.svg#only-light)

At expiry the time value is zero, so an ITM option is worth its intrinsic value and an OTM option is worth nothing. That is why the payoff diagrams in lesson 2 have sharp corners.

## The option symbol

An option has a symbol like a stock does. The OCC format has 21 characters: the root symbol, the expiry as YYMMDD, C or P, and the strike times 1,000 padded to 8 digits. The [Tickers and symbols](../00-start-here/tickers-and-symbols.md) page lists the parts. For Stock A, with the made-up ticker STKA, the 50-strike call that expires on Friday February 19, 2027 is:

`STKA  270219C00050000`

The root STKA is padded to six characters with spaces, 270219 is February 19, 2027, C is a call, and 00050000 is 50.000, so US$50. Many platforms drop the spaces. A US$47.50 put on the same date is `STKA  270219P00047500`.

## Common mistakes

- Choosing by the last price. A contract that traded once at 1.30 yesterday can have a bid of 1.10 today. Use the bid and ask.
- Trading a contract with a wide spread and no open interest. The cost of getting out can be larger than the premium.
- Mixing up ITM for calls and puts. A strike below the stock is ITM for a call and OTM for a put.

## Try it

1\. With Stock A at US$50.20, is the 52.50 call ITM, ATM or OTM? What is its intrinsic value and time value at the 2.15 midpoint?

<details class="solution" markdown>
<summary>Answer</summary>

OTM: the strike is above the stock. Intrinsic value = max(50.20 - 52.50, 0) = 0, so the time value is the whole 2.15.

</details>

2\. What are the intrinsic and time values of the 52.50 put at its 3.925 midpoint?

<details class="solution" markdown>
<summary>Answer</summary>

It is ITM. Intrinsic value = 52.50 - 50.20 = 2.30. Time value = 3.925 - 2.30 = 1.625 (about US$1.63 per share).

</details>

3\. You buy 5 of the 50-strike calls at the ask and sell them at once at the bid. How much do you lose to the spread?

<details class="solution" markdown>
<summary>Answer</summary>

The ask is 3.45 and the bid is 3.35, a difference of 0.10. 0.10 x 100 x 5 = US$50.

</details>

4\. Decode `STKA  270219P00047500`.

<details class="solution" markdown>
<summary>Answer</summary>

Root STKA, expiry 270219 (February 19, 2027), P for a put, strike 00047500 = 47,500 / 1,000 = US$47.50.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Open a chain for a liquid stock. For the nearest strike to the price, write the bid, ask, spread as a percent of the mid, volume and open interest for the call and the put. |
| 3 | Pick one ITM and one OTM option. Split each mid price into intrinsic and time value. |
| 3 | Find the symbol your platform shows for one of them and decode it by hand. |

</div>

## Key terms

- **Options chain**: a table of every strike and expiry of a stock, with a call and a put for each.
- **Volume**: the contracts traded today.
- **Open interest**: the number of contracts that exist and have not been closed or exercised.
- **Moneyness**: where the strike sits relative to the stock price.
- **In the money (ITM), at the money (ATM), out of the money (OTM)**: a strike that gives value if exercised now, near the stock price, or that gives none.
- **Intrinsic value**: what an option is worth if exercised now.
- **Time value**: the premium minus the intrinsic value.

Next: [What sets an option's price](04-what-sets-an-option-price.md)
