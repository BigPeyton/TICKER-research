# Luke's cold run

November 17, 2026 — Windows, Python 3.13.15.



| Item | Observation |
|---|---|
| Exact command | `python run.py`, from a fresh copy of the `project2` folder. Offline fallback: `python run.py --report`. |
| First error | `Failed to resolve 'pypi.org' ([Errno 11001] getaddrinfo failed)`. Streamlit installation failed, and the launcher exited with code 1. |
| Time to decision | The decision was visible near the top of the README; reading time was not measured. The offline report confirmed it 36 seconds after the first launch command. Later, the browser control test took 7 seconds from reading the loaded app to observing the changed verdict, excluding Peyton's startup time. |
| Result location | README, `outputs/results.md`, and the main decision heading and full-mandate alert at http://127.0.0.1:8503/. |
| Control changed | Minimum SGOV reserve: **3% to 80%**; other controls remained at defaults. |
| Resulting verdict | **REJECT this scenario; no feasible grid allocation.** Full mandate remained **FAIL — live use is not cleared**. |
| Rerun outcome | Retrying startup produced the same DNS error; the offline report worked. Peyton later supplied the running browser app, where the control change worked without a visible error. No source fix was made; his successful launch command and the running app's commit were not verified. |
| Restored defaults | Reserve returned to **3%**. The app showed **PILOT ON PAPER; 0% live allocation**, modeled rules **PASS**, estimated net return **5.51%**, and full mandate **FAIL**. |

The README clearly explained how to start the app and find the decision. The 80% reserve scenario was infeasible on the model's 5-percentage-point grid; this was a scenario rejection, not an application crash.
