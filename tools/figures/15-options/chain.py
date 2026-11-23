"""Stock A's made-up options chain used in lessons 3 to 8 of part 15.

Stock A last traded at US$50.20. One expiry, T = 0.25 years away, risk-free rate 4%, no dividends.
Rows: strike, bid, ask, last, volume, open interest.
"""
from bs import implied_vol, greeks

S = 50.20
T = 0.25
R = 0.04

CALLS = [
    (45.0, 6.90, 7.00, 6.95, 120, 1840),
    (47.5, 4.95, 5.10, 5.00, 310, 2210),
    (50.0, 3.35, 3.45, 3.40, 1850, 6420),
    (52.5, 2.10, 2.20, 2.15, 940, 3980),
    (55.0, 1.30, 1.35, 1.30, 610, 5120),
]
PUTS = [
    (45.0, 1.25, 1.35, 1.30, 260, 3120),
    (47.5, 1.80, 1.90, 1.85, 780, 4050),
    (50.0, 2.65, 2.75, 2.70, 1210, 5210),
    (52.5, 3.85, 4.00, 3.95, 430, 2060),
    (55.0, 5.50, 5.65, 5.60, 150, 1480),
]


def rows(kind):
    out = []
    for K, bid, ask, last, vol, oi in CALLS if kind == "call" else PUTS:
        mid = (bid + ask) / 2
        iv = implied_vol(mid, S, K, T, R, kind=kind)
        d = greeks(S, K, T, R, iv, kind=kind)["delta"]
        out.append(dict(K=K, bid=bid, ask=ask, last=last, vol=vol, oi=oi, mid=mid, iv=iv, delta=d))
    return out


if __name__ == "__main__":
    for kind in ("call", "put"):
        print(kind)
        for r in rows(kind):
            print(f"| {r['K']:.2f} | {r['bid']:.2f} | {r['ask']:.2f} | {r['last']:.2f} | {r['vol']:,} | {r['oi']:,} | {r['iv']*100:.1f}% | {r['delta']:.2f} | mid {r['mid']:.3f}")
