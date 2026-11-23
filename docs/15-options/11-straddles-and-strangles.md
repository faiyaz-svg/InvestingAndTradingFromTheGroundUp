# Straddles and strangles

<span class="tag tag-strategy">Strategy</span> <span class="tag tag-part">OPT</span>

After this lesson you can build a long straddle and a long strangle, find both breakevens, compare the move they need with the implied expected move, and say when the cost does not fit your risk limit.

Before this: [Vertical spreads](10-vertical-spreads.md), [Implied volatility](08-implied-volatility.md), [Theta, vega and rho](07-theta-vega-and-rho.md). You need: a calculator.

## The idea

A call wins if the stock rises. A put wins if it falls. Suppose you expect a large move and have no view on the direction: an earnings report, a court ruling, a data release. Buying both pays when the stock moves far enough either way.

A **long straddle** buys a call and a put with the same strike and expiry. A **long strangle** buys an out-of-the-money call and an out-of-the-money put with the same expiry, so it costs less and needs a larger move. Both are debits, and both are long volatility: they gain when the stock moves more than the market priced, or when IV rises.

## The construction

Stock A is US$50.20, expiry February 19, 2027. Buy at the ask.

| Position | Trade | Debit |
|---|---|---|
| Long straddle, strike 50 | Buy the 50 call at 3.45, buy the 50 put at 2.75 | 6.20, so US$620 |
| Long strangle, 47.50 and 52.50 | Buy the 47.50 put at 1.90, buy the 52.50 call at 2.20 | 4.10, so US$410 |

With the total debit \(D\) per share, the strikes \(K_p\) (put) and \(K_c\) (call), and \(S\) the stock at expiry:

\[ \text{profit} = \max(S - K_c, 0) + \max(K_p - S, 0) - D \]

- For the straddle \(K_p = K_c = 50\). For the strangle \(K_p = 47.50\) and \(K_c = 52.50\).
- The upper breakeven is \(K_c + D\) and the lower breakeven is \(K_p - D\).
- The maximum loss is \(D \times 100\), reached at expiry when \(S\) lies between the strikes.
- The maximum profit is unlimited on the upside. On the downside it is \((K_p - D) \times 100\), if the stock goes to 0.

| | Long straddle | Long strangle |
|---|---|---|
| Maximum loss | US$620, at \(S = 50\) | US$410, at \(S\) from 47.50 to 52.50 |
| Lower breakeven | 50 - 6.20 = 43.80 | 47.50 - 4.10 = 43.40 |
| Upper breakeven | 50 + 6.20 = 56.20 | 52.50 + 4.10 = 56.60 |
| Maximum profit | Unlimited up, (43.80 x 100) = US$4,380 down | Unlimited up, US$4,340 down |

The strangle's flat bottom is its cost saving: you lose the same US$410 anywhere between the strikes. The dashed line is the position six weeks before expiry. It sits above the solid one in the middle, because the options still have time value.

