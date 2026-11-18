"""Scholarship fund research model; deterministic, offline, standard-library only.

All rates and weights inside the model are decimals. Asset order is checked.
This is an estimate comparison, not a backtest or an approved client allocation.
"""
from dataclasses import asdict, dataclass, replace
from datetime import date, datetime, timezone
from pathlib import Path
import hashlib
import json
import math

from portfolio import (equal_weights, estimate_from_csv, expected_return,
                       inverse_volatility_weights, portfolio_volatility)

ROOT = Path(__file__).resolve().parent
NAMES = ("SGOV", "SCHR", "VTC", "ACWI")
REFERENCE = (0.75, 0.0, 0.0, 0.25)  # Lab 15 proposal, NOT actual client holdings.
BOUNDARY = "2026-09-30"
TOL = 1e-12


@dataclass(frozen=True)
class Settings:
    objective: float = 0.055        # 2.5% assumed inflation + 3% real objective.
    reserve_minimum: float = 0.03   # $300,000 / $10 million.
    annual_cost_bps: float = 25.0   # Illustrative advisory/operating drag, not ETF fees.
    trading_cost_bps: float = 10.0  # Per dollar of one-way turnover, illustrative.
    turnover_limit: float = 0.25
    last_36: bool = False
    equity_change_pp: float = 0.0   # Percentage POINTS added to ACWI's annual mean.

    def validate(self):
        numbers = (self.objective, self.reserve_minimum, self.annual_cost_bps,
                   self.trading_cost_bps, self.turnover_limit, self.equity_change_pp)
        if not all(math.isfinite(x) for x in numbers):
            raise ValueError("Inputs must be finite numbers.")
        if not 0 <= self.objective <= 1 or not 0 <= self.reserve_minimum <= 1:
            raise ValueError("Objective and reserve must be between 0% and 100%.")
        if not 0 <= self.turnover_limit <= 1:
            raise ValueError("Turnover limit must be between 0% and 100%.")
        if self.annual_cost_bps < 0 or self.trading_cost_bps < 0:
            raise ValueError("Costs cannot be negative.")
        if not -100 <= self.equity_change_pp <= 100:
            raise ValueError("Equity adjustment must be between -100 and 100 pp.")


def checked_weights(weights):
    weights = tuple(float(x) for x in weights)
    if len(weights) != len(NAMES):
        raise ValueError("Weights must follow SGOV, SCHR, VTC, ACWI order.")
    if not all(math.isfinite(x) and x >= 0 for x in weights):
        raise ValueError("Weights must be finite and long-only.")
    if not math.isclose(sum(weights), 1, abs_tol=TOL, rel_tol=0):
        raise ValueError("Weights must sum to one.")
    return weights


def turnover(weights):
    """One-way rebalance turnover relative to the illustrative Lab 15 proposal."""
    return 0.5 * sum(abs(w - old) for w, old in zip(weights, REFERENCE, strict=True))


def signal_record(path=None):
    """Read the archived, student-checked vintage summary; never use a later vintage."""
    path = path or ROOT / "data" / "signal-record.json"
    record = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    if record["series"] != "FEDFUNDS" or record["units"] != "percent":
        raise ValueError("Signal must be FEDFUNDS in percent.")
    boundary = date.fromisoformat(BOUNDARY)
    vintage = date.fromisoformat(record["vintage_date"])
    measured = date.fromisoformat(record["measurement_month"])
    if vintage != boundary or measured > vintage:
        raise ValueError("Signal must match the decision-date vintage, not a later release.")
    value = float(record["value"])
    if not math.isfinite(value) or not 0 <= value <= 100:
        raise ValueError("Signal must contain a finite percentage rate.")
    if record["evidence_kind"] != "student_checked_lab17_transcription":
        raise ValueError("Unrecognized evidence type; review the data card before using it.")
    return record


def estimates(settings):
    settings.validate()
    with (ROOT / "data" / "prices.csv").open(encoding="utf-8-sig", newline="") as source:
        result = estimate_from_csv(source, settings.last_36)
    if tuple(result["names"]) != NAMES:
        raise ValueError("Price columns must be SGOV, SCHR, VTC, ACWI, in that order.")
    if result["end"] != BOUNDARY:
        raise ValueError("Unexpected price boundary; review the data card before changing it.")
    signal = signal_record()
    result["historical_returns"] = list(result["returns"])
    # Explicit heuristic: do not assume future bill returns exceed this known policy-rate proxy.
    # FEDFUNDS is NOT an ETF return or a proven predictor. Evidence limitations block live use.
    result["returns"][0] = min(result["returns"][0], signal["value"] / 100)
    result["returns"][3] += settings.equity_change_pp / 100
    result["signal"] = signal
    return result


