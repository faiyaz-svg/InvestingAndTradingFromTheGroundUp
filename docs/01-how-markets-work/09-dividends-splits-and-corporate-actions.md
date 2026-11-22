# Dividends, splits and corporate actions

<span class="tag tag-idea">Idea</span> <span class="tag tag-part">MKT</span>

After this lesson you can say which date decides who gets a dividend, work out what a split does to your shares and price, and read a price history that has been adjusted for splits.

Before this: [Short selling](08-short-selling.md). You need: a calculator.

## The idea

A **corporate action** is an event the company decides that changes your holding: a dividend, a split, a merger, a spin-off. Your broker applies it to your account without an order from you, so you need to know what each one does to your shares, your cash and the price on your chart.

### Dividends

A dividend is a cash payment per share. Four dates matter.

| Date | Meaning |
|---|---|
| Declaration date | The company announces the amount and the other dates |
| Ex-dividend date | The first day the stock trades without the right to this dividend |
| Record date | The day the company checks who owns the shares |
| Payment date | The day the cash is paid |

You get the dividend if you own the shares before the **ex-dividend date**. Since the US and Canada moved to T+1 settlement in May 2024 (lesson 7), the ex-dividend date and the record date are the same day, so you must buy at least one business day before it ([DTCC T+1 dividend processing FAQ](https://www.dtcc.com/-/media/Files/PDFs/T2/T1-Dividend-Processing-FAQ.pdf)). Buy on the ex-date itself and you do not get it. Sell on the ex-date and you still get it, because you owned the shares the day before.

On the ex-date the stock's price drops by about the dividend. A buyer on that day does not receive the dividend, so the shares are worth less by that amount. The chart shows it for a made-up dividend of US$1.00 (larger than most, so the drop is visible).

```chart
data: 01-how-markets-work/ex-dividend.json
title: Stock A, daily: an ex-dividend gap
marker: 2026-08-24 | below | Ex-dividend
level: 49.95 | Close before the ex-date
range: 2026-08-03 to 2026-09-04
caption: Stock A closed at 49.95 on Friday, August 21, and opened at 48.95 on the ex-dividend date, Monday, August 24, a drop of US$1.00.
```

The dividend is not a free gain. You received US$1.00 of cash and the stock is worth US$1.00 less. The price after the ex-date is also pushed by other news, so the drop is not exact, and on a normal day-to-day move it is often hard to see.

The **dividend yield** is the yearly dividend per share divided by the price:

\[ y = \frac{D}{P} \]

- \(D\) is the dividends paid over a year, per share, in US$.
- \(P\) is the share price, in US$.
- \(y\) is the yield, a percentage.

A **dividend reinvestment plan** (DRIP) uses your dividends to buy more shares. Wealthsimple's DRIP is turned on per account and buys shares, including fractional shares, on the open market after the dividend arrives, not through a company plan ([Wealthsimple DRIP help](https://help.wealthsimple.com/hc/en-ca/articles/15755618952347-Learn-about-dividend-reinvestments-on-Wealthsimple), as of 2026). Check IBKR Canada's own page for its handling.

### Splits

A **stock split** changes the number of shares and the price per share without changing the value of your holding. In a 2-for-1 split each share becomes two, and the price halves. A **reverse split** goes the other way: 1-for-10 turns ten shares into one and multiplies the price by ten. Companies split to bring the price to a level they prefer, and reverse-split to lift a very low price.

<div class="example" markdown>

### Worked example: a 2-for-1 split

You own 100 shares of Stock A at the Monday, October 12, 2026 close of US$227.63.

1. Value before: 100 x 227.63 = US$22,763.00.
2. After a 2-for-1 split you hold 200 shares.
3. The new price is 227.63 / 2 = US$113.815, which the chart shows as the 113.82 open on Tuesday, October 13.
4. Value after: 200 x 113.815 = US$22,763.00. Nothing changed but the count and the price.

For a 1-for-10 reverse split of 1,000 shares at US$2.00: 1,000 / 10 = 100 shares at 2.00 x 10 = US$20.00, and 1,000 x 2.00 = 100 x 20.00 = US$2,000.

</div>

```chart
data: 01-how-markets-work/stock-a-split.json
title: Stock A, daily: a 2-for-1 split shown at raw prices
marker: 2026-10-13 | below | 2-for-1 split
level: 227.63 | Close before the split
range: 2026-09-08 to 2026-11-02
caption: At raw prices the split looks like a 50% crash, from a close of 227.63 to an open of 113.82. The stock lost no value.
```

Data providers **split-adjust** history so you do not see that false crash. They divide every price before the split by the split ratio (and multiply volume by it). A chart on your broker or TradingView is usually adjusted, which is why an old price on a chart can differ from the price you remember. Use adjusted prices for returns and raw prices only to check an actual past fill.

<details class="code" markdown>
<summary>In code</summary>

Download [stock-a-split-daily.csv](../assets/data/stock-a-split-daily.csv). It holds raw prices around a 2-for-1 split on 2026-10-13. The code adjusts earlier rows and compares the one-day returns.

```python
import pandas as pd

bars = pd.read_csv("stock-a-split-daily.csv", parse_dates=["date"])
split_date = pd.Timestamp("2026-10-13")
ratio = 2

adjusted = bars.copy()
before = adjusted["date"] < split_date
for col in ["open", "high", "low", "close"]:
    adjusted.loc[before, col] = adjusted.loc[before, col] / ratio
adjusted.loc[before, "volume"] = adjusted.loc[before, "volume"] * ratio

for name, df in [("raw", bars), ("adjusted", adjusted)]:
    ret = df["close"].pct_change()
    row = df["date"] == split_date
    print(name, round(float(ret[row].iloc[0]) * 100, 2))
```

The raw return on the split date is about -49.2%, and the adjusted return is a small ordinary move.

</details>

### Other corporate actions

A **special dividend** is a one-off payment. A **spin-off** gives shareholders shares of a new company split from the old one. In a **merger** or acquisition, your shares may be exchanged for cash or for shares of the buyer. A **buyback** is the company buying its own shares, which reduces the share count (Part 9, [Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md)).

<div class="canada" markdown>

### For Canadians

Dividends on US stocks are paid in USD and can be subject to US withholding tax before they reach you. The rate and how it works by account (RRSP, TFSA, FHSA, non-registered) is covered in Part 2 ([US withholding tax and the W-8BEN](../02-accounts-currency-and-taxes/06-us-withholding-tax-and-w-8ben.md)). Do not plan around a dividend yield until you know what you keep after that tax.

</div>

## Common mistakes

- Buying on the ex-date to "catch" the dividend. You needed to own the stock the business day before.
- Reading a split as a crash or a gain. The adjusted chart shows what happened to value.
- Treating a high dividend yield as a gift. A yield rises when the price falls, so it can signal trouble.

## Try it

1\. A stock pays a US$0.80 dividend a quarter and trades at US$40.00. What is the yield?

<details class="solution" markdown>
<summary>Answer</summary>

D = 4 x 0.80 = US$3.20 a year. y = 3.20 / 40.00 = 8.0%.

</details>

2\. A stock's ex-dividend date is Wednesday, July 8, 2026. What is the last day you could buy it to receive the dividend?

<details class="solution" markdown>
<summary>Answer</summary>

Tuesday, July 7, 2026, the business day before the ex-date.

</details>

3\. You own 150 shares at US$80.00. The company announces a 3-for-1 split. How many shares and at what price after, and what is the value?

<details class="solution" markdown>
<summary>Answer</summary>

Shares = 150 x 3 = 450. Price = 80.00 / 3 = US$26.67 (rounded). Value = 450 x 26.6667 = US$12,000, the same as 150 x 80.00.

</details>

4\. Stock A's raw split-date chart shows a close of 227.63 and the next open of 113.82. What is the raw percentage change, and why is it misleading?

<details class="solution" markdown>
<summary>Answer</summary>

(113.82 - 227.63) / 227.63 = -0.5000, so -50.0%. It is misleading because the split halved the price per share and doubled the share count, so no value was lost.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Find the next ex-dividend date for a dividend stock you follow. Write the last day to buy to receive it. |
| 3 | Look up a stock that split in the last five years. Compare its chart with split adjustment on and off if your platform lets you. |
| 3 | In your account, find where corporate actions appear and whether DRIP is on or off. |

</div>

## Key terms

- **Corporate action**: a company event that changes your holding, such as a dividend or split.
- **Ex-dividend date**: the first day the stock trades without the right to the dividend.
- **Record date**: the date the company checks who owns the shares.
- **Dividend yield**: yearly dividends per share divided by the price.
- **DRIP**: a plan that uses dividends to buy more shares.
- **Stock split**: a change in share count and price with no change in value.
- **Reverse split**: a split that cuts the share count and raises the price.
- **Split-adjust**: restate old prices to remove the effect of a split.
- **Spin-off**: a new company's shares given to existing shareholders.

Next: [Indexes, sectors and market cap](10-indexes-sectors-and-market-cap.md)
