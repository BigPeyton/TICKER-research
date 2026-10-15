"""Lab 13: Meridian Foundation mandate checker; standard library only."""
import argparse
import math

# Editable inputs: weights in percent, money in USD millions.
# Holding: (issuer, business days to redeem, reserve-eligible)
HOLDINGS = {
    "Cash": ("none", 0, True),
    "Treasury bills": ("U.S. Treasury", 1, True),
    "Treasury 10-year note": ("U.S. Treasury", 1, True),
    "Global equity index fund": ("diversified fund", 2, False),
    "Investment-grade bond fund": ("diversified fund", 3, False),
    "Private real estate fund": ("diversified fund", 90, False),
    "Acme Corp bonds": ("Acme Corp", 4, False),
    "Acme Corp stock": ("Acme Corp", 1, False),
}
# Each list follows the holdings order above.
CANDIDATES = {
    "A": dict(zip(HOLDINGS, [2, 2, 10, 60, 26, 0, 0, 0])),
    "B": dict(zip(HOLDINGS, [1, 0, 0, 55, 20, 15, 5, 4])),
    "C": dict(zip(HOLDINGS, [1, 1, 0, 70, 20, 0, 0, 8])),
    "D": dict(zip(HOLDINGS, [100, 0, 0, 0, 0, 0, 0, 0])),
}
RESERVE_SIZE = 100
QUARTERLY_DISTRIBUTION = 0.75
QUARTERS_TO_COVER = 4
LIQUIDITY_WINDOW = 5
MINIMUM_LIQUID_SHARE = 90
ISSUER_LIMIT = 8
EXEMPT_ISSUERS = {"none", "U.S. Treasury", "diversified fund"}


def check_portfolio(weights):
    if set(weights) != set(HOLDINGS):
        raise ValueError("Provide a weight for every listed holding and no others.")
    if not all(math.isfinite(value) for value in weights.values()):
        raise ValueError("Weights must be finite numbers.")
    minimum = QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE * 100
    total = sum(weights.values())
    lowest = min(weights.values())
    reserve = sum(weights[name] for name, info in HOLDINGS.items() if info[2])
    liquid = sum(weights[name] for name, info in HOLDINGS.items()
                 if info[1] <= LIQUIDITY_WINDOW)
    companies = {}
    for name, info in HOLDINGS.items():
        issuer = info[0]
        if issuer not in EXEMPT_ISSUERS:
            companies[issuer] = companies.get(issuer, 0) + weights[name]
    largest = max(companies.values(), default=0)
    return [
        ("Weights sum to 100", total, math.isclose(total, 100, rel_tol=0, abs_tol=1e-9)),
        ("Long-only (lowest weight)", lowest, lowest >= 0),
        (f"Reserve >= {minimum:.1f}%", reserve, reserve >= minimum),
        (f"Redeemable in {LIQUIDITY_WINDOW} days >= {MINIMUM_LIQUID_SHARE:.1f}%",
         liquid, liquid >= MINIMUM_LIQUID_SHARE),
        (f"Largest single company <= {ISSUER_LIMIT:.1f}%", largest, largest <= ISSUER_LIMIT),
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true", help="Temporarily test negative cash in A")
    args = parser.parse_args()
    minimum = QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE * 100
    print(f"Reserve minimum: {minimum:.1f}%")
    for name, original in CANDIDATES.items():
        weights = original.copy()
        if args.probe and name == "A":
            weights["Cash"] = -2
            weights["Global equity index fund"] = 64
        print(f"\nCandidate {name}")
        failures = 0
        for label, value, passed in check_portfolio(weights):
            print(f"{label}: {value:.1f} {'pass' if passed else 'FAIL'}")
            failures += not passed
        print("Calendar-year loss: requires CIO clarification")
        print("passes every checkable rule" if failures == 0 else f"fails {failures} rule(s)")


if __name__ == "__main__":
    main()
