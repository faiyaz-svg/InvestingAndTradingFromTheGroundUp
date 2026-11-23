"""Made-up VIX futures curves in contango and in backwardation (lesson 2)."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from figstyle import save_pair, preview
import vol_data


def draw(fig, ax, c):
    for a, d, title, col in ((ax[0], vol_data.CONTANGO, "Contango (calm market)", c["accent"]),
                             (ax[1], vol_data.BACKWARDATION, "Backwardation (stress)", c["down"])):
        xs = list(range(0, len(d["futures"]) + 1))
        ys = [d["spot"]] + d["futures"]
        a.plot(xs, ys, "o-", color=col)
        a.plot([0], [d["spot"]], "s", color=c["fg"])
        a.annotate("VIX now", (0, d["spot"]), (0.3, d["spot"] - (2.2 if ys[1] > ys[0] else -1.0)), color=c["fg"], fontsize=9)
        a.set_title(title, fontsize=11, color=c["fg"])
        a.set_xlabel("Months to futures expiry")
        a.set_xticks(xs)
    ax[0].set_ylabel("Level (volatility points)")
    ax[0].set_ylim(10, 36)
    ax[1].set_ylim(10, 36)
    fig.tight_layout()


if __name__ == "__main__":
    for q in save_pair(draw, "16-volatility-and-event-trading", "vix-term-structure", width=7.0, height=3.4, axes=2):
        preview(q)
