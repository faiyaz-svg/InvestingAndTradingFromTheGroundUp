# Formulas

Every formula the book uses, grouped by topic, written the way its lesson writes it. Each row has a short line on the symbols and a link to the lesson that teaches it, with worked numbers. Check the lesson for units and for where the formula stops working.

## Markets, accounts and costs

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{Market cap} = P \times N \) | \(P\) is the share price, \(N\) the shares outstanding | [What a stock is](../01-how-markets-work/01-what-a-stock-is.md) |
| \( r = \frac{P_1 - P_0}{P_0} \) | \(r\) is the return, \(P_0\) the start price, \(P_1\) the end price | [What a stock is](../01-how-markets-work/01-what-a-stock-is.md) |
| \( \text{Spread} = A - B \qquad \text{Spread \%} = \frac{A - B}{(A + B)/2} \) | \(A\) is the best ask, \(B\) the best bid | [Bid, ask and the order book](../01-how-markets-work/04-bid-ask-and-the-order-book.md) |
| \( \text{Equity ratio} = \frac{V - L}{V} \) | \(V\) is the position value, \(L\) the loan | [Settlement, cash accounts and margin](../01-how-markets-work/07-settlement-cash-and-margin.md) |
| \( \text{Profit} = (P_0 - P_1) \times N - C \) | Short sale: \(P_0\) is the sale price, \(P_1\) the buy-back price, \(N\) the shares, \(C\) the costs | [Short selling](../01-how-markets-work/08-short-selling.md) |
| \( y = \frac{D}{P} \) | \(y\) is the dividend yield, \(D\) the yearly dividend per share, \(P\) the price | [Dividends, splits and corporate actions](../01-how-markets-work/09-dividends-splits-and-corporate-actions.md) |
| \( I = \frac{\sum P_i}{d} \) | Price-weighted index: \(P_i\) are the stock prices, \(d\) the divisor | [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md) |
| \( w_i = \frac{P_i \, N_i \, f_i}{\sum_j P_j \, N_j \, f_j} \) | Weight of stock \(i\): price, shares, and the share of shares available to the public (\(f_i\)) | [Indexes, sectors and market cap](../01-how-markets-work/10-indexes-sectors-and-market-cap.md) |
| \( \text{Change \%} = \frac{\text{Last} - \text{Previous close}}{\text{Previous close}} \) | Day change on a quote page | [Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md) |
| \( \text{Position} = \frac{\text{Last} - \text{Low}}{\text{High} - \text{Low}} \) | Where the last price sits in the day's range | [Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md) |
| \( \text{Relative volume} = \frac{\text{Volume}}{\text{Average volume}} \) | Volume against its average | [Reading a quote page](../01-how-markets-work/11-reading-a-quote-page.md) |
| \( \text{Yearly cost} = N \times (c + 2 f V) + F \) | \(N\) round trips a year, \(c\) commission per round trip, \(f\) currency fee per conversion, \(V\) position size, \(F\) fixed yearly fees | [Wealthsimple and IBKR compared](../02-accounts-currency-and-taxes/02-wealthsimple-and-ibkr.md) |
| \( \text{Conversion cost} = \frac{R_b - R_m}{R_m} \) | \(R_b\) is the broker's rate, \(R_m\) the mid-market rate | [USD or CAD, and currency conversion fees](../02-accounts-currency-and-taxes/03-usd-vs-cad-and-fx-fees.md) |
| \( 1 + r_c = (1 + r_s)(1 + r_x) \) | CAD return \(r_c\) from the stock return \(r_s\) and the currency return \(r_x\) | [Currency risk on US stocks](../02-accounts-currency-and-taxes/05-currency-risk-on-us-stocks.md) |
| \( \text{Gain} = P_{\text{CAD}} - n \times \text{ACB per share} \) | \(P_{\text{CAD}}\) is the proceeds in C$, \(n\) the shares sold | [Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md) |
| \( V_{\text{call}} = \frac{L}{1 - m} \) | Position value that triggers a margin call: \(L\) is the loan, \(m\) the maintenance requirement | [Margin rules in Canada](../02-accounts-currency-and-taxes/10-margin-rules-in-canada.md) |

## Risk and sizing

