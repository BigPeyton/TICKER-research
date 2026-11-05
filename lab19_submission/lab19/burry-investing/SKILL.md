---
name: burry-investing
description: Apply the FIN 439 Michael Burry cash-flow and liabilities checks to shared SEC facts and write a numerically supported skeptical business memo.
---

# Burry investing

Use `C:/Users/Peyto/.codex/lab19/panel.py TICKER` to obtain the shared five-year SEC report. In a relocated submission, run panel.py from the lab19 folder. `burry_checks` implements operating cash flow >= net income every year and latest liabilities/equity <= 2.0. Use unrounded values; missing inputs or nonpositive denominator mean not known. Use only permitted SEC tags and retain their filing provenance.

Read the printed report before writing TICKER_burry_memo.md beside panel.py. Emphasize cash backing of earnings and balance-sheet risk, following [FAskills Burry](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/michael_burry.md). The lab's limited screen overrides the source's demands for estimates, scores, price targets, holdings and predictions. Do not equate an adverse ratio with accounting fraud or infer footnote findings from aggregate data.

Label the memo an AI simulation, not Burry's actual opinion. Choose **Verdict: own the business**, **Verdict: watch it**, or **Verdict: pass** with reasons; code must not choose the judgment. Use only printed numbers with matching units and precision. Preserve missing facts. Explain limitations and additional evidence needed. Validate using panel.unsupported_numbers and manually review metric attribution. Save a matching .meta.json containing the report facts_signature. Do not invent the student's trust decision or classroom participation.
