# What moves currencies

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">CMDTY</span>

After this lesson you can name the main forces behind exchange rates, price a one-year forward rate from two interest rates, and work out when a carry trade pays and when it does not.

Before this: [Forex basics](04-forex-basics.md), [The Bank of Canada and a macro week](../11-macro-and-economic-data/11-the-bank-of-canada-and-a-macro-week.md), [Interest rates and asset prices](../11-macro-and-economic-data/03-interest-rates-and-asset-prices.md). You need: a calculator.

## The idea

You have C$100,000 and can earn 2.50% a year on it in a Canadian deposit. A US deposit pays 4.00%. Moving the money to US dollars looks like an extra 1.50 percentage points. Why would anyone keep Canadian dollars?

Because the exchange rate can move against you by more than 1.50%, and because other traders already know about the gap. The forces below explain why a currency moves, and the last section shows how the gap in rates is built into the forward price.

## What moves exchange rates

**Interest rate differentials.** Money that can earn more in one country tends to flow there, which raises demand for its currency. The market looks at the expected path of policy rates, not today's level, as lesson 11 of Part 11 showed ([The Bank of Canada and a macro week](../11-macro-and-economic-data/11-the-bank-of-canada-and-a-macro-week.md)). When the market expects the Fed to cut less than the Bank of Canada, USD/CAD tends to rise.

**Growth and inflation data.** A strong jobs report or a high inflation print changes what traders expect central banks to do, which changes the rate path. This is the reaction function of Part 11 ([How markets react to data](../11-macro-and-economic-data/08-how-markets-react-to-data.md)) applied to a currency.

**Risk appetite.** **Risk-on** days are days when investors buy stocks and other risky assets; **risk-off** days are days when they sell them and move to assets seen as safe. In risk-off periods the US dollar, the Japanese yen and the Swiss franc have often been bought as safe currencies, and currencies of commodity exporters and high-yielding countries have often been sold. The pattern is common, and it does not hold every time.

**Commodity prices.** Canada exports oil and other raw materials, so a rise in oil tends to bring in more foreign currency and support the Canadian dollar. That is why the Canadian dollar is often called a **commodity currency**. The link changes over time and other forces overlap it, so oil alone does not give a forecast. Lesson 2 gave an oil example ([What moves oil and gold](02-what-moves-oil-and-gold.md)).

**Trade, flows and policy.** Large purchases of a country's assets, tariffs and interventions by central banks also move rates. They are hard to see in advance.

Each force is a question to ask when a pair moves. None is a rule.

## Interest rate parity

How much is the rate difference worth? A forward contract fixes today the exchange rate for a date in the future. The **forward rate** is set so that two ways of ending up with the same currency cost the same, which is the idea of interest rate parity.

Say you have C$1 and want to hold it for a year. You can deposit it in Canada and have 1 + \(i_{CAD}\). Or you can convert it to US dollars at the spot rate, deposit it in the US, and lock in the rate to convert back with a forward. If those two did not end in the same amount, a trader could earn a risk-free profit, and trading would close the gap.

\[ F = S \times \frac{1 + i_{quote}}{1 + i_{base}} \]

- \(F\) is the one-year forward rate of the pair, in units of quote currency per base currency.
- \(S\) is the spot rate, in the same units.
- \(i_{quote}\) is the one-year interest rate of the quote currency, as a fraction.
- \(i_{base}\) is the one-year interest rate of the base currency, as a fraction.
- This form is for one year. For a shorter term of \(T\) years, use \(1 + i \times T\) in place of \(1 + i\) on both lines.

For USD/CAD, the base is USD and the quote is CAD.

<div class="example" markdown>

### Worked example: a forward rate and a carry trade

Spot USD/CAD is 1.3650. The one-year US rate is 4.00% and the Canadian rate is 2.50% (both made up).

1. Forward rate: F = 1.3650 x 1.025 / 1.04 = 1.3453.
2. The forward is below spot by 0.0197, so the US dollar is at a forward discount. The currency with the higher rate trades cheaper in the forward market.

Now the carry trade. You start with C$100,000.