| Formula | Symbols | Lesson |
|---|---|---|
| \( (1 - L)(1 + G) = 1 \quad\Rightarrow\quad G = \frac{L}{1 - L} \) | \(L\) is a loss, \(G\) the gain needed to get back to even | [Risk first](../03-risk-and-position-sizing/01-risk-first.md) |
| \( \text{risk per share} = E - S \qquad R = N \times (E - S) \qquad r = \frac{X - E}{E - S} \) | \(E\) entry, \(S\) stop, \(X\) exit, \(N\) shares, \(R\) the risk in dollars, \(r\) the result in R | [R-multiples](../03-risk-and-position-sizing/02-r-multiples.md) |
| \( p = \frac{\text{winners}}{\text{trades}} \qquad b = \frac{W}{L} \qquad E = p\,W - (1 - p)\,L \) | \(p\) win rate, \(W\) average win, \(L\) average loss, \(b\) payoff ratio, \(E\) expectancy | [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md) |
| \( p_{\text{break-even}} = \frac{1}{1 + b} \) | Win rate at which expectancy is zero | [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md) |
| \( SE = \sqrt{\frac{p\,(1 - p)}{n}} \) | Standard error of a win rate over \(n\) trades | [Win rate, payoff and expectancy](../03-risk-and-position-sizing/03-win-rate-payoff-and-expectancy.md) |
| \( \text{shares} = \left\lfloor \frac{f \times A}{E - S} \right\rfloor \) | \(f\) is the share of the account risked, \(A\) the account | [Position sizing with fixed fractional risk](../03-risk-and-position-sizing/04-fixed-fractional-sizing.md) |
| \( TR = \max\bigl(H - L,\ \lvert H - C_{\text{prev}}\rvert,\ \lvert L - C_{\text{prev}}\rvert\bigr) \) | True range from high \(H\), low \(L\) and the previous close | [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md) |
| \( S = E - k \times ATR \) | ATR stop: \(k\) is the multiple of the average true range | [Where to put the stop](../03-risk-and-position-sizing/05-where-to-put-the-stop.md) |
| \( r_{\text{stop}} = -\frac{E - F}{E - S} \) | Result in R of a stop that fills at \(F\) | [Slippage, gaps and costs](../03-risk-and-position-sizing/06-slippage-gaps-and-costs.md) |
| \( \text{open risk} = N \times (P - S) \qquad \text{heat} = \frac{\sum \text{open risk}}{A} \) | \(P\) is the current price, \(A\) the account | [Portfolio heat and correlation](../03-risk-and-position-sizing/07-portfolio-heat-and-correlation.md) |
| \( \text{effective bets} = \frac{n}{1 + (n - 1)\rho} \qquad \text{spread of outcomes} = \sqrt{n + n(n - 1)\rho} \times \sigma \) | \(n\) positions, \(\rho\) average correlation, \(\sigma\) the standard deviation of one position's result | [Portfolio heat and correlation](../03-risk-and-position-sizing/07-portfolio-heat-and-correlation.md) |
| \( DD_t = \frac{\text{peak}_t - \text{equity}_t}{\text{peak}_t} \) | Drawdown at time \(t\) | [Drawdowns and risk of ruin](../03-risk-and-position-sizing/08-drawdowns-and-risk-of-ruin.md) |
| \( P(\text{ruin}) = \left(\frac{1 - p}{p}\right)^{N} \) | \(p\) win probability (above 0.5), \(N\) the account in bet units | [Drawdowns and risk of ruin](../03-risk-and-position-sizing/08-drawdowns-and-risk-of-ruin.md) |
| \( g(f) = p \ln(1 + b f) + (1 - p)\ln(1 - f) \) | Growth rate per bet when you risk fraction \(f\) | [The Kelly criterion and fractional Kelly](../03-risk-and-position-sizing/09-kelly-and-fractional-kelly.md) |
| \( \frac{p\,b}{1 + b f} = \frac{1 - p}{1 - f} \quad\Rightarrow\quad f^{*} = p - \frac{1 - p}{b} \) | \(f^{*}\) is the Kelly fraction | [The Kelly criterion and fractional Kelly](../03-risk-and-position-sizing/09-kelly-and-fractional-kelly.md) |
| \( v(x) = x^{0.88} \text{ for } x \ge 0, \qquad v(x) = -2.25\,(-x)^{0.88} \text{ for } x < 0 \) | Prospect theory value of a gain or loss \(x\) | [Biases that cost traders money](../04-psychology-journal-and-paper-trading/01-biases-that-cost-traders.md) |
| \( \text{Reward-to-risk} = \frac{T - E}{E - S} \quad \text{(long trade)} \) | \(T\) is the target | [Rules and checklists](../04-psychology-journal-and-paper-trading/03-rules-and-checklists.md) |
| \( \text{Risk} = \lvert E - S\rvert \times N \) | Dollar risk of a trade | [The trade journal](../04-psychology-journal-and-paper-trading/04-the-trade-journal.md) |
| \( \text{P/L} = (X - E) \times N \times d - F \) | \(d\) is +1 for a long and -1 for a short, \(F\) the fees | [The trade journal](../04-psychology-journal-and-paper-trading/04-the-trade-journal.md) |
| \( R = \frac{\text{P/L}}{\text{Risk}} \) | Result in R | [The trade journal](../04-psychology-journal-and-paper-trading/04-the-trade-journal.md) |
| \( p_{\text{be}} = \frac{1}{1 + r} \) | Break-even win rate for reward-to-risk \(r\) | [Entries, stops and targets](../07-swing-trading/07-entries-stops-and-targets.md) |
| \( \text{room} = \frac{L - E}{E - S} \) | Room to the nearest level \(L\), in R | [Premarket prep](../08-day-trading/02-premarket-prep.md) |
| \( c = s + 2f + 2k \) | Round-trip cost per share: spread \(s\), commission \(f\), extra slippage \(k\) | [Execution costs and scalping](../08-day-trading/08-execution-costs-and-scalping.md) |
| \( c_R = \frac{c}{r} \) | Cost in R, with \(r\) the risk per share | [Execution costs and scalping](../08-day-trading/08-execution-costs-and-scalping.md) |
| \( p^{*} = \frac{1 + c_R}{T + 1} \) | Break-even win rate after costs, for a target of \(T\) R | [Execution costs and scalping](../08-day-trading/08-execution-costs-and-scalping.md) |
| \( N = \min\left( \left\lfloor \frac{\text{risk amount}}{E - S} \right\rfloor, \left\lfloor \frac{\text{buying power}}{E} \right\rfloor \right) \) | Day trade size: the smaller of the risk limit and the buying power limit | [A day trading routine and limits](../08-day-trading/09-day-trading-routine-and-limits.md) |
| \( \text{contracts} = \left\lfloor \frac{f \times A}{T \times V} \right\rfloor \) | Futures size: \(T\) is the stop distance in ticks, \(V\) the tick value | [Index futures](../14-futures/03-index-futures.md) |