![Profit of a long straddle and a long strangle on Stock A, at expiry and six weeks before](../assets/figures/15-options/straddle-strangle-dark.svg#only-dark)
![Profit of a long straddle and a long strangle on Stock A, at expiry and six weeks before](../assets/figures/15-options/straddle-strangle-light.svg#only-light)

## The move you need

The straddle costs 6.20, which is 12.4% of the stock price. Compare that with the expected move of lesson 8. At 30.6% IV and three months, the one-standard-deviation move is 50.20 x 0.306 x 0.5 = US$7.68. The straddle's price is about 0.8 of that number, and the factor comes from the normal curve: the average absolute move of a normal variable is about 0.8 of its standard deviation. So the market prices the straddle at about the typical move, and you must beat that average move to profit. You need the stock to end outside 43.80 to 56.20, which is a move of at least US$6.20 from the strike of 50 in either direction.

## The Greeks

At the chain's volatilities, per contract, the straddle has delta +13.34, gamma +10.25, theta -US$3.31 a day and vega +US$19.75 per volatility point. The strangle has delta +11.75, gamma +9.71, theta -US$3.20 and vega +US$18.80. Delta is small, so the position does not care about direction at first. Gamma is positive, so it gains from a large move. Theta is the daily cost: 14 days at -US$3.31 is about -US$46 if nothing else changes.

## When it works and how it fails

The idea is that the stock moves more than the options imply. It fails in two ways. The stock can move less than the premium, and theta eats the debit. And the IV can fall after the event: this is the **IV crush** of lesson 7. If IV falls five points the day after earnings and the stock does not move, the straddle loses about 5 x 19.75 = US$98.75 at once, before any decay. Options priced before a known event already contain the move the market expects, so you profit only from a bigger one.

What tests found: Coval and Shumway (Journal of Finance, 2001) studied zero-beta at-the-money straddles on the S&P 500 and report that they lose about 3% a week on average. They read that as a sign of an extra priced factor, such as systematic stochastic volatility ([paper](https://econpapers.repec.org/RePEc:bla:jfinan:v:56:y:2001:i:3:p:983-1009)). That is an index study from a past sample, and it does not say a straddle held through one earnings date loses money, but it is a warning against buying straddles as a habit.

## Assignment risk

A long straddle or strangle has no assignment risk, because you hold only long options. The opposite side does. Selling a straddle (the bids are 3.35 and 2.65, a credit of US$600) has an unlimited loss on the call and a loss of up to 50 x 100 = US$5,000 less the credit on the put, and brokers allow it only at the highest approval level. It is not a defined-risk position, so it is outside the paper trading block of lesson 15.

## Sizing in R

For a long straddle the maximum loss is the debit, so 1R can be the debit plus fees. With a US$25,000 account and 1R = US$250 the numbers do not fit, and that is a result.

<div class="example" markdown>

### Worked example: a straddle that is too big, then sized

Commissions are made up: US$0.65 per contract per leg, charged on opening and on closing. A round trip for two legs is US$2.60.

1. Straddle cost with fees: 620 + 2.60 = US$622.60. For US$25,000 and 1R = US$250, that is 2.49R, so zero contracts. The strangle, at 410 + 2.60 = US$412.60, is 1.65R, also zero.
2. The smallest account where one straddle fits 1% is 622.60 / 0.01 = US$62,260. We use US$65,000, so 1R = US$650 and one straddle risks 622.60 / 650 = 0.96R.
3. Stock A at 57 at expiry: the call is worth 7.00, the put 0. Profit = (7.00 - 6.20) x 100 - 2.60 = US$77.40, which is 0.12R.
4. Stock A at 60: profit = (10.00 - 6.20) x 100 - 2.60 = US$377.40, or 0.58R.
5. Stock A at 50: both expire worthless. Loss = US$622.60, or 0.96R.

A straddle that expires 14% above the strike earns only 0.12R, so the payoff is lopsided: a lot of room for a small gain unless the move is large.

</div>

<div class="canada" markdown>

### For Canadians

Long straddles and strangles are two long single-leg trades, so they need no margin. Check that your broker's approval level lets you open two single-leg buys in one order (some platforms treat the two together as a multi-leg order). Lesson 15 covers accounts.

</div>

## Common mistakes

- Buying a straddle right before an event without comparing its price with the expected move.
- Ignoring IV crush. A correct call on the size of the move can still lose.
- Sizing by the premium of one leg. The risk is the debit of both.

## Try it

1\. Buy the 52.50 call at the ask 2.20 and the 52.50 put at the ask 4.00. What is the debit, and what are the breakevens?

<details class="solution" markdown>
<summary>Answer</summary>

Debit = 2.20 + 4.00 = 6.20, US$620. Breakevens: 52.50 + 6.20 = 58.70 and 52.50 - 6.20 = 46.30.

</details>

2\. For the strangle (debit 4.10), what is the profit at expiry if Stock A is at 58?

<details class="solution" markdown>
<summary>Answer</summary>

The 52.50 call is worth 5.50, the put 0. Profit = 5.50 - 4.10 = 1.40, so US$140 before fees.

</details>

3\. The straddle's vega is US$19.75 per volatility point. IV falls from 31% to 27% and the stock does not move. What is the first estimate of the loss?

<details class="solution" markdown>
<summary>Answer</summary>

4 x 19.75 = US$79.00.

</details>

4\. The straddle costs US$622.60 with fees. What account size makes it 1% risk?

<details class="solution" markdown>
<summary>Answer</summary>

622.60 / 0.01 = US$62,260.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a stock with a coming earnings date. Write the at-the-money straddle's ask prices, the debit and both breakevens. |
| 3 | Compute the expected move from the IV and compare it with the breakevens. |
| 3 | Write whether the debit fits 1R of your account and the number of contracts ([paper trading](../practice/paper-trading.md)). |

</div>

## Key terms

- **Long straddle**: a call and a put with the same strike and expiry, both bought.
- **Long strangle**: an out-of-the-money call and an out-of-the-money put with the same expiry, both bought.
- **Long volatility**: a position that gains when volatility rises or the stock moves more than priced.

Next: [Iron condors and butterflies](12-iron-condors-and-butterflies.md)
