"""Loads the model from tools/checks/13-etfs-portfolios-and-factors.py (the part above the marker)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from figstyle import save_pair, preview  # noqa: E402,F401

_p = Path(__file__).resolve().parents[2] / "checks" / "13-etfs-portfolios-and-factors.py"
ns: dict = {"__file__": str(_p)}
exec(_p.read_text(encoding="utf-8").rsplit("# ==== LESSON CHECKS", 1)[0], ns)