## Indicators and chart measures

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{Range} = H - L, \quad \text{Body} = \lvert C - O\rvert, \quad \text{Upper wick} = H - \max(O, C), \quad \text{Lower wick} = \min(O, C) - L \) | Candle parts from open \(O\), high \(H\), low \(L\), close \(C\) | [Candles, bars and timeframes](../05-reading-charts/01-candles-bars-and-timeframes.md) |
| \( \text{CL} = \frac{C - L}{H - L} \) | Close location within the bar | [Candles, bars and timeframes](../05-reading-charts/01-candles-bars-and-timeframes.md) |
| \( \text{RVOL} = \frac{V_t}{\bar{V}_{20}} \) | Relative volume: today's volume over the 20-day average | [Volume and relative volume](../05-reading-charts/04-volume-and-relative-volume.md) |
| \( \text{SMA}_t = \frac{1}{N} \sum_{i=0}^{N-1} C_{t-i} \) | Simple moving average over \(N\) closes | [Moving averages](../05-reading-charts/05-moving-averages.md) |
| \( \text{EMA}_t = k\,C_t + (1 - k)\,\text{EMA}_{t-1}, \qquad k = \frac{2}{N + 1} \) | Exponential moving average with weight \(k\) | [Moving averages](../05-reading-charts/05-moving-averages.md) |
| \( \text{RSI} = 100 - \frac{100}{1 + RS}, \qquad RS = \frac{\text{average gain}}{\text{average loss}} \) | Relative strength index | [Momentum indicators](../05-reading-charts/06-momentum-indicators.md) |
| \( \text{MACD} = \text{EMA}_{12} - \text{EMA}_{26}, \quad \text{Signal} = \text{EMA}_9(\text{MACD}), \quad \text{Histogram} = \text{MACD} - \text{Signal} \) | MACD line, signal line and histogram | [Momentum indicators](../05-reading-charts/06-momentum-indicators.md) |
| \( \text{raw } \%K = 100 \times \frac{C - LL_{14}}{HH_{14} - LL_{14}} \) | Stochastic: \(LL_{14}\) and \(HH_{14}\) are the 14-bar lowest low and highest high | [Momentum indicators](../05-reading-charts/06-momentum-indicators.md) |
| \( TR = \max\big(H - L,\ \lvert H - C_{prev}\rvert,\ \lvert L - C_{prev}\rvert\big) \) | True range | [Volatility indicators](../05-reading-charts/07-volatility-indicators.md) |
| \( ATR_t = \frac{(N-1)\,ATR_{t-1} + TR_t}{N} \) | Average true range, smoothed over \(N\) bars | [Volatility indicators](../05-reading-charts/07-volatility-indicators.md) |
| \( \text{Middle} = \text{SMA}_{20}, \qquad \text{Upper} = \text{Middle} + 2\sigma, \qquad \text{Lower} = \text{Middle} - 2\sigma \) | Bollinger Bands, with \(\sigma\) the standard deviation of the closes | [Volatility indicators](../05-reading-charts/07-volatility-indicators.md) |
| \( \text{VWAP}_t = \frac{\sum_{i=1}^{t} TP_i \times V_i}{\sum_{i=1}^{t} V_i}, \qquad TP_i = \frac{H_i + L_i + C_i}{3} \) | Volume-weighted average price from typical price \(TP\) and volume \(V\) | [VWAP and anchored VWAP](../05-reading-charts/08-vwap-and-anchored-vwap.md) |
| \( \text{Gap} = O_t - C_{t-1}, \qquad \text{Gap \%} = \frac{O_t - C_{t-1}}{C_{t-1}}, \qquad \text{Gap in ATR} = \frac{O_t - C_{t-1}}{ATR_{t-1}} \) | Gap from the previous close to today's open | [Gaps](../05-reading-charts/10-gaps.md) |
| \( RS_t = 100 \times \frac{S_t / S_0}{I_t / I_0} \) | Relative strength of stock \(S\) against index \(I\), both from a start date 0 | [Multiple timeframes and relative strength](../05-reading-charts/11-multi-timeframe-and-relative-strength.md) |
| \( \text{level}_k = H - k\,(H - L) \) | Retracement level at fraction \(k\) of a swing from \(H\) to \(L\) | [Sessions, kill zones and premium and discount](../06-ict-and-smart-money-tested/05-sessions-kill-zones-and-premium-discount.md) |
| \( I = \frac{B - A}{B + A} \) | Order book imbalance from bid size \(B\) and ask size \(A\) | [Level 2 and time and sales](../08-day-trading/07-level-2-and-time-and-sales.md) |

## Financial statements and ratios

The [ratios page](ratios.md) adds what each ratio tells you and its usual caveat.

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{Gross profit} = R - C \qquad \text{EBIT} = \text{Gross profit} - O \qquad \text{EBITDA} = \text{EBIT} + D \) | \(R\) revenue, \(C\) cost of goods sold, \(O\) operating expenses, \(D\) depreciation and amortization | [The income statement](../09-company-financials/02-the-income-statement.md) |
| \( \text{Net income} = (\text{EBIT} - I) \times (1 - t) \) | \(I\) is interest expense, \(t\) the tax rate | [The income statement](../09-company-financials/02-the-income-statement.md) |
| \( A = L + E \) | Assets equal liabilities plus equity | [The balance sheet](../09-company-financials/03-the-balance-sheet.md) |
| \( \text{PP\&E}_{\text{end}} = \text{PP\&E}_{\text{start}} + \text{capex} - \text{depreciation} \) | Roll-forward of property, plant and equipment | [The balance sheet](../09-company-financials/03-the-balance-sheet.md) |
| \( \text{CFO} = NI + D + S + \Delta W \) | Operating cash flow from net income, D&A, stock pay \(S\) and working capital changes \(\Delta W\) | [The cash flow statement](../09-company-financials/04-the-cash-flow-statement.md) |
| \( \text{FCF} = \text{CFO} - \text{capex} \) | Free cash flow | [The cash flow statement](../09-company-financials/04-the-cash-flow-statement.md) |
| \( \text{Margin} = \frac{\text{Profit measure}}{R} \) | Gross, operating, EBITDA or net margin | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |
| \( g = \frac{X_1 - X_0}{X_0} \) | Growth between two periods | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |
| \( \text{CAGR} = \left(\frac{X_n}{X_0}\right)^{1/n} - 1 \) | Compound annual growth rate over \(n\) years | [Margins and growth](../09-company-financials/06-margins-and-growth.md) |
| \( \text{ROE} = \frac{NI}{\bar{E}} \qquad \text{ROA} = \frac{NI}{\bar{A}} \qquad \text{ROIC} = \frac{\text{NOPAT}}{\bar{IC}} \) | Bars mark averages of the opening and closing balances | [Returns on capital](../09-company-financials/07-returns-on-capital.md) |
| \( \text{ROE} = \frac{NI}{R} \times \frac{R}{\bar{A}} \times \frac{\bar{A}}{\bar{E}} \) | DuPont: net margin, asset turnover, equity multiplier | [Returns on capital](../09-company-financials/07-returns-on-capital.md) |
| \( \text{Current ratio} = \frac{CA}{CL} \qquad \text{Quick ratio} = \frac{\text{Cash} + AR}{CL} \) | \(CA\) current assets, \(CL\) current liabilities, \(AR\) receivables | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| \( \text{Debt to equity} = \frac{D}{E} \qquad \text{Net debt} = D - \text{Cash} \qquad \text{Interest coverage} = \frac{\text{EBIT}}{I} \) | \(D\) total debt, \(E\) equity, \(I\) interest expense | [Debt, liquidity and solvency](../09-company-financials/08-debt-liquidity-and-solvency.md) |
| \( \text{Basic EPS} = \frac{NI - P}{\bar{N}} \) | \(P\) is preferred dividends, \(\bar{N}\) the weighted average shares | [Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md) |
| \( \text{Net new shares} = n - \frac{n \times K}{\bar{P}} \) | Treasury stock method: \(n\) options, strike \(K\), average price \(\bar{P}\) | [Shares, EPS, dilution and buybacks](../09-company-financials/09-shares-eps-dilution-and-buybacks.md) |
| \( \text{Cash conversion} = \frac{\text{CFO}}{NI} \qquad \text{Accrual ratio} = \frac{NI - \text{CFO}}{\bar{A}} \) | Two earnings quality tests | [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md) |
| \( \text{DSO} = \frac{AR}{R} \times 365 \qquad \text{DIO} = \frac{\text{Inventory}}{C} \times 365 \) | Days of sales in receivables, days of cost of goods sold in inventory | [GAAP, non-GAAP and earnings quality](../09-company-financials/10-gaap-non-gaap-and-earnings-quality.md) |
| \( \text{Surprise} = A - E \qquad \text{Surprise \%} = \frac{A - E}{\lvert E\rvert} \) | \(A\) actual, \(E\) expected (the consensus) | [Earnings season and earnings calls](../09-company-financials/11-earnings-season-and-calls.md) |

