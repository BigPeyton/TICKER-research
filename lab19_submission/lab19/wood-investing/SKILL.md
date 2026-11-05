---
name: wood-investing
description: Apply custom Cathie Wood-inspired growth and R&D screens to five years of SEC facts for FIN 439 and write a numerically checked innovation-focused memo.
---

# Cathie Wood-inspired investing

Run `python C:/Users/Peyto/.codex/lab19/panel.py TICKER`; for a relocated submission use its panel.py path. Read the printed report before writing. The professor's investor change supersedes the online Graham assignment. The student authorized choosing these rules; they are custom classroom proxies, not official Wood or ARK thresholds.

Checks in `wood_checks`: revenue CAGR >= 10%; latest R&D / revenue >= 5%; R&D / revenue greater in the final than initial year. CAGR uses elapsed fiscal-end days / 365.25 between five observations, approximately four years. Require all five revenue values positive and present; use ResearchAndDevelopmentExpense only for R&D, annual 10-K USD facts, latest filing per fiscal end. Require complete R&D intensity observations for its first-to-last check. Preserve missing data, invalid ratios and incomplete checks as not found/not known. Compare unrounded values.

Use `--growth-threshold 5` for the threshold probe. Retain 10% as the default to distinguish stronger sustained growth; 5% is a sensitivity comparison. R&D intensity measures spending, not successful innovation. Neither check establishes disruptive technology, market size, cost curves or future growth.

Adapt [FAskills Wood](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/cathie_wood.md): growth, innovation spending and evidence of technology adoption. Read it only; do not install FAskills. The lab's observed-facts rules override its predictions, price targets, probability weights and ARK holdings requests.

Write TICKER_wood_t10_memo.md and a separate TICKER_wood_t5_memo.md beside panel.py. Label each an AI simulation, not Wood's actual opinion. Choose **Verdict: own the business**, **Verdict: watch it**, or **Verdict: pass** using judgment; do not hardcode verdicts from pass counts. Use only printed numbers with correct units. Include the threshold and reason under each memo. A changed check need not change the overall verdict when other gaps remain. Validate with panel.unsupported_numbers, review metric attribution, and save each memo's .meta.json with facts_signature. Do not invent the user's trust decision or partner participation.
