# Set up your tools

You need four things, and all of them have a free option: a charting platform, a paper-trading account, a spreadsheet for the trade journal, and (optionally) Python. Set them up once, before lesson 1. This should take about 30 minutes.

## A charting platform

You need a place to look at real charts while you work through the book. The book's own charts use made-up data, so a platform is for the practice tasks and for the charts you will look at on your own.

TradingView has a free plan called Basic. As of November 2026, its [pricing page](https://www.tradingview.com/pricing/) lists 1 chart per tab, 2 indicators per chart and 3 active price alerts for Basic. Those limits are enough for the first parts of the book. Plans and limits change, so check the page before you rely on them.

Any other platform works too, including the one inside your broker, as long as it draws candles, volume and moving averages.

## A paper-trading account

A paper account trades with pretend money at real prices. Parts 4, 7, 8, 14, 15 and 16 use it. You have two options, and you can use both.

- TradingView paper trading. TradingView's [help page](https://www.tradingview.com/support/solutions/43000516466-paper-trading-main-functionality/) says it is available to all users. Open Supercharts, click Trade, choose Paper Trading and click Connect. The page does not list plan limits, so check what your plan allows.
- Interactive Brokers (IBKR). IBKR's [paper trading account](https://www.interactivebrokers.com/campus/trading-lessons/request-paper-trading-account/) is tied to a live account: you request it in Client Portal under Settings, Account Configuration, Paper Trading Account. IBKR also offers a [free trial account](https://www.interactivebrokers.com/support/faq/content/open-free-trial-account-35803518) that does not need funding. IBKR's pages differ on whether the live account must be funded or only approved, so check the current requirements on those pages.

Wealthsimple has no paper-trading mode that we could find as of November 2026, so use one of the two above.

## A spreadsheet for the trade journal

The trade journal is a table with one row per trade. Use Excel or Google Sheets, whichever you already have. The journal lessons in part 4 give the columns. You only need basic formulas (sums, differences and averages).

## Python for the optional code boxes

Python is optional. Every In code box shows an idea that the lesson already explained in words, and you can skip any box. If you want to run them, you need Python 3, a virtual environment and two libraries.

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Make a folder for the book's code and open a terminal in it.
3. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    # Windows (Git Bash): source .venv/Scripts/activate
    # Windows (PowerShell): .venv\Scripts\Activate.ps1
    # macOS or Linux: source .venv/bin/activate
    ```

4. Install the libraries:

    ```bash
    python -m pip install pandas matplotlib
    ```

5. Check that it works:

    ```bash
    python -c "import pandas, matplotlib; print(pandas.__version__)"
    ```

When a lesson uses a sample data file, it says so and gives a download link the first time. Save the CSV file into your project folder, next to your script, and read it with `pd.read_csv("file-name.csv")`.

If virtual environments or `pip` are new to you, the CS book has a lesson on them: [Modules, packages, pip and venv](https://faiyaz-svg.github.io/CSFromTheGroundUp/03-programming-fundamentals/01-python-basics/08-modules-packages-pip-and-venv/).

Some later snippets download data from the internet (they start with the comment `# needs internet`). Part 19 explains which sources need what.
