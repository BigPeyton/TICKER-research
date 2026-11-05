"""SEC facts and deterministic Buffett lab calculations; the AI writes the memo."""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import time
import requests

USER_AGENT = "Peyton Dow peytonpdow@gmail.com"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
TAGS = {
    "revenue": ("RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"),
    "net_income": ("NetIncomeLoss",),
    "operating_cash_flow": ("NetCashProvidedByUsedInOperatingActivities",),
    "capital_spending": ("PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"),
    "equity": ("StockholdersEquity",),
}
LABELS = {"revenue": "Revenue", "net_income": "Net income", "operating_cash_flow": "Operating cash flow",
          "capital_spending": "Capital spending", "equity": "Equity", "roe": "ROE", "owner_earnings": "Owner earnings"}
NUMBER = re.compile(r"\d{4}-\d{2}-\d{2}|[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?\s*%?")


def download_json(url, path, refresh=False):
    """Cache for a day. HTTP errors are not missing financial data."""
    path = Path(path)
    meta = path.with_suffix(".meta.json")
    if not refresh and path.exists() and meta.exists() and time.time() - path.stat().st_mtime < 86400:
        return json.loads(path.read_text(encoding="utf-8-sig")), json.loads(meta.read_text(encoding="utf-8-sig"))
    response = requests.get(url, headers={"User-Agent": USER_AGENT, "Accept-Encoding": "gzip, deflate"}, timeout=(15, 60))
    response.raise_for_status()
    data = response.json()
    metadata = {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat()}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")
    meta.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    time.sleep(0.15)
    return data, metadata


def annual(fact):
    """Accept calendar and 52/53-week years; exclude quarters and YTD."""
    try:
        return fact.get("form") == "10-K" and 350 <= (date.fromisoformat(fact["end"]) - date.fromisoformat(fact["start"])).days <= 380
    except (KeyError, ValueError):
        return False


def facts_for(company, tag):
    return company.get("facts", {}).get("us-gaap", {}).get(tag, {}).get("units", {}).get("USD", [])


def fiscal_ends(company):
    # A filing's fy can be later than the year measured by comparative values.
    ends = {f["end"] for field in TAGS if field != "equity" for tag in TAGS[field]
            for f in facts_for(company, tag) if annual(f)}
    return sorted(ends)[-5:]


def pick_fact(company, field, end):
    for tag in TAGS[field]:
        candidates = [f for f in facts_for(company, tag)
                      if f.get("end") == end and f.get("form") == "10-K"
                      and (field == "equity" and "start" not in f or field != "equity" and annual(f))]
        if candidates:
            chosen = max(candidates, key=lambda f: (f.get("filed", ""), f.get("accn", ""), f.get("start", "")))
            return {"value": chosen["val"], "tag": "us-gaap:" + tag,
                    "start": chosen.get("start"), "end": end, "filed": chosen.get("filed"),
                    "accession": chosen.get("accn"), "unit": "USD"}
    return {"value": None, "tag": "not found", "searched_tags": list(TAGS[field]), "end": end, "unit": "USD"}


def year_row(company, end):
    """Turn EDGAR facts into one year's row; explain this function for the lab."""
    row = {"fiscal_year_end": end}
    for field in TAGS:
        row[field] = pick_fact(company, field, end)
    income = row["net_income"]["value"]
    equity = row["equity"]["value"]
    cash = row["operating_cash_flow"]["value"]
    spending = row["capital_spending"]["value"]
    row["roe"] = {"value": income / equity * 100 if income is not None and equity is not None and equity > 0 else None,
                  "tag": "derived: NetIncomeLoss / StockholdersEquity", "unit": "%"}
    row["owner_earnings"] = {"value": cash - spending if cash is not None and spending is not None else None,
                            "tag": "derived: " + row["operating_cash_flow"]["tag"] + " - " + row["capital_spending"]["tag"], "unit": "USD"}
    return row


def checks(rows):
    roe = [r["roe"]["value"] for r in rows]
    owner = [r["owner_earnings"]["value"] for r in rows]
    def complete(values):
        return len(values) == 5 and all(v is not None for v in values)
    def result(valid, passed):
        return ("pass" if passed else "fail") if valid else "not known"
    return {
        "ROE >= 15% every year": result(complete(roe), all(v is not None and v >= 15 for v in roe)),
        "Owner earnings positive every year": result(complete(owner), all(v is not None and v > 0 for v in owner)),
        "Owner earnings grew first to last": result(complete(owner), bool(owner) and owner[0] is not None and owner[-1] is not None and owner[-1] > owner[0]),
    }


