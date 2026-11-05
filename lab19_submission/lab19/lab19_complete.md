# Lab 19 — Buffett, Cathie Wood and Michael Burry

## Assignment adaptation

Peyton reported the professor's change from Graham to Wood and authorized choosing Wood's rules. On November 5, the week-11 README, lab, handout, slides and prework still specified Graham. Our Wood thresholds are custom classroom choices, not professor-published requirements or official Wood/ARK rules.

Sources: [course lab](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-19-legend-panel.md), [Wood perspective](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/cathie_wood.md), [Burry perspective](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md). FAskills was read, not installed.

## Run

`python -m streamlit run lab19/panel_app.py`

Try COST, AAPL and JPM. Toggle Wood's revenue CAGR threshold between 10% and 5%. The app retains SEC refresh, facts, charts, missing-data handling, provenance, memo editing and downloads, and adds side-by-side checks, verdicts and memos. Each editor checks unsupported numbers. Numeric membership cannot prove metric attribution or qualitative claims. New tickers need AI-written memos; the app does not generate automatic judgments. Original Lab 18 files are preserved.

## Custom Wood rules and rationale

- Revenue CAGR >= 10%: a deliberate stronger-growth hurdle; probe at 5%.
- Latest R&D/revenue >= 5%: material research spending relative to sales.
- R&D/revenue greater in the final than initial year: greater relative research commitment, not necessarily monotonic growth.

CAGR uses (last revenue / first revenue)^(1 / elapsed years) - 1; elapsed years is fiscal-end days / 365.25. Five observations span approximately four years. Require all five revenues positive and present. R&D uses only ResearchAndDevelopmentExpense annual 10-K USD facts, latest filing per fiscal end. Require complete intensity observations for the first-to-last test. Missing inputs and invalid denominators stay missing/unknown. Comparisons use full precision.

These proxies do not establish disruptive innovation, successful R&D, technology moats or future returns. Default retained: 10% to distinguish stronger sustained growth; 5% is a sensitivity probe. This implementation choice is not the student's personal trust decision.

## ACWI holding

Apple (AAPL): largest holding in the downloaded official iShares CSV dated November 4, 2026, at 5.02%, ahead of NVIDIA at 4.50%. An earlier browser snapshot dated November 3 also ranked Apple first. Evidence: references/ACWI_holdings.csv. [Official source](https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf/latest-holdings.csv). Apple has eligible 10-K facts; no substitute needed.

## Results

| Company | Buffett | Wood at 10% growth | Burry |
|---|---|---|---|
| COST | All three pass | Growth fails; both R&D checks unknown | Both pass |
| AAPL | All three pass | Growth fails; both R&D checks pass | Both fail |
| JPM | ROE fails; owner-earnings checks unknown | Growth passes; both R&D checks unknown | Both fail |

Costco current ratios (1.02, 1.07, 0.97, 1.03, 1.06) and liabilities/equity (2.11, 1.75, 1.96, 1.64, 1.49) match the posted known answers. Graham's original checks/probe were replaced following the professor's change.

Costco CAGR is 7.50%: fails at 10%, passes at 5%. Both R&D checks stay unknown. Wood's verdict remains **watch it** because relaxing a rule adds no innovation evidence.

Apple CAGR is 4.97%, failing both thresholds. R&D intensity rises from 6.66% to 9.56%; both R&D checks pass. Buffett's provisional business verdict is **own the business**; Wood and Burry say **watch it**. Burry flags 2025 cash flow of 111,482 below net income of 112,010 and latest liabilities/equity of 2.61 above 2.0. Monetary values are USD millions. These memos assess business quality, not price.

JPM CAGR is 10.66%. Missing capital spending, owner earnings, current balance-sheet inputs and R&D stay missing. General industrial-style screens have limitations for banks.

## Verification

`python lab19/test_panel.py`: seven tests passed, covering known answers, Apple failure year, missing/invalid inputs, annual/latest R&D extraction, threshold probes, all twelve memos, and app interactions. Each memo editor rejected an inserted 40.0%. All three packaged skills passed validation; Wood and Burry are installed locally.

## Student verification and discussion

Peyton confirmed the COST results, Wood threshold probe at 10% versus 5%, and restoration to 10%. Peyton also confirmed the AAPL checks and verdicts in the app.

Peyton provided a line-by-line explanation of wood_checks, including result's missing-input handling, and reported the partner explanation complete. Clarification: CAGR is annualized endpoint growth, not a requirement for growth to exceed the threshold in every individual year.

Peyton reported completing both roles in the Apple bull/bear discussion. The submitted discussion mentioned brand, loyalty, iPhone dependence and valuation; these are not established by this panel. The assistant supplied the following evidence-based revision for review:

- Bull: Apple passes all three Buffett checks, with positive owner earnings that increased from $111,443 million to $136,056 million. R&D spending rose from 6.66% to 9.56% of revenue, passing both innovation-spending checks.
- Bear: Apple's 4.97% revenue CAGR fails the 10% growth threshold. Both Burry checks fail because operating cash flow fell below net income in 2025 and latest liabilities/equity was 2.61, above 2.0.

## Personal trust decision

Peyton's response:

> I would only use this panel to screen companies for Project 2 if the financial data is accurate, missing information is clearly identified, and the results are reviewed before making investment decisions.

## Remaining student work

Peyton confirmed the final partner discussion complete. All written learning answers, the trust decision, the final reflection and reported partner activities are complete. Remaining: upload and submit GitHub links in Brightspace. No Lab 19 upload or submission performed.

## Panel-of-agents learning answers

Peyton's responses:

1. A panel of AI agents is a group of AI systems that analyze the same information from different perspectives to help make a more informed decision.
2. Three investor personas can disagree because they have different investment strategies and priorities. For example, Buffett focuses on profitability and long-term value, Wood focuses on growth and innovation, and Burry focuses on financial strength and risk.

Implementation clarification: this app presents three skill-guided perspectives using shared Python calculations and saved AI-written memos. It does not run three independent AI systems live. Different priorities and screening rules can produce different conclusions from identical facts.

## Final reflection

Peyton's responses:

1. Wood and Burry agreed on “watch it,” while Buffett said “own the business” because Apple passed all three profitability and owner-earnings checks. Wood’s two R&D checks passed, but revenue growth failed. Burry’s checks both failed: operating cash flow fell below net income in 2025, and liabilities were 2.61 times equity, above the 2.0 limit. All three still called for more research.
2. Lowering Wood’s growth threshold from 10% to 5% did not change Apple’s failed growth check or “watch it” verdict because its revenue CAGR was only 4.97%. This taught me to examine the exact numbers and assumptions behind a screen instead of rounding results or trusting the verdict alone.

## Files to upload

Keep the lab19 folder structure: panel.py, panel_app.py, requirements.txt, test_panel.py, this write-up; buffett-investing/, wood-investing/, burry-investing/; COST/AAPL/JPM *_panel.json and *_panel.md; *_buffett_memo.md, *_burry_memo.md, *_wood_t10_memo.md, *_wood_t5_memo.md and matching .meta.json files; references/ACWI_holdings.csv.

Skip data/ and __pycache__/; first run downloads SEC data. Legacy *_memo.md files, historical lab19_notes.md and save_reviewed_memos.py are local build artifacts and not required. Source-reference copies are optional. The packaged Buffett script under buffett-investing/scripts/ is required by panel.py.
