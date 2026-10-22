"""Lab 14: Meridian portfolio baselines. Uses only Python's standard library."""
import math

# Course-authored annual training inputs, expressed as decimals, not percentages.
# Order throughout: bills, 10-year Treasury, IG bonds, global equity.
SLEEVES = [
    ("Treasury bills", 0.035, 0.005),
    ("Treasury 10-year note", 0.043, 0.070),
    ("Investment-grade bond fund", 0.050, 0.060),
    ("Global equity index fund", 0.080, 0.160),1
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



def search_portfolio(returns, covariance, objective, reserve_minimum, reserve_indices):
    """Try all long-only allocations in 5 percentage-point steps."""
    size = len(returns)
    if not 1 <= size <= 6:
        raise ValueError("Use one to six assets.")
    if not all(math.isfinite(x) for x in [*returns, objective, reserve_minimum]):
        raise ValueError("Returns and mandate inputs must be finite.")
    if not 0 <= reserve_minimum <= 1:
        raise ValueError("Reserve minimum must be between 0 and 100%.")
    if any(i < 0 or i >= size for i in reserve_indices):
        raise ValueError("Invalid reserve asset index.")
    if len(covariance) != size or any(len(row) != size for row in covariance):
        raise ValueError("Covariance dimensions must match the assets.")

    def allocations(slots, remaining):
        # Twenty units, each worth 5%, must be allocated across all assets.
        if slots == 1:
            yield [remaining / 20]
        else:
            for units in range(remaining + 1):
                for rest in allocations(slots - 1, remaining - units):
                    yield [units / 20] + rest

    best = None
    for weights in allocations(size, 20):
        result = expected_return(weights, returns)
        reserve = reserve_weight(weights, reserve_indices)
        if result < objective - 1e-12 or reserve < reserve_minimum - 1e-12:
            continue
        risk = portfolio_volatility(weights, covariance)
        if best is None or risk < best["volatility"]:
            best = {"weights": weights, "return": result,
                    "volatility": risk, "reserve": reserve}
    return best


def estimate_from_csv(source, last_36=False):
    """Read monthly adjusted prices; estimate annual moments from simple returns.

    source is a text file-like object. Last 36 means 36 monthly RETURNS,
    calculated from the last 37 prices. Sample standard deviations are used.
    """
    import csv
    import statistics
    from datetime import date

    rows = list(csv.reader(source))
    if not rows or len(rows[0]) < 4 or len(rows[0]) > 7:
        raise ValueError("CSV needs a date column and three to six ticker columns.")
    names = [name.strip() for name in rows[0][1:]]
    if any(not name for name in names) or len(set(names)) != len(names):
        raise ValueError("Ticker names must be nonempty and unique.")
    prices, dates = [], []
    previous_month = None
    for row in rows[1:]:
        if not row or not any(cell.strip() for cell in row):
            continue
        if len(row) != len(names) + 1:
            raise ValueError("Every row must have a date and a price for every ticker.")
        try:
            day = date.fromisoformat(row[0].strip())
            values = [float(value) for value in row[1:]]
        except ValueError as error:
            raise ValueError("Use YYYY-MM-DD dates and numeric adjusted prices.") from error
        month = day.year * 12 + day.month
        if previous_month is not None and month != previous_month + 1:
            raise ValueError("Use consecutive monthly rows, oldest first, with no duplicates.")
        if any(not math.isfinite(value) or value <= 0 for value in values):
            raise ValueError("Prices must be positive finite numbers, with no missing cells.")
        previous_month = month
        prices.append(values)
        dates.append(day.isoformat())
    if len(prices) < 3:
        raise ValueError("At least three monthly prices are needed.")
    monthly = [[current[i] / previous[i] - 1 for i in range(len(names))]
               for previous, current in zip(prices, prices[1:])]
    if last_36:
        if len(monthly) < 36:
            raise ValueError("The last-36-month view needs at least 37 monthly prices.")
        monthly = monthly[-36:]
    columns = list(zip(*monthly))
    returns = [statistics.mean(column) * 12 for column in columns]
    volatilities = [statistics.stdev(column) * math.sqrt(12) for column in columns]
    if any(vol <= 0 for vol in volatilities):
        raise ValueError("Every asset needs nonzero return variation to estimate correlations.")
    correlations = [[1.0 if i == j else max(-1.0, min(1.0,
                     statistics.correlation(columns[i], columns[j])))
                     for j in range(len(names))] for i in range(len(names))]
    return {"names": names, "returns": returns, "volatilities": volatilities,
            "covariance": build_covariance(volatilities, correlations),
            "months": len(monthly), "start": dates[-len(monthly)-1], "end": dates[-1]}


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
