# JPM — JPMORGAN CHASE & CO

Amounts: USD millions. ROE: percent. Other ratios: times.
Source: https://data.sec.gov/api/xbrl/companyfacts/CIK0000019617.json
Retrieved: 2026-11-05T18:59:56.664702+00:00
Latest available filings; not a point-in-time backtest.

| Fiscal year end | Revenue | Net income | Operating cash flow | Capital spending | Equity | ROE | Owner earnings | Liabilities | Current assets | Current liabilities | Current ratio | Liabilities / equity | Research and development | R&D / revenue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021-12-31 | 121,649 | 48,334 | 78,084 | not found | 294,127 | 16.4% | not found | 3,449,440 | not found | not found | not known | 11.73 | not found | not known |
| 2022-12-31 | 128,695 | 37,676 | 107,119 | not found | 292,332 | 12.9% | not found | 3,373,411 | not found | not found | not known | 11.54 | not found | not known |
| 2023-12-31 | 158,104 | 49,552 | 12,974 | not found | 327,878 | 15.1% | not found | 3,547,515 | not found | not found | not known | 10.82 | not found | not known |
| 2024-12-31 | 177,556 | 58,471 | -42,012 | not found | 344,758 | 17.0% | not found | 3,658,056 | not found | not found | not known | 10.61 | not found | not known |
| 2025-12-31 | 182,447 | 57,048 | -147,782 | not found | 362,438 | 15.7% | not found | 4,062,462 | not found | not found | not known | 11.21 | not found | not known |

Revenue CAGR: 10.66%
CAGR uses elapsed fiscal-end days / 365.25 (five observations, approximately four years).
Custom Wood proxies: growth >= 10.0% (probe 5.0%); latest R&D/revenue >= 5.0%; R&D/revenue increased first to last.
These are our lab design choices, not official Wood rules. They do not prove disruptive innovation.

## Panel checks

| Investor | Check | Result |
|---|---|---|
| Buffett | ROE >= 15% every year | fail |
| Buffett | Owner earnings positive every year | not known |
| Buffett | Owner earnings grew first to last | not known |
| Wood | Revenue CAGR >= 10.0% | pass |
| Wood | Latest R&D / revenue >= 5.0% | not known |
| Wood | R&D / revenue increased first to last | not known |
| Burry | Operating cash flow >= net income every year | fail |
| Burry | Liabilities <= 2.0 times equity, latest year | fail |

Owner earnings = operating cash flow minus capital spending. ROE uses year-end equity.
Burry liabilities/equity ceiling: 2.0.

## Tags and filing provenance

