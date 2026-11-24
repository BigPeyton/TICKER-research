I used OpenAI Codex to help adapt my earlier lab code, build and revise the app, check calculations and primary sources, and draft documentation and recording guides. The analysis and decision are mine to review, explain, and defend.

This is an educational project for a fictional university scholarship fund, not investment advice.

# Scholarship fund — Project 2 / Lab 20

**Current status — November 23, 2026, revised after readiness review.** The app now enforces a proposed 6% annualized-volatility ceiling and verifies a dated, archived Federal Reserve policy announcement. Default paper allocation is still 75% SGOV / 25% ACWI, now **5.57% net and 3.81% volatility**. The original student experiment remains unchanged on its original version (5.51%→5.83%); the revised model's cost scenario is 5.57%→5.89%. See the [revision record](docs/readiness-revision.md), [risk policy](docs/risk-policy.md) and [data card](docs/data-card.md). Luke's run and Lab 20 are completed per Peyton. **Post-submission update, November 24:** all three videos and transcripts were submitted in Brightspace on November 23 at 11:58 p.m., receipt 24002684. See the [final manifest](docs/submission-manifest.md) for video links, transcripts and timestamps, and the [dated cleanup record](docs/post-submission-cleanup-20261124.md). The application and original experiment evidence are unchanged.

