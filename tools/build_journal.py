"""Build the trade journal downloads: docs/downloads/trade-journal.xlsx and .csv.

Run from the repo root:
    .venv/Scripts/python tools/build_journal.py

The Trades sheet has one row per trade. Risk, P/L and R are formulas. The Stats
sheet reads the Trades sheet with formulas. The two example rows are made up.
"""

from __future__ import annotations

import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "downloads"
LAST = 500  # formulas cover rows 2 to 500

HEADERS = [
    "Date", "Ticker", "Setup", "Direction", "Entry", "Stop", "Target", "Shares",
    "Risk (US$)", "Exit", "Fees (US$)", "P/L (US$)", "R", "Followed plan",
    "Emotion", "Notes", "Screenshot",
]

# Made-up example rows. Columns: date, ticker, setup, direction, entry, stop, target,
# shares, exit, fees, followed plan, emotion, notes, screenshot.
EXAMPLES = [
    ("2026-03-02", "Stock A", "Breakout", "Long", 50.00, 48.50, 54.50, 166, 53.00, 2.00,
     "Yes", "Calm", "Took the planned target area; no changes to the stop.", ""),
    ("2026-03-04", "Stock B", "Pullback", "Short", 30.00, 31.00, 27.00, 250, 31.00, 2.00,
     "Yes", "Annoyed", "Stopped out at the plan. Wanted to re-enter at once and did not.", ""),
]


# 20 made-up trades for lessons 5 and 7: (setup, R result, followed the plan).
TRADES = [
    ("Breakout", 2.1, True), ("Pullback", -1.0, True), ("Breakout", -1.0, True), ("Pullback", 1.6, True),
    ("Breakout", -1.0, True), ("Pullback", 2.4, True), ("Breakout", -1.8, False), ("Pullback", -1.0, True),
    ("Breakout", 0.9, False), ("Pullback", 1.8, True), ("Breakout", -1.0, True), ("Pullback", -1.0, True),
    ("Breakout", -2.2, False), ("Pullback", 2.0, True), ("Breakout", 3.1, True), ("Pullback", -1.0, True),
    ("Breakout", -1.0, True), ("Pullback", 1.5, True), ("Breakout", 0.6, False), ("Pullback", 2.2, True),
]


def risk(direction: str, entry: float, stop: float, shares: int) -> float:
    return abs(entry - stop) * shares


def pnl(direction: str, entry: float, exit_: float, shares: int, fees: float) -> float:
    sign = 1 if direction == "Long" else -1
    return (exit_ - entry) * shares * sign - fees


def r_multiple(direction, entry, stop, shares, exit_, fees) -> float:
    return pnl(direction, entry, exit_, shares, fees) / risk(direction, entry, stop, shares)


def example_values() -> list[dict]:
    out = []
    for d, tk, setup, dr, e, s, tg, sh, ex, fee, *_ in EXAMPLES:
        out.append({"risk": risk(dr, e, s, sh), "pnl": pnl(dr, e, ex, sh, fee), "r": r_multiple(dr, e, s, sh, ex, fee)})
    return out


def row_formulas(row: int) -> dict[str, str]:
    return {
        "I": f'=IF(OR(E{row}="",F{row}="",H{row}=""),"",ABS(E{row}-F{row})*H{row})',
        "L": f'=IF(OR(J{row}="",I{row}=""),"",(J{row}-E{row})*H{row}*IF(D{row}="Short",-1,1)-K{row})',
        "M": f'=IF(OR(L{row}="",I{row}="",I{row}=0),"",L{row}/I{row})',
    }


