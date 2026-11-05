# AAPL — Apple Inc.

Amounts: USD millions. ROE: percent. Other ratios: times.
Source: https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json
Retrieved: 2026-11-05T18:59:32.664908+00:00
Latest available filings; not a point-in-time backtest.

| Fiscal year end | Revenue | Net income | Operating cash flow | Capital spending | Equity | ROE | Owner earnings | Liabilities | Current assets | Current liabilities | Current ratio | Liabilities / equity | Research and development | R&D / revenue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022-09-24 | 394,328 | 99,803 | 122,151 | 10,708 | 50,672 | 197.0% | 111,443 | 302,083 | 135,405 | 153,982 | 0.88 | 5.96 | 26,251 | 6.66% |
| 2023-09-30 | 383,285 | 96,995 | 110,543 | 10,959 | 62,146 | 156.1% | 99,584 | 290,437 | 143,566 | 145,308 | 0.99 | 4.67 | 29,915 | 7.80% |
| 2024-09-28 | 391,035 | 93,736 | 118,254 | 9,447 | 56,950 | 164.6% | 108,807 | 308,030 | 152,987 | 176,392 | 0.87 | 5.41 | 31,370 | 8.02% |
| 2025-09-27 | 416,161 | 112,010 | 111,482 | 12,715 | 73,733 | 151.9% | 98,767 | 285,508 | 147,957 | 165,631 | 0.89 | 3.87 | 34,550 | 8.30% |
| 2026-09-26 | 478,834 | 132,175 | 145,097 | 9,041 | 112,093 | 117.9% | 136,056 | 292,455 | 173,857 | 169,915 | 1.02 | 2.61 | 45,765 | 9.56% |

Revenue CAGR: 4.97%
CAGR uses elapsed fiscal-end days / 365.25 (five observations, approximately four years).
Custom Wood proxies: growth >= 10.0% (probe 5.0%); latest R&D/revenue >= 5.0%; R&D/revenue increased first to last.
These are our lab design choices, not official Wood rules. They do not prove disruptive innovation.

## Panel checks

| Investor | Check | Result |
|---|---|---|
| Buffett | ROE >= 15% every year | pass |
| Buffett | Owner earnings positive every year | pass |
| Buffett | Owner earnings grew first to last | pass |
| Wood | Revenue CAGR >= 5.0% | fail |
| Wood | Latest R&D / revenue >= 5.0% | pass |
| Wood | R&D / revenue increased first to last | pass |
| Burry | Operating cash flow >= net income every year | fail |
| Burry | Liabilities <= 2.0 times equity, latest year | fail |

Owner earnings = operating cash flow minus capital spending. ROE uses year-end equity.
Burry liabilities/equity ceiling: 2.0.

## Tags and filing provenance

