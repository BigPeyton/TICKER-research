# Lab 17 — Point-in-Time Audit

## Question

Was each number in the series knowable on the day I would have traded on it, and may Project 2 use it?

## App and validation

Run `python -m streamlit run asof_app.py`.

The app downloads today's observations from FRED and date-specific vintages from ALFRED, caches each download, and treats dots as missing observations. It compares shared measurement dates for revisions and counts nonmissing observations after the last date available in the selected vintage. The chart start date only limits the charts; the table compares the full downloaded histories.

Live checks on October 29, 2026 reproduced all four supplied October 5 answers: BAA 6.47 (September), FEDFUNDS 3.75 (September), DGS10 5.28 (October 2), and MORTGAGE30US 7.28 (October 1). The student confirmed the displayed results after setting the vintage date correctly.

The PAYEMS January 15, 2025 probe returned December 2024 at 159,536 and 381 revised observations. The same December observation in the current download was 158,316. The student confirmed the probe matched. Automated Streamlit checks also verified the app renders and that an invalid additional ID does not remove the four valid series.

## FEDFUNDS data card

- Source: Board of Governors of the Federal Reserve System, H.15 Selected Interest Rates, distributed by [FRED](https://fred.stlouisfed.org/series/FEDFUNDS); historical vintages from [ALFRED](https://alfred.stlouisfed.org/series?seid=FEDFUNDS).
- Measure: monthly average of daily effective federal funds rates, describing overnight lending of reserve balances between depository institutions.
- Units: percent; monthly; not seasonally adjusted. A value of 3.75 means 3.75%, not a 3.75% monthly investment return.
- Publication lag: the September 2026 observation was absent from the September 30 vintage. The FRED page lists an October 1, 2026 update for September's value. This example became available after month-end; do not assume a universal fixed lag from this one observation.
- Revisions: the student confirmed zero revised FEDFUNDS observations when comparing the September 30 vintage with the October 29 download. The automated October 5 versus October 29 comparison also found zero revisions. These checks show no revisions on shared observation dates in these comparisons; they do not establish that the series can never be revised.
- Download/access date: October 29, 2026.
- Portfolio relevance: a candidate short-term interest-rate input for the SGOV, SCHR, VTC, and ACWI portfolio, especially the short-term Treasury sleeve. It is not an ETF return series.

### Student-reported vintage comparison

| As known on | Last measurement available | Value (%) |
|---|---|---:|
| September 30, 2026 | August 2026 (2026-08-01) | 3.63 |
| October 29, 2026 | September 2026 (2026-09-01) | 3.75 |

The first-of-month observation label identifies the month being measured, not the date the monthly average was published. Using September's 3.75 for a September 30 decision would introduce information not present in that day's vintage.

### Three-value source check — completed

The student confirmed personally checking these three values against the FRED page: July 2026 3.63%, August 2026 3.63%, and September 2026 3.75%. All three matched. Source accessed October 29, 2026.

## Code explanation and partner exchange

The student supplied a line-by-line explanation of `download_asof()`, covering its arguments, docstring, GET request, endpoint, query parameters, ISO date formatting, connection/read timeout, and returned parsed response.

Partner question: "How does the function tell ALFRED which historical date to use?"

Student answer: `params={"id": series_id, "vintage_date": vintage_date.isoformat()}` sends the historical date through the `vintage_date` parameter, with `.isoformat()` formatting it as text.

After swapping roles, the student asked: "Does download_date affect the request?"

Reported partner answer: it does not affect the HTTP request, which uses `series_id` and `vintage_date`.

Clarification supplied by the assistant: `download_date` is not used inside the function body or sent to ALFRED, but the `@st.cache_data` decorator includes it in the cache key. Passing a different download date causes a separate cache entry. The decorator also expires cached results after 3,600 seconds.

Helper clarification: `read_csv_response()` checks the HTTP status, parses the CSV, treats dots as missing, converts dates and numeric values, drops missing rows, sorts by date, and returns a pandas Series of values indexed by measurement date.

## Partner attack: publication timing

Field chosen: publication timing.

Partner's concern: "Your data card labels the observation September 1, but that doesn't prove the value was available on September 1—or even September 30. What evidence shows when someone could actually have known September's value?"

Two-sentence response: "The September 30 ALFRED vintage contains only August's 3.63% as its latest observation, while the October 29 vintage includes September's 3.75%, so the September 1 label identifies the measurement month rather than availability. FRED lists the September observation's update as October 1, 2026 at 3:16 p.m. CDT, supporting availability after September ended; for a backtest, I would use the vintage available on each decision date and separately verify release times for intraday decisions."

Evidence: the student-reported vintage comparison above and the [FEDFUNDS source page](https://fred.stlouisfed.org/series/FEDFUNDS), accessed October 29, 2026. The app uses calendar-day vintages, not intraday timestamps.

## Decision: admit with an as-of rule

I would **admit FEDFUNDS** for Project 2, provided I use only values available as of each decision date. My rule is to retrieve the ALFRED vintage for that date and use the latest observation available then, without filling gaps with later releases or revisions; a month's observation label does not establish when its value became available.

I would **quarantine** the series if I could not verify its historical availability, and **reject** it if the project required information more timely than the series could provide.

## Learning and reflection

Saying "I cleaned the data" does not explain what changed or whether the data is suitable for the project. A data card documents the source, units, publication timing, revisions, transformations, and limitations so someone else can evaluate and reproduce the work.

Using September's 3.75% for a September 30 decision would incorrectly imply that the value was already available then. This introduces look-ahead bias: the backtest gives the strategy future information, potentially making its performance appear better than it could have been in real time.

## Remaining work

- Review the files, upload to GitHub, and submit the links in the Lab 17 checkout. No upload or submission is claimed here.
