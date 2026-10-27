"""Lab 16: show which training data was knowable on a decision date."""

from datetime import date, datetime


# Editable inputs: row number, ticker, month measured, published on, index.
DECISION_DATE = "2026-03-31"
TABLE = [
    (1, "AAA", "2026-01", "2026-02-10", 101.0),
    (2, "AAA", "2026-02", "2026-03-10", 104.0),
    (3, "AAA", "2026-03", "2026-04-10", 109.0),
    (4, "AAA", "2026-02", "2026-03-25", 103.0),
    (5, "BBB", "2026-01", "2026-02-10", 98.0),
    (6, "BBB", "2026-02", "2026-03-10", 97.0),
    (7, "BBB", "2026-02", "2026-03-10", 97.0),
    (8, "BBB", "2026-03", "2026-04-10", 92.0),
    (9, "CCC", "2026-01", "2026-02-10", 110.0),
    (10, "CCC", "2026-02", "2026-04-05", 112.0),
    (11, "", "2026-02", "2026-03-10", 99.0),
    (12, "CCC", "2026-02", "2026-03-10", 111.0),
]


def latest_publications(rows):
    """Keep the latest publication for each ticker and measured month."""
    latest = {}
    for row in rows:
        key = (row[1], row[2])
        if key not in latest or row[3] > latest[key][3]:
            latest[key] = row
    return sorted(latest.values(), key=lambda row: (row[1], row[2]))


def filter_asof(table, decision_date):
    """Apply the four rules in order and retain an audit of removed rows."""
    cutoff = date.fromisoformat(decision_date)
    audit = []

    # Rule 1: quarantine missing tickers.
    removed = [row for row in table if not row[1].strip()]
    rows = [row for row in table if row[1].strip()]
    audit.append(("Quarantined: no ticker", removed))

    # Rule 2: compare data fields, excluding the identifying row number.
    seen = set()
    clean = []
    removed = []
    for row in rows:
        fields = row[1:]
        if fields in seen:
            removed.append(row)
        else:
            seen.add(fields)
            clean.append(row)
    audit.append(("Exact duplicate", removed))

    # Rule 3: exclude publications that were not yet available.
    removed = [row for row in clean if date.fromisoformat(row[3]) > cutoff]
    available = [row for row in clean if date.fromisoformat(row[3]) <= cutoff]
    audit.append(("Published after " + decision_date, removed))

    # Rule 4: select revisions only from publications available by the cutoff.
    panel = latest_publications(available)
    kept_ids = {row[0] for row in panel}
    removed = [row for row in available if row[0] not in kept_ids]
    audit.append(("Older vintage replaced by a revision", removed))

    # The naive comparison uses the same clean data but ignores the cutoff.
    naive_panel = latest_publications(clean)
    return panel, naive_panel, audit


def signals(panel):
    """Calculate percent changes into each ticker's latest measured month."""
    grouped = {}
    for row in panel:
        grouped.setdefault(row[1], []).append(row)

    result = {}
    for ticker, rows in sorted(grouped.items()):
        rows = sorted(rows, key=lambda row: row[2])
        latest = rows[-1]
        year, month = map(int, latest[2].split("-"))
        previous_month = f"{year - 1}-12" if month == 1 else f"{year}-{month - 1:02d}"
        previous = next((row for row in rows if row[2] == previous_month), None)
        change = None
        if previous is not None and previous[4] != 0:
            change = (latest[4] / previous[4] - 1) * 100
        result[ticker] = (latest[2], change)
    return result


def format_signal(signal):
    if signal is None:
        return "N/A (no available data)"
    month, change = signal
    label = datetime.strptime(month, "%Y-%m").strftime("%B %Y")
    if change is None:
        return f"N/A ({label}; previous month missing or zero)"
    return f"{change:+.2f}% ({label})"


def main():
    panel, naive_panel, audit = filter_asof(TABLE, DECISION_DATE)
    print("Fictional training data; decision date:", DECISION_DATE)
    print(f"\nRow funnel (starting rows: {len(TABLE)})")
    for label, removed in audit:
        numbers = ", ".join(str(row[0]) for row in removed) or "none"
        print(f"{label}: removed {len(removed)}; rows: {numbers}")
    print(f"As-of panel: {len(panel)} rows; rows: " + ", ".join(str(row[0]) for row in panel))

    print("\nAs-of panel")
    print(f"{'Row':>3}  {'Ticker':6}  {'Month':7}  {'Published':10}  {'Index':>7}")
    for number, ticker, month, published, value in panel:
        print(f"{number:>3}  {ticker:6}  {month:7}  {published:10}  {value:>7.1f}")

    asof_signals = signals(panel)
    naive_signals = signals(naive_panel)
    print("\nSignals: percent change from previous month")
    for ticker in sorted(naive_signals):
        print(f"{ticker}: as-of {format_signal(asof_signals.get(ticker))}; "
              f"naive {format_signal(naive_signals[ticker])}")


if __name__ == "__main__":
    main()
