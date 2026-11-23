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

## Current point-in-time signal: dated FOMC target lower bound

Updated November 23, 2026. The current model replaces the prior 3.63% monthly FEDFUNDS transcription with a **different measure**, the **3.75% lower bound of the announced policy target range**. It does not relabel the monthly series or claim the failed ALFRED download succeeded.

| Field | Current evidence / rule |
|---|---|
| Publisher | Board of Governors of the Federal Reserve System |
| Measure / units | FOMC federal-funds target lower bound, percent per annum; an event-based policy setting, not a monthly effective-rate observation |
| Announcement | September 16, 2026, 2:00 p.m. EDT (18:00 UTC) |
| Effective | September 17, 2026 |
| Announced range | 3.75% to 4.00%; use the 3.75% lower bound |
| Decision cutoff | September 30, 2026; announcement and effective dates both precede it |
| Primary sources | [Dated statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) and [implementation note](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a1.htm) |
| Bundled evidence | [Statement HTML](../data/raw/fomc-20260916.html), [implementation HTML](../data/raw/fomc-implementation-20260916.html), [URLs, retrieval times, hashes and text checks](../data/policy-signal-sources.json) |
| Parsed record | [policy-signal.json](../data/policy-signal.json) |
| Retrieval | November 23, 2026; this is a later retrieval of a dated historical publication, not a contemporaneous download |
| Timing / revisions | Use the event's publication and effective dates, not a measurement-month label. Later policy decisions are new events and must not be substituted across the cutoff. These archived copies were checked against the publisher; a hash establishes file identity, not a guarantee the website never had an erratum. |

The code validates units, published/effective dates, expected target bounds, hashes of both HTML files, and the source text supporting the dates and range. A missing, changed or unsupported source blocks calculation rather than reverting to the earlier transcription.

**Use:** `SGOV estimate = min(historical annual SGOV mean, 3.75% target lower bound)`. The 60-return historical mean is about 3.715%, so this cap is nonbinding at defaults. It binds in the recent 36-return scenario. This is a disclosed research heuristic; the policy target is neither an SGOV yield nor a validated return forecast.

## Preserved historical signal and experiment

The earlier [Lab 17 comparison](prior-evidence/lab17_point_in_time.md), [signal-record.json](../data/signal-record.json), [failed source attempts](../data/signal-source.json), and original [student experiment](student-experiment.md) retain the 3.63% monthly FEDFUNDS evidence used then. Additional retrieval attempts on November 23 also failed. They are historical evidence, not the current model's signal inputs.

Original experiment: default 5.51% net, changed-cost selected return 5.83%. Current revised model: default **5.57%**, changed-cost selected return **5.89%**. Allocation choices and volatility are unchanged. See [revision reconciliation](readiness-revision.md). No historical prediction or export was overwritten.

## Other assumptions and limits

Inflation of 2.5%, annual additional cost of 25 bps, trading cost of 10 bps, and the new 6% volatility ceiling are explicit research assumptions. They are not measured CPI, actual fee quotes or client approvals. Fund expenses embedded in adjusted prices are not deducted twice. Only SGOV is reserve-eligible in this model.

The reported net return is a first-year arithmetic estimate including one rebalance, not demonstrated rolling five-year CPI + 3% performance. The later-downloaded adjusted-price archive is still not a point-in-time price backtest. Fund eligibility, five-day liquidity, actual holdings/annual turnover and client risk-policy approval remain unresolved. The recommendation stays paper-only, 0% live.