## Valuation

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{P/E} = \frac{P}{\text{EPS}} \) | Price over earnings per share | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| \( \text{Earnings yield} = \frac{\text{EPS}}{P} = \frac{1}{\text{P/E}} \) | The P/E turned upside down | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| \( \text{P/S} = \frac{\text{market cap}}{\text{revenue}} \qquad \text{P/B} = \frac{\text{market cap}}{\text{book equity}} \) | Price to sales, price to book | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| \( \text{PEG} = \frac{\text{P/E}}{g} \) | \(g\) is expected EPS growth in percent per year | [Price multiples](../10-valuation-and-research/01-multiples.md) |
| \( \text{EV} = \text{equity value} + \text{debt} + \text{preferred stock} + \text{minority interest} - \text{cash} \) | Enterprise value | [Enterprise value and EV/EBITDA](../10-valuation-and-research/02-enterprise-value-and-ev-ebitda.md) |
| \( \text{EV/EBITDA} = \frac{\text{EV}}{\text{EBITDA}} \qquad \text{EV/sales} = \frac{\text{EV}}{\text{revenue}} \) | Multiples that match EV with a profit before interest | [Enterprise value and EV/EBITDA](../10-valuation-and-research/02-enterprise-value-and-ev-ebitda.md) |
| \( \text{Levered FCF} = \text{CFO} - \text{capex} \) | Free cash flow after interest | [Free cash flow](../10-valuation-and-research/03-free-cash-flow.md) |
| \( \text{UFCF} = \text{EBIT} \times (1 - t) + \text{D\&A} - \text{capex} - \Delta \text{NWC} \) | Unlevered free cash flow; \(\Delta\text{NWC}\) is the rise in net working capital | [Free cash flow](../10-valuation-and-research/03-free-cash-flow.md) |
| \( k_e = r_f + \beta \times \text{ERP} \) | CAPM cost of equity: risk-free rate, beta, equity risk premium | [Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md) |
| \( \text{WACC} = \frac{E}{E + D}\, k_e + \frac{D}{E + D}\, k_d (1 - t) \) | Weights use market values; \(k_d\) is the cost of debt, \(t\) the tax rate | [Discount rates, CAPM and WACC](../10-valuation-and-research/04-discount-rates-capm-and-wacc.md) |
| \( \text{TV}_5 = \frac{\text{UFCF}_5 \times (1 + g)}{r - g} \) | Terminal value after year 5: growth \(g\), discount rate \(r\) | [A DCF step by step](../10-valuation-and-research/05-dcf-step-by-step.md) |
| \( \text{EV} = \frac{\text{UFCF} \times (1 + g)}{r - g} \quad\Rightarrow\quad g = \frac{r \times \text{EV} - \text{UFCF}}{\text{EV} + \text{UFCF}} \) | Growth the price implies | [Reverse DCF and market expectations](../10-valuation-and-research/06-reverse-dcf-and-expectations.md) |
| \( \text{NRR} = \frac{\text{start ARR} + \text{expansion} - \text{contraction} - \text{churn}}{\text{start ARR}} \) | Net revenue retention for a software company | [Comparables and industry KPIs](../10-valuation-and-research/07-comparables-and-industry-kpis.md) |
| \( \text{Economic profit} = \text{NOPAT} - \text{WACC} \times \text{invested capital} \) | Profit above the cost of capital | [Moats and qualitative research](../10-valuation-and-research/08-moats-and-qualitative-research.md) |

## Macro

