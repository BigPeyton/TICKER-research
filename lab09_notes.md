# Lab 09: ABG pro-forma build

Status: I ran the normal model, the deliberate failure test,
and the normal model again in VS Code. The outputs confirmed the expected results.

## Question

What are five years of a company's statements worth, built from assumptions
you can defend, and how do you know the statements are right?

## Source and scope

The model uses the assumptions and FY2025 opening balances supplied in the
[Lab 09 instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-05/lab-09-proforma-build.md),
accessed September 24, 2026. Financial amounts are USD millions, shares are in
millions, and the resulting per-share value is USD. These are training inputs;
this work does not independently authenticate their historical/guidance labels.
The depreciation, inventory-days, and floor-plan ratios retain the exact
arithmetic supplied by the lab. Calculations retain full precision; tables round
only for display. No external Python packages are needed.

## Run and verify

I ran `python proforma.py` in my course folder and shared the output for checking.
All five years passed the balance-sheet and minimum-cash checks. The results below
matched the lab's reference values.

| Measure (USD millions except per-share value) | FY2026E | FY2030E |
|---|---:|---:|
| Revenue | 18,323.0 | 19,678.3 |
| Operating income | 844.2 | 971.4 |
| Net income | 413.6 | 527.5 |
| FCFE | 211.4 | 342.3 |
| Ending cash | 101.8 | 719.8 |
| Assets minus liabilities minus equity | 0.0 | 0.0 |

Equity value is $5,237.34 million; value per share is $291.75.
The present value of the terminal value is 79.76% of total equity value.
All provided reference results match at their stated precision.

I then ran `python proforma.py --break-cash`, which deliberately replaces FY2026
cash with 40.4. The model stopped before valuation with:

```text
ValueError: FY2026E: gap -61.4; balance sheet does not balance
```

I reran `python proforma.py` without the flag. All five checks passed again and
the value returned to $291.75 per share. The failure flag changes cash only during
that run, so no permanent code change needed to be undone.

## Simulated partner exercise and my contribution

The lab was assigned to be completed outside class, so I used an
AI-assisted self-check to simulate the technical swap-and-break exercise.
AI helped compare my results with the reference values. The model reproduced the
reference results, rejected the deliberately incorrect FY2026 cash balance with
a -$61.4 million gap, and passed again without the deliberate error. No human
partner swap or discussion occurred.

Additional checks confirmed that raising minimum cash to 200 triggers a
revolver draw followed by repayment, and raising it to 2,000 causes rejection
when the 850 revolver limit cannot fund the minimum. These temporary test changes
did not change the saved base-case inputs.

## Explanation and reflection

The three operating judgments highlighted in the assumption table are 1.8%
annual revenue growth, a 17.05% gross margin, and SG&A falling from 66.5% to 64.5%
of gross profit. They determine the revenue base, gross profit earned on that
revenue, and how much gross profit survives operating expenses. The lower SG&A
ratio assumes improved operating efficiency. Matching the reference answer shows
that the model implements the assumptions correctly; it does not prove that
those assumptions will occur.

Cash is computed last because it is the result of opening cash, operating cash
generation, investment, debt repayment, buybacks, and any revolver activity.
It is not an independently chosen figure used to force the balance sheet to work.

The -61.4 gap means assets are understated by 61.4 relative to liabilities and
equity. In this deliberate test, that amount is exactly the omitted increase in
cash: 101.8 minus 40.4. A balance gap alone would not prove the cause in an
unfamiliar model; the controlled edit makes the diagnosis possible here.

Floor-plan loans finance vehicle inventory through manufacturers' finance arms
or banks. The lab links their closing balance to inventory, charges interest on
their opening balance, and includes their changes in operating cash flow for
this model. Removing the financing while retaining the inventory means the
company must find cash elsewhere. The lab refers to approximately negative
$1.1 billion in the video; this work has not reproduced that specific video
scenario, which depends on exactly how the financing is removed.

The terminal calculation adds back the final year's debt repayment before
growing FCFE, as instructed. This assumes that the annual 150 repayment does
not continue in perpetuity. A 2.5% terminal growth rate below the 10% cost of
equity makes the perpetuity formula finite, but does not establish that the
long-run forecast is economically realistic. With 79.76% of value beyond 2030,
the long-run assumptions strongly influence the answer.
