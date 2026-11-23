# Data sources

The free data sources the book uses, with what each offers, what it asks of you and what you may do with the data. The rules come from [Free data sources and their licences](../19-data-flows-and-forecasting/01-free-data-sources.md) and the lessons named below. They are as of 2026, and each provider can change them, so read the provider's own terms.

Two questions apply to every source. What does the provider ask when you download (a key, a header, a speed limit)? And what may you do with the data afterwards? Using data in your own notebook is the low-risk case. Republishing means putting the data, or a chart that reproduces it, where other people can see it, and that is where licences apply. The book's own price charts use made-up data for this reason.

## US government sources

| Source | What it holds | Access | Reuse | Lessons |
|---|---|---|---|---|
| [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Filings (10-K, 10-Q, 8-K) and XBRL facts; the "companyfacts" endpoint returns all of a company's XBRL facts | No key. Declare a User-Agent with your real name and a working email. Maximum 10 requests per second, and the SEC can limit rates further ([Accessing EDGAR data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data)) | SEC filings are public documents | [Filings and EDGAR](../09-company-financials/01-filings-and-edgar.md), [Fundamentals from EDGAR](../20-quant-track-in-python/04-fundamentals-from-edgar.md) |
| [BLS](https://www.bls.gov/opub/copyright-information.htm) | Jobs, CPI, productivity | Cite the source | BLS says its published material is in the public domain, except previously copyrighted photographs and illustrations | [Inflation reports](../11-macro-and-economic-data/04-inflation-reports.md), [The jobs report](../11-macro-and-economic-data/05-the-jobs-report.md) |
| [BEA](https://www.bea.gov/help/faq/145) | GDP, PCE | The API needs a free registration (a UserID) | BEA says material on its site is public domain unless stated otherwise, and asks for a citation | [Growth data](../11-macro-and-economic-data/06-growth-data.md) |
| [Treasury Fiscal Data](https://fiscaldata.treasury.gov/about-us/) | Yields, debt, auctions | See the API documentation. The daily par yield curve file needs no key | Treasury says the data may be copied, adapted and redistributed for commercial and non-commercial use | [Macro data from FRED and Treasury](../20-quant-track-in-python/05-macro-data-from-fred-and-treasury.md) |
| [CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) | Commitments of Traders | Free downloads. The report is generally published on Friday at 3:30 p.m. ET, with data as of the prior Tuesday | Check the notice on the CFTC site before you republish | [The Commitments of Traders report](../19-data-flows-and-forecasting/05-commitments-of-traders.md) |

The COT covers CFTC-regulated US markets, so Canadian contracts such as the SXF are not in it. The CFTC announced on October 27, 2026 that it plans to publish twice a week, by the end of 2026, with no start date given. See the lesson for the details.

## FRED

FRED is a database run by the Federal Reserve Bank of St. Louis that collects thousands of series from government and private sources. You need your own free API key, and you should never paste someone else's or commit yours to a public repository. A missing observation arrives as the string ".", so tell pandas that "." means missing. FRED's terms say some series are copyrighted and marked in their notes, and the API does not override that copyright. For third-party data you must ask the data owner before using it beyond your own personal use. The S&P 500 series (SP500) is the example: S&P Dow Jones Indices owns the copyright and FRED carries 10 years of daily history, so a private plot is fine and a public copy of the series is not ([FRED terms of use](https://fred.stlouisfed.org/docs/api/terms_of_use.html), [SP500](https://fred.stlouisfed.org/series/SP500)). The API can return a series as it looked on a past date through its `realtime_start` and `realtime_end` parameters, which matters for tests that must not use revised numbers ([Macro data from FRED and Treasury](../20-quant-track-in-python/05-macro-data-from-fred-and-treasury.md)).

## Bank of Canada

The lessons use the Bank of Canada as a source of exchange rates and policy dates, not as a data feed. The CRA says to generally use the Bank of Canada rate for the transaction day, and the Bank publishes its daily average by 4:30 p.m. ET each business day ([Bank of Canada](https://www.bankofcanada.ca/rates/exchange/background-information-on-foreign-exchange-rates/), as of 2026). Decision dates and times are on its [upcoming events](https://www.bankofcanada.ca/press/upcoming-events/) page. The lessons do not cover the Bank's data API, so read its terms before you rely on one. See [Cost base in CAD and keeping records](../02-accounts-currency-and-taxes/08-cost-base-in-cad-and-records.md).

## Canadian sources

Canadian filings live on SEDAR+, and Canadian insider reports on SEDI. Statistics Canada publishes Canada's economic data under an [Open Licence](https://www.statcan.gc.ca/en/terms-conditions/open-licence) that lets you use, publish and distribute its information if you keep a source notice and do not imply that Statistics Canada endorses you (as of 2026). See [Insider trades and Form 4](../19-data-flows-and-forecasting/02-insider-trades-form-4.md) for SEDI.

## Yahoo Finance and yfinance

yfinance is an open-source Python package that downloads Yahoo Finance data. It is unofficial. Its [README](https://github.com/ranaroussi/yfinance) says it is not affiliated with Yahoo, that it is meant for research and educational use, and that the Yahoo API is intended for personal use only. It can break when Yahoo changes its pages. Use it to learn and to explore, and do not build anything you need to rely on, or publish, on it. See [Python and pandas for prices](../20-quant-track-in-python/01-python-and-pandas-for-prices.md).

## Which rule applies

| Who made the data | What to do |
|---|---|
| A US agency | Read the agency's terms. It is usually reusable with a citation |
| An index or exchange owner | Assume personal use only, and ask the owner before you republish |
| Yahoo, through yfinance | Assume personal use only |

## Polite downloading

The SEC's limit is 10 requests per second. A loop that waits 0.11 seconds between requests sends about 9.09 requests per second and stays under the limit. A loop with no wait can burst far above it, and the SEC may block your address. The lesson's snippet shows the header and the wait.