### 2022-09-24
- Revenue: 394,328; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; filed 2024-11-01; accession 0000320193-24-000123
- Net income: 99,803; us-gaap:NetIncomeLoss; filed 2024-11-01; accession 0000320193-24-000123
- Operating cash flow: 122,151; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2024-11-01; accession 0000320193-24-000123
- Capital spending: 10,708; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2024-11-01; accession 0000320193-24-000123
- Equity: 50,672; us-gaap:StockholdersEquity; filed 2025-10-31; accession 0000320193-25-000079
- ROE: 197.0%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: 111,443; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed n/a; accession n/a
- Liabilities: 302,083; us-gaap:Liabilities; filed 2023-11-03; accession 0000320193-23-000106
- Current assets: 135,405; us-gaap:AssetsCurrent; filed 2023-11-03; accession 0000320193-23-000106
- Current liabilities: 153,982; us-gaap:LiabilitiesCurrent; filed 2023-11-03; accession 0000320193-23-000106
- Current ratio: 0.88; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 5.96; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: 26,251; us-gaap:ResearchAndDevelopmentExpense; filed 2024-11-01; accession 0000320193-24-000123
- R&D / revenue: 6.66%; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2023-09-30
- Revenue: 383,285; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; filed 2025-10-31; accession 0000320193-25-000079
- Net income: 96,995; us-gaap:NetIncomeLoss; filed 2025-10-31; accession 0000320193-25-000079
- Operating cash flow: 110,543; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2025-10-31; accession 0000320193-25-000079
- Capital spending: 10,959; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2025-10-31; accession 0000320193-25-000079
- Equity: 62,146; us-gaap:StockholdersEquity; filed 2026-11-03; accession 0000320193-26-000026
- ROE: 156.1%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: 99,584; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed n/a; accession n/a
- Liabilities: 290,437; us-gaap:Liabilities; filed 2024-11-01; accession 0000320193-24-000123
- Current assets: 143,566; us-gaap:AssetsCurrent; filed 2024-11-01; accession 0000320193-24-000123
- Current liabilities: 145,308; us-gaap:LiabilitiesCurrent; filed 2024-11-01; accession 0000320193-24-000123
- Current ratio: 0.99; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 4.67; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: 29,915; us-gaap:ResearchAndDevelopmentExpense; filed 2025-10-31; accession 0000320193-25-000079
- R&D / revenue: 7.80%; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2024-09-28
- Revenue: 391,035; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; filed 2026-11-03; accession 0000320193-26-000026
- Net income: 93,736; us-gaap:NetIncomeLoss; filed 2026-11-03; accession 0000320193-26-000026
- Operating cash flow: 118,254; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-11-03; accession 0000320193-26-000026
- Capital spending: 9,447; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2026-11-03; accession 0000320193-26-000026
- Equity: 56,950; us-gaap:StockholdersEquity; filed 2026-11-03; accession 0000320193-26-000026
- ROE: 164.6%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: 108,807; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed n/a; accession n/a
- Liabilities: 308,030; us-gaap:Liabilities; filed 2025-10-31; accession 0000320193-25-000079
- Current assets: 152,987; us-gaap:AssetsCurrent; filed 2025-10-31; accession 0000320193-25-000079
- Current liabilities: 176,392; us-gaap:LiabilitiesCurrent; filed 2025-10-31; accession 0000320193-25-000079
- Current ratio: 0.87; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 5.41; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: 31,370; us-gaap:ResearchAndDevelopmentExpense; filed 2026-11-03; accession 0000320193-26-000026
- R&D / revenue: 8.02%; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2025-09-27
- Revenue: 416,161; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; filed 2026-11-03; accession 0000320193-26-000026
- Net income: 112,010; us-gaap:NetIncomeLoss; filed 2026-11-03; accession 0000320193-26-000026
- Operating cash flow: 111,482; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-11-03; accession 0000320193-26-000026
- Capital spending: 12,715; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2026-11-03; accession 0000320193-26-000026
- Equity: 73,733; us-gaap:StockholdersEquity; filed 2026-11-03; accession 0000320193-26-000026
- ROE: 151.9%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: 98,767; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed n/a; accession n/a
- Liabilities: 285,508; us-gaap:Liabilities; filed 2026-11-03; accession 0000320193-26-000026
- Current assets: 147,957; us-gaap:AssetsCurrent; filed 2026-11-03; accession 0000320193-26-000026
- Current liabilities: 165,631; us-gaap:LiabilitiesCurrent; filed 2026-11-03; accession 0000320193-26-000026
- Current ratio: 0.89; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 3.87; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: 34,550; us-gaap:ResearchAndDevelopmentExpense; filed 2026-11-03; accession 0000320193-26-000026
- R&D / revenue: 8.30%; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
### 2026-09-26
- Revenue: 478,834; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; filed 2026-11-03; accession 0000320193-26-000026
- Net income: 132,175; us-gaap:NetIncomeLoss; filed 2026-11-03; accession 0000320193-26-000026
- Operating cash flow: 145,097; us-gaap:NetCashProvidedByUsedInOperatingActivities; filed 2026-11-03; accession 0000320193-26-000026
- Capital spending: 9,041; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed 2026-11-03; accession 0000320193-26-000026
- Equity: 112,093; us-gaap:StockholdersEquity; filed 2026-11-03; accession 0000320193-26-000026
- ROE: 117.9%; derived: NetIncomeLoss / StockholdersEquity; filed n/a; accession n/a
- Owner earnings: 136,056; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; filed n/a; accession n/a
- Liabilities: 292,455; us-gaap:Liabilities; filed 2026-11-03; accession 0000320193-26-000026
- Current assets: 173,857; us-gaap:AssetsCurrent; filed 2026-11-03; accession 0000320193-26-000026
- Current liabilities: 169,915; us-gaap:LiabilitiesCurrent; filed 2026-11-03; accession 0000320193-26-000026
- Current ratio: 1.02; derived: current_assets / current_liabilities; filed n/a; accession n/a
- Liabilities / equity: 2.61; derived: liabilities / equity; filed n/a; accession n/a
- Research and development: 45,765; us-gaap:ResearchAndDevelopmentExpense; filed 2026-11-03; accession 0000320193-26-000026
- R&D / revenue: 9.56%; derived: ResearchAndDevelopmentExpense / revenue * 100; filed n/a; accession n/a