def build_xlsx(path: Path) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Trades"
    ws.append(HEADERS)
    head_fill = PatternFill("solid", fgColor="DDDDDD")
    for c in ws[1]:
        c.font = Font(bold=True)
        c.fill = head_fill
        c.alignment = Alignment(wrap_text=True, vertical="top")
    for i, ex in enumerate(EXAMPLES):
        row = i + 2
        d, tk, setup, dr, e, s, tg, sh, xt, fee, plan, emo, notes, shot = ex
        vals = {"A": d, "B": tk, "C": setup, "D": dr, "E": e, "F": s, "G": tg, "H": sh, "J": xt, "K": fee,
                "N": plan, "O": emo, "P": notes, "Q": shot}
        for col, v in vals.items():
            ws[f"{col}{row}"] = v
    for row in range(2, LAST + 1):
        for col, f in row_formulas(row).items():
            ws[f"{col}{row}"] = f
        ws[f"I{row}"].number_format = "#,##0.00"
        ws[f"L{row}"].number_format = "#,##0.00"
        ws[f"M{row}"].number_format = "0.00"
    widths = [12, 10, 14, 10, 9, 9, 9, 8, 11, 9, 10, 11, 8, 13, 14, 40, 20]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A2"
    dv_dir = DataValidation(type="list", formula1='"Long,Short"', allow_blank=True)
    dv_plan = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
    ws.add_data_validation(dv_dir)
    ws.add_data_validation(dv_plan)
    dv_dir.add(f"D2:D{LAST}")
    dv_plan.add(f"N2:N{LAST}")

    st = wb.create_sheet("Stats")
    R = f"Trades!$M$2:$M${LAST}"
    C = f"Trades!$C$2:$C${LAST}"
    N = f"Trades!$N$2:$N${LAST}"
    rows = [
        ("Closed trades", f"=COUNT({R})"),
        ("Winners", f'=COUNTIF({R},">0")'),
        ("Losers", f'=COUNTIF({R},"<0")'),
        ("Win rate", '=IF(B2=0,"",B3/B2)'),
        ("Average win (R)", f'=IFERROR(AVERAGEIF({R},">0"),"")'),
        ("Average loss (R)", f'=IFERROR(AVERAGEIF({R},"<0"),"")'),
        ("Expectancy (R per trade)", f'=IF(B2=0,"",AVERAGE({R}))'),
        ("Total R", f"=SUM({R})"),
        ("Total P/L (US$)", f"=SUM(Trades!$L$2:$L${LAST})"),
        ("Plan followed", f'=IF(B2=0,"",COUNTIF({N},"Yes")/B2)'),
    ]
    st["A1"], st["B1"] = "Measure", "Value"
    for i, (label, f) in enumerate(rows, 2):
        st[f"A{i}"] = label
        st[f"B{i}"] = f
    st["B5"].number_format = "0.0%"
    st["B11"].number_format = "0.0%"
    for cell in ("B6", "B7", "B8", "B9"):
        st[cell].number_format = "0.00"
    st["B10"].number_format = "#,##0.00"

    st["A14"], st["B14"], st["C14"], st["D14"], st["E14"] = "Setup", "Trades", "Win rate", "Average R", "Total R"
    setups = ["Breakout", "Pullback", "Reversal", "Other"]
    for i, name in enumerate(setups, 15):
        st[f"A{i}"] = name
        st[f"B{i}"] = f'=COUNTIFS({C},A{i},{R},">-1E+99")'
        st[f"C{i}"] = f'=IF(B{i}=0,"",COUNTIFS({C},A{i},{R},">0")/B{i})'
        st[f"D{i}"] = f'=IF(B{i}=0,"",AVERAGEIFS({R},{C},A{i}))'
        st[f"E{i}"] = f'=SUMIFS({R},{C},A{i})'
        st[f"C{i}"].number_format = "0.0%"
        st[f"D{i}"].number_format = "0.00"
        st[f"E{i}"].number_format = "0.00"
    st["A20"] = "Type your own setup names in column A, rows 15 to 18, and the table follows."
    for c in list(st[1]) + list(st[14]):
        c.font = Font(bold=True)
        c.fill = head_fill
    st.column_dimensions["A"].width = 28
    for col in "BCDE":
        st.column_dimensions[col].width = 12

    OUT.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def build_csv(path: Path) -> None:
    vals = example_values()
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HEADERS)
        for ex, v in zip(EXAMPLES, vals):
            d, tk, setup, dr, e, s, tg, sh, xt, fee, plan, emo, notes, shot = ex
            w.writerow([d, tk, setup, dr, f"{e:.2f}", f"{s:.2f}", f"{tg:.2f}", sh, f"{v['risk']:.2f}", f"{xt:.2f}",
                        f"{fee:.2f}", f"{v['pnl']:.2f}", f"{v['r']:.2f}", plan, emo, notes, shot])


def build_sample_trades(path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["trade", "setup", "r", "followed_plan"])
        for i, (setup, r, plan) in enumerate(TRADES, 1):
            w.writerow([i, setup, f"{r:.1f}", "yes" if plan else "no"])


if __name__ == "__main__":
    build_sample_trades(ROOT / "docs" / "assets" / "data" / "journal-20-trades.csv")
    build_xlsx(OUT / "trade-journal.xlsx")
    build_csv(OUT / "trade-journal.csv")
    print("wrote", OUT / "trade-journal.xlsx", "and", OUT / "trade-journal.csv")
