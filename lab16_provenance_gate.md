# Lab 16 — Provenance Gate

## Question and method

On the day you would have traded, what did this data actually say, and how much of what you see now came later?

The decision date is March 31, 2026. The fictional card-spend table contains twelve rows for AAA, BBB, and CCC. The month measured describes the period covered by a number; the publication date determines when that number became available. A revision is a later publication updating a previously measured month.

`asof.py` uses only Python's standard library. It quarantines missing tickers, removes exact duplicates, excludes publications after the decision date, and keeps the latest available publication for each ticker and month, in that order. It calculates the percentage change from the previous month to the latest knowable month. The naive comparison uses the latest publications without the decision-date cutoff. All results are calculated from the editable inputs.

Run:

```powershell
python asof.py
```

## Verified results

| Rule | Count removed | Row numbers |
|---|---:|---|
| Missing ticker | 1 | 11 |
| Exact duplicate | 1 | 7 |
| Published after March 31 | 3 | 3, 8, 10 |
| Older publication replaced by an available revision | 1 | 2 |

The remaining six rows are 1, 4, 5, 6, 9, and 12.

| Ticker | As-of signal | Naive signal |
|---|---|---|
| AAA | +1.98% (February) | +5.83% (March) |
| BBB | -1.02% (February) | -5.15% (March) |
| CCC | +0.91% (February) | +1.82% (February, revised) |

The executed output matches every supplied known answer.

## Code quiz

Question: What two situations make `key not in latest or row[3] > latest[key][3]` true, and why keep that row?

My answer:

1. `key not in latest`: We haven't saved a row for that ticker and month yet, so we keep this one as our first candidate.
2. `row[3] > latest[key][3]`: This row was published later than the saved row, so we replace the older row with this newer version.

For the as-of panel, the cutoff is applied before this revision selection.

## Partner code explanation and discussion

I explained the following block:

```python
latest = {}
for row in rows:
    key = (row[1], row[2])
    if key not in latest or row[3] > latest[key][3]:
        latest[key] = row
```

- `latest = {}` creates an empty dictionary to store the latest row for each ticker and month.
- `for row in rows:` goes through the rows one at a time.
- `key = (row[1], row[2])` combines the ticker and month into a key, so rows for the same ticker and month are compared together.
- The `if` condition checks whether this is the first row for that key or whether its publication date is later than the saved row's.
- `latest[key] = row` saves that row, replacing the previous one if there was one.

Partner's question: What happens if two rows have the same publication date?

My answer: The first one stays. The code uses `>`, so an equal date doesn't replace the saved row.

After swapping roles, my partner explained that the dictionary holds one row per ticker and month. Each new row is saved only if its key is missing or its publication date is newer.

My question: Would a newer row for a different month replace the previous month's row?

Partner's answer: No. The month is part of the key, so different months have separate dictionary entries.

## Swap-and-break validation

I reported that both files passed the partner test. Changing the decision date to April 15, 2026 makes the as-of signals equal the naive signals: AAA +5.83%, BBB -5.15%, and CCC +1.82%.

My saved file was then checked and executed again: `DECISION_DATE` is restored to `2026-03-31`, and all original results match. The AI also independently tested the April 15 calculation in my implementation; the partner-file result is based on my report.

## Look-ahead bias

AAA's naive +5.83% signal uses information published after March 31, which wasn't available when the decision had to be made.

Using it would introduce look-ahead bias: judging a past decision with future information. The +1.98% as-of signal reflects what was actually available by March 31.

## Final reflection

The publication-date cutoff rule removed row 3: AAA's March index of 109, published April 10. It wasn't available for a March 31 decision. Including it produces the naive +5.83% signal instead of the available +1.98% signal.

A naive backtest could claim the strategy identified stronger AAA growth in advance and made better investment decisions. That apparent foresight would rely on future information. Also, +5.83% is an index-change signal, not a demonstrated investment return.

## AI assistance

AI generated the Python implementation, checked the known answers and later-date behavior, and assembled this write-up from my responses. The code quiz, partner discussion, partner test report, and reflection above were supplied by me in the conversation.
