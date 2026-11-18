# Lab 13 — Portfolio Mandate Defense

**Case:** Meridian Foundation Reserve (fictional), $100 million.

**Question:** Which portfolios does the mandate permit, and what must the CIO answer before optimization?

## Statement types and investment policy mapping

| Statement | Type | Reason and IPS role |
|---|---|---|
| S1: Seven-year horizon; annual rebalancing | Hard constraint | Establishes the investment horizon and required rebalancing schedule. |
| S2: CPI + 4% annually, net of costs, over rolling five-year periods | Objective | Defines the desired real return, cost basis, and evaluation period; it is a target, not a guaranteed result. |
| S3: $0.75 million quarterly payouts; twelve months held in eligible reserves | Hard constraint | Sets the spending obligation and minimum reserve of $3 million, or 3% of assets. |
| S4: 60% global equity / 40% U.S. investment-grade bond benchmark | Preference | Specifies the performance reference; it does not explicitly require portfolio weights to equal 60/40. Within the five offered categories, preference is the closest fit. |
| S5: Long-only; no borrowing, shorts, or derivatives | Hard constraint | Limits permitted investment methods; the listed holdings contain no derivatives. |
| S6: No single issuer above 8% | Hard constraint | Limits company concentration; combine a company's stock and bonds and apply the stated exemptions. |
| S7: Annual turnover at most 25% without committee approval | Hard constraint | Sets a trading limit with an approval exception; testing needs trading history and approval information. |
| S8: At least 90% redeemable within five business days | Hard constraint | Sets an explicit portfolio liquidity threshold. |
| S9: No calendar-year loss greater than 10%, without a measure or breach rule | Unverifiable promise | A holdings snapshot cannot guarantee future losses; the risk definition and response to a breach need clarification. |
| S10: No listed preferences; pilot optimization goal unspecified | Missing | Sector, ESG, tax, and home-bias preferences are expressly absent; the missing decision is what the pilot should optimize. |

## Checker and validation

Code: [mandate.py](mandate.py). Standard library only; no installation or data downloads required.

Run in the folder containing the file:

```powershell
python mandate.py
```

Reserve minimum = 4 × $0.75 million ÷ $100 million × 100 = **3.0%**.

| Measured rule | A | B | C | D |
|---|---|---|---|---|
| Total weights | 100.0 pass | 100.0 pass | 100.0 pass | 100.0 pass |
| Lowest weight | 0.0 pass | 0.0 pass | 0.0 pass | 0.0 pass |
| Eligible reserve, minimum 3% | 14.0 pass | 1.0 FAIL | 2.0 FAIL | 100.0 pass |
| Liquid within five days, minimum 90% | 100.0 pass | 85.0 FAIL | 100.0 pass | 100.0 pass |
| Largest company, maximum 8% | 0.0 pass | 9.0 FAIL | 8.0 pass | 0.0 pass |
| Verdict | Passes every checkable rule | Fails 3 rules | Fails 1 rule | Passes every checkable rule |

All candidates print **requires CIO clarification** for the calendar-year loss rule. The code does not test it.

**Execution verified October 15, 2026:** Ran the normal checker, the negative-weight probe, and a final normal run. All values matched the tables above; the probe failed only A's long-only rule, and the final normal run confirmed the original inputs remained intact.

A's eligible reserve includes the 10-year Treasury because the assignment explicitly marks it reserve-eligible. B's Acme bonds and stock count together. C's 8% company weight is allowed because the limit is inclusive.

### Long-only probe

```powershell
python mandate.py --probe
python mandate.py
```

The probe temporarily sets A's Cash to -2 and global equity fund to 64. A then has total weight 100.0, lowest weight -2.0, reserve 10.0, liquid weight 100.0, and company exposure 0.0: **only long-only fails**. The option edits a copy; the original inputs stay unchanged, and the next normal run restores A's passing result.

### Required code quiz

Question posed to the student: If Acme bonds are 5% and Acme stock is 4%, what issuer weight is compared with the 8% limit, and does it pass?

Student answer: Answer before requesting the explanation. The relevant line is `companies[issuer] = companies.get(issuer, 0) + weights[name]`.

## Candidate D: attack the checker

D holds **100% cash and 0% in every other holding**. It passes all five implemented checks; no optimization was performed.

**Judgment:** The objection holds because an all-cash portfolio has no demonstrated basis for meeting CPI + 4% net of costs over rolling five-year periods. S2 is the deciding statement: passing liquidity and concentration checks does not establish that the return objective is achievable.

This does not claim cash must fail under every future interest-rate scenario. The case provides no return forecasts, so the reasonable objection is the lack of support for suitability.

**Skeptical-colleague self-review:** A colleague might argue that cash is liquid and avoids equity volatility. The response would cite S2 and ask how the all-cash choice supports the real-return target; S4 is a comparison benchmark, not an automatic rule that D violates. The lab permits playing both roles; no human exchange is claimed here.

## One question for the CIO

**Question:** When pursuing CPI + 4% conflicts with the stated 10% calendar-year loss limit, what precise risk definition and breach response should govern the pilot's optimization?

**Answer that changes the design:** If the CIO says the return target is primary and the 10% figure is a monitored risk threshold with a defined review process, the pilot can consider growth assets under that clarified risk policy. If the CIO instead requires an absolute loss guarantee, I would pause optimization and resolve feasibility and the return target before choosing a portfolio; the checker cannot establish that guarantee. This connects the ambiguity in S9 to the missing optimization priority in S10.

## Investment policy statement and reflection

An investment policy statement (IPS) documents an investor's objectives, constraints, responsibilities, and approach to monitoring the portfolio. It guides investment decisions and makes the reasons for those decisions explicit. Objectives describe the results sought; constraints restrict how they may be pursued. [CFA Institute, Introduction and Section 3](https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/position-paper/investment-policy-statement-institutional-investors.pdf).

The S1–S10 table above maps the case into an IPS: horizon and rebalancing, return objective, spending and liquidity, benchmark, permitted methods, concentration, trading governance, and unresolved risk and optimization terms.

**Reflection:** A portfolio can pass every implemented check and still be wrong because those checks establish only the measurable restrictions in the supplied holdings snapshot. They do not establish future returns, future losses, or compliance with turnover and rebalancing over time. D illustrates the gap between permissible holdings and a suitable investment plan.

The classification I would review most carefully is S4. A benchmark tells us how to compare performance; it is not necessarily a hard allocation rule. I classified it as a preference within the available categories and would not force a 60/40 allocation without an explicit instruction.

## After-lab Project 2 mandate — proposed client

This is for a fictional university scholarship fund, not a confirmed personal client choice.

- **Objective:** Preserve purchasing power while funding scholarships; target CPI + 3% annually net of costs over rolling five-year periods, with a ten-year horizon.
- **Hard constraints:** $10 million starting assets; $0.075 million quarterly payouts; maintain twelve months of payouts ($0.3 million, 3%) in cash or daily-liquid government securities; long-only, no borrowing or derivatives; at least 90% redeemable within five business days; maximum 8% per company with the same cash, Treasury, and diversified-fund exemptions; annual rebalancing; annual turnover above 25% requires committee approval.
- **One client question:** What temporary loss is the committee willing and able to tolerate while maintaining scholarship payments? The answer would change the risk budget and balance between growth assets and liquid reserves before optimization.
