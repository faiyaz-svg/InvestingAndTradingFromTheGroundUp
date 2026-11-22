# Shares, EPS, dilution and buybacks

<span class="tag tag-data">Data</span> <span class="tag tag-part">FIN</span>

After this lesson you can work out basic and diluted earnings per share with the treasury stock method, follow a company's share count through a year, and say what stock-based pay and buybacks do to your slice of the company.

Before this: [Debt, liquidity and solvency](08-debt-liquidity-and-solvency.md), and the buyback in [Dividends, splits and corporate actions](../01-how-markets-work/09-dividends-splits-and-corporate-actions.md). You need: a calculator.

## The idea

You own a slice of a company, and the size of the slice depends on how many shares exist. If Northwind earns US$165 million and has 100 million shares, each share has a claim on US$1.65. If the company creates more shares, that claim shrinks. If it buys shares back, the claim grows. **Earnings per share** (EPS) is net income divided by the number of shares, and it is the profit figure that connects the income statement to the price you pay per share.

Shares have several counts. **Shares issued** is every share the company has ever created and not cancelled. **Shares outstanding** is issued shares less treasury shares (those the company bought back and holds). Outstanding shares are the ones held by investors, and the 10-K cover page gives the latest count. A **weighted average** counts each share for the part of the year it existed.

## How it works

### Basic EPS

\[ \text{Basic EPS} = \frac{NI - P}{\bar{N}} \]

- \(NI\) is net income, in US$ millions.
- \(P\) is dividends owed to preferred shareholders (zero for Northwind).
- \(\bar{N}\) is the weighted average shares outstanding, in millions.

Northwind started FY2025 with 100.0 million shares, issued 0.5 million to employees who exercised options, and bought back 2.0 million, ending with 100.0 + 0.5 - 2.0 = 98.5 million. Its weighted average was 99.5 million. Basic EPS = 165 / 99.5 = US$1.66.

### Diluted EPS and the treasury stock method

Northwind has promises that could create more shares: employee **stock options** (the right to buy a share at a fixed strike price) and **restricted stock units** (RSUs, promises of shares that vest over time). **Diluted EPS** assumes those promises are used and divides by the larger share count. US GAAP requires companies to report both numbers.

For options, the **treasury stock method** assumes that when an option is exercised, the company uses the cash it receives to buy back shares at the average market price. Only the net new shares count:

\[ \text{Net new shares} = n - \frac{n \times K}{\bar{P}} \]

- \(n\) is the number of options, in millions.
- \(K\) is the strike price, in US$.
- \(\bar{P}\) is the average share price over the period, in US$.
- Options with \(K\) above \(\bar{P}\) are out of the money and add nothing (they would be **anti-dilutive**, raising EPS if counted, so the rules leave them out).

<div class="example" markdown>

### Worked example: diluted EPS

Northwind has 4.0 million options with a strike of US$20 and 0.6 million RSUs. The average share price in FY2025 was US$50.

1. Exercise cash = 4.0 x 20 = US$80 million.
2. Shares bought back with it = 80 / 50 = 1.6 million.
3. Net new shares from options = 4.0 - 1.6 = 2.4 million.
4. RSUs add 0.6 million. (Real filings adjust RSUs for unrecognized pay, which this book ignores.)
5. Diluted shares = 99.5 + 2.4 + 0.6 = 102.5 million.
6. Diluted EPS = 165 / 102.5 = US$1.61.

Dilution cut EPS from 1.66 to 1.61, which is 2.9%. Rounded to the cent at the end.

</div>

The figure follows the share count from the start of the year to basic and diluted. Look at how issuing and buying back almost cancel out, and how the diluted bar sits above both.

