# Cost base in CAD and keeping records

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can work out the adjusted cost base of a US stock in Canadian dollars across several purchases, compute the capital gain on a sale, and say which records and reports the CRA expects.

Before this: [Capital gains or business income](07-capital-gains-vs-business-income.md), [Currency risk on US stocks](05-currency-risk-on-us-stocks.md). You need: a calculator.

## The idea

You buy shares of Stock A three times, at three prices and three exchange rates. When you sell some, the CRA wants the gain in Canadian dollars. The number you subtract from the proceeds is the **adjusted cost base** (ACB): what you paid for the shares, in Canadian dollars, including commissions, averaged across identical shares.

Three CRA rules from its capital gains guide T4037 shape the calculation ([CRA T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html), as of 2026):

1. Convert the proceeds of a sale using the exchange rate in effect at the time of the sale, the ACB using the rate in effect when you acquired the property, and expenses using the rate when they were incurred.
2. For identical shares bought at different prices, recalculate the average cost after each purchase: total cost, including acquisition expenses, divided by the total number of shares you own.
3. A sale does not change the average cost of the shares you still hold.

For the rate, the CRA says to generally use the Bank of Canada rate in effect on the transaction day, and that it will also generally accept another source that is widely available, verifiable and used consistently from year to year (same T4037 page). The Bank of Canada publishes its daily average by 4:30 p.m. ET each business day ([Bank of Canada](https://www.bankofcanada.ca/rates/exchange/background-information-on-foreign-exchange-rates/)). Pick one source and use it every year.

## How it works

1. For each purchase, convert the cost (price times shares, plus commission) to C$ at that day's rate.
2. Add the C$ costs and divide by the total shares to get the ACB per share.
3. On a sale, convert the proceeds (less selling costs) to C$ at the sale day's rate.
4. Gain or loss = proceeds - (ACB per share x shares sold).
5. The remaining shares keep the same ACB per share, and the next purchase starts a new average.

\[ \text{Gain} = P_{\text{CAD}} - n \times \text{ACB per share} \]

- \(P_{\text{CAD}}\) is the sale proceeds in C$, converted at the sale-day rate.
- \(n\) is the number of shares sold.
- ACB per share is the average cost in C$ of all the shares you hold.

<div class="example" markdown>

### Worked example: three purchases and a sale

Rates are made-up Bank of Canada daily rates, and commissions are zero (as at a no-commission broker).

| Date | Shares | Price (US$) | Rate | Cost (C$) |
|---|---|---|---|---|
| March 3 | 100 | 50.00 | 1.3600 | 6,800.00 |
| May 12 | 100 | 60.00 | 1.4000 | 8,400.00 |
| August 5 | 50 | 55.00 | 1.3000 | 3,575.00 |

1. After the three purchases you hold 250 shares with a total cost of 6,800 + 8,400 + 3,575 = C$18,775.00.
2. ACB per share = 18,775.00 / 250 = C$75.10.
3. In October you sell 150 shares at US$65.00 when the rate is 1.3500. Proceeds = 150 x 65.00 x 1.35 = C$13,162.50.
4. ACB of the shares sold = 150 x 75.10 = C$11,265.00.
5. Gain = 13,162.50 - 11,265.00 = C$1,897.50. If this is a capital gain, half is taxable: C$948.75.
6. The 100 shares you still hold keep an ACB of 100 x 75.10 = C$7,510.00.

The same sale in US dollars has a gain of 150 x (65.00 - 55.00) = US$1,500, because the average US cost is (5,000 + 6,000 + 2,750) / 250 = US$55.00. At 1.3500 that is C$2,025.00, not C$1,897.50. The difference is the currency: you bought when the US dollar was dearer, so your Canadian cost is higher.

</div>

## In code

The same calculation as a short script.

<details class="code" markdown>
<summary>In code</summary>

```python
buys = [(100, 50.00, 1.3600), (100, 60.00, 1.4000), (50, 55.00, 1.3000)]  # shares, US$ price, C$ per US$

shares = sum(n for n, _, _ in buys)
cost_cad = sum(n * price * rate for n, price, rate in buys)
acb_per_share = cost_cad / shares

sold, price, rate = 150, 65.00, 1.3500
proceeds_cad = sold * price * rate
gain = proceeds_cad - sold * acb_per_share
print(round(acb_per_share, 2), round(proceeds_cad, 2), round(gain, 2))
```

</details>

## Records and reports

Keep the trade confirmations (they show date, price and quantity), the account statements and the rate you used for each conversion. A spreadsheet with one row per trade, in C$, is enough. The CRA can ask for the support behind your return, and your broker's tax slips may not give you an ACB in Canadian dollars for every case. I did not confirm which slips each broker issues, so check your broker's tax page.

There is one more form. If you are a Canadian resident and the total cost of your specified foreign property was more than C$100,000 at any time in the year, you file Form T1135. The test uses cost, generally the ACB, not market value. Shares of non-resident corporations are specified foreign property even when a Canadian broker holds them. If your total cost was between C$100,000 and C$250,000 throughout the year you can use the simplified Part A, and at C$250,000 or more you complete Part B. Property held in an RRSP or TFSA is excluded ([CRA T1135 questions and answers](https://www.canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/foreign-reporting/questions-answers-about-form-t1135.html), as of 2026).

<div class="canada" markdown>

### For Canadians

Report the gain in Canadian dollars on Schedule 3 of your return. The CRA's guide says that most of what goes on Schedule 3 comes from amounts on tax slips (same T4037 page); where your broker's slip lacks a Canadian ACB, your own record fills the gap. A USD account does not change this: each purchase and sale is still converted at the rate on its day.

</div>

## Common mistakes

- Computing the gain in US dollars and converting once. The CRA wants each leg at its own date's rate.
- Resetting the average cost after a sale. A sale does not change the average of what remains.
- Using a different rate source from year to year.

## Try it

1\. You buy 100 shares at US$20.00 when the rate is 1.4000 and another 100 at US$30.00 when it is 1.3000. What is the ACB per share in C$?

<details class="solution" markdown>
<summary>Answer</summary>

Costs: 100 x 20 x 1.40 = C$2,800.00 and 100 x 30 x 1.30 = C$3,900.00. Total = C$6,700.00 for 200 shares. ACB per share = C$33.50.

</details>

2\. You sell 80 of those shares at US$35.00 at a rate of 1.3500. What is the gain in C$?

<details class="solution" markdown>
<summary>Answer</summary>

Proceeds = 80 x 35.00 x 1.35 = C$3,780.00. ACB of shares sold = 80 x 33.50 = C$2,680.00. Gain = C$1,100.00.

</details>

3\. After question 2, you hold 120 shares. What is their total ACB?

<details class="solution" markdown>
<summary>Answer</summary>

120 x 33.50 = C$4,020.00. The sale did not change the per-share average.

</details>

4\. Your non-registered account holds specified foreign property with a total cost of C$90,000 at all times in the year. Do you file Form T1135?

<details class="solution" markdown>
<summary>Answer</summary>

No, if that is your only specified foreign property. The threshold is more than C$100,000 total cost at any time in the year.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 5 | Pick one US stock you bought more than once. Find each purchase's date, price and the Bank of Canada rate for that day. |
| 3 | Compute the ACB per share in C$. |
| 2 | Note where you store your trade confirmations and name the folder for this year's tax records. |

</div>

## Key terms

- **Adjusted cost base (ACB)**: what you paid for a property in Canadian dollars, including costs, averaged across identical shares.
- **Specified foreign property**: foreign assets, such as shares of non-resident corporations, that count toward the T1135 test.
- **Form T1135**: the form that reports specified foreign property of more than C$100,000 in cost.
- **Schedule 3**: the part of the tax return where capital gains and losses are reported.

Next: [Tax losses and the superficial loss rule](09-tax-losses-and-superficial-loss.md)
