"""Independent arithmetic and archived-price reconciliation; no network calls.

Run: python tools/audit_model.py
Uses direct centered cross-products rather than the model's correlation helper.
These are AI-assisted development checks, not the student's locked experiment.
"""
import csv
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import model


def close(actual, expected, label, tolerance=1e-11):
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance):
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def audit():
    with (ROOT / 'data/prices.csv').open(newline='') as source:
        rows = list(csv.reader(source))
    names = rows[0][1:]
    dates = [r[0] for r in rows[1:]]
    prices = [[float(v) for v in r[1:]] for r in rows[1:]]
    reconciled = 0
    source_metadata = json.loads((ROOT / 'data/price-sources.json').read_text())
    for i, name in enumerate(names):
        raw = (ROOT / 'data/raw' / f'{name}_yahoo_raw.json').read_bytes()
        metadata = next(s for s in source_metadata if s['ticker'] == name)
        assert hashlib.sha256(raw).hexdigest() == metadata['sha256']
        daily = json.loads(raw)['chart']['result'][0]
        last_in_month = {}
        for stamp, price in zip(daily['timestamp'], daily['indicators']['adjclose'][0]['adjclose'], strict=True):
            if price is not None:
                day = datetime.fromtimestamp(stamp, timezone.utc).date().isoformat()
                # These US-market timestamps occur during the UTC trading day.
                last_in_month[day[:7]] = (day, price)
        for day, values in zip(dates, prices, strict=True):
            raw_day, raw_price = last_in_month[day[:7]]
            assert raw_day == day, (name, day, raw_day)
            close(values[i], raw_price, f'{name} {day}', tolerance=1e-8)
            reconciled += 1

    checks = []
    # Only the existing published stress suite is used; no new human experiment.
    for stress in model.stress_suite():
        settings = model.Settings(**stress['settings'])
        sample = prices[-37:] if settings.last_36 else prices
        monthly = [[b[i] / a[i] - 1 for i in range(4)] for a, b in zip(sample, sample[1:])]
        n = len(monthly)
        means = [sum(r[i] for r in monthly) / n for i in range(4)]
        cov = [[12 * sum((r[i] - means[i]) * (r[j] - means[j]) for r in monthly) / (n - 1)
                for j in range(4)] for i in range(4)]
        annual = [12 * x for x in means]
        annual[0] = min(annual[0], 0.0375)  # Independently checked Sep 16 FOMC target lower bound.
        annual[3] += settings.equity_change_pp / 100
        production = model.solve(settings)
        for p in production['portfolios']:
            w = [p['weights'][name] for name in names]
            gross = sum(w[i] * annual[i] for i in range(4))
            turnover = sum(abs(w[i] - [0.75, 0, 0, 0.25][i]) for i in range(4)) / 2
            cost = settings.annual_cost_bps / 10000 + settings.trading_cost_bps * turnover / 10000
            variance = sum(w[i] * cov[i][j] * w[j] for i in range(4) for j in range(4))
            close(p['net_return'], gross - cost, p['name'] + ' net')
            close(p['volatility'], math.sqrt(variance), p['name'] + ' risk')
        feasible = []
        for a in range(21):
            for b in range(21 - a):
                for c in range(21 - a - b):
                    w = [a / 20, b / 20, c / 20, (20 - a - b - c) / 20]
                    turnover = sum(abs(w[i] - [0.75, 0, 0, 0.25][i]) for i in range(4)) / 2
                    net = sum(w[i] * annual[i] for i in range(4)) - settings.annual_cost_bps / 10000 - settings.trading_cost_bps * turnover / 10000
                    variance = sum(w[i] * cov[i][j] * w[j] for i in range(4) for j in range(4))
                    if net >= settings.objective - 1e-12 and w[0] >= settings.reserve_minimum - 1e-12 and turnover <= settings.turnover_limit + 1e-12 and math.sqrt(variance) <= settings.volatility_limit + 1e-12:
                        feasible.append((variance, w))
        chosen = production['selected']
        if feasible:
            variance, w = min(feasible, key=lambda p: p[0])
            assert chosen is not None
            assert w == [chosen['weights'][name] for name in names]
            close(chosen['volatility'], math.sqrt(variance), 'minimum risk')
        else:
            assert chosen is None
        checks.append({'scenario': stress['scenario'], 'feasible_grid_allocations': len(feasible), 'independent_result_matches': True})
    return {'audited_at_utc': datetime.now(timezone.utc).isoformat(), 'archived_monthly_prices_reconciled': reconciled,
            'checks': checks, 'conclusion': 'Archived price reconstruction, arithmetic, and published grid-search scenarios agree.',
            'limits': ['Archive consistency is not fresh external source authentication.',
                       'The dated policy source is archived; its use as a return cap is not forecast validation.',
                       'No approved loss limit, actual holdings, or rolling five-year real-return compliance is established.',
                       'This is AI-assisted development validation, not an independent partner cold run or locked experiment.']}


if __name__ == '__main__':
    report = audit()
    (ROOT / 'outputs/audit-checks.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