**Use this copy:** [current project folder](https://github.com/BigPeyton/TICKER-research/tree/main/FIN439-Project2-ready-20261117/ready-to-upload/project2). After extracting the repository ZIP, open `FIN439-Project2-ready-20261117/ready-to-upload/project2`. Older copies elsewhere in the repository are historical; the [submission manifest](docs/submission-manifest.md) directs graders to this copy.

**Decision: pilot on paper; allocate 0% live until the client risk-policy approval and operational checks are resolved.** The default hypothetical portfolio is 75% SGOV / 25% ACWI. Its estimated annual net return is **5.57%**, annualized volatility **3.81%**, and SGOV reserve **75%**. It passes the modeled numeric rules but **fails full-mandate clearance**. See the [executed results](outputs/results.md), [memo](docs/decision-memo.md), and [Lab 20 record](docs/lab20-readiness.md).

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

The completed Project 2 locked record is the [November 23 student-operated experiment](docs/student-experiment.md). Its original prediction remains in an immutable pre-run commit. The earlier [assistant-operated turnover experiment](docs/locked-experiment.md) and engineering stresses remain supporting evidence; they are not represented as AI-off student runs.

### If installation cannot reach PyPI

If setup reports `Failed to resolve pypi.org`, `getaddrinfo failed`, or socket access denied, the dependency download failed before the app started. Check the machine's internet/DNS and any sandbox or firewall restrictions, then rerun the README command in an environment allowed to reach PyPI. Changing the portfolio cannot repair this setup problem. `python run.py --report` works offline but is not the interactive app and does not establish a successful app cold run.

Peyton confirmed that the partner-run task and Lab 20 check-in were completed. The historical note preserves the original DNS failure and assisted app check; no new clean-install log is invented. Future users should follow the startup instructions above and record any first failure. The offline fallback is not the web app.

## Produce or check the saved result without installing anything

```powershell
python run.py --report
python run.py --check
```

The first command regenerates `outputs/results.md` and `outputs/results.json`; these are readable on GitHub without running anything. The second runs the 16 standard-library model/data checks. After app setup, the optional integration check is:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

On macOS/Linux replace `.venv\Scripts\python.exe` with `.venv/bin/python`. This runs all 18 checks, including the Streamlit controls and timestamped scenario-export evidence. Tests are development validation, not Luke's independent cold run.

Independent arithmetic/archive audit (no installation or network needed):

```powershell
python tools/audit_model.py
```

This reconciles the 244 monthly prices against bundled daily responses, independently recomputes portfolio moments, and checks the selected weights against all 1,771 grid allocations for the existing stress cases. The current signal checker verifies the archived dated policy sources. This does not validate the return-cap forecast heuristic.

## Mandate and default assumptions

| Item | Definition |
|---|---|
| Client and horizon | Fictional $10 million university scholarship fund; ten years |
| Objective | CPI + 3% net annually over rolling five-year periods; **2.5% assumed inflation** makes the modeled annual target 5.50% |
| Payout and reserve | $75,000 quarterly; twelve months = $300,000 = **3%**; only SGOV is treated as reserve-eligible in this model |
| Universe, fixed column order | SGOV, SCHR, VTC, ACWI |
| Benchmark | 60% ACWI / 40% VTC; a comparison, not a mandatory allocation |
| Baselines | Equal weight; inverse standalone volatility |
| Selection | Minimum estimated annualized volatility on a **5-percentage-point grid**, subject to return, reserve, modeled turnover and volatility limits |
| Proposed paper risk limit | **Annualized volatility ≤6%**, enforced in selection; breach withdraws the candidate and requires review. This is a new research assumption; client loss-policy approval remains unresolved. See [risk policy](docs/risk-policy.md). |
| Trading constraints | Fully invested, long-only; no direct borrowing or derivatives; annual rebalance; turnover above 25% requires approval |
| Turnover reference | Lab 15's proposed 75% SGOV / 25% ACWI, **not actual holdings**; a single one-way rebalance estimate, not cumulative annual turnover |
| Additional costs | 25 bps annual advisory/operating drag, plus 10 bps times one-way turnover; illustrative, not a verified fee quote |
| Liquidity/concentration | At least 90% redeemable within five business days; 8% company limit with cash, Treasury and diversified-fund exemptions; operational confirmation pending |

Historical returns are arithmetic monthly means multiplied by twelve; covariance is the monthly sample covariance multiplied by twelve. The net estimate charges the proposed rebalance once, so it is a first-year estimate. Fund expenses already embedded in adjusted returns are not charged again. None of these calculations establishes the rolling five-year real-return objective or a maximum-loss guarantee.

## Data and signal

The bundled prices cover September 30, 2021 through September 30, 2026: 61 prices / 60 monthly returns. They were downloaded October 22, 2026, so **this is not a historical point-in-time return backtest**.

The current point-in-time signal is the **3.75% lower bound of the FOMC target range**, published September 16 at 2 p.m. EDT and effective September 17, both before the September 30 cutoff. The dated official statement and implementation note are bundled with URLs, hashes and extraction checks. The code fails on unsupported timing, values or damaged source evidence. This policy target replaces the earlier monthly FEDFUNDS transcription; it is a different measure.

The SGOV estimate is capped at that lower bound. This cap is nonbinding in the 60-return default window and binding in the 36-return scenario. It remains a research heuristic, not a Treasury yield or validated ETF forecast. See the [data card](docs/data-card.md).

The original [student experiment](docs/student-experiment.md) and its exports are preserved byte for byte. Its 5.51% / 5.83% values belong to the original 3.63% signal model. Do not replace those historical results with the revised model's 5.57% / 5.89% values.

## Package map

- [Executed output](outputs/results.md) and [machine-readable results](outputs/results.json)
- [Decision memo](docs/decision-memo.md)
- [Validation and AI use, including the full student locked record](docs/validation-and-ai-use.md)
- [Student experiment and original prediction evidence](docs/student-experiment.md)
- [Lab 20 partner cold-run record and checkout](docs/lab20-readiness.md)
- [Video preparation](docs/video-plan.md) and [submission manifest](docs/submission-manifest.md)
- Source: `app.py` (interface), `model.py` (decision and stress engine), `portfolio.py` (reused Lab 14/15 calculations), `run.py` (launcher)

Course requirements: [Lab 20](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-13/lab-20-project2-readiness.md), [Project 2](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md), [checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md). The Brightspace assignment header controls the deadline.