![Northwind share count in millions: start 100.0, issued 0.5, bought back 2.0, end 98.5, weighted basic 99.5, plus 2.4 option shares and 0.6 RSUs gives 102.5 diluted](../assets/figures/09-company-financials/share-bridge-dark.svg#only-dark)
![Northwind share count in millions: start 100.0, issued 0.5, bought back 2.0, end 98.5, weighted basic 99.5, plus 2.4 option shares and 0.6 RSUs gives 102.5 diluted](../assets/figures/09-company-financials/share-bridge-light.svg#only-light)

### Stock-based compensation

**Stock-based compensation** (SBC) pays employees in shares, options or RSUs. It is a real cost: the employees receive value that would otherwise cost cash, and existing shareholders' slice shrinks. It is also an expense that uses no cash in the period, so the cash flow statement adds it back (lesson 4). Northwind's SBC was US$30 million, which is 30 / 1,150 = 2.6% of revenue, and at US$50 a share it equals 0.6 million shares of pay. When you read free cash flow, look at SBC too: FCF of 125 less SBC of 30 leaves 95 (lesson 4).

### Buybacks

A **share buyback** (or repurchase) is the company spending cash to buy its own shares, which it then retires or holds as treasury shares. It reduces the count, so each remaining share has a larger claim on earnings. Northwind spent US$100 million to buy back 2.0 million shares at an average of US$50. With 0.5 million new shares issued, the net reduction is 1.5 million, or 1.5% of 100.0.

With the share price at US$50, the market cap at year end is 98.5 x 50 = US$4,925 million. The buyback was 100 / 4,925 = 2.0% of it. Adding the 30 of dividends, the company returned 130 / 4,925 = 2.6% of its market cap to shareholders (its **shareholder yield**).

Buybacks raise EPS even when profit does not move, because the divisor shrinks. They are worth the cash only if the price paid is below what the shares are worth, and in many companies they only offset the shares issued as pay. Compare the gross buyback (2.0 million) with the net reduction (1.5 million) to see how much they absorbed.

<div class="canada" markdown>

### For Canadians

Canadian-listed companies run buybacks through a normal course issuer bid (NCIB), announced to the exchange with a maximum number of shares. The same share-count and EPS rules apply, but check whether a company reports under IFRS, where EPS is also reported basic and diluted.

</div>

## Common mistakes

- Using the share count from last quarter's quote page. Use the weighted average for EPS, and the latest cover page count for market cap.
- Treating diluted EPS as a forecast. It is a calculation of what EPS would be if the promises were used today.
- Calling a buyback good because EPS rose. Check what it cost, and whether the share count really fell after pay.

## Try it

1\. A company has net income of US$80 million and 40 million weighted average shares. It has 10 million options with a US$30 strike and an average share price of US$45. Find basic EPS, the net new option shares and diluted EPS.

<details class="solution" markdown>
<summary>Answer</summary>

Basic EPS = 80 / 40 = US$2.00. Net new shares = 10 - (10 x 30) / 45 = 10 - 6.67 = 3.33 million. Diluted shares = 43.33 million, so diluted EPS = 80 / 43.33 = US$1.85.

</details>

2\. The average share price falls to US$25, below the US$30 strike. How many net new option shares count?

<details class="solution" markdown>
<summary>Answer</summary>

None. The options are out of the money, so exercising them would be a loss and they are left out (anti-dilutive).

</details>

3\. A company has 200 million shares and net income of US$400 million. It buys back 10 million shares and profit stays the same. What happens to EPS?

<details class="solution" markdown>
<summary>Answer</summary>

Before: 400 / 200 = US$2.00. After: 400 / 190 = US$2.11, up 5.3%. (In practice the cash spent also costs interest income or adds debt, so profit would move a little.)

</details>

4\. Northwind bought back 2.0 million shares at US$50 and issued 0.5 million. What share of the US$100 million buyback was absorbed by issuing new shares?

<details class="solution" markdown>
<summary>Answer</summary>

0.5 / 2.0 = 25%. A quarter of the shares it bought were replaced by new issues, so the net reduction was 1.5 million.

</details>

<div class="practice" markdown>

## Practice today (10 min)

| Minutes | Task |
|---|---|
| 4 | In a real 10-K, find the EPS note: basic and diluted EPS and the weighted shares for each. |
| 3 | Compute the dilution percentage (diluted divided by basic, minus 1). |
| 3 | Find the cash flow lines for share repurchases and stock-based compensation, and compare them. |

</div>

## Key terms

- **Earnings per share (EPS)**: net income divided by shares.
- **Shares issued**: all shares ever created and not cancelled.
- **Shares outstanding**: shares held by investors (issued less treasury shares).
- **Weighted average shares**: shares outstanding, each counted for the part of the period it existed.
- **Stock option**: the right to buy a share at a fixed strike price.
- **Restricted stock unit (RSU)**: a promise of shares that vest over time.
- **Diluted EPS**: EPS after counting shares that options, RSUs and similar promises could create.
- **Treasury stock method**: counting only the net new shares from options after assuming the proceeds buy back shares.
- **Anti-dilutive**: an item that would raise EPS if counted, so it is excluded.
- **Stock-based compensation (SBC)**: pay in shares, options or RSUs.
- **Share buyback**: the company buying its own shares, then retiring them or holding them as treasury shares.
- **Shareholder yield**: dividends plus buybacks as a share of market cap (some definitions net out new shares issued).
- **Dilution**: the shrinking of each shareholder's slice when the share count rises.

Next: [GAAP, non-GAAP and earnings quality](10-gaap-non-gaap-and-earnings-quality.md)
