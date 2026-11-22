# Earnings season and earnings calls

<span class="tag tag-data">Data</span> <span class="tag tag-review">Review</span> <span class="tag tag-part">FIN</span>

After this lesson you can read an earnings release and call in a fixed order, work out an earnings surprise against consensus, say why a beat can still send a price down, and use the whole part to review a company.

Before this: [GAAP, non-GAAP and earnings quality](10-gaap-non-gaap-and-earnings-quality.md). You need: a calculator.

## The idea

On Wednesday, February 4, 2026, after the close, Northwind reports its fourth quarter. Revenue is US$310 million against a consensus of US$300 million. Diluted EPS is US$0.45 against US$0.42. Both beat. On Thursday, February 5, the stock opens 5.0% lower. A good quarter can still fall short of what the price already assumed, and this lesson shows how to read that.

An **earnings season** is the few weeks after each quarter ends when most US companies report: late January and February for the fourth quarter, then April and May, July and August, and October and November. Each company's date is on its investor relations page and your broker's earnings calendar.

## How it works

### The sequence

1. The company announces the date and time weeks ahead. Most report before the open or after the close, outside the regular session ([Market hours and the opening and closing auctions](../01-how-markets-work/03-market-hours-and-auctions.md)).
2. It files an 8-K under Item 2.02 with the press release as Exhibit 99.1 (lesson 1).
3. A live **earnings call** follows: prepared remarks from the chief executive and chief financial officer, then analysts' questions. It is webcast to everyone because of SEC **Regulation FD**, which requires material information given to some investors to reach all of them.
4. The full 10-Q or 10-K arrives on the same day or soon after, with the notes the release leaves out.

### Reading the release in order

1. The headline numbers against consensus and against last year: revenue, EPS, any margin.
2. The GAAP to non-GAAP reconciliation (lesson 10). Find what was added back.
3. The guidance, the company's forecast for coming periods.
4. The balance sheet and cash flow: cash conversion, debt, buybacks (lessons 4, 8 and 9).

### Consensus and the surprise

**Consensus** is the average of the estimates analysts publish before the report, for EPS and sometimes revenue. Data providers collect them, and many broker apps show them. **Guidance** is the company's own forecast of revenue or EPS for a coming quarter or year.

The **earnings surprise** is the actual figure against consensus:

\[ \text{Surprise} = A - E \qquad \text{Surprise \%} = \frac{A - E}{|E|} \]

- \(A\) is the reported EPS (or revenue), in US$.
- \(E\) is the consensus estimate, in the same unit.
- The absolute value in the denominator keeps the sign right when \(E\) is negative.

<div class="example" markdown>

### Worked example: a beat and a guide

Northwind's fourth quarter, FY2025. The first three quarters had revenue of US$840 million, so Q4 revenue of 310 brings the year to 1,150, and Q4 net income of US$46 million (of the year's 165) over 102.5 million diluted shares gives EPS of 46 / 102.5 = US$0.45.

1. EPS surprise = 0.45 - 0.42 = US$0.03, or 0.03 / 0.42 = 7.1%.
2. Revenue surprise = 310 - 300 = US$10 million, or 10 / 300 = 3.3%.
3. Guidance for FY2026: EPS of US$1.74 to US$1.84, midpoint 1.79, against a pre-report consensus of US$1.86. The midpoint is 1.79 / 1.86 - 1 = -3.8% below consensus. Revenue guidance is US$1,250 to 1,290 million, a midpoint of 1,270, up 10.4% from 1,150.
4. Against last year, the EPS midpoint is 1.79 / 1.61 - 1 = +11.2% on FY2025 diluted EPS.

The quarter beat by 7.1%, and the forward view came in 3.8% under consensus.

</div>

The chart shows what the price did. Look at the gap between the close of February 4 and the open of February 5.

```chart
data: 09-company-financials/northwind-earnings-gap.json
title: Northwind (made up), daily: a gap down after a beat and soft guidance
marker: 2026-02-05 | below | Opens at 47.50
level: 50.00 | Close before the report
range: 2026-01-12 to 2026-02-23
caption: Northwind closed at 50.00 on February 4 and opened at 47.50 on February 5, 5.0% lower. The day closed at 46.90.
```

The stock closed that Thursday at 46.90, 6.2% below 50.00, on 4,050,000 shares against 1,170,800 the day before. In the next 12 sessions it traded between 46.82 and 48.26, without recovering the gap.

### Why a beat can fall

A price already holds what the market expects ([What a stock is and why prices move](../01-how-markets-work/01-what-a-stock-is.md)). The move is driven by everything new: the quarter, the guidance, margins, cash and the tone of the call. Here the guide mattered more than a three-cent beat. Some traders watch the **implied move**, the size of move that options prices suggest. Part 16 covers it (Earnings trades and IV crush<!-- link: ../16-volatility-and-event-trading/04-earnings-trades-and-iv-crush.md -->).

### Listening to the call

