# Trade journal

A journal records every trade so you can measure your results and review your decisions. [The trade journal](../04-psychology-journal-and-paper-trading/04-the-trade-journal.md) explains why. This page lists what to record, the formulas, the weekly review, and how to build the sheet.

Downloads: [trade-journal.xlsx](../downloads/trade-journal.xlsx) (formulas included) and [trade-journal.csv](../downloads/trade-journal.csv) (headers and two made-up example rows). The example trades use made-up Stock A and Stock B.

## What to record

Fill the first group before you place the order, and do not change it afterward. Fill the second group when the trade is closed.

| Column | Field | Group | Notes |
|---|---|---|---|
| A | Date | Before | Entry date, YYYY-MM-DD |
| B | Ticker | Before | |
| C | Setup | Before | A name from your short list of setups |
| D | Direction | Before | Long or Short |
| E | Entry | Before | Price per share, US$ |
| F | Stop | Before | Price per share, US$ |
| G | Target | Before | Price per share, US$ |
| H | Shares | Before | From the sizing formula |
| I | Risk (US$) | Formula | Planned loss at the stop |
| J | Exit | After | Price per share, US$ |
| K | Fees (US$) | After | Entry and exit together |
| L | P/L (US$) | Formula | Result after fees |
| M | R | Formula | P/L divided by risk |
| N | Followed plan | After | Yes or No |
| O | Emotion | Before and after | One word before, one word after |
| P | Notes | After | What you would change |
| Q | Screenshot | After | A file name or link for the chart at entry and exit |

Write one reason the trade could fail in the Notes column before you enter, and the result in the same cell afterward.

## Formulas

\[ \text{Risk} = |E - S| \times N \qquad \text{P/L} = (X - E) \times N \times d - F \qquad R = \frac{\text{P/L}}{\text{Risk}} \]

- \(E\), \(S\) and \(X\) are the entry, stop and exit prices, in US$ per share.
- \(N\) is the number of shares.
- \(d\) is +1 for a long trade and -1 for a short trade.
- \(F\) is the fees in US$.

Over all closed trades:

| Measure | Formula |
|---|---|
| Win rate | winners / closed trades |
| Average win | sum of R on winners / number of winners |
| Average loss | sum of R on losers / number of losers (a negative number) |
| Expectancy | win rate x average win + (1 - win rate) x average loss, which equals the average R of all trades |
| Total R | sum of R |
| By setup | the same measures, for the trades of one setup |

Example: Stock A, long, entry 50.00, stop 48.50, 166 shares, exit 53.00, fees US$2.00 gives risk US$249.00, P/L US$496.00 and R 1.99. The expectancy of the two example rows is (1.99 - 1.01) / 2 = 0.49R, which is two trades and not evidence of anything.

## Weekly review checklist

Do it once a week for about 20 minutes ([Reviewing your trades](../04-psychology-journal-and-paper-trading/05-reviewing-your-trades.md)).

1. Every trade of the week is in the journal, both stages.
2. Rule breaks counted, each with a reason.
3. Win rate, average win, average loss, expectancy and total R updated.
4. Results split by setup and by "followed plan".
5. Largest loss of the week checked against your 1R plus fees.
6. At most one change for next week, written as a rule.

## Build it in Excel or Google Sheets

1. Create a sheet named Trades and put the headers from the table in row 1, columns A to Q.
2. In row 2, enter risk, P/L and R as formulas, then fill down:
    - I2: `=IF(OR(E2="",F2="",H2=""),"",ABS(E2-F2)*H2)`
    - L2: `=IF(OR(J2="",I2=""),"",(J2-E2)*H2*IF(D2="Short",-1,1)-K2)`
    - M2: `=IF(OR(L2="",I2="",I2=0),"",L2/I2)`
3. Create a sheet named Stats. With R in Trades column M, rows 2 to 500:
    - Closed trades: `=COUNT(Trades!M2:M500)`
    - Win rate: `=COUNTIF(Trades!M2:M500,">0")/COUNT(Trades!M2:M500)`
    - Average win: `=AVERAGEIF(Trades!M2:M500,">0")`
    - Average loss: `=AVERAGEIF(Trades!M2:M500,"<0")`
    - Expectancy: `=AVERAGE(Trades!M2:M500)`
4. Add a by-setup table: setup names in a column, then for each name `=COUNTIFS(Trades!C2:C500,A15,Trades!M2:M500,">-1E+99")` for the count, `=AVERAGEIFS(Trades!M2:M500,Trades!C2:C500,A15)` for the average R, and `=SUMIFS(Trades!M2:M500,Trades!C2:C500,A15)` for the total R.
5. In Google Sheets, upload the xlsx or import the CSV (File, Import), then check the formulas in columns I, L and M.

The count formula uses `">-1E+99"` so it counts only rows where R is a number. A formula that returns an empty string would otherwise be counted as a row.

Fees go into P/L, so a trade stopped at exactly the stop shows a little worse than -1R. That is the real cost of the trade.
