"""FIN 43900 Lab 09 ABG model. USD millions except value per share.
Run python proforma.py; use --break-cash for the deliberate failure test.
Inputs are supplied training assumptions, not independently verified forecasts.
"""
import sys

GROWTH = 0.018
GROSS_MARGIN = 0.1705
SGA_RATIOS = [0.665, 0.655, 0.645, 0.645, 0.645]
DEPRECIATION_RATIO = 82.4 / 3070.4
INVENTORY_DAYS = 2135.8 / (17999.0 - 3071.7) * 365
FLOOR_PLAN_RATIO = 2027.0 / 2135.8
MINIMUM_CASH, REVOLVER_LIMIT = 25.0, 850.0
COST_OF_EQUITY, TERMINAL_GROWTH, SHARES = 0.10, 0.025, 17.951349
OPENING = dict(revenue=17999.0, inventory=2135.8, ppe=3070.4,
               other_assets=6371.6, cash=40.4, floor_plan=2027.0,
               debt=3572.0, other_liabilities=2127.5, equity=3891.7,
               revolver=0.0)


def balance_gap(r):
    return (r['cash'] + r['inventory'] + r['ppe'] + r['other_assets']
            - r['floor_plan'] - r['debt'] - r['revolver']
            - r['other_liabilities'] - r['equity'])


def assert_balanced(r):
    gap = balance_gap(r)
    problems = []
    if abs(gap) > 1e-6:
        problems.append('balance sheet does not balance')
    if r['cash'] < MINIMUM_CASH - 1e-6:
        problems.append('cash below minimum')
    if not -1e-6 <= r['revolver'] <= REVOLVER_LIMIT + 1e-6:
        problems.append('revolver outside permitted range')
    if problems:
        raise ValueError(f"FY{r['year']}E: gap {gap:.1f}; " + '; '.join(problems))


def project(break_cash=False):
    rows = []
    prior = OPENING.copy()
    for i, year in enumerate(range(2026, 2031)):
        r = dict(year=year)
        # Income statement. Interest uses opening financing balances.
        r['revenue'] = prior['revenue'] * (1 + GROWTH)
        r['gross_profit'] = r['revenue'] * GROSS_MARGIN
        r['cost_of_sales'] = r['revenue'] - r['gross_profit']
        r['sga'] = r['gross_profit'] * SGA_RATIOS[i]
        r['depreciation'] = prior['ppe'] * DEPRECIATION_RATIO
        r['impairment'] = 120.0
        r['operating_income'] = r['gross_profit'] - r['sga'] - r['depreciation'] - r['impairment']
        r['interest'] = prior['floor_plan'] * 0.0467 + prior['debt'] * 0.0544 + prior['revolver'] * 0.06
        r['pretax'] = r['operating_income'] - r['interest']
        r['tax'] = max(0, r['pretax']) * 0.255
        r['net_income'] = r['pretax'] - r['tax']
        # Balance sheet except cash.
        r['inventory'] = r['cost_of_sales'] * INVENTORY_DAYS / 365
        r['floor_plan'] = r['inventory'] * FLOOR_PLAN_RATIO
        r['capex'], r['repayment'], r['buyback'] = 250.0, 150.0, 150.0
        r['ppe'] = prior['ppe'] + r['capex'] - r['depreciation']
        r['change_other_wc'] = 0.008 * (r['revenue'] - prior['revenue'])
        r['other_assets'] = prior['other_assets'] + r['change_other_wc'] - r['impairment']
        r['debt'] = prior['debt'] - r['repayment']
        r['other_liabilities'] = prior['other_liabilities']
        r['equity'] = prior['equity'] + r['net_income'] - r['buyback']
        # Cash flow. Inventory and other working capital increases use cash.
        r['change_inventory'] = r['inventory'] - prior['inventory']
        r['change_floor_plan'] = r['floor_plan'] - prior['floor_plan']
        r['operating_cash_flow'] = (r['net_income'] + r['depreciation'] + r['impairment']
                                   - r['change_inventory'] - r['change_other_wc'] + r['change_floor_plan'])
        r['fcfe'] = r['operating_cash_flow'] - r['capex'] - r['repayment']
        cash_before_revolver = prior['cash'] + r['fcfe'] - r['buyback']
        if cash_before_revolver < MINIMUM_CASH:
            r['change_revolver'] = min(MINIMUM_CASH - cash_before_revolver, REVOLVER_LIMIT - prior['revolver'])
        else:
            r['change_revolver'] = -min(prior['revolver'], cash_before_revolver - MINIMUM_CASH)
        r['revolver'] = prior['revolver'] + r['change_revolver']
        r['opening_cash'] = prior['cash']
        r['cash'] = cash_before_revolver + r['change_revolver']
        r['change_cash'] = r['cash'] - prior['cash']
        if break_cash and year == 2026:
            r['cash'] = OPENING['cash']  # Deliberate lab error; normal run is unchanged.
        r['assets'] = r['cash'] + r['inventory'] + r['ppe'] + r['other_assets']
        r['liabilities_equity'] = r['floor_plan'] + r['debt'] + r['revolver'] + r['other_liabilities'] + r['equity']
        assert_balanced(r)
        rows.append(r)
        prior = r
    return rows