Listen for what changed from last quarter. A question analysts ask more than once points at the real worry, and a vague answer to a direct question is information. The prepared remarks are written to be positive; the questions show more.

<div class="canada" markdown>

### For Canadians

Canadian-listed companies also report each quarter on SEDAR+ (lesson 1). Canada's five largest banks have an October 31 fiscal year end, so their quarters end on January 31, April 30, July 31 and October 31.

</div>

## Common mistakes

- Judging a report by the headline beat or miss. Read the guidance, the margins and the cash flow.
- Comparing with the wrong consensus. Use the one published right before the report, and know whether it is for GAAP or adjusted EPS.

## Try it

1\. A company reports EPS of US$1.20 against a consensus of US$1.05. What is the surprise in dollars and in percent?

<details class="solution" markdown>
<summary>Answer</summary>

1.20 - 1.05 = US$0.15. 0.15 / 1.05 = 14.3%.

</details>

2\. A company reports a loss of US$0.20 a share against an expected loss of US$0.25. Is that a beat? What is the surprise percent?

<details class="solution" markdown>
<summary>Answer</summary>

Yes, the loss is smaller. Surprise = -0.20 - (-0.25) = +US$0.05. Surprise % = 0.05 / |-0.25| = 20.0%.

</details>

3\. A stock closes at US$80.00 and opens at US$84.80 after a beat. What is the gap in percent?

<details class="solution" markdown>
<summary>Answer</summary>

(84.80 - 80.00) / 80.00 = +6.0%.

</details>

## Part check

1\. A company has revenue of US$800 million, COGS of US$480 million, operating expenses of US$220 million, interest of US$20 million and a 25% tax rate. Find gross profit, EBIT and net income.

<details class="solution" markdown>
<summary>Answer</summary>

Gross profit = 800 - 480 = US$320 million. EBIT = 320 - 220 = US$100 million. Pretax = 100 - 20 = 80. Net income = 80 x 0.75 = US$60 million.

</details>

2\. Net income is US$60 million, D&A US$15 million, SBC US$5 million, receivables rose US$10 million and payables rose US$4 million. Capex is US$30 million. Find CFO and FCF.

<details class="solution" markdown>
<summary>Answer</summary>

CFO = 60 + 15 + 5 - 10 + 4 = US$74 million. FCF = 74 - 30 = US$44 million.

</details>

3\. Current assets are US$300 million (including US$120 million of inventory), current liabilities US$200 million, debt US$250 million, cash US$50 million, EBIT US$80 million and interest US$16 million. Find the current ratio, net debt and interest coverage.

<details class="solution" markdown>
<summary>Answer</summary>

Current ratio = 300 / 200 = 1.50. Net debt = 250 - 50 = US$200 million. Interest coverage = 80 / 16 = 5.0 times.

</details>

4\. A company has 50 million shares, net income of US$100 million, 6 million options with a US$20 strike, and an average share price of US$40. Find diluted EPS.

<details class="solution" markdown>
<summary>Answer</summary>

Net new shares = 6 - (6 x 20) / 40 = 6 - 3 = 3 million. Diluted shares = 53 million. Diluted EPS = 100 / 53 = US$1.89 (basic is US$2.00).

</details>

5\. Adjusted EPS is US$2.50 and GAAP EPS is US$1.90. Cash conversion is 0.6 and receivables grew 35% on revenue growth of 10%. What do you check first?

<details class="solution" markdown>
<summary>Answer</summary>

The reconciliation first: what do the US$0.60 of add-backs hold, and do they recur? Then the receivables: 35% growth against 10% revenue growth, with cash conversion of 0.6, says profit is not turning into cash. Read the MD&A for the reason.

</details>

6\. A company beats EPS by 5% and its stock falls 4% the next morning. Give two things in the report that could explain it.

<details class="solution" markdown>
<summary>Answer</summary>

Guidance below consensus, shrinking margins, weak cash flow or a worse tone on the call. Any of these can outweigh a beat, because the price already held the expected EPS.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | Pick a company reporting this month. Find the date and time on its investor relations page, and the consensus EPS on your broker or data site. |
| 4 | After it reports, open the 8-K (Exhibit 99.1). Compute the EPS surprise and the guidance against the consensus you wrote down. |
| 2 | Write the stock's close before the report and its open after, and the gap in percent. Add it to your [trade journal](../practice/trade-journal.md) notes on earnings moves. |

</div>

## Key terms

- **Earnings season**: the weeks after each quarter ends when most companies report.
- **Earnings call**: the call where management presents results and analysts ask questions.
- **Regulation FD**: the SEC rule that requires material information to reach all investors at the same time.
- **Consensus**: the average of analysts' published estimates.
- **Guidance**: the company's own forecast for coming periods.
- **Earnings surprise**: the reported figure minus consensus, in dollars or percent.
- **Implied move**: the size of the earnings-day move that options prices suggest.

Next: Price multiples<!-- link: ../10-valuation-and-research/01-multiples.md -->
