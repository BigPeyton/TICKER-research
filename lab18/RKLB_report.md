# RKLB - Rocket Lab Corp

Amounts: USD millions. ROE: percent. Fiscal years labelled by end date.
Source: https://data.sec.gov/api/xbrl/companyfacts/CIK0001819994.json
Retrieved: 2026-11-03T19:03:57.141937+00:00
Latest available filings are used; this is not a point-in-time backtest.

| Fiscal year end | Revenue | Net income | Operating cash flow | Capital spending | Equity | ROE | Owner earnings |
|---|---|---|---|---|---|---|---|
| 2021-12-31 | 62.237 | -117.32 | -71.791 | 25.699 | 698.448 | -16.8% | -97.49 |
| 2022-12-31 | 210.996 | -135.944 | -106.538 | 42.412 | 673.206 | -20.2% | -148.95 |
| 2023-12-31 | 244.592 | -182.571 | -98.867 | 54.707 | 554.544 | -32.9% | -153.574 |
| 2024-12-31 | 436.214 | -190.175 | -48.89 | 67.093 | 382.453 | -49.7% | -115.983 |
| 2025-12-31 | 601.799 | -198.209 | -165.521 | 156.285 | 1,721.854 | -11.5% | -321.806 |

## Checks

- ROE >= 15% every year: **fail**
- Owner earnings positive every year: **fail**
- Owner earnings grew first to last: **fail**

The 15% ROE threshold is the lab's screening choice. Owner earnings is cash flow minus capital spending.

## Tags and filing provenance

### 2021-12-31
- Revenue: 62.237; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; starts 2021-01-01; filed 2024-02-28; accession 0000950170-24-022160
- Net income: -117.32; us-gaap:NetIncomeLoss; starts 2021-01-01; filed 2024-02-28; accession 0000950170-24-022160
- Operating cash flow: -71.791; us-gaap:NetCashProvidedByUsedInOperatingActivities; starts 2021-01-01; filed 2024-02-28; accession 0000950170-24-022160
- Capital spending: 25.699; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; starts 2021-01-01; filed 2024-02-28; accession 0000950170-24-022160
- Equity: 698.448; us-gaap:StockholdersEquity; filed 2025-02-27; accession 0001628280-25-008724
- ROE: -16.8%; derived: NetIncomeLoss / StockholdersEquity
- Owner earnings: -97.49; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment
### 2022-12-31
- Revenue: 210.996; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; starts 2022-01-01; filed 2025-02-27; accession 0001628280-25-008724
- Net income: -135.944; us-gaap:NetIncomeLoss; starts 2022-01-01; filed 2025-02-27; accession 0001628280-25-008724
- Operating cash flow: -106.538; us-gaap:NetCashProvidedByUsedInOperatingActivities; starts 2022-01-01; filed 2025-02-27; accession 0001628280-25-008724
- Capital spending: 42.412; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; starts 2022-01-01; filed 2025-02-27; accession 0001628280-25-008724
- Equity: 673.206; us-gaap:StockholdersEquity; filed 2026-02-26; accession 0001819994-26-000013
- ROE: -20.2%; derived: NetIncomeLoss / StockholdersEquity
- Owner earnings: -148.95; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment
### 2023-12-31
- Revenue: 244.592; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; starts 2023-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Net income: -182.571; us-gaap:NetIncomeLoss; starts 2023-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Operating cash flow: -98.867; us-gaap:NetCashProvidedByUsedInOperatingActivities; starts 2023-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Capital spending: 54.707; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; starts 2023-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Equity: 554.544; us-gaap:StockholdersEquity; filed 2026-02-26; accession 0001819994-26-000013
- ROE: -32.9%; derived: NetIncomeLoss / StockholdersEquity
- Owner earnings: -153.574; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment
### 2024-12-31
- Revenue: 436.214; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; starts 2024-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Net income: -190.175; us-gaap:NetIncomeLoss; starts 2024-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Operating cash flow: -48.89; us-gaap:NetCashProvidedByUsedInOperatingActivities; starts 2024-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Capital spending: 67.093; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; starts 2024-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Equity: 382.453; us-gaap:StockholdersEquity; filed 2026-02-26; accession 0001819994-26-000013
- ROE: -49.7%; derived: NetIncomeLoss / StockholdersEquity
- Owner earnings: -115.983; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment
### 2025-12-31
- Revenue: 601.799; us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax; starts 2025-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Net income: -198.209; us-gaap:NetIncomeLoss; starts 2025-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Operating cash flow: -165.521; us-gaap:NetCashProvidedByUsedInOperatingActivities; starts 2025-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Capital spending: 156.285; us-gaap:PaymentsToAcquirePropertyPlantAndEquipment; starts 2025-01-01; filed 2026-02-26; accession 0001819994-26-000013
- Equity: 1,721.854; us-gaap:StockholdersEquity; filed 2026-02-26; accession 0001819994-26-000013
- ROE: -11.5%; derived: NetIncomeLoss / StockholdersEquity
- Owner earnings: -321.806; derived: us-gaap:NetCashProvidedByUsedInOperatingActivities - us-gaap:PaymentsToAcquirePropertyPlantAndEquipment