| Formula | Symbols | Lesson |
|---|---|---|
| \( S = A - C \) | Surprise: actual minus consensus | [How the economy is measured](../11-macro-and-economic-data/01-how-the-economy-is-measured.md) |
| \( r_{\text{annual}} = (1 + r_{\text{month}})^{12} - 1 \) | Monthly change restated as a yearly pace | [How the economy is measured](../11-macro-and-economic-data/01-how-the-economy-is-measured.md) |
| \( p = \frac{R_0 - (100 - F)}{\Delta} \) | Odds of a cut from a fed funds futures price \(F\): \(R_0\) is the middle of the current range, \(\Delta\) the size of the cut | [The Fed and the FOMC](../11-macro-and-economic-data/02-the-fed-and-the-fomc.md) |
| \( PV = \sum_{t=1}^{T} \frac{CF_t}{(1+r)^t} \) | Present value of cash flows \(CF_t\) at rate \(r\) | [Interest rates and asset prices](../11-macro-and-economic-data/03-interest-rates-and-asset-prices.md) |
| \( u = \frac{U}{L} \times 100 \) | Unemployment rate: unemployed over the labour force | [The jobs report](../11-macro-and-economic-data/05-the-jobs-report.md) |
| \( g_{\text{annual}} = (1 + g_{\text{quarter}})^4 - 1 \) | GDP growth restated at an annual rate | [Growth data](../11-macro-and-economic-data/06-growth-data.md) |
| \( D = P_{\text{higher}} + 0.5 \times P_{\text{same}} \) | Diffusion index for a PMI | [Growth data](../11-macro-and-economic-data/06-growth-data.md) |

## Bonds

| Formula | Symbols | Lesson |
|---|---|---|
| \( P = \sum_{k=1}^{N} \frac{C}{(1+i)^k} + \frac{F}{(1+i)^N} \) | Bond price: coupon \(C\) per period, face value \(F\), yield per period \(i\), \(N\) periods | [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md) |
| \( \text{CY} = \frac{\text{annual coupon}}{P} \) | Current yield | [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md) |
| \( \text{Accrued} = C \times \frac{d}{D} \) | Accrued interest: \(d\) days since the last coupon, \(D\) days in the period | [Bond prices and yields](../12-bonds-and-the-yield-curve/01-bond-prices-and-yields.md) |
| \( P = F \left(1 - \frac{d \times t}{360}\right) \) | Treasury bill price from the discount rate \(d\) and \(t\) days | [Treasuries and TIPS](../12-bonds-and-the-yield-curve/02-treasuries-and-tips.md) |
| \( y_{BEY} = \frac{F - P}{P} \times \frac{365}{t} = \frac{365\, d}{360 - d\, t} \) | Bond equivalent yield of a bill | [Treasuries and TIPS](../12-bonds-and-the-yield-curve/02-treasuries-and-tips.md) |
| \( \text{Adjusted principal} = F \times \text{index ratio}, \qquad \text{index ratio} = \frac{\text{CPI reference at settlement}}{\text{CPI reference at issue}} \) | TIPS principal | [Treasuries and TIPS](../12-bonds-and-the-yield-curve/02-treasuries-and-tips.md) |
| \( \pi_{BE} = \frac{1 + y_{nom}}{1 + y_{real}} - 1 \approx y_{nom} - y_{real} \) | Break-even inflation from nominal and real yields | [Treasuries and TIPS](../12-bonds-and-the-yield-curve/02-treasuries-and-tips.md) |
| \( S_{2s10s} = y_{10Y} - y_{2Y}, \qquad S_{3m10y} = y_{10Y} - y_{3M} \) | Yield curve spreads | [The yield curve](../12-bonds-and-the-yield-curve/03-the-yield-curve.md) |
| \( \Pr(\text{recession in month } t+12) = \Phi\left(\alpha + \beta \times S_t\right), \qquad \alpha = -0.6045,\ \beta = -0.7374 \) | Probit model of recession odds from the spread \(S_t\); \(\Phi\) is the normal distribution function | [The yield curve](../12-bonds-and-the-yield-curve/03-the-yield-curve.md) |
| \( \text{Sahm gap}_t = \bar{u}_t - \min\left(\bar{u}_{t-12}, \dots, \bar{u}_{t-1}\right) \) | Sahm rule gap from the averaged unemployment rate \(\bar{u}\) | [The yield curve](../12-bonds-and-the-yield-curve/03-the-yield-curve.md) |
| \( D_{mac} = \frac{1}{P} \sum_{k=1}^{N} \frac{t_k \times CF_k}{(1+i)^k} \) | Macaulay duration | [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md) |
| \( D_{mod} = \frac{D_{mac}}{1 + y/2}, \qquad \frac{\Delta P}{P} \approx -D_{mod} \times \Delta y \) | Modified duration and the price change for a yield change \(\Delta y\) | [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md) |
| \( \frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \tfrac{1}{2}\, C\, (\Delta y)^2, \qquad C = \frac{1}{P} \sum_{k=1}^{N} \frac{CF_k \, k(k+1)/4}{(1+i)^{k+2}} \) | Duration plus convexity \(C\) | [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md) |
| \( DV01 = D_{mod} \times P \times 0.0001 \) | Dollar change for one basis point | [Duration and convexity](../12-bonds-and-the-yield-curve/04-duration-and-convexity.md) |
| \( \text{Spread} = y_{corp} - y_{Treasury} \) | Credit spread | [Credit spreads and high yield](../12-bonds-and-the-yield-curve/05-credit-spreads-and-high-yield.md) |
| \( EL = p \times (1 - R) \) | Expected loss: default probability \(p\), recovery rate \(R\) | [Credit spreads and high yield](../12-bonds-and-the-yield-curve/05-credit-spreads-and-high-yield.md) |
| \( \frac{\Delta P}{P} \approx -D_{mod} \times \Delta s \) | Price change for a spread change \(\Delta s\) | [Credit spreads and high yield](../12-bonds-and-the-yield-curve/05-credit-spreads-and-high-yield.md) |
| \( R \approx y - D_{eff} \times \Delta y \) | One-year return of a bond fund from its yield and effective duration | [Bond ETFs, and rates against stocks](../12-bonds-and-the-yield-curve/06-bond-etfs-and-rates-vs-stocks.md) |
| \( \text{Earnings yield} = \frac{E}{P} = \frac{1}{P/E} \) | Used to compare stocks with bonds | [Bond ETFs, and rates against stocks](../12-bonds-and-the-yield-curve/06-bond-etfs-and-rates-vs-stocks.md) |

