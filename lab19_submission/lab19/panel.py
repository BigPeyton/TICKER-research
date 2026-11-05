"""Shared SEC facts and Lab 19 checks. Memo judgments are written separately by AI."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('base_buffett', ROOT / 'buffett-investing/scripts/buffett.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
EXTRA = {'liabilities': 'Liabilities', 'current_assets': 'AssetsCurrent', 'current_liabilities': 'LiabilitiesCurrent'}
LABELS = {**b.LABELS, 'liabilities': 'Liabilities', 'current_assets': 'Current assets',
          'current_liabilities': 'Current liabilities', 'current_ratio': 'Current ratio', 'liabilities_equity': 'Liabilities / equity',
          'research': 'Research and development', 'research_intensity': 'R&D / revenue'}

def research_fact(company, end):
    candidates = [f for f in b.facts_for(company, 'ResearchAndDevelopmentExpense') if f.get('end') == end and b.annual(f)]
    if not candidates:
        return {'value': None, 'tag': 'not found', 'searched_tags': ['ResearchAndDevelopmentExpense'], 'end': end, 'unit': 'USD'}
    f = max(candidates, key=lambda f: (f.get('filed',''), f.get('accn',''), f.get('start','')))
    return {'value': f['val'], 'tag': 'us-gaap:ResearchAndDevelopmentExpense', 'start': f.get('start'), 'end': end, 'filed': f.get('filed'), 'accession': f.get('accn'), 'unit': 'USD'}

def revenue_cagr(rows):
    if len(rows) != 5 or any(r['revenue']['value'] is None or r['revenue']['value'] <= 0 for r in rows):
        return None
    years = (date.fromisoformat(rows[-1]['fiscal_year_end']) - date.fromisoformat(rows[0]['fiscal_year_end'])).days / 365.25
    return ((rows[-1]['revenue']['value'] / rows[0]['revenue']['value']) ** (1 / years) - 1) * 100 if years > 0 else None

def wood_checks(rows, growth_threshold=10.0):
    """Custom lab proxies, not Wood's official thresholds. Missing required inputs stay unknown."""
    growth = revenue_cagr(rows)
    latest = [rows[-1]['research_intensity']['value']] if rows else []
    intensity = [r['research_intensity']['value'] for r in rows]
    return {
        f'Revenue CAGR >= {growth_threshold:.1f}%': result([growth], lambda v: v[0] >= growth_threshold, 1),
        'Latest R&D / revenue >= 5.0%': result(latest, lambda v: v[0] >= 5, 1),
        'R&D / revenue increased first to last': result(intensity, lambda v: v[-1] > v[0], 5),
    }

def instant(company, tag, end):
    candidates = [f for f in b.facts_for(company, tag) if f.get('form') == '10-K' and f.get('end') == end and 'start' not in f]
    if not candidates:
        return {'value': None, 'tag': 'not found', 'searched_tags': [tag], 'end': end, 'unit': 'USD'}
    f = max(candidates, key=lambda f: (f.get('filed', ''), f.get('accn', '')))
    return {'value': f['val'], 'tag': 'us-gaap:' + tag, 'end': end, 'filed': f.get('filed'), 'accession': f.get('accn'), 'unit': 'USD'}

def ratio(a, c):
    return a / c if a is not None and c is not None and c > 0 else None

def result(values, predicate, required):
    if len(values) != required or any(v is None for v in values):
        return 'not known'
    return 'pass' if predicate(values) else 'fail'

def burry_checks(rows):
    pairs = [r[k]['value'] for r in rows for k in ('operating_cash_flow', 'net_income')]
    leverage = [rows[-1]['liabilities_equity']['value']] if rows else []
    return {
        'Operating cash flow >= net income every year': result(pairs, lambda v: all(v[i] >= v[i+1] for i in range(0, len(v), 2)), 10),
        'Liabilities <= 2.0 times equity, latest year': result(leverage, lambda v: v[0] <= 2, 1),
    }

def build_report(company, ticker, metadata, growth_threshold=10.0):
    report = b.build_report(company, ticker, metadata)
    for row in report['rows']:
        row['research'] = research_fact(company, row['fiscal_year_end'])
        intensity = ratio(row['research']['value'],row['revenue']['value'])
        row['research_intensity'] = {'value': None if intensity is None else intensity*100, 'tag':'derived: ResearchAndDevelopmentExpense / revenue * 100', 'unit':'%'}
        for field, tag in EXTRA.items():
            row[field] = instant(company, tag, row['fiscal_year_end'])
        for field, a, c in [('current_ratio', 'current_assets', 'current_liabilities'), ('liabilities_equity', 'liabilities', 'equity')]:
            row[field] = {'value': ratio(row[a]['value'], row[c]['value']), 'tag': f'derived: {a} / {c}', 'unit': 'ratio'}
    report['wood_growth_threshold'] = growth_threshold
    report['revenue_cagr'] = revenue_cagr(report['rows'])
    report['panel_checks'] = {'Buffett': report['checks'], 'Wood': wood_checks(report['rows'],growth_threshold), 'Burry': burry_checks(report['rows'])}
    report['facts_signature'] = hashlib.sha256(json.dumps(report['rows'], sort_keys=True).encode()).hexdigest()
    return report

