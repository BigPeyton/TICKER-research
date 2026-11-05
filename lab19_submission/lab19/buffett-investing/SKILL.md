---
name: buffett-investing
description: Analyze public-company business quality using five years of SEC EDGAR facts, compute Buffett-style ROE and owner-earnings checks, and write a numerically checked memo. Use for the FIN 439 Buffett lab or this SEC-based business screen.
---

# Buffett investing

Run `scripts/buffett.py TICKER --out OUTPUT_DIRECTORY` using this skill's script path. Read the generated TICKER_report.md before writing the memo. SEC User-Agent: Peyton Dow peytonpdow@gmail.com. Use --refresh for new downloads; cached downloads retain original timestamps.

Code owns all numbers: 10-K only, last five annual fiscal periods, latest filing for a repeated period within each permitted tag, preferred tag before fallback. Annual flows accept calendar and 52/53-week years. Use year-end equity. Preserve not found for missing facts, not known for invalid ratios or checks with missing inputs. Do not substitute unapproved tags or estimates.

Owner earnings is the lab's proxy: operating cash flow minus capital spending, not an estimate of maintenance capital. Checks: ROE >= 15% every year, positive owner earnings every year, growth first to last. Keep the lab's 15% threshold for comparability; it is a screening choice, not a universal law.

Write TICKER_memo.md in the output directory, from a Buffett-inspired business-owner perspective, labelled AI simulation, not Buffett's actual opinion. Choose own the business, watch it, or pass, with reasons and limitations. Use only report numbers, preserving units and precision. No invented scores, forecasts, growth rates, price targets, valuation, holdings claims, or unsupported assertions about management or moats. Missing owner earnings means the memo cannot judge owner earnings from these facts. The model makes the judgment, never a verdict hardcoded in Python.

Validate with `scripts/buffett.py TICKER --out OUTPUT_DIRECTORY --check-memo OUTPUT_DIRECTORY/TICKER_memo.md`. Numeric membership is not proof of metric attribution or qualitative truth; review these yourself. Save TICKER_memo.meta.json containing the report's facts_signature so the app warns about changed facts. Do not invent the student's trust decision or claim partner activities occurred.

Companion app: `python -m streamlit run lab18/buffett_app.py` from the workspace. For another ticker, use this skill to write its memo; the app does not call a paid model API or present a template as fresh AI judgment.

Sources: [lab rules](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-18-legend-investor-as-skill.md), [Buffett philosophy](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md), [SEC API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces). Read FAskills only; never install it or use its paid services. Lab rules override its price and prediction requests.

