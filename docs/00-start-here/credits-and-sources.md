# Credits and sources

## Software and fonts

The interactive price charts are drawn with TradingView Lightweight Charts. This is the notice that ships with the copy used here:

> TradingView Lightweight Charts v5.2.1. Copyright (c) 2026 TradingView, Inc. Licensed under the Apache License 2.0. Downloaded from npm (lightweight-charts@5.2.1), unchanged.

Lightweight Charts is a product of [TradingView](https://www.tradingview.com/). TradingView does not endorse this book.

The other tools behind the book:

| Tool | Used for |
|---|---|
| [IBM Plex](https://github.com/IBM/plex) | The fonts, under the SIL Open Font License |
| [Zensical](https://zensical.org/) | Building the website from the Markdown files |
| [KaTeX](https://katex.org/) | Formulas |
| [Mermaid](https://mermaid.js.org/) | Flow diagrams |
| [matplotlib](https://matplotlib.org/) and [mplfinance](https://github.com/matplotlib/mplfinance) | Static figures and chart previews |
| [pandas](https://pandas.pydata.org/) | The In code boxes and the sample data |

## Data

All price charts use made-up data. The script `tools/make_charts.py` generates it, so no real stock or index price history is reproduced.

Real numbers quoted in text or drawn in figures come from these sources, with the source and date given where they appear:

- [SEC EDGAR](https://www.sec.gov/edgar): company filings
- [BLS](https://www.bls.gov/): jobs and inflation data
- [BEA](https://www.bea.gov/): national accounts and GDP
- [US Treasury](https://home.treasury.gov/): yields and auctions
- [CFTC](https://www.cftc.gov/): Commitments of Traders reports

These are US government sources whose data is in the public domain, with the exceptions each agency states on its own site.

[FRED](https://fred.stlouisfed.org/), run by the Federal Reserve Bank of St. Louis, republishes many series. Some of them belong to third parties and carry their own copyright. Read the [FRED legal page](https://fred.stlouisfed.org/legal/) and each series' notes before you reuse a series. The book quotes only the numbers it needs, with a source.

## The other books

- [Math From the Ground Up](https://faiyaz-svg.github.io/MathFromTheGroundUp/): arithmetic to university math, proofs and finance math.
- [CS From the Ground Up](https://faiyaz-svg.github.io/CSFromTheGroundUp/): programming and computer science from the basics.
- [Music From the Ground Up](https://faiyaz-svg.github.io/MusicFromTheGroundUp/): piano and guitar for beginners.
- [French From the Ground Up](https://faiyaz-svg.github.io/FrenchFromTheGroundUp/): French from zero to B2.
