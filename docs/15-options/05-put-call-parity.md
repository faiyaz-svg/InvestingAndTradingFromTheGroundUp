# Put-call parity

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">OPT</span>

After this lesson you can state the put-call parity relationship, use it to find a missing option price, and say why it holds exactly for European options but only roughly for American ones.

Before this: [What sets an option's price](04-what-sets-an-option-price.md), [Short selling](../01-how-markets-work/08-short-selling.md). You need: a calculator.

## The idea

A call and a put with the same strike and expiry look like opposites. They are tied together by the stock. Take two portfolios.

- Portfolio 1: buy one call (strike 50) and put aside enough cash to pay the strike at expiry.
- Portfolio 2: buy one share and buy one put (strike 50).

At expiry, if the stock is above 50, portfolio 1 exercises the call: it pays the 50 it set aside and owns one share. The put in portfolio 2 expires worthless, so portfolio 2 is one share too. If the stock is below 50, the call is worthless, so portfolio 1 is the cash, 50. Portfolio 2 exercises the put and sells its share for 50, so it is also 50 in cash.

In both cases the two portfolios are worth the same thing at expiry. If they are worth the same later, they must cost the same now. If they did not, a trader could buy the cheaper and sell the dearer and keep the difference with no risk. That is **put-call parity**.

## How it works

For European options on a stock paying no dividend:

\[ C + K e^{-rT} = P + S \quad\Longleftrightarrow\quad C - P = S - K e^{-rT} \]

- \(C\) and \(P\) are the call and put prices per share, for the same strike and expiry.
- \(S\) is the stock price now and \(K\) the strike, both in US$.
- \(K e^{-rT}\) is the present value of the strike: the cash you put aside today, which grows to \(K\) by expiry at the risk-free rate \(r\) (a decimal per year) over \(T\) years.

With a dividend yield \(q\), replace \(S\) with \(S e^{-qT}\):

\[ C - P = S e^{-qT} - K e^{-rT} \]

With known cash dividends before expiry, subtract their present value from \(S\) instead: \(C - P = S - PV(\text{dividends}) - K e^{-rT}\), where \(PV\) is the present value. The shareholder in portfolio 2 collects those dividends and the call holder does not, so portfolio 1 needs extra cash equal to their present value to match.

<div class="example" markdown>

### Worked example: the base case and a mispricing

Take the lesson 4 numbers: \(S = 50\), \(K = 50\), \(T = 0.25\), \(r = 4\%\), \(\sigma = 30\%\).

1. Call = 3.2297 and put = 2.7322, so \(C - P\) = 0.4975.
2. \(S - K e^{-rT}\) = 50 - 49.5025 = 0.4975. They match, as they must, since both prices came from the same model.
3. With a 2% dividend yield, the call is 3.0926 and the put 2.8445. \(C - P\) = 0.2481, and \(S e^{-qT} - K e^{-rT}\) = 49.7506 - 49.5025 = 0.2481.

Now a market that breaks the rule. Stock A is US$50 and the market quotes the 50-strike call at 3.60 and the put at 2.70 (made-up).

4. \(C - P\) = 0.90, but parity says 0.4975. The call is too dear compared with the put.
5. Sell the call, buy the put and buy the stock. The cost today is 50 + 2.70 - 3.60 = US$49.10.
6. At expiry, whatever the stock does, you end with US$50: the stock is called away at 50 or put at 50. Its present value is 49.5025.
7. You paid 49.10 for something worth 49.5025, a gain of 0.4025 per share today, which is US$40.25 per contract before costs.

</div>

Steps 5 to 7 are a **conversion**, and the opposite trade (buy the call, sell the put, sell the stock short) is a **reversal**. Both are riskless on paper. In practice professional market makers close such gaps in a fraction of a second, so you will rarely see a gap this large. Commissions, the bid-ask spread on three legs, and the cost of borrowing a stock to short it all eat what is left.

The made-up chain from lesson 3 follows parity closely. For the 50 strike, \(C - P\) = 3.40 - 2.70 = 0.70 at the midpoints, and \(S - K e^{-rT}\) = 50.20 - 49.5025 = 0.6975. The two differ by a quarter of a cent.

## Synthetic positions

Rearrange parity: \(C - P = S - K e^{-rT}\). A long call and a short put at the same strike behave like owning the stock. This is **synthetic long stock**. Its profit at expiry is a straight line, as the figure shows.

![A long call plus a short put gives a straight profit line like holding 100 shares, strike 50](../assets/figures/15-options/synthetic-long-dark.svg#only-dark)
![A long call plus a short put gives a straight profit line like holding 100 shares, strike 50](../assets/figures/15-options/synthetic-long-light.svg#only-light)

Look at the dashed line: it is the sum of the other two, a straight line with slope 100 (US$100 per US$1 move), the same as 100 shares. It crosses zero at the strike plus the net cost, 50 + 0.4975 = US$50.50. The reverse, a short call and a long put, is **synthetic short stock**. These matter later: a spread built one way can be rebuilt another way with the same payoff.

## American options

Parity is exact only for European options with no dividends, because the two-portfolio argument needs the holder not to exercise early. Single-stock options are American, and the holder of an American option can exercise early, which is an extra right. Without dividends, the relationship becomes a pair of bounds:

\[ S - K \le C - P \le S - K e^{-rT} \]

Here \(C\) and \(P\) are the American prices. For Stock A that is 0 to 0.4975 (the American put can be worth more than the European one). With dividends the bounds shift. So you cannot treat parity as an exact test of an American chain, and what looks like a gap may only be the value of early exercise or a dividend. Lesson 14 covers early exercise ([Assignment, exercise and 0DTE](14-assignment-exercise-and-0dte.md)).

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def parity_gap(call, put, S, K, T, r, q=0.0):
    """Market C - P minus the parity value. About 0 for European options."""
    return (call - put) - (S * math.exp(-q * T) - K * math.exp(-r * T))

print(round(parity_gap(3.60, 2.70, 50, 50, 0.25, 0.04), 4))
print(round(parity_gap(3.40, 2.70, 50.20, 50, 0.25, 0.04), 4))
```

</details>

## Common mistakes

- Using parity with different strikes or expiries. It needs the same strike and the same expiry.
- Forgetting the dividend. A stock that pays one before expiry moves the call and put apart.
- Treating a gap as free money. After spreads, commissions and borrow costs, most gaps are gone.

## Try it

1\. A European call has \(S = 100\), \(K = 100\), \(T = 0.5\), \(r = 4\%\) and the call costs 7.50. What does parity say the put costs?

<details class="solution" markdown>
<summary>Answer</summary>

\(S - K e^{-rT}\) = 100 - 100 x \(e^{-0.02}\) = 100 - 98.0199 = 1.9801. Put = 7.50 - 1.9801 = US$5.52.

</details>

2\. You buy the 50 call at 3.45 (the ask) and sell the 50 put at 2.65 (the bid). What is the net cost per share, and the breakeven for the pair at expiry?

<details class="solution" markdown>
<summary>Answer</summary>

Net cost = 3.45 - 2.65 = 0.80. The pair is synthetic long stock bought at 50 + 0.80 = US$50.80, so the breakeven is US$50.80.

</details>

3\. Stock A is US$50, the 50 call is 3.10 and the 50 put is 3.00, all European, with \(T = 0.25\) and \(r = 4\%\). What does parity say, and what trade closes the gap?

<details class="solution" markdown>
<summary>Answer</summary>

\(C - P\) = 0.10, and parity says 0.4975, so the call is too cheap against the put. Do a reversal: buy the call, sell the put, short the stock. You receive 50 + 3.00 - 3.10 = 49.90 and owe the strike of 50 at expiry, which has a present value of 49.5025. The gain today is 49.90 - 49.5025 = 0.3975, or US$39.75 per contract.

</details>

4\. Why is parity only a range for American options?

<details class="solution" markdown>
<summary>Answer</summary>

The holder can exercise early, so the two portfolios no longer match exactly at all times. The extra right adds value to the American put (and to calls before a dividend), so only the inequality \(S - K \le C - P \le S - K e^{-rT}\) holds without dividends.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Take one strike from a chain for a stock with no dividend. Compute \(C - P\) from the mids and \(S - K e^{-rT}\) using a 4% rate. Write the gap. |
| 3 | Do it for a second strike. Is the gap the same sign? |
| 2 | Run the code with both strikes and compare with your hand numbers. |

</div>

## Key terms

- **Put-call parity**: the relationship \(C - P = S - K e^{-rT}\) between a European call and put with the same strike and expiry.
- **Present value**: today's value of an amount paid later, discounted at the interest rate.
- **Conversion and reversal**: trades that lock in the parity gap, one buying the stock and one shorting it.
- **Synthetic long stock**: a long call and a short put at the same strike, which behave like owning the stock.
- **Synthetic short stock**: a short call and a long put at the same strike.

Next: [Delta and gamma](06-delta-and-gamma.md)
