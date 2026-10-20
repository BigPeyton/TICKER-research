"""Lab 14: Meridian portfolio baselines. Uses only Python's standard library."""
import math

# Course-authored annual training inputs, expressed as decimals, not percentages.
# Order throughout: bills, 10-year Treasury, IG bonds, global equity.
SLEEVES = [
    ("Treasury bills", 0.035, 0.005),
    ("Treasury 10-year note", 0.043, 0.070),
    ("Investment-grade bond fund", 0.050, 0.060),
    ("Global equity index fund", 0.080, 0.160),
]
CORRELATIONS = [
    [1.00, 0.10, 0.05, 0.00],
    [0.10, 1.00, 0.80, -0.10],
    [0.05, 0.80, 1.00, 0.25],
    [0.00, -0.10, 0.25, 1.00],
]
OBJECTIVE_RETURN = 0.065  # Estimated CPI of 2.5% plus 4%.
RESERVE_INDICES = (0, 1)


def build_covariance(volatilities, correlations):
    """Check the correlation table, then convert it to covariances."""
    size = len(volatilities)
    if len(correlations) != size or any(len(row) != size for row in correlations):
        raise ValueError("Correlation table must have one row and column per sleeve.")
    if any(not math.isfinite(vol) or vol <= 0 for vol in volatilities):
        raise ValueError("Volatilities must be finite and positive.")
    for i in range(size):
        for j in range(size):
            value = correlations[i][j]
            if not math.isfinite(value) or not -1 <= value <= 1:
                raise ValueError("Every correlation must be between -1 and 1.")
            if not math.isclose(value, correlations[j][i], rel_tol=0, abs_tol=1e-12):
                raise ValueError("Correlation table must be symmetric.")
        if correlations[i][i] != 1:
            raise ValueError("Each sleeve's correlation with itself must be 1.")
    return [
        [correlations[i][j] * volatilities[i] * volatilities[j]
         for j in range(size)]
        for i in range(size)
    ]


def equal_weights(size):
    """Give every sleeve the same share."""
    return [1 / size] * size


def inverse_volatility_weights(volatilities):
    """Give lower-volatility sleeves more weight, then scale to a total of 1."""
    if any(not math.isfinite(vol) or vol <= 0 for vol in volatilities):
        raise ValueError("Inverse-volatility weights require positive finite volatilities.")
    inverse = [1 / vol for vol in volatilities]
    total = sum(inverse)
    return [value / total for value in inverse]


def expected_return(weights, returns):
    """Add each sleeve's weight times its expected return."""
    return sum(weight * value for weight, value in zip(weights, returns, strict=True))


def portfolio_volatility(weights, covariance):
    """Include every pair of sleeves, then take the square root of variance."""
    variance = sum(
        weights[i] * weights[j] * covariance[i][j]
        for i in range(len(weights))
        for j in range(len(weights))
    )
    if variance < -1e-12:
        raise ValueError("Negative portfolio variance; check the covariance inputs.")
    return math.sqrt(max(variance, 0))


def reserve_weight(weights, indices=RESERVE_INDICES):
    """Add the bills and 10-year Treasury weights."""
    return sum(weights[index] for index in indices)


def meets_objective(portfolio_return, objective=OBJECTIVE_RETURN):
    return portfolio_return >= objective


def main():
    returns = [sleeve[1] for sleeve in SLEEVES]
    volatilities = [sleeve[2] for sleeve in SLEEVES]
    covariance = build_covariance(volatilities, CORRELATIONS)
    portfolios = {
        "Benchmark": [0, 0, 0.4, 0.6],
        "Equal weight": equal_weights(len(SLEEVES)),
        "Inverse volatility": inverse_volatility_weights(volatilities),
    }
    print("Course training inputs; these are not market estimates.")
    print("Weight order: bills / 10-year / IG bonds / equity")
    for name, weights in portfolios.items():
        result = expected_return(weights, returns)
        print(f"\n{name}")
        print("Weights (%): " + " / ".join(f"{weight * 100:.1f}" for weight in weights))
        print(f"Expected return: {result * 100:.2f}%")
        print(f"Volatility: {portfolio_volatility(weights, covariance) * 100:.2f}%")
        print(f"Reserve-eligible: {reserve_weight(weights) * 100:.1f}%")
        print(f"Meets {OBJECTIVE_RETURN * 100:.1f}% objective: "
              f"{'yes' if meets_objective(result) else 'no'}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"Cannot calculate portfolios: {error}")
