"""Loss on equity for a fall in asset value at different leverage (lessons 2 and 3). Made-up numbers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import numpy as np
from figstyle import save_pair, preview

LEV = [(1, "1 to 1", "muted"), (10, "10 to 1", "blue"), (28, "28 to 1", "accent"), (40, "40 to 1", "down")]


def draw(fig, ax, c):
    x = np.linspace(0, 6, 241)
    for lev, label, col in LEV:
        ax.plot(x, np.minimum(100, lev * x), color=c[col], linewidth=2, label=label)
        if lev > 10:
            ax.plot([100 / lev], [100], "o", color=c[col], markersize=5)
            ax.text(100 / lev + 0.08, 102, f"{100 / lev:.1f}%", color=c[col], fontsize=9)
    ax.set_xlabel("Fall in the value of the assets (%)")
    ax.set_ylabel("Loss of equity (% of equity)")
    ax.set_ylim(0, 110)
    ax.set_xlim(0, 6)
    ax.legend(loc="lower left", bbox_to_anchor=(0.66, 0.1), fontsize=9, title="Assets to equity", title_fontsize=9)


if __name__ == "__main__":
    for p in save_pair(draw, "21-crashes-scams-and-case-studies", "ltcm-leverage", width=6.0, height=3.6):
        preview(p)
