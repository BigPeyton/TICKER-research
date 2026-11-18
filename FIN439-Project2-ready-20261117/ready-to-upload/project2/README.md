I used OpenAI Codex to help adapt my earlier lab code, build the web app, test calculations, and draft documentation. The analysis and decision are mine to review, explain, and defend.

This is an educational project for a fictional university scholarship fund, not investment advice.

# Scholarship fund — Project 2 / Lab 20

**Audited working copy, November 17, 2026 (EST).** Peyton previously confirmed the paper-only recommendation and AI-off code explanation. Luke's cold-run attempt and the prior experiment are documented, but independent startup and the required pre-run prediction commit remain unresolved. This revised copy still needs publication and student review. Final videos/transcripts are not recorded. See the [audit and remaining requirements](docs/project2-audit.md).

**Decision: pilot on paper; allocate 0% live until the missing risk policy and evidence checks are resolved.** The default hypothetical portfolio is 75% SGOV / 25% ACWI. Its estimated annual net return is **5.51%**, annualized volatility **3.81%**, and SGOV reserve **75%**. It passes the modeled numeric rules but **fails full-mandate clearance**. See the [executed results](outputs/results.md), [memo](docs/decision-memo.md), and [Lab 20 record](docs/lab20-readiness.md).

## Run the app

Prerequisite: Python **3.11–3.13** installed with its `venv` and `pip` modules; tested with **3.13.15 on Windows**. No API key is required. First setup needs internet to download Streamlit; afterward the application uses only bundled data.

1. Download this repository's ZIP from GitHub, extract it, and open a terminal **inside the `project2` folder containing this README and `run.py`**. Do not run inside the ZIP viewer. In Windows File Explorer, right-click the extracted folder and choose **Open in Terminal**.
2. Run this one command on Windows:

   ```powershell
   python run.py
   ```

   On macOS/Linux use `python3 run.py`. The launcher creates `.venv`, installs the pinned app dependency, and starts the web server. It may take several minutes on the first run.
3. When the terminal displays the local URL, open **http://127.0.0.1:8501**. Leave the terminal running. Stop it with **Ctrl+C**.

If Windows opens the Microsoft Store instead of Python, install Python from [python.org](https://www.python.org/downloads/) and enable **Add python.exe to PATH**, or use `py run.py` when the Python launcher is installed. If port 8501 is occupied, run `python run.py --server.port=8502` and open http://127.0.0.1:8502. If dependency setup fails, check the connection and rerun the same command; no market-data download is needed. Linux distributions that omit `venv` may require their `python3-venv` package.

**Move a control:** change any sidebar assumption; the allocation, return, risk, and verdict update. The rule panels explain every failure. Restore the defaults shown below to reproduce the saved report. The download button saves that scenario's exact results with a UTC export timestamp and calculation-code/input hashes. Preserve its unique filename and record the GitHub code commit separately; a timestamp or hash does not prove a prediction was committed before testing. A scenario can be infeasible; the app then shows no proposed allocation.

For the Lab 20 locked experiment, close AI, write and commit your own prediction **before moving the selected control**, then preserve both result downloads. The already-disclosed engineering stress scenarios are not that experiment.

### If installation cannot reach PyPI

If setup reports `Failed to resolve pypi.org`, `getaddrinfo failed`, or socket access denied, the dependency download failed before the app started. Check the machine's internet/DNS and any sandbox or firewall restrictions, then rerun the README command in an environment allowed to reach PyPI. Changing the portfolio cannot repair this setup problem. `python run.py --report` works offline but is not the interactive app and does not establish a successful app cold run.

For the independent rerun, use a fresh extracted copy, follow this README without coaching, and record the command, first failure or none, elapsed time, result location, and a control change. Preserve the original failed attempt as well.

## Produce or check the saved result without installing anything

```powershell
python run.py --report
python run.py --check
```

The first command regenerates `outputs/results.md` and `outputs/results.json`; these are readable on GitHub without running anything. The second runs the 14 standard-library model/data checks. After app setup, the optional integration check is:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

On macOS/Linux replace `.venv\Scripts\python.exe` with `.venv/bin/python`. This runs all 15 checks, including the Streamlit controls and timestamped scenario-export evidence. Tests are development validation, not Luke's independent cold run.

Independent arithmetic/archive audit (no installation or network needed):

```powershell
python tools/audit_model.py
```

This reconciles the 244 monthly prices against bundled daily responses, independently recomputes portfolio moments, and checks the selected weights against all 1,771 grid allocations for the existing stress cases. It does not authenticate the missing external signal vintage.

## Mandate and default assumptions

| Item | Definition |
|---|---|
| Client and horizon | Fictional $10 million university scholarship fund; ten years |
| Objective | CPI + 3% net annually over rolling five-year periods; **2.5% assumed inflation** makes the modeled annual target 5.50% |
| Payout and reserve | $75,000 quarterly; twelve months = $300,000 = **3%**; only SGOV is treated as reserve-eligible in this model |
| Universe, fixed column order | SGOV, SCHR, VTC, ACWI |
| Benchmark | 60% ACWI / 40% VTC; a comparison, not a mandatory allocation |
| Baselines | Equal weight; inverse standalone volatility |
| Selection | Minimum estimated annualized volatility on a **5-percentage-point grid**, subject to return, reserve, and modeled turnover limits |
| Risk limit | **Unresolved**: the committee has not supplied an acceptable loss, metric, limit, or breach response |
| Trading constraints | Fully invested, long-only; no direct borrowing or derivatives; annual rebalance; turnover above 25% requires approval |
| Turnover reference | Lab 15's proposed 75% SGOV / 25% ACWI, **not actual holdings**; a single one-way rebalance estimate, not cumulative annual turnover |
| Additional costs | 25 bps annual advisory/operating drag, plus 10 bps times one-way turnover; illustrative, not a verified fee quote |
| Liquidity/concentration | At least 90% redeemable within five business days; 8% company limit with cash, Treasury and diversified-fund exemptions; operational confirmation pending |

Historical returns are arithmetic monthly means multiplied by twelve; covariance is the monthly sample covariance multiplied by twelve. The net estimate charges the proposed rebalance once, so it is a first-year estimate. Fund expenses already embedded in adjusted returns are not charged again. None of these calculations establishes the rolling five-year real-return objective or a maximum-loss guarantee.

## Data and signal

The bundled prices cover September 30, 2021 through September 30, 2026: 61 prices / 60 monthly returns. They were downloaded October 22, 2026, so **this is not a historical point-in-time return backtest**.

The point-in-time signal is the prior Lab 17 record of August 2026 FEDFUNDS **3.63%**, available in the **September 30, 2026 vintage**. The model caps SGOV's historical annual mean at this rate as a disclosed heuristic. The policy rate is not an ETF return, and the heuristic is not a validated forecast. The raw historical CSV timed out during preparation; only the prior student-checked evidence is bundled. See the [data card](docs/data-card.md). This unresolved provenance issue blocks live clearance.

## Package map

- [Executed output](outputs/results.md) and [machine-readable results](outputs/results.json)
- [Decision memo](docs/decision-memo.md)
- [Validation, AI use, and Locked Changed-Input Record](docs/validation-and-ai-use.md)
- [Lab 20 partner cold-run record and checkout](docs/lab20-readiness.md)
- [Video preparation](docs/video-plan.md) and [submission manifest](docs/submission-manifest.md)
- Source: `app.py` (interface), `model.py` (decision and stress engine), `portfolio.py` (reused Lab 14/15 calculations), `run.py` (launcher)

Course requirements: [Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md), [Project 2](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md). The Brightspace assignment header controls the deadline.