def print_table(title, rows, fields):
    print(f'\n{title} (USD millions)')
    print(f"{'Line':<30}" + ''.join(f"{'FY' + str(r['year']) + 'E':>13}" for r in rows))
    for label, key in fields:
        print(f'{label:<30}' + ''.join(f'{r[key]:>13,.1f}' for r in rows))


def valuation(rows):
    for r in rows:
        assert_balanced(r)
    if COST_OF_EQUITY <= TERMINAL_GROWTH:
        raise ValueError('Cost of equity must exceed terminal growth.')
    pv_fcfe = sum(r['fcfe'] / (1 + COST_OF_EQUITY) ** t for t, r in enumerate(rows, 1))
    terminal = (rows[-1]['fcfe'] + rows[-1]['repayment']) * (1 + TERMINAL_GROWTH) / (COST_OF_EQUITY - TERMINAL_GROWTH)
    pv_terminal = terminal / (1 + COST_OF_EQUITY) ** 5
    equity = pv_fcfe + pv_terminal
    return equity, pv_terminal / equity * 100, equity / SHARES


def main():
    rows = project('--break-cash' in sys.argv)
    print_table('INCOME STATEMENT', rows, [(k.replace('_', ' ').title(), k) for k in
        ['revenue', 'cost_of_sales', 'gross_profit', 'sga', 'depreciation', 'impairment',
         'operating_income', 'interest', 'pretax', 'tax', 'net_income']])
    print_table('BALANCE SHEET', rows, [(k.replace('_', ' ').title(), k) for k in
        ['cash', 'inventory', 'ppe', 'other_assets', 'assets', 'floor_plan', 'debt',
         'revolver', 'other_liabilities', 'equity', 'liabilities_equity']])
    print_table('CASH FLOW', rows, [
        ('Net income', 'net_income'), ('+ Depreciation', 'depreciation'), ('+ Impairment', 'impairment'),
        ('- Inventory increase', 'change_inventory'), ('- Other WC increase', 'change_other_wc'),
        ('+ Floor plan increase', 'change_floor_plan'), ('Operating cash flow', 'operating_cash_flow'),
        ('- Capex', 'capex'), ('- Debt repayment', 'repayment'), ('FCFE', 'fcfe'),
        ('- Buyback', 'buyback'), ('+ Net revolver borrowing', 'change_revolver'),
        ('Change in cash', 'change_cash'), ('Opening cash', 'opening_cash'), ('Ending cash', 'cash')])
    print('\nCHECKS')
    for r in rows:
        gap = balance_gap(r)
        gap = 0.0 if abs(gap) < 1e-6 else gap
        print(f"FY{r['year']}E: assets - liabilities - equity = {gap:.1f}; cash >= {MINIMUM_CASH:.1f}: PASS")
    equity, terminal_share, per_share = valuation(rows)
    print(f'\nEquity value (USD millions): ${equity:,.2f}')
    print(f'Share of value after 2030: {terminal_share:.2f}%')
    print(f'Value per share: ${per_share:.2f}')


if __name__ == '__main__':
    main()
