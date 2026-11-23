# Assignment, exercise and 0DTE

<span class="tag tag-skill">Skill</span> <span class="tag tag-part">OPT</span>

After this lesson you can say what happens when an option is exercised or assigned, spot when early exercise is likely, handle expiry day without a surprise, and size a same-day option trade.

Before this: [Calls and puts](01-calls-and-puts.md), [Covered calls and cash-secured puts](09-covered-calls-and-cash-secured-puts.md), [Delta and gamma](06-delta-and-gamma.md). You need: a calculator.

## The idea

When a holder exercises, a seller is assigned. If that is you, stock moves in or out of your account at the strike, possibly before you have looked.

## How exercise and assignment work

When a call holder exercises, the holder buys 100 shares at the strike and the writer sells them. When a put holder exercises, the holder sells 100 shares at the strike and the writer buys them. Exercise notices go to the OCC, which assigns them at random among its clearing members, and your broker then assigns a customer under its own method ([OCC options education, exercise FAQ](https://www.optionseducation.org/referencelibrary/faq/options-exercise), as of 2026). You may learn of an assignment only the next morning.

At expiry, the OCC's **exercise by exception** rule exercises an equity option that is in the money by US$0.01 or more, unless the holder instructs otherwise. The OCC calls this an administrative procedure, not strictly automatic, since clearing members can choose not to exercise, and a firm may apply its own threshold ([same FAQ](https://www.optionseducation.org/referencelibrary/faq/options-exercise)). Interactive Brokers warns that a spread can end unhedged if the long leg is in the money by under US$0.01 and the short leg by more ([IBKR option expiration FAQ](https://ibkb.interactivebrokers.com/fr/node/1718)). To override the default, tell your broker before its cutoff.

## Early exercise

American options can be exercised on any day, but early exercise gives up the option's time value, which selling the option would keep. There is one common exception.

A call holder who exercises before the ex-dividend date gets the dividend. An assigned call writer loses it. With \(D\) the dividend per share and \(i\) the interest you lose by paying the strike early:

\[ \text{exercise early if } D > \text{time value} + i \]

- \(D\) is the dividend, US$ per share.
- The time value is the option's bid less its intrinsic value (lesson 3).
- \(i\) is the interest on the strike for the days you pay early, \(K \times r \times \text{days} / 365\).

<div class="example" markdown>

### Worked example: when a call is exercised before the ex-date

Stock A is US$50.20 and goes ex-dividend tomorrow, with a made-up dividend of US$0.50. You hold a 45-strike call. On the lesson 3 chain its bid is 6.90, so the time value is 6.90 - (50.20 - 45) = 1.70. That is larger than 0.50, so nobody exercises early.

Now suppose the call's bid is 5.25 with the stock unchanged. Intrinsic value is 5.20, so the time value is 0.05.

1. Sell the call: you receive 5.25.
2. Exercise instead: you pay 45, own a stock worth 50.20, and receive the 0.50 dividend. That is worth 5.20 + 0.50 = 5.70.
3. Interest lost on 45 for one day at 4%: 45 x 0.04 / 365 = 0.005.
4. Exercise gains 5.70 - 5.25 - 0.005 = about 0.45 a share, which is US$45 per contract.

A short 45 call here is likely to be assigned, and a covered call writer loses the dividend as well as the shares.

</div>

## Pin risk

**Pin risk** is the chance that the stock closes near your short strike at expiry, so assignment is uncertain. Suppose you are short a 50 call and the stock closes Friday at 50.02. The option is in the money by US$0.02 and likely exercised, so you are short 100 shares at 50 on Monday. At expiry the option cost you US$2. If the stock gaps to 53 on Monday, you are down (53 - 50) x 100 = US$300. 

## 0DTE options

A **0DTE** option has zero days to expiration. FINRA describes a 0DTE strategy as opening a position on the option's expiration day, even though the contract may have been listed weeks or months earlier, and says that some options now expire almost every day of the week ([FINRA, "Zeroing In on an Options Trading Strategy: 0DTE"](https://www.finra.org/investors/insights/zeroing-in-options-trading-strategy), published June 4, 2026). FINRA warns that losses can come fast and buyers can lose the entire premium. It adds that a brokerage may liquidate a physically settled position before the close if you lack the funds or shares for a possible obligation, which can cap your profit or cause a loss.

Gamma grows fast near expiry. For the 50 call at the money, with 30% volatility and 4% rates, gamma is 0.0527 with three months left and 0.9763 with 6.5 hours left, about 18.5 times higher. It reaches 4.98 with 15 minutes left. Delta swings from near 0 to near 1 within about 50 cents.

The left of the figure shows the call's value as the day runs down, for three stock prices, and the right shows the gamma peak. We use 6.5 / 8,760 of a year for 6.5 hours, which ignores the overnight gap.

![The 50-strike call's value in the last 6.5 hours for three stock prices, and its gamma 6.5 hours and 30 minutes before expiry](../assets/figures/15-options/zero-dte-dark.svg#only-dark)
![The 50-strike call's value in the last 6.5 hours for three stock prices, and its gamma 6.5 hours and 30 minutes before expiry](../assets/figures/15-options/zero-dte-light.svg#only-light)

| Hours left | 6.5 | 3 | 1 | 0.5 | 0.25 |
|---|---|---|---|---|---|
| ATM call value, per contract | US$16.37 | US$11.11 | US$6.41 | US$4.53 | US$3.20 |

The one-standard-deviation move over the 6.5 hours is 50 x 0.30 x \(\sqrt{6.5/8760}\) = US$0.41. After three hours, a US$0.50 rise takes the call to US$50.47 and a US$0.50 fall takes it to US$0.39.

<div class="example" markdown>

### Worked example: a same-day call sized by its premium

Stock A is US$50.00 with 6.5 hours to expiry. Buy the 50 call at a made-up ask of 0.17. Commissions are made up: US$0.65 per contract, opening and closing.

1. Premium US$17. Add fees 2 x 0.65 = US$1.30, so the loss if it expires worthless is US$18.30 per contract. With US$25,000 and 1R = US$250, 250 / 18.30 = 13.7, so 13 contracts, a risk of 13 x 18.30 = US$237.90, or 0.95R.
2. Three hours later Stock A is at 50.50 and the call is worth US$50.47. Close: profit per contract = 50.47 - 17 - 1.30 = US$32.17. For 13: US$418.21, or 1.67R.
3. Stock A at 49.50: the call is worth US$0.39. Loss per contract = 17 - 0.39 + 1.30 = US$17.91. For 13: -US$232.83, or -0.93R.
4. Stock A unchanged: the call is worth US$11.11. Loss = 17 - 11.11 + 1.30 = US$7.19 per contract, or -US$93.47 for 13 (-0.37R).

A US$1 range in the stock spans 2.6R of outcomes, and an unchanged stock loses 0.37R in three hours.

</div>

We found no published test of retail 0DTE strategies after costs, so we quote none.

<div class="canada" markdown>

### For Canadians

Your Canadian broker has its own exercise threshold, instruction cutoff and rule for closing short positions that lack cash or shares. Wealthsimple's fee schedule charges US$45 for each early exercise or do-not-exercise instruction on equity and ETF options (as of 2026, [fees](https://www.wealthsimple.com/legal/fees/trade)). The other rules were not confirmed for this book, so ask in writing before your first short option.

</div>

## Common mistakes

- Keeping a deep in-the-money short call through an ex-dividend date. Assignment is likely.
- Sizing a same-day option below its true risk. The premium can go to zero in an hour, so 1R is the premium plus fees.

## Try it

1\. Stock A is at 50.20, a 45 call has a bid of 6.90, and a dividend of 0.30 is coming. Should you exercise early?

<details class="solution" markdown>
<summary>Answer</summary>

Time value = 6.90 - 5.20 = 1.70. The dividend 0.30 is less than 1.70, so no. Selling the option keeps the time value.

</details>

2\. A short 50 call expires with the stock at 50.03. Is it likely to be exercised, and what is the loss at expiry?

<details class="solution" markdown>
<summary>Answer</summary>

Yes, it is in the money by 0.03, which is over the US$0.01 threshold. The loss at expiry is 0.03 x 100 = US$3 before the premium you collected.

</details>

3\. The 50 call with 3 months left has gamma 0.0527 and with 6.5 hours left 0.9763. By what factor did gamma grow?

<details class="solution" markdown>
<summary>Answer</summary>

0.9763 / 0.0527 = 18.5.

</details>

4\. In the worked example, how many contracts fit if 1R is US$500?

<details class="solution" markdown>
<summary>Answer</summary>

500 / 18.30 = 27.3, so 27 contracts.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Read your broker's page on option expiry and exercise: the threshold, the cutoff time and what it does to short options. Write the three facts down. |
| 3 | Look up the next ex-dividend date of one stock you know. Mark the day before it as a day to review any short calls. |
| 3 | Compute how many same-day contracts fit your 1R at a premium you pick, with fees. |

</div>

## Key terms

- **Exercise by exception**: the OCC procedure that exercises an expiring equity option in the money by US$0.01 or more unless the holder says not to.
- **Early exercise**: exercising an American option before expiry.
- **Pin risk**: the chance that the stock closes near a short strike at expiry, leaving assignment uncertain.
- **0DTE**: an option with zero days to expiration, traded on its last day.

Next: [Options in Canadian accounts](15-options-in-canadian-accounts.md)
