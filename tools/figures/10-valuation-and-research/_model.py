"""Loads the valuation model from tools/checks/10-valuation-and-research.py (the part above the marker).

Also puts tools/figures on the path, so a script can say: from _model import ns, save_pair, preview
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview  # noqa: E402,F401

_p = Path(__file__).resolve().parents[2] / "checks" / "10-valuation-and-research.py"
ns: dict = {"__file__": str(_p)}
exec(_p.read_text(encoding="utf-8").rsplit("# ==== LESSON CHECKS", 1)[0], ns)