## ETFs and portfolios

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{NAV} = \frac{A - L}{N} \) | Net asset value per share: assets, liabilities, shares | [How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md) |
| \( \text{premium or discount} = \frac{P - \text{NAV}}{\text{NAV}} \) | Market price against NAV | [How ETFs work](../13-etfs-portfolios-and-factors/01-how-etfs-work.md) |
| \( V_{30} = V_0 \, (1 + g - f)^{30} \) | Value after 30 years with growth \(g\) and fee \(f\) | [Index funds, fees and tracking](../13-etfs-portfolios-and-factors/02-index-funds-fees-and-tracking.md) |
| \( TE = \sqrt{12} \times \text{sd}\left(r_{\text{fund},m} - r_{\text{index},m}\right) \) | Tracking error from monthly return differences | [Index funds, fees and tracking](../13-etfs-portfolios-and-factors/02-index-funds-fees-and-tracking.md) |
| \( (1 + L r_1)(1 + L r_2) - 1 = L(r_1 + r_2) + L^2 r_1 r_2 \) | Two days of a fund with leverage \(L\) | [Leveraged and inverse ETFs](../13-etfs-portfolios-and-factors/04-leveraged-and-inverse-etfs.md) |
| \( g_L \approx L\mu - \frac{L^2 \sigma^2}{2} \) | Growth of a leveraged fund; \(\mu\) is the index's average return, \(\sigma\) its volatility | [Leveraged and inverse ETFs](../13-etfs-portfolios-and-factors/04-leveraged-and-inverse-etfs.md) |
| \( E[R_p] = w_s E[R_s] + w_b E[R_b] \) | Expected return of a stock and bond mix | [Asset allocation](../13-etfs-portfolios-and-factors/05-asset-allocation.md) |
| \( \sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho \, \sigma_1 \sigma_2 \) | Variance of a two-asset portfolio | [Diversification and correlation](../13-etfs-portfolios-and-factors/06-diversification-and-correlation.md) |
| \( \sigma_p^2 = \sigma^2 \left( \frac{1}{N} + \left(1 - \frac{1}{N}\right) \rho \right) \) | Variance of \(N\) equal-weight assets with the same \(\sigma\) and correlation \(\rho\) | [Diversification and correlation](../13-etfs-portfolios-and-factors/06-diversification-and-correlation.md) |
| \( T_i = w_i^{*} V - H_i \) | Rebalancing trade for fund \(i\): target weight, portfolio value, current holding | [Rebalancing](../13-etfs-portfolios-and-factors/07-rebalancing.md) |
| \( \mu_p = \sum_i w_i \mu_i, \qquad \sigma_p^2 = \sum_i \sum_j w_i w_j \sigma_i \sigma_j \rho_{ij} \) | Portfolio return and variance | [Modern portfolio theory](../13-etfs-portfolios-and-factors/08-modern-portfolio-theory.md) |
| \( w_A = \frac{\sigma_B^2 - \rho \sigma_A \sigma_B}{\sigma_A^2 + \sigma_B^2 - 2 \rho \sigma_A \sigma_B} \) | Minimum variance weight of asset A in a two-asset mix | [Modern portfolio theory](../13-etfs-portfolios-and-factors/08-modern-portfolio-theory.md) |
| \( S = \frac{\mu_p - r_f}{\sigma_p} \) | Sharpe ratio | [Modern portfolio theory](../13-etfs-portfolios-and-factors/08-modern-portfolio-theory.md) |
| \( E[r_i - r_f] = \beta_i \, E[r_m - r_f], \qquad \beta_i = \frac{\text{Cov}(r_i, r_m)}{\text{Var}(r_m)} \) | CAPM | [Factor investing](../13-etfs-portfolios-and-factors/09-factor-investing.md) |
| \( r_i - r_f = \alpha + b\,(r_m - r_f) + s\,\text{SMB} + h\,\text{HML} + \varepsilon \) | Three-factor regression; SMB is size, HML is value | [Factor investing](../13-etfs-portfolios-and-factors/09-factor-investing.md) |

## Futures

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{P\&L} = (P_{\text{exit}} - P_{\text{entry}}) \times M \times n \quad \text{for a long position} \) | \(M\) is the multiplier, \(n\) the contracts | [What futures are](../14-futures/01-what-futures-are.md) |
| \( N = P \times M \times n \) | Notional value | [Margin, leverage and mark to market](../14-futures/02-margin-leverage-and-mark-to-market.md) |
| \( E_t = E_{t-1} + (S_t - S_{t-1}) \times M \times n \quad \text{for a long position} \) | Daily mark to market of account equity; \(S_t\) is the settlement price | [Margin, leverage and mark to market](../14-futures/02-margin-leverage-and-mark-to-market.md) |
| \( \text{contracts} = \left\lfloor \frac{f \times A}{T \times V} \right\rfloor \) | Position size from the risk limit | [Index futures](../14-futures/03-index-futures.md) |
| \( F = S \times \bigl(1 + (r - d) \times T\bigr) \) | Fair futures price: spot \(S\), interest rate \(r\), dividend yield \(d\), time \(T\) in years | [Contango, backwardation and basis](../14-futures/05-contango-backwardation-and-basis.md) |

## Options and Greeks

