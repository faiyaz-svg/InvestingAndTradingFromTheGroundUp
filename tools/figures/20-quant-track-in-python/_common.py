"""Shared loaders for the part 20 figures. Data is the made-up sample data in docs/assets/data/."""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
DATA = Path(__file__).resolve().parents[3] / "docs" / "assets" / "data"
FOLDER = "20-quant-track-in-python"


def load(name, col="close"):
    df = pd.read_csv(DATA / f"{name}.csv", parse_dates=["date"], index_col="date")
    return df[col] if col else df


def fmt_dates(ax):
    import matplotlib.dates as mdates

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
