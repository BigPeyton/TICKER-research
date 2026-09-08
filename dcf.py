"""Lab 05: five-year FCFF discounted cash flow model.

All monetary inputs are in USD millions, except the resulting value per share.
"""

# Editable inputs
STARTING_FCFF = 100.0
GROWTH_RATES = [0.08, 0.06, 0.05, 0.04, 0.03]
WACC = 0.10
TERMINAL_GROWTH = 0.03
NON_OPERATING_CASH = 50.0
DEBT = 300.0
DILUTED_SHARES = 50.0


def main() -> None:
    if TERMINAL_GROWTH >= WACC:
        print("Error: terminal growth must be less than WACC.")
        return

    if len(GROWTH_RATES) != 5:
        print("Error: provide exactly five yearly growth rates.")
        return

    fcff_values = []
    fcff = STARTING_FCFF
    for growth_rate in GROWTH_RATES:
        fcff *= 1 + growth_rate
        fcff_values.append(fcff)

    pv_explicit_fcff = sum(
        yearly_fcff / (1 + WACC) ** year
        for year, yearly_fcff in enumerate(fcff_values, start=1)
    )
    terminal_value_year_5 = fcff_values[-1] * (1 + TERMINAL_GROWTH) / (
        WACC - TERMINAL_GROWTH
    )
    pv_terminal_value = terminal_value_year_5 / (1 + WACC) ** 5
    enterprise_value = pv_explicit_fcff + pv_terminal_value
    equity_value = enterprise_value + NON_OPERATING_CASH - DEBT
    value_per_share = equity_value / DILUTED_SHARES
    pv_terminal_share = pv_terminal_value / enterprise_value

    for year, yearly_fcff in enumerate(fcff_values, start=1):
        print(f"FCFF Year {year}: {yearly_fcff:.4f}")
    print(f"Present value of explicit FCFF: {pv_explicit_fcff:.4f}")
    print(f"Terminal value at Year 5: {terminal_value_year_5:.4f}")
    print(f"Present value of terminal value: {pv_terminal_value:.4f}")
    print(f"Enterprise value: {enterprise_value:.4f}")
    print(f"Equity value: {equity_value:.4f}")
    print(f"Value per diluted share: {value_per_share:.4f}")
    print(
        "Present value of terminal value as a share of enterprise value: "
        f"{pv_terminal_share:.4f}"
    )


if __name__ == "__main__":
    main()
