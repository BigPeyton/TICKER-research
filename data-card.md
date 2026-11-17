# Data card and transformations

Prepared November 17, 2026. The analysis uses a fixed September 30, 2026 boundary for comparison with earlier labs; it does not recommend trades at today's prices.

## Adjusted-price inputs

- Universe and required order: **SGOV, SCHR, VTC, ACWI**. Daily Yahoo Finance adjusted closes were reduced to the last available trading observation in each calendar month. Adjusted prices account for the provider's distribution/split adjustments; future provider revisions are possible.
- Source: Yahoo Finance chart endpoints documented per ticker in [`data/price-sources.json`](../data/price-sources.json). Original daily responses are bundled in [`data/raw/`](../data/raw/), with SHA-256 hashes checked against that metadata. URLs and retrieval timestamps are preserved, not replaced with today's timestamp.
- Retrieval: **October 22, 2026**. Monthly file copied without alteration from Peyton's prior repository commit [`7904f42d1c0f3f800c7ff285d96c7cc87d32d761`](https://github.com/BigPeyton/TICKER-research/tree/7904f42d1c0f3f800c7ff285d96c7cc87d32d761).
- Coverage: September 30, 2021–September 30, 2026; 61 price rows, 60 simple monthly returns. A row may use September 29 when that is the month's last trading day.
- Monthly simple return: current adjusted price / previous adjusted price − 1. Annual mean: monthly arithmetic mean × 12. Annual covariance: monthly sample covariance × 12. Annual volatility: square root of the weighted annual covariance. Recent window: final 37 prices, producing 36 returns.
- Validation: exact column order; unique names; consecutive months; positive finite prices; no dropped or forward-filled missing values. Invalid files fail instead of silently changing the sample.
- **Availability limitation:** these prices were downloaded after the chosen historical boundary. No historical price-vintage archive or execution-cost study is available. This is not an out-of-sample performance backtest, and no point-in-time price claim is made.

## FEDFUNDS point-in-time signal

| Field | Evidence / rule |
|---|---|
| Source | Federal Reserve H.15 via [FRED](https://fred.stlouisfed.org/series/FEDFUNDS) and [ALFRED](https://alfred.stlouisfed.org/series?seid=FEDFUNDS) |
| Measure | Monthly average of daily effective federal funds rates; percent, not seasonally adjusted |
| Historical vintage used | September 30, 2026 |
| Latest observation in prior check | August 2026, label `2026-08-01`, **3.63%** |
| Later value excluded | September 2026, 3.75%, recorded in the October 29 vintage; not present at the September 30 cutoff |
| Evidence | [Lab 17 student-checked comparison](prior-evidence/lab17_point_in_time.md), preserved from the source commit above |
| Original access/check date | October 29, 2026, as recorded in Lab 17 |
| Fresh retrieval | Attempted November 17, 2026; endpoint timed out. **No raw vintage is bundled and no fresh validation is claimed.** |
| Revisions | Prior Lab 17 reported none among the shared observations in its specific comparison; this does not establish that FEDFUNDS never revises |
| Publication timing | Observation labels identify measurement months, not availability; the prior Lab 17 record reports September's release/update on October 1 |

[`signal-record.json`](../data/signal-record.json) is an explicitly labeled transcription of that prior checked summary, **not a downloaded ALFRED CSV**. `signal-source.json` records the failed retrieval. The code requires the specified historical vintage and rejects a later vintage; the date gate alone cannot authenticate the transcription. Raw source verification is an unresolved live-use requirement. Calendar-day vintages also do not establish intraday availability.

**Model use:** SGOV's assumed annual return is `min(historical annual SGOV mean, 3.63% FEDFUNDS proxy)`. This converts percent to decimal once. It prevents using a trailing bill return above the available policy-rate proxy, but it is a disclosed research heuristic; the federal funds rate is neither a Treasury yield nor an SGOV total-return forecast. ACWI's scenario adjustment is then added in percentage points. The user can see both raw historical means and estimates actually used in the app.

To replace the transcription with authenticated raw evidence, retrieve the exact [September 30 vintage CSV](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=FEDFUNDS&vintage_date=2026-09-30), preserve it and its hash, check the last nonmissing observation and release timing, update the parser/data card/validation together, and rerun the checks. Do not silently substitute the current series or a later vintage.

## Assumptions introduced for Project 2

Inflation of 2.5% is a planning assumption, not a fetched CPI observation. The 25 bps annual additional cost and 10 bps one-way trading charge are hypothetical scenario inputs; they are not fee quotes. ETF expenses already reflected in adjusted prices are not deducted twice. The 60/40 comparator follows the earlier lab benchmark structure; it does not impose those weights as a mandate. Only SGOV is designated as reserve-eligible in this research model.

The reported annual return is a first-year net estimate including one rebalance cost, not a five-year compounded real return. The reference holdings are a previous paper proposal. Fund eligibility, five-day liquidity, actual turnover, and a committee-approved risk limit still require evidence.