def display(field, value):
    if value is None:
        return "not known" if field == "roe" else "not found"
    if field == "roe":
        return f"{value:.1f}%"
    return f"{value / 1_000_000:,.3f}".rstrip("0").rstrip(".")


def build_report(company, ticker, metadata):
    rows = [year_row(company, end) for end in fiscal_ends(company)]
    if not rows:
        raise ValueError("No annual USD facts from permitted 10-K tags found. No report can be produced.")
    signature = hashlib.sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest()
    return {"ticker": ticker, "company": company.get("entityName", ticker), "cik": company.get("cik"),
            "source": metadata, "rows": rows, "checks": checks(rows), "facts_signature": signature}


def report_markdown(report):
    lines = [f"# {report['ticker']} - {report['company']}", "", "Amounts: USD millions. ROE: percent. Fiscal years labelled by end date.",
             f"Source: {report['source']['url']}", f"Retrieved: {report['source']['retrieved_at']}",
             "Latest available filings are used; this is not a point-in-time backtest.", "",
             "| Fiscal year end | " + " | ".join(LABELS.values()) + " |",
             "|---|" + "---|" * len(LABELS)]
    for row in report["rows"]:
        lines.append("| " + row["fiscal_year_end"] + " | " + " | ".join(display(k, row[k]["value"]) for k in LABELS) + " |")
    lines += ["", "## Checks", ""] + [f"- {k}: **{v}**" for k, v in report["checks"].items()]
    lines += ["", "The 15% ROE threshold is the lab's screening choice. Owner earnings is cash flow minus capital spending.", "", "## Tags and filing provenance", ""]
    for row in report["rows"]:
        lines.append(f"### {row['fiscal_year_end']}")
        for field in LABELS:
            cell = row[field]
            source = f"; filed {cell['filed']}; accession {cell['accession']}" if cell.get("filed") else ""
            period = f"; starts {cell['start']}" if cell.get("start") else ""
            searched = "; searched " + ", ".join(cell["searched_tags"]) if "searched_tags" in cell else ""
            lines.append(f"- {LABELS[field]}: {display(field, cell['value'])}; {cell['tag']}{period}{source}{searched}")
    return "\n".join(lines) + "\n"


def number_key(token):
    token = token.strip().replace(",", "")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", token):
        return ("date", token)
    return ("percent" if token.endswith("%") else "number", Decimal(token.rstrip("%").strip()))


def unsupported_numbers(memo, report):
    # URLs, timestamps and accession numbers are not financial evidence.
    printed = ["15%"]
    for row in report["rows"]:
        printed.extend([row["fiscal_year_end"], row["fiscal_year_end"][:4]])
        printed.extend(display(field, row[field]["value"]) for field in LABELS)
    allowed = {number_key(m.group()) for text in printed for m in NUMBER.finditer(text)}
    return [{"number": match.group().strip(), "line": memo.count("\n", 0, match.start()) + 1}
            for match in NUMBER.finditer(memo) if number_key(match.group()) not in allowed]


def load_report(ticker, out, refresh=False):
    ticker = ticker.strip().upper()
    if not re.fullmatch(r"[A-Z][A-Z0-9.-]{0,9}", ticker):
        raise ValueError("Enter a valid ticker, such as COST or JPM.")
    out = Path(out)
    mapping, _ = download_json(TICKERS_URL, out / "data/company_tickers.json", refresh)
    matches = [v for v in mapping.values() if v["ticker"].upper() == ticker]
    if not matches:
        raise ValueError(f"Ticker {ticker} was not found in SEC's mapping.")
    cik = int(matches[0]["cik_str"])
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
    company, meta = download_json(url, out / f"data/{ticker}_facts.json", refresh)
    report = build_report(company, ticker, meta)
    (out / f"{ticker}_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    (out / f"{ticker}_report.md").write_text(report_markdown(report), encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker")
    parser.add_argument("--out", default="lab18")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--check-memo", type=Path)
    args = parser.parse_args()
    report = load_report(args.ticker, args.out, args.refresh)
    print(report_markdown(report))
    if args.check_memo:
        bad = unsupported_numbers(args.check_memo.read_text(encoding="utf-8-sig"), report)
        print("Unsupported memo numbers: " + json.dumps(bad))
        if bad:
            raise SystemExit(1)


if __name__ == "__main__":
    main()

