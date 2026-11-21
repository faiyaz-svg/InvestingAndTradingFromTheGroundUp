# Paper trading

Paper trading means placing trades with fake money at real prices. This page says what it can and cannot do, how to set it up, how to keep it realistic, which paper blocks the book sets, and when to go live. [Setting up paper trading](../04-psychology-journal-and-paper-trading/06-paper-trading-setup.md) and [From paper to live trading](../04-psychology-journal-and-paper-trading/07-from-paper-to-live.md) cover the reasoning.

## Why paper trade, and the limits

Paper trading lets you practise your plan, checklist and journal at no cost. It shows whether you can follow your rules. It does not show whether a plan makes money, because a few dozen trades is too few. It also hides some costs:

- Fills are kinder than live ones. IBKR says its simulated fills come from the top of the book, with no deep book access, and that stop and complex orders are always simulated ([IBKR, about paper trading accounts](https://www.ibkrguides.com/clientportal/aboutpapertradingaccounts.htm), as of 2026).
- No order of yours competes with others, so a limit order that touches a price can fill when a live order would not.
- Losses do not hurt, so the biases of [lesson 1](../04-psychology-journal-and-paper-trading/01-biases-that-cost-traders.md) are weaker.
- Slippage, fees, currency conversion and tax do not appear unless you add them.

## Setup options

| Option | How | Note |
|---|---|---|
| IBKR paper account | Client Portal, Settings, Account Configuration, Paper Trading Account. Starts with US$1,000,000 of simulated equity ([IBKR Campus](https://www.interactivebrokers.com/campus/glossary-terms/paper-trading-account/), as of 2026). | Real-time data can be shared from your live account, so it depends on your subscriptions ([IBKR](https://www.ibkrguides.com/clientportal/papertradingaccount.htm)). |
| TradingView paper trading | Supercharts, Trade, Paper Trading, Connect. TradingView says it is available to all users and uses simulated money ([TradingView help](https://www.tradingview.com/support/solutions/43000516466-paper-trading-main-functionality/), as of 2026). | Check which features your plan includes. |
| Wealthsimple | Its public pages did not list a paper trading mode when this was checked in 2026. Check the app and help centre. | Do not assume it has one. |
| The journal alone | Write each trade with entry, stop and target, and fill it from a chart. | Works for swing trades. Too slow for day trading. |

## Rules to make paper realistic

1. Size from your real account, not the paper balance.
2. Add fees from your real broker's schedule to every trade.
3. Add slippage to each fill: move the price against you by a set amount per share.
4. Count a limit order as filled only if the price trades through it.
5. Run one setup at a time.
6. Journal every trade, both stages, before you click ([trade journal](trade-journal.md)).
7. Keep your daily loss limit and your cooling-off rule.

## The paper blocks

The book sets six paper blocks. Each is a fixed number of trades of one kind, with a purpose, done after the part named. Each block uses the same rules above.

| Block | After | Trades | Purpose |
|---|---|---|---|
| 1 | [From paper to live trading](../04-psychology-journal-and-paper-trading/07-from-paper-to-live.md) (part 4) | 20, any setups in your plan | Follow your plan and checklist and journal every trade. The goal is 90% plan-following, not profit. |
| 2 | A weekly swing routine<!-- link: ../07-swing-trading/09-weekly-swing-routine.md --> (part 7) | 20 swing trades, one setup | Run the weekly routine and collect a by-setup record. |
| 3 | A day trading routine and limits<!-- link: ../08-day-trading/09-day-trading-routine-and-limits.md --> (part 8) | 20 day trades, one setup | Add costs and slippage, and keep the daily loss limit. |
| 4 | Futures in Canada<!-- link: ../14-futures/07-futures-in-canada.md --> (part 14) | 10 micro futures trades | Check tick value, margin and sizing before real contracts. |
| 5 | Options in Canadian accounts<!-- link: ../15-options/15-options-in-canadian-accounts.md --> (part 15) | 10 defined-risk option trades | Size by maximum loss and follow each trade to exit or expiry. |
| 6 | Opex, gamma and index rebalances<!-- link: ../16-volatility-and-event-trading/06-opex-gamma-and-index-rebalances.md --> (part 16) | 10 event trades | Plan the event, the size and the exit before it happens. |

The trade counts are the book's own example numbers, not tested standards. Block 1 is a first step: the go-live criteria below ask for 30 trades of one setup, so keep going past 20 if you are not there yet. Change them in your plan if you have a reason, and write the reason down.

## Criteria for going live with small size

These six are the book's own rules of thumb, not tested standards. Write your own version of them before you start a block, and check them at the end.

1. At least 30 paper trades of the one setup you will trade live.
2. You followed the plan on at least 90% of them.
3. Every trade is in the journal in both stages, with realism rules applied.
4. No loss is worse than 1.2R.
5. The largest drawdown in R stayed inside the limit in your plan.
6. The live account holds only money you can afford to lose.

When all six pass, start at 0.25% risk per trade for 20 trades, then 0.5% for 20 trades, then the plan's 1%, moving up only while the criteria still hold on live trades. If you fall below, return to paper. A positive paper result is welcome, but it is not a criterion.