### 2021-12-31
- Revenue: 121,649; us-gaap:Revenues; filed 2024-02-16; accession 0000019617-24-000225
- Net income: 48,334; us-gaap:NetIncomeLoss; filed 2024-02-16; accession 0000019617-24-000225
- Operating cash flow: 78,084; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2024-02-16; accession 0000019617-24-000225
- Capital spending: not found; not found; filed n/a; accession n/a; searched PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets
- Equity: 294,127; us-gaap:StockholdersEquity; filed 2024-02-16; accession 0000019617-24-000225
- ROE: 16.4%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: not found; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - not found; filed n/a; accession n/a
- Liabilities: 3,449,440; us-gaap:Liabilities; filed 2023-02-21; accession 0000019617-23-000231
- Current assets: not found; not found; filed n/a; accession n/a; searched AssetsCurrent
- Current liabilities: not found; not found; filed n/a; accession n/a; searched LiabilitiesCurrent
- Current ratio: not known; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 11.73; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: not found; not found; filed n/a; accession n/a; searched ResearchAndDevelopmentExpense
- R&D / revenue: not known; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2022-12-31
- Revenue: 128,695; us-gaap:Revenues; filed 2025-02-14; accession 0000019617-25-000270
- Net income: 37,676; us-gaap:NetIncomeLoss; filed 2025-02-14; accession 0000019617-25-000270
- Operating cash flow: 107,119; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2025-02-14; accession 0000019617-25-000270
- Capital spending: not found; not found; filed n/a; accession n/a; searched PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets
- Equity: 292,332; us-gaap:StockholdersEquity; filed 2025-02-14; accession 0000019617-25-000270
- ROE: 12.9%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: not found; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - not found; filed n/a; accession n/a
- Liabilities: 3,373,411; us-gaap:Liabilities; filed 2024-02-16; accession 0000019617-24-000225
- Current assets: not found; not found; filed n/a; accession n/a; searched AssetsCurrent
- Current liabilities: not found; not found; filed n/a; accession n/a; searched LiabilitiesCurrent
- Current ratio: not known; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 11.54; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: not found; not found; filed n/a; accession n/a; searched ResearchAndDevelopmentExpense
- R&D / revenue: not known; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2023-12-31
- Revenue: 158,104; us-gaap:Revenues; filed 2026-02-13; accession 0001628280-26-008131
- Net income: 49,552; us-gaap:NetIncomeLoss; filed 2026-02-13; accession 0001628280-26-008131
- Operating cash flow: 12,974; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-02-13; accession 0001628280-26-008131
- Capital spending: not found; not found; filed n/a; accession n/a; searched PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets
- Equity: 327,878; us-gaap:StockholdersEquity; filed 2026-02-13; accession 0001628280-26-008131
- ROE: 15.1%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: not found; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - not found; filed n/a; accession n/a
- Liabilities: 3,547,515; us-gaap:Liabilities; filed 2025-02-14; accession 0000019617-25-000270
- Current assets: not found; not found; filed n/a; accession n/a; searched AssetsCurrent
- Current liabilities: not found; not found; filed n/a; accession n/a; searched LiabilitiesCurrent
- Current ratio: not known; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 10.82; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: not found; not found; filed n/a; accession n/a; searched ResearchAndDevelopmentExpense
- R&D / revenue: not known; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2024-12-31
- Revenue: 177,556; us-gaap:Revenues; filed 2026-02-13; accession 0001628280-26-008131
- Net income: 58,471; us-gaap:NetIncomeLoss; filed 2026-02-13; accession 0001628280-26-008131
- Operating cash flow: -42,012; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-02-13; accession 0001628280-26-008131
- Capital spending: not found; not found; filed n/a; accession n/a; searched PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets
- Equity: 344,758; us-gaap:StockholdersEquity; filed 2026-02-13; accession 0001628280-26-008131
- ROE: 17.0%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: not found; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - not found; filed n/a; accession n/a
- Liabilities: 3,658,056; us-gaap:Liabilities; filed 2026-02-13; accession 0001628280-26-008131
- Current assets: not found; not found; filed n/a; accession n/a; searched AssetsCurrent
- Current liabilities: not found; not found; filed n/a; accession n/a; searched LiabilitiesCurrent
- Current ratio: not known; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 10.61; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: not found; not found; filed n/a; accession n/a; searched ResearchAndDevelopmentExpense
- R&D / revenue: not known; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2025-12-31
- Revenue: 182,447; us-gaap:Revenues; filed 2026-02-13; accession 0001628280-26-008131
- Net income: 57,048; us-gaap:NetIncomeLoss; filed 2026-02-13; accession 0001628280-26-008131
- Operating cash flow: -147,782; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-02-13; accession 0001628280-26-008131
- Capital spending: not found; not found; filed n/a; accession n/a; searched PaymentsToAcquirePropertyPlantAndEquipment, PaymentsToAcquireProductiveAssets
- Equity: 362,438; us-gaap:StockholdersEquity; filed 2026-02-13; accession 0001628280-26-008131
- ROE: 15.7%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: not found; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - not found; filed n/a; accession n/a
- Liabilities: 4,062,462; us-gaap:Liabilities; filed 2026-02-13; accession 0001628280-26-008131
- Current assets: not found; not found; filed n/a; accession n/a; searched AssetsCurrent
- Current liabilities: not found; not found; filed n/a; accession n/a; searched LiabilitiesCurrent
- Current ratio: not known; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 11.21; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: not found; not found; filed n/a; accession n/a; searched ResearchAndDevelopmentExpense
- R&D / revenue: not known; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
