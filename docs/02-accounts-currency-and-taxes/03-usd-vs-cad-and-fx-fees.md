# USD or CAD, and currency conversion fees

<span class="tag tag-canada">Canada</span> <span class="tag tag-part">ACCT</span>

After this lesson you can say what happens to your money when you buy a US stock from a CAD account or a USD account, work out the cost of a round trip in each, and measure the all-in cost of a conversion against the Bank of Canada rate.

Before this: [Wealthsimple and IBKR compared](02-wealthsimple-and-ibkr.md). You need: a calculator.

## The idea

A US stock is priced in US dollars. If your cash is in Canadian dollars, someone has to change it. There are two ways the change happens.

In a **CAD account**, you place an order for a US stock and the broker converts the money at the moment the order fills. You never see a US dollar balance. In a **USD account** (or a US dollar balance inside a multi-currency account), you convert once, hold US dollars, and buy and sell US stocks with them. Dividends and sale proceeds stay in US dollars until you convert them.

The cost of each path is a **conversion fee**: a percentage the broker adds to the exchange rate. At Wealthsimple, a US-listed trade from a CAD account carries a 1.5% fee on the conversion, charged when the order fills. A US-listed trade from a USD account carries no conversion fee, and the USD account costs $10 a month plus tax. Moving cash between your CAD and USD accounts costs 1.5% under $10,000, 1.0% from $10,000 to $24,999.99, 0.5% from $25,000 to $99,999.99 and 0% from $100,000 ([Wealthsimple trade fees](https://www.wealthsimple.com/legal/fees/trade), as of 2026). The fee is applied to the broker's own rate, so it is a markup on the rate you could see elsewhere.

The figure shows the tiers against the flat fee.

![The tiered conversion fee falls from 1.5% to 0% as the amount converted grows, against a flat 1.5% line](../assets/figures/02-accounts-currency-and-taxes/conversion-tiers-dark.svg#only-dark)
![The tiered conversion fee falls from 1.5% to 0% as the amount converted grows, against a flat 1.5% line](../assets/figures/02-accounts-currency-and-taxes/conversion-tiers-light.svg#only-light)

## How it works

1. Pick a reference rate, such as the Bank of Canada daily average for the day (below).
2. Take the rate your broker gave you on the fill.
3. The cost of the conversion is how far the broker's rate is from the reference.

\[ \text{Conversion cost} = \frac{R_b - R_m}{R_m} \]

- \(R_b\) is the rate your broker used, in C$ per US$ (when you buy US dollars).
- \(R_m\) is the reference rate, in C$ per US$.
- The result is a fraction of the amount converted. When you sell US dollars, the broker's rate is below the reference, so reverse the numerator.

The **Bank of Canada** publishes a daily average rate for each business day by 4:30 p.m. ET. It is built from mid-market quotes collected every minute from 8:00 a.m. to 4:00 p.m. ET, with the highest and lowest 2.5% removed. The Bank says the rates are indicative only and may not match rates from actual trades ([Bank of Canada background on rates](https://www.bankofcanada.ca/rates/exchange/background-information-on-foreign-exchange-rates/), as of 2026). Use it as a yardstick, not as a price you can get.

<div class="example" markdown>

### Worked example: a round trip in each account

Take a made-up mid-market rate of C$1.3800 per US$1 that does not change while you hold. Stock A costs US$50.00 a share, you buy 200 shares (US$10,000) and sell at the same price. The broker applies a 1.5% fee to the rate in a CAD account, and for the USD account we use the tiered fee with the same cash amount.

CAD account:

1. Buy: 10,000 x 1.3800 x 1.015 = C$14,007.00.
2. Sell: 10,000 x 1.3800 x 0.985 = C$13,593.00.
3. Cost: 14,007.00 - 13,593.00 = C$414.00, which is 2.96% of C$14,007.00.

USD account (convert once, then trade with no conversion fee):

1. Convert: the amount is above C$10,000, so the 1.0% tier applies: 10,000 x 1.3800 x 1.01 = C$13,938.00.
2. Convert back: 10,000 x 1.3800 x 0.99 = C$13,662.00.
3. Cost: 13,938.00 - 13,662.00 = C$276.00, which is 1.98% of C$13,938.00.

The stock did not move, and you are down C$414 in one case and C$276 in the other. The USD account saves C$138 here, and more each time you trade the same US cash again without converting it.

</div>

<div class="example" markdown>

### Worked example: all-in cost against the Bank of Canada rate

You convert C$14,000 into US dollars. The Bank of Canada daily average for the day is 1.3800. Your broker's statement shows that C$14,000 became US$9,950.

1. Your effective rate: 14,000 / 9,950 = 1.4070 C$ per US$ (rounded to four places).
2. Conversion cost: (1.4070 - 1.3800) / 1.3800 = 1.96% (rounded to two places).

Remember the reference is indicative, so a part of that 1.96% may be a normal bid-ask spread in the currency market, not a markup.

</div>

## In code

A function for a tiered fee, using the Wealthsimple tiers from the table above.

<details class="code" markdown>
<summary>In code</summary>

```python
def conversion_fee(amount_cad):
    """Fee fraction on moving cash between CAD and USD accounts (tiers as of 2026)."""
    if amount_cad < 10_000:
        return 0.015
    if amount_cad < 25_000:
        return 0.010
    if amount_cad < 100_000:
        return 0.005
    return 0.0

for amount in (5_000, 13_938, 50_000, 120_000):
    print(amount, conversion_fee(amount))
```

</details>

<div class="canada" markdown>

### For Canadians

IBKR Canada does not convert automatically: you place a currency trade yourself, and its page lists the commission for that ([IBKR commissions](https://www.interactivebrokers.ca/en/pricing/commissions-home.php), check the current numbers). Whichever broker you use, ask three questions. What is the fee? What reference rate is it applied to? Is there a monthly fee for the USD side? Lesson 4, [Norbert's gambit and CDRs](04-norberts-gambit-and-cdrs.md), covers a way around the fee for larger amounts.

</div>

## Common mistakes

- Judging cost by the headline fee. A 1.5% fee charged on both the buy and the sell is about 3% of the position.
- Converting back to CAD after each trade. In a USD account the fee returns every time you do, so keep the US dollars while you trade US stocks.
- Treating the Bank of Canada rate as what you could have got. It is an average of mid quotes, not a price.

## Try it

1\. In a CAD account with a 1.5% fee on each fill and a flat rate of 1.4000, you buy US$5,000 of Stock A and sell it at the same price. What is the round-trip cost in C$?

<details class="solution" markdown>
<summary>Answer</summary>

Buy: 5,000 x 1.4000 x 1.015 = C$7,105.00. Sell: 5,000 x 1.4000 x 0.985 = C$6,895.00. Cost = C$210.00.

</details>

2\. You convert C$30,000 into US dollars at the 0.5% tier and the mid-market rate is 1.3500. How many US dollars do you get?

<details class="solution" markdown>
<summary>Answer</summary>

The broker's rate is 1.3500 x 1.005 = 1.35675. US dollars = 30,000 / 1.35675 = US$22,111.66.

</details>

3\. Your broker gives you 1.4100 on a day the Bank of Canada rate is 1.3900. What is the conversion cost?

<details class="solution" markdown>
<summary>Answer</summary>

(1.4100 - 1.3900) / 1.3900 = 1.44%.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find your last currency conversion or US-stock fill. Write the rate you got and the Bank of Canada rate for that day. |
| 3 | Compute the conversion cost for that fill with the formula. |
| 3 | Write down what you will do next time: trade from a CAD account or hold US dollars. Give one reason. |

</div>

## Key terms

- **CAD account**: an account where the broker converts your cash to US dollars at each US-stock fill.
- **USD account**: an account that holds US dollars, so US-stock trades need no conversion.
- **Conversion fee**: the percentage added to the exchange rate when money changes currency.
- **Bank of Canada daily average rate**: the Bank's indicative rate for each business day, from minute-by-minute mid quotes.
- **Effective rate**: the amount of one currency you paid divided by the amount of the other you received.

Next: [Norbert's gambit and CDRs](04-norberts-gambit-and-cdrs.md)
