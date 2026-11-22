"""Loads Northwind's model from tools/checks/09-company-financials.py (the part above the marker)."""
from pathlib import Path

_p = Path(__file__).resolve().parents[2] / "checks" / "09-company-financials.py"
ns: dict = {}
exec(_p.read_text(encoding="utf-8").split("# ==== LESSON CHECKS")[0], ns)
