import csv
from dataclasses import replace
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import model
from portfolio import (CORRELATIONS, SLEEVES, build_covariance, estimate_from_csv,
                       expected_return, portfolio_volatility)


class PortfolioTests(unittest.TestCase):
    def test_prior_course_known_answers(self):
        returns = [r for _, r, _ in SLEEVES]
        cov = build_covariance([v for _, _, v in SLEEVES], CORRELATIONS)
        weights = [0, 0, 0.4, 0.6]
        self.assertAlmostEqual(expected_return(weights, returns), 0.068)
        self.assertAlmostEqual(portfolio_volatility(weights, cov), 0.10461357464497618)

    def test_independent_two_asset_variance(self):
        cov = [[0.04, 0.012], [0.012, 0.09]]
        variance = 0.25**2 * 0.04 + 0.75**2 * 0.09 + 2 * 0.25 * 0.75 * 0.012
        self.assertAlmostEqual(portfolio_volatility([0.25, 0.75], cov)**2, variance)
        with self.assertRaises(ValueError):
            expected_return([0.25], [0.08, 0.02])

    def test_grid_is_exhaustive_for_four_sleeves(self):
        grid = list(model.allocations())
        self.assertEqual(len(grid), 1771)  # combinations with replacement: C(23,3)
        self.assertEqual(len(set(grid)), 1771)
        for weights in grid:
            model.checked_weights(weights)

    def test_original_lab15_result_is_reproduced(self):
        with (model.ROOT / 'data/prices.csv').open() as f:
            estimates = estimate_from_csv(f)
        self.assertEqual(estimates['months'], 60)
        self.assertAlmostEqual(expected_return(model.REFERENCE, estimates['returns']), 0.0582, places=4)
        self.assertAlmostEqual(portfolio_volatility(model.REFERENCE, estimates['covariance']), 0.0381, places=4)

    def test_window_uses_36_returns_and_signal_cap(self):
        inputs = model.estimates(model.Settings(last_36=True))
        self.assertEqual(inputs['months'], 36)
        self.assertEqual(inputs['start'], '2023-09-29')
        self.assertEqual(inputs['returns'][0], 0.0363)
        self.assertGreater(inputs['historical_returns'][0], inputs['returns'][0])

    def test_asset_order_rejected(self):
        inputs = model.estimates(model.Settings())
        inputs['names'] = ['ACWI', 'SCHR', 'VTC', 'SGOV']
        with patch('model.estimate_from_csv', return_value=inputs):
            with self.assertRaisesRegex(ValueError, 'order'):
                model.estimates(model.Settings())

    def test_no_missing_month_or_nonfinite_price(self):
        for text in [
            'Date,A,B,C\n2026-01-31,1,2,3\n2026-03-31,2,3,4\n2026-04-30,3,4,5\n',
            'Date,A,B,C\n2026-01-31,1,2,3\n2026-02-28,nan,3,4\n2026-03-31,3,4,5\n',
        ]:
            with self.assertRaises(ValueError):
                estimate_from_csv(io.StringIO(text))

    def test_signal_rejects_later_vintage_and_invalid_units(self):
        base = model.signal_record()
        for key, value in [('vintage_date', '2026-10-29'), ('units', 'monthly return'), ('value', float('nan'))]:
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'signal.json'
                path.write_text(json.dumps({**base, key: value}))
                with self.assertRaises(ValueError):
                    model.signal_record(path)

    def test_turnover_and_cost_units(self):
        inputs = model.estimates(model.Settings())
        base = model.evaluate('probe', (0.65, 0, 0, 0.35), inputs, model.Settings())
        self.assertAlmostEqual(base['turnover'], 0.1)
        self.assertAlmostEqual(base['cost_drag'], 0.0025 + 0.1 * 0.001)
        higher = model.evaluate('probe', (0.65, 0, 0, 0.35), inputs, model.Settings(annual_cost_bps=100))
        self.assertAlmostEqual(base['net_return'] - higher['net_return'], 0.0075)

    def test_default_rules_and_full_mandate_are_distinct(self):
        result = model.solve()
        self.assertEqual(result['selected']['weights'], dict(zip(model.NAMES, model.REFERENCE)))
        self.assertEqual(result['selected']['modeled_verdict'], 'PASS')
        self.assertTrue(result['selected']['full_mandate_verdict'].startswith('FAIL'))
        self.assertEqual([x['modeled_verdict'] for x in result['portfolios'][:3]], ['FAIL'] * 3)

    def test_boundaries_and_infeasibility(self):
        base = model.Settings()
        inputs = model.estimates(base)
        initial = model.evaluate('probe', model.REFERENCE, inputs, base)
        exact = replace(base, objective=initial['net_return'], reserve_minimum=0.75, turnover_limit=0)
        self.assertEqual(model.evaluate('probe', model.REFERENCE, inputs, exact)['modeled_verdict'], 'PASS')
        self.assertIsNone(model.solve(replace(base, reserve_minimum=0.8))['selected'])
        for settings in [replace(base, annual_cost_bps=-1), replace(base, objective=float('nan'))]:
            with self.assertRaises(ValueError):
                model.solve(settings)

    def test_stresses_separate_original_and_reoptimized(self):
        rows = model.stress_suite()
        self.assertEqual(rows[1]['fixed_base_weights']['modeled_verdict'], 'FAIL')
        self.assertEqual(rows[1]['reoptimized']['modeled_verdict'], 'PASS')
        self.assertIsNone(rows[-1]['reoptimized'])

    def test_archived_raw_source_hashes(self):
        sources = json.loads((model.ROOT / 'data/price-sources.json').read_text())
        for source in sources:
            raw = model.ROOT / 'data/raw' / (source['ticker'] + '_yahoo_raw.json')
            self.assertEqual(hashlib.sha256(raw.read_bytes()).hexdigest(), source['sha256'])


if __name__ == '__main__':
    unittest.main()