The lessons give theta and rho in code and as numbers, not as a formula. See [Theta, vega and rho](../15-options/07-theta-vega-and-rho.md).

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{call payoff} = \max(S_T - K,\ 0) \qquad \text{put payoff} = \max(K - S_T,\ 0) \) | \(S_T\) stock price at expiry, \(K\) strike | [Payoff diagrams](../15-options/02-payoff-diagrams.md) |
| \( \text{long profit} = \text{payoff} - p \qquad \text{short profit} = p - \text{payoff} \) | \(p\) is the premium per share | [Payoff diagrams](../15-options/02-payoff-diagrams.md) |
| \( \text{call breakeven} = K + p \qquad \text{put breakeven} = K - p \) | Expiry price where profit is zero | [Payoff diagrams](../15-options/02-payoff-diagrams.md) |
| \( \text{premium} = \text{intrinsic value} + \text{time value} \) | Split of an option's price | [The options chain and moneyness](../15-options/03-the-chain-and-moneyness.md) |
| \( C = S e^{-qT} N(d_1) - K e^{-rT} N(d_2) \qquad P = K e^{-rT} N(-d_2) - S e^{-qT} N(-d_1) \) | Black-Scholes: \(q\) dividend yield, \(r\) rate, \(T\) years, \(N\) the normal distribution function | [What sets an option's price](../15-options/04-what-sets-an-option-price.md) |
| \( d_1 = \frac{\ln(S/K) + (r - q + \sigma^2/2)\,T}{\sigma \sqrt{T}} \qquad d_2 = d_1 - \sigma \sqrt{T} \) | \(\sigma\) is the volatility | [What sets an option's price](../15-options/04-what-sets-an-option-price.md) |
| \( C + K e^{-rT} = P + S \quad\Longleftrightarrow\quad C - P = S - K e^{-rT} \) | Put-call parity | [Put-call parity](../15-options/05-put-call-parity.md) |
| \( C - P = S e^{-qT} - K e^{-rT} \) | Parity with a dividend yield | [Put-call parity](../15-options/05-put-call-parity.md) |
| \( S - K \le C - P \le S - K e^{-rT} \) | \(C\) and \(P\) are American prices, with no dividends | [Put-call parity](../15-options/05-put-call-parity.md) |
| \( \Delta = \frac{\text{change in option price}}{\text{change in stock price}} \) | Delta | [Delta and gamma](../15-options/06-delta-and-gamma.md) |
| \( \Gamma = \frac{\text{change in delta}}{\text{change in stock price}} \) | Gamma | [Delta and gamma](../15-options/06-delta-and-gamma.md) |
| \( \mathcal{V} = \frac{S\, e^{-qT}\, n(d_1)\, \sqrt{T}}{100} \) | Vega per volatility point; \(n\) is the normal density | [Theta, vega and rho](../15-options/07-theta-vega-and-rho.md) |
| \( \text{expected move} \approx S \times \text{IV} \times \sqrt{T} \) | One standard deviation move from implied volatility | [Implied volatility](../15-options/08-implied-volatility.md) |
| \( \text{covered call} = (S - 50.20) + 2.10 - \max(S - 52.50,\, 0) \) | The lesson's example per share; see [options strategies](options-strategies.md) for the general rules | [Covered calls and cash-secured puts](../15-options/09-covered-calls-and-cash-secured-puts.md) |
| \( \text{cash-secured put} = 1.80 - \max(47.50 - S,\, 0) \) | The lesson's example per share | [Covered calls and cash-secured puts](../15-options/09-covered-calls-and-cash-secured-puts.md) |
| \( \text{debit spread: max profit} = (W - D) \times 100, \quad \text{max loss} = D \times 100 \) | \(W\) is the strike width, \(D\) the debit per share | [Vertical spreads](../15-options/10-vertical-spreads.md) |
| \( \text{credit spread: max profit} = D \times 100, \quad \text{max loss} = (W - D) \times 100 \) | \(D\) is the credit per share | [Vertical spreads](../15-options/10-vertical-spreads.md) |
| \( \text{profit} = \max(S - K_c, 0) + \max(K_p - S, 0) - D \) | Long straddle or strangle with call strike \(K_c\) and put strike \(K_p\) | [Straddles and strangles](../15-options/11-straddles-and-strangles.md) |
| \( \text{condor: max profit} = C \times 100, \quad \text{max loss} = (W - C) \times 100 \) | \(C\) is the credit, \(W\) the wing width | [Iron condors and butterflies](../15-options/12-iron-condors-and-butterflies.md) |
| \( \text{butterfly: max profit} = (W - D) \times 100, \quad \text{max loss} = D \times 100 \) | \(D\) is the debit | [Iron condors and butterflies](../15-options/12-iron-condors-and-butterflies.md) |
| \( \text{profit} = -\max(S - K_s, 0) + V_{far}(S) - D \) | Calendar or diagonal when the near leg expires; \(V_{far}\) is the model value of the far leg | [Calendars and diagonals](../15-options/13-calendars-and-diagonals.md) |
| \( \text{exercise early if } D > \text{time value} + i \) | \(D\) is the dividend, \(i\) the interest lost by paying the strike early | [Assignment, exercise and 0DTE](../15-options/14-assignment-exercise-and-0dte.md) |

## Commodities, forex and REITs

| Formula | Symbols | Lesson |
|---|---|---|
| \( V_{12} = V_0 \times \frac{S_{12}}{S_0} \times \left(\frac{1}{1+c}\right)^{12} \) | Value of a commodity ETF after 12 monthly rolls with contango \(c\) per month | [Commodity ETFs and roll costs](../17-commodities-forex-and-reits/03-commodity-etfs-and-roll-costs.md) |
| \( \text{pip value (quote currency)} = \text{units} \times \text{pip size} \) | Forex pip value | [Forex basics](../17-commodities-forex-and-reits/04-forex-basics.md) |
| \( F = S \times \frac{1 + i_{quote}}{1 + i_{base}} \) | Forward rate from the two interest rates | [What moves currencies](../17-commodities-forex-and-reits/05-what-moves-currencies.md) |
| \( \text{leverage} = \frac{1}{\text{margin rate}} \) | Forex leverage | [Trading forex from Canada](../17-commodities-forex-and-reits/06-trading-forex-from-canada.md) |
| \( \text{FFO} = NI + D - G \) | Funds from operations: net income, depreciation, gains on property sales \(G\) | [REIT metrics: FFO and cap rates](../17-commodities-forex-and-reits/08-reit-metrics-ffo-and-cap-rates.md) |
| \( \text{cap rate} = \frac{NOI}{V} \) | Net operating income over property value | [REIT metrics: FFO and cap rates](../17-commodities-forex-and-reits/08-reit-metrics-ffo-and-cap-rates.md) |

## Crypto

| Formula | Symbols | Lesson |
|---|---|---|
| \( p = 2^{-k} \qquad \text{expected guesses} = 2^{k} \) | Mining: \(k\) leading zero bits | [What bitcoin is](../18-crypto/01-what-bitcoin-is.md) |
| \( \text{supply} = 210{,}000 \times (50 + 25 + 12.5 + \dots) \) | Bitcoin's supply from halvings | [What bitcoin is](../18-crypto/01-what-bitcoin-is.md) |
| \( \text{fee} = \text{gas used} \times (\text{base fee} + \text{tip}) \) | Ethereum transaction fee | [Ethereum, stablecoins and DeFi](../18-crypto/03-ethereum-stablecoins-and-defi.md) |
| \( x \times y = k \) | Constant product pool | [Ethereum, stablecoins and DeFi](../18-crypto/03-ethereum-stablecoins-and-defi.md) |
| \( \text{liquidation value} = \frac{\text{loan}}{\text{threshold}} \) | Collateral value at which a DeFi loan is sold | [Ethereum, stablecoins and DeFi](../18-crypto/03-ethereum-stablecoins-and-defi.md) |
| \( \text{round-trip cost} = 1 - (1 - f)(1 - f) \) | \(f\) is the cost of one trade, fee and spread together | [Buying crypto in Canada](../18-crypto/04-buying-crypto-in-canada.md) |
| \( V_n = V_0 \, (1 - m)^n \) | Fee drag of a fund over \(n\) years at fee \(m\) | [Crypto ETFs](../18-crypto/05-crypto-etfs.md) |
| \( \text{payment} = N \times r \) | Perpetual futures funding: notional \(N\) times funding rate \(r\) | [Crypto market structure](../18-crypto/06-crypto-market-structure.md) |
| \( P_{\text{liq}} = \frac{E \, (1 - 1/L)}{1 - m} \) | Liquidation price: entry \(E\), leverage \(L\), maintenance margin \(m\) | [Crypto market structure](../18-crypto/06-crypto-market-structure.md) |
| \( \text{MVRV} = \frac{\text{market cap}}{\text{realized cap}} \) | On-chain valuation ratio | [On-chain data and crypto cycles](../18-crypto/07-on-chain-data-and-cycles.md) |
| \( S = E - k \times ATR \qquad \text{units} = \left\lfloor \frac{f \times A}{E - S} \right\rfloor \) | Stop and size for a coin | [Crypto taxes and position sizing](../18-crypto/09-crypto-taxes-and-sizing.md) |

## Data, forecasting and quant

| Formula | Symbols | Lesson |
|---|---|---|
| \( \text{Days to cover} = \frac{S}{V} \qquad \text{Short percent of float} = \frac{S}{F} \) | \(S\) shares short, \(V\) average daily volume, \(F\) float | [Short interest and borrow](../19-data-flows-and-forecasting/04-short-interest-and-borrow.md) |
| \( N = L - S \qquad \text{Share of open interest} = \frac{N}{OI} \) | Net position from long and short contracts; \(OI\) is open interest | [The Commitments of Traders report](../19-data-flows-and-forecasting/05-commitments-of-traders.md) |
| \( B = \frac{1}{N} \sum_{i=1}^{N} (f_i - o_i)^2 \) | Brier score of forecasts \(f_i\) against outcomes \(o_i\) | [Base rates, calibration and forecast logs](../19-data-flows-and-forecasting/07-base-rates-calibration-and-forecast-logs.md) |
| \( \text{EV} = p - (A + c) \qquad p^{*} = A + c \) | Prediction market contract: your probability \(p\), ask price \(A\), cost \(c\) | [Prediction markets](../19-data-flows-and-forecasting/08-prediction-markets.md) |
| \( r_t = \frac{P_t}{P_{t-1}} - 1 \) | Simple return | [Returns and volatility in pandas](../20-quant-track-in-python/02-returns-and-volatility.md) |
| \( \ell_t = \ln\frac{P_t}{P_{t-1}} \) | Log return | [Returns and volatility in pandas](../20-quant-track-in-python/02-returns-and-volatility.md) |
| \( \sigma_{\text{annual}} = \sigma_{\text{daily}} \times \sqrt{252} \) | Annualized volatility | [Returns and volatility in pandas](../20-quant-track-in-python/02-returns-and-volatility.md) |
| \( \rho = \frac{\operatorname{Cov}(r_s, r_m)}{\sigma_s \, \sigma_m} \) | Correlation | [Correlation, beta and regression](../20-quant-track-in-python/06-correlation-beta-and-regression.md) |
| \( \beta = \frac{\operatorname{Cov}(r_s, r_m)}{\operatorname{Var}(r_m)}, \qquad r_s = \alpha + \beta\, r_m + \varepsilon \) | Beta and the market model | [Correlation, beta and regression](../20-quant-track-in-python/06-correlation-beta-and-regression.md) |
| \( t = \frac{\bar{s}}{\operatorname{sd}(s)/\sqrt{T}} \) | t-statistic of a factor spread series \(s\) over \(T\) periods | [Factor sorts](../20-quant-track-in-python/07-factor-sorts.md) |
| \( \text{CAGR} = E_n^{1/y} - 1 \) | \(E_n\) is the final equity as a multiple of the start, \(y\) the years | [Performance metrics](../20-quant-track-in-python/10-performance-metrics.md) |
| \( \text{Sharpe} = \frac{\bar{r} - r_f/252}{\sigma}\sqrt{252} \) | Annualized Sharpe ratio from daily returns | [Performance metrics](../20-quant-track-in-python/10-performance-metrics.md) |
| \( D_t = \frac{E_t}{\max_{s \le t} E_s} - 1, \qquad \text{MaxDD} = \min_t D_t \) | Drawdown and maximum drawdown | [Performance metrics](../20-quant-track-in-python/10-performance-metrics.md) |

The expected maximum Sharpe ratio and the deflated Sharpe ratio are in [Overfitting and out-of-sample testing](../20-quant-track-in-python/09-overfitting-and-out-of-sample.md), and the Sortino ratio is in [Performance metrics](../20-quant-track-in-python/10-performance-metrics.md). They need several symbols each, so read them there.