def evaluate(label, weights, inputs, settings):
    """Calculate the decision numbers and explicitly separate measured rules from gaps."""
    weights = checked_weights(weights)
    gross = expected_return(weights, inputs["returns"])
    traded = turnover(weights)
    cost = settings.annual_cost_bps / 10000 + traded * settings.trading_cost_bps / 10000
    net = gross - cost
    risk = portfolio_volatility(weights, inputs["covariance"])
    measured = {
        "Fully invested, long-only; no direct leverage/derivatives": True,
        "Estimated annual net return meets objective": net >= settings.objective - TOL,
        "SGOV reserve meets minimum": weights[0] >= settings.reserve_minimum - TOL,
        "Illustrative one-way rebalance turnover within limit": traded <= settings.turnover_limit + TOL,
    }
    unresolved = [
        "Committee loss tolerance, risk limit and breach response are not approved.",
        "Five-day redemption capacity and reserve eligibility need operational verification.",
        "Diversified-fund concentration exemption and fund mandates need confirmation.",
        "Actual holdings, cumulative annual turnover and rebalance authorization are unknown.",
        "Historical signal uses a prior student-checked summary; raw vintage is not bundled.",
        "Annual arithmetic estimates do not demonstrate rolling five-year CPI + 3% net returns.",
    ]
    return {
        "name": label, "weights": dict(zip(NAMES, weights, strict=True)),
        "gross_return": gross, "cost_drag": cost, "net_return": net,
        "volatility": risk, "reserve": weights[0], "turnover": traded,
        "modeled_rules": measured,
        "modeled_verdict": "PASS" if all(measured.values()) else "FAIL",
        "failed_rules": [rule for rule, passed in measured.items() if not passed],
        "full_mandate_verdict": "FAIL — not cleared for live use",
        "unresolved_rules": unresolved,
    }


def allocations(slots=4, remaining=20):
    """Every allocation on the 5 percentage-point grid, totaling exactly 100%."""
    if slots == 1:
        yield (remaining / 20,)
    else:
        for units in range(remaining + 1):
            for rest in allocations(slots - 1, remaining - units):
                yield (units / 20,) + rest


def solve(settings=None):
    settings = settings or Settings()
    inputs = estimates(settings)
    candidates = [
        evaluate("Equal weight", equal_weights(4), inputs, settings),
        evaluate("Inverse volatility", inverse_volatility_weights(inputs["volatilities"]), inputs, settings),
        evaluate("60% ACWI / 40% VTC benchmark", (0, 0, 0.4, 0.6), inputs, settings),
    ]
    best = None
    for weights in allocations():
        if weights[0] < settings.reserve_minimum - TOL or turnover(weights) > settings.turnover_limit + TOL:
            continue
        candidate = evaluate("Constrained portfolio", weights, inputs, settings)
        if candidate["modeled_verdict"] == "PASS" and (best is None or candidate["volatility"] < best["volatility"]):
            best = candidate
    if best:
        candidates.append(best)
    return {
        "settings": asdict(settings), "inputs": inputs,
        "portfolios": candidates, "selected": best,
        "decision": "PILOT ON PAPER; 0% live allocation" if best else "REJECT this scenario; no feasible grid allocation",
        "stop_condition": "Stop the paper candidate when its estimated net return or reserve fails, turnover requires unapproved action, or source timing is unverifiable. Do not deploy live before all mandate gaps are resolved.",
    }