def display(field, value):
    if field in ('research_intensity','revenue_cagr'):
        return 'not known' if value is None else f'{value:.2f}%'
    if field in ('current_ratio', 'liabilities_equity'):
        return 'not known' if value is None else f'{value:.2f}'
    return b.display(field, value)

def report_markdown(report):
    lines = [f"# {report['ticker']} — {report['company']}", '', 'Amounts: USD millions. ROE: percent. Other ratios: times.',
             f"Source: {report['source']['url']}", f"Retrieved: {report['source']['retrieved_at']}",
             'Latest available filings; not a point-in-time backtest.', '',
             '| Fiscal year end | ' + ' | '.join(LABELS.values()) + ' |', '|---|' + '---|' * len(LABELS)]
    for r in report['rows']:
        lines.append('| ' + r['fiscal_year_end'] + ' | ' + ' | '.join(display(k, r[k]['value']) for k in LABELS) + ' |')
    lines += ['', 'Revenue CAGR: ' + display('revenue_cagr', report['revenue_cagr']),
              'CAGR uses elapsed fiscal-end days / 365.25 (five observations, approximately four years).',
              'Custom Wood proxies: growth >= 10.0% (probe 5.0%); latest R&D/revenue >= 5.0%; R&D/revenue increased first to last.',
              'These are our lab design choices, not official Wood rules. They do not prove disruptive innovation.',
              '', '## Panel checks', '', '| Investor | Check | Result |', '|---|---|---|']
    for who, checks in report['panel_checks'].items():
        lines += [f'| {who} | {name} | {value} |' for name, value in checks.items()]
    lines += ['', 'Owner earnings = operating cash flow minus capital spending. ROE uses year-end equity.',
              'Burry liabilities/equity ceiling: 2.0.', '', '## Tags and filing provenance', '']
    for r in report['rows']:
        lines.append('### ' + r['fiscal_year_end'])
        for k in LABELS:
            c = r[k]
            lines.append(f"- {LABELS[k]}: {display(k,c['value'])}; {c['tag']}; filed {c.get('filed','n/a')}; accession {c.get('accession','n/a')}" + ('; searched ' + ', '.join(c['searched_tags']) if 'searched_tags' in c else ''))
    return '\n'.join(lines) + '\n'

def unsupported_numbers(memo, report):
    printed = ['15%', '2.0', '10.0%', '5.0%',display('revenue_cagr',report['revenue_cagr'])]
    for r in report['rows']:
        printed += [r['fiscal_year_end'], r['fiscal_year_end'][:4]]
        printed += [display(k, r[k]['value']) for k in LABELS]
    allowed = {b.number_key(m.group()) for text in printed for m in b.NUMBER.finditer(text)}
    return [{'number': m.group().strip(), 'line': memo.count('\n', 0, m.start()) + 1}
            for m in b.NUMBER.finditer(memo) if b.number_key(m.group()) not in allowed]

def load_report(ticker, out=ROOT, refresh=False, growth_threshold=10.0):
    out = Path(out)
    base = b.load_report(ticker, out, refresh)
    company = json.loads((out / f"data/{base['ticker']}_facts.json").read_text(encoding='utf-8-sig'))
    report = build_report(company, base['ticker'], base['source'],growth_threshold)
    (out / f"{base['ticker']}_panel.json").write_text(json.dumps(report, indent=2), encoding='utf-8')
    (out / f"{base['ticker']}_panel.md").write_text(report_markdown(report), encoding='utf-8')
    return report

def memo_path(ticker, investor, growth_threshold=10.0):
    suffix = f'_t{growth_threshold:.0f}' if investor == 'Wood' else ''
    return ROOT / f'{ticker}_{investor.lower()}{suffix}_memo.md'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ticker')
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--growth-threshold', type=float, choices=[5.0,10.0], default=10.0)
    args = parser.parse_args()
    print(report_markdown(load_report(args.ticker, refresh=args.refresh,growth_threshold=args.growth_threshold)))