3. Convert at 1.3650: 100,000 / 1.3650 = US$73,260.07.
4. Deposit at 4.00% for a year: 73,260.07 x 1.04 = US$76,190.48.
5. Convert back at the rate a year later. Case A, USD/CAD unchanged at 1.3650: 76,190.48 x 1.3650 = C$104,000.00. The Canadian deposit gives 100,000 x 1.025 = C$102,500, so the carry gain is C$1,500.
6. Case B, USD/CAD falls to the forward rate of 1.3453: 76,190.48 x 1.3453 = C$102,500, so the gain is zero.
7. Case C, USD/CAD falls to 1.3200: 76,190.48 x 1.3200 = C$100,571.43, so the trade loses C$1,928.57 against the Canadian deposit.

</div>

A trade that borrows in a low-rate currency and invests in a high-rate currency is a **carry trade**. It earns the rate gap as long as the exchange rate does not move by more than the gap. Case B shows the break-even: the forward rate. Carry traders are hurt in risk-off periods, because the high-yield currency often falls at the same time as other risky assets.

## In code

<details class="code" markdown>
<summary>In code</summary>

```python
def forward(spot, i_quote, i_base):
    return spot * (1 + i_quote) / (1 + i_base)

f = forward(1.3650, 0.025, 0.04)
print(round(f, 4))                      # 1.3453
cad = 100_000
usd = cad / 1.3650 * 1.04               # convert, deposit at 4%
for end_rate in (1.3650, f, 1.3200):
    print(round(usd * end_rate - cad * 1.025, 2))   # carry result against the CAD deposit
```

</details>

<div class="canada" markdown>

### For Canadians

Every US stock you hold in a CAD view carries this exposure, and the gap between the Fed and the Bank of Canada is one of the inputs. Part 2 shows how to measure the effect on your return ([Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md)). The Bank of Canada publishes daily exchange rates, which the CRA accepts for converting amounts ([Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md)).

</div>

## Common mistakes

- Using the current rate gap as a forecast. The market prices the expected path, and the forward rate already has the gap in it.
- Reading a carry gain as free. It is paid for taking exchange-rate risk, and a move larger than the gap erases it.
- Swapping base and quote in the formula. The quote currency's rate goes on top.

## Try it

1\. Spot EUR/USD is 1.0800 (made up), the one-year US rate is 4.00% and the euro rate is 3.00%. What is the one-year forward rate?

<details class="solution" markdown>
<summary>Answer</summary>

Quote is USD and base is EUR. F = 1.0800 x 1.04 / 1.03 = 1.0905. The euro, with the lower rate, trades at a forward premium.

</details>

2\. Using the lesson's numbers, what must USD/CAD be after a year for the carry trade to break even, in pips below spot?

<details class="solution" markdown>
<summary>Answer</summary>

Break-even is the forward rate of 1.3453, which is 1.3650 - 1.3453 = 0.0197 below spot, so 197 pips.

</details>

3\. You start with C$50,000 and run the same carry trade with USD/CAD ending at 1.3400. What is the result against the Canadian deposit?

<details class="solution" markdown>
<summary>Answer</summary>

US$ = 50,000 / 1.3650 x 1.04 = US$38,095.24. Back at 1.3400: C$51,047.62. Canadian deposit: 50,000 x 1.025 = C$51,250.00. Result: -C$202.38.

</details>

4\. Name two forces that could push USD/CAD down in the same week, one from rates and one from commodities.

<details class="solution" markdown>
<summary>Answer</summary>

Rates: the market starts to expect the Bank of Canada to cut less than the Fed, which makes Canadian deposits look better. Commodities: the price of oil rises, which tends to support the Canadian dollar. Both lower USD/CAD.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the Bank of Canada's policy rate and the Fed's target range today. Write the gap in percentage points and which way it points. |
| 4 | Using spot USD/CAD and those two rates as one-year stand-ins, compute the one-year forward rate with the formula. |
| 2 | Write a [journal](../practice/trade-journal.md) line: which of the five forces you think moved USD/CAD this week, and what you would check to test it. |

</div>

## Key terms

- **Risk-on and risk-off**: days when investors buy risky assets, and days when they sell them for safer ones.
- **Commodity currency**: the currency of a country whose exports are largely raw materials.
- **Forward rate**: an exchange rate fixed today for a future date.
- **Interest rate parity**: the link that sets the forward rate from spot and the two interest rates.
- **Carry trade**: borrowing a low-rate currency to invest in a high-rate currency.

Next: [Trading forex from Canada](06-trading-forex-from-canada.md)