def stress_suite():
    """Predefined engineering scenarios, separate from the student's locked experiment."""
    base = Settings()
    baseline = solve(base)
    selected = baseline["selected"]
    weights = tuple(selected["weights"][name] for name in NAMES) if selected else None
    scenarios = [
        ("Base", base),
        ("ACWI estimate -2 percentage points", replace(base, equity_change_pp=-2)),
        ("Last 36 monthly returns", replace(base, last_36=True)),
        ("Annual additional cost 100 bps", replace(base, annual_cost_bps=100)),
        ("Reserve minimum 80%", replace(base, reserve_minimum=0.8)),
        ("Combined: equity -2 pp; cost 100 bps; reserve 80%", replace(base, equity_change_pp=-2, annual_cost_bps=100, reserve_minimum=0.8)),
    ]
    results = []
    for label, settings in scenarios:
        result = solve(settings)
        fixed = evaluate("Unchanged base weights", weights, result["inputs"], settings) if weights else None
        results.append({"scenario": label, "settings": asdict(settings), "fixed_base_weights": fixed,
                        "reoptimized": result["selected"], "decision": result["decision"]})
    return results


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def export_result(result):
    """Stamp the actual scenario and hash its calculation code and bundled inputs.

    Hashes identify the local files; they do not claim a GitHub commit or establish
    that the student's prediction preceded the run.
    """
    paths = ("app.py", "model.py", "portfolio.py", "requirements.txt",
             "data/prices.csv", "data/price-sources.json",
             "data/signal-record.json", "data/signal-source.json")
    return {
        **result,
        "exported_at_utc": datetime.now(timezone.utc).isoformat(),
        "analysis_boundary": BOUNDARY,
        "analysis_type": "Reconstruction using later-downloaded prices; NOT a point-in-time return backtest.",
        "sha256": {name: file_hash(ROOT / name) for name in paths},
    }


def package_results():
    result = solve()
    result["stress_runs"] = stress_suite()
    result["run_date"] = date.today().isoformat()
    return export_result(result)


def percent(value):
    return f"{100 * value:.2f}%"


def weight_text(portfolio):
    return "; ".join(f"{name} {100 * w:.1f}%" for name, w in portfolio["weights"].items()) if portfolio else "No feasible grid allocation"


def render_report(result):
    lines = ["# Executed results", "", f"Run date: {result['run_date']}. Fixed input boundary: {BOUNDARY}.",
             "", result["analysis_type"], "", f"**{result['decision']}**", "",
             "Annual target 5.50% net; SGOV reserve minimum 3%; additional annual cost 25 bps; trading cost 10 bps × one-way turnover. Turnover is measured from the illustrative Lab 15 proposal (75% SGOV / 25% ACWI), not actual holdings.", "",
             "| Portfolio | Weights | Net estimate | Volatility | Reserve | Turnover | Modeled rules | Full mandate |",
             "|---|---|---:|---:|---:|---:|---|---|"]
    for p in result["portfolios"]:
        lines.append(f"| {p['name']} | {weight_text(p)} | {percent(p['net_return'])} | {percent(p['volatility'])} | {percent(p['reserve'])} | {percent(p['turnover'])} | {p['modeled_verdict']} | FAIL: unresolved |")
    lines += ["", "Full-mandate FAIL means compliance has not been established; it is not a prediction of a future loss.", ""]
    for p in result["portfolios"]:
        lines.append(f"- {p['name']}: " + (("FAIL — " + "; ".join(p['failed_rules'])) if p['failed_rules'] else "passes the modeled numeric rules; unresolved rules still block live use."))
    lines += ["", "## Stress runs", "", "Fixed weights show whether the original candidate survives; reoptimized results show a different possible allocation. These are engineering tests, not the student's locked changed-input record.", "",
              "| Scenario | Fixed net | Fixed rules | Reoptimized weights | Reoptimized net | Reoptimized risk |",
              "|---|---:|---|---|---:|---:|"]
    for s in result["stress_runs"]:
        fixed, new = s["fixed_base_weights"], s["reoptimized"]
        lines.append(f"| {s['scenario']} | {percent(fixed['net_return']) if fixed else 'N/A'} | {fixed['modeled_verdict'] if fixed else 'N/A'} | {weight_text(new)} | {percent(new['net_return']) if new else 'N/A'} | {percent(new['volatility']) if new else 'N/A'} |")
    lines += ["", "## Unresolved mandate and evidence", ""]
    lines += [f"- {x}" for x in result['portfolios'][0]['unresolved_rules']]
    lines += ["", "Signal: August 2026 FEDFUNDS 3.63%, recorded as available in the September 30 vintage by the student's prior Lab 17 check. Raw historical CSV retrieval failed on November 17; no fresh source validation is claimed. The SGOV annual estimate is capped at this policy-rate proxy. This is a modeling heuristic, not a Treasury yield observation.", "", result['stop_condition'], "", "Exact unrounded results and input/code hashes: [results.json](results.json)."]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    result = package_results()
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    (out / "results.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    (out / "results.md").write_text(render_report(result), encoding="utf-8")
    print(render_report(result))
