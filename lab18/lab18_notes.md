# Lab 18 — Buffett investor skill
Prepared for Peyton Dow.

## Build and use
From C:\Users\Peyto\.codex:
```powershell
python -m streamlit run lab18/buffett_app.py
```

The app opens on COST. Change the ticker to JPM for the missing-data probe. In COST's memo editor append "ROE is 40.0%." The app flags that number; remove the sentence afterward. Editing in the app does not overwrite the saved memo; use its download button to save an edited copy.

The submitted skill source is buffett-investing/SKILL.md and buffett-investing/scripts/buffett.py inside this folder. A matching copy is installed in C:\Users\Peyto\.codex\skills\buffett-investing. In a new Codex chat, ask to use $buffett-investing for a ticker and save outputs to this lab18 directory. The app loads saved AI memos; it does not require or call a paid model API.

Run the bundled script directly:
```powershell
python lab18/buffett-investing/scripts/buffett.py COST --out lab18
python lab18/buffett-investing/scripts/buffett.py JPM --out lab18
python lab18/test_lab18.py
```
Use --refresh to bypass the one-day cache. Requests identify Peyton Dow peytonpdow@gmail.com to SEC. Cached JSON files retain source URLs and retrieval timestamps. requirements.txt lists dependencies.

## Rules implemented
Only 10-K facts in USD; five latest annual fiscal endpoints; annual flow duration 350–380 elapsed days (including calendar and 52/53-week years); quarters and 10-Q values excluded. Latest filing wins within the preferred tag before a fallback tag is considered. Each raw number retains its tag, period, filing date and accession. No missing metric is estimated.

ROE = net income / year-end equity. Owner earnings = operating cash flow minus capital spending, the assignment's simplified proxy. Zero/negative equity produces "not known" ROE. Missing facts produce "not found"; affected checks produce "not known". The 15% threshold is retained to match the lab and make runs comparable, not because it universally identifies a good business.

## Verification completed
- All five COST fiscal years and all seven financial columns match the supplied lab table.
- COST: ROE, positive owner earnings, and first-to-last owner-earnings growth all pass.
- JPM: capital spending and owner earnings remain "not found"; both owner-earnings checks remain "not known". The ROE consistency check fails.
- Both AI-written memos contain only supported numeric tokens.
- Inserting 40.0% in COST's memo triggers an unsupported-number error in the actual Streamlit AppTest interaction.
- Extraction tests cover later filings, quarter exclusion, fallback tags, 53-week years, zero/negative equity, and incomplete five-year inputs.
- Streamlit tests cover COST, editing the memo, switching to JPM, and invalid-ticker error handling.
- Six automated tests passed. The skill-creator validator reports "Skill is valid!".

Numeric checking compares values, signs and percent units with printed financial values and fiscal-year labels. It does not prove that a supported number is attached to the right metric, validate qualitative claims, or interpret number words. A saved memo fingerprint prompts review if its source facts change. Latest-filed values are not historical-vintage backtest data.

## Files for review and GitHub
Keep this directory structure:
- buffett-investing/SKILL.md
- buffett-investing/scripts/buffett.py
- buffett_app.py
- requirements.txt
- COST_report.md and COST_report.json
- JPM_report.md and JPM_report.json
- COST_memo.md and COST_memo.meta.json
- JPM_memo.md and JPM_memo.meta.json
- test_lab18.py
- lab18_notes.md

The data directory is a reproducible download cache and can be regenerated. Preserve folder structure so the app can import its bundled engine.

## Remaining classroom work
Peyton confirmed the opening partner discussion was done and supplied the build request.
Status of classroom activities:
- Open the Lab 18 Brightspace quiz at the instructed point.
- Fresh-chat comparison: completed. The supplied answer reported ROE of 30.55%, 27.53%, 30.27%, 30.69%, and 28.40% for 2022–2026, claiming average equity and S&P Global/Stock Analysis as sources. The lab uses year-end equity. The other answer's figures and extra business claims were not independently verified.
- Explain year_row() to a partner without AI; answer where "not found" originates (pick_fact finds no permitted value).
- Student trust decision: completed and saved beneath the COST memo. Customer loyalty and competitive advantage are Peyton's qualitative judgments, not verified outputs of the script.
- Written reflection and skills-learning answers: completed below. The required spoken partner explanations and discussions are not yet explicitly confirmed complete.
- Review, upload the files to GitHub, and submit their links in Brightspace.

## Sources
- [Lab 18 instructions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/lab-18-legend-investor-as-skill.md)
- [Student handout](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-11/student-handout.md)
- [Buffett reference](https://github.com/CinderZhang/FAskills/blob/main/financial-researcher/experts/warren_buffett.md) (read, not installed)
- [SEC APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Official skill documentation](https://learn.chatgpt.com/docs/build-skills)

## Student app checks
Peyton confirmed COST's three passes and latest ROE/owner earnings; inserted 40.0%, saw the unsupported-number warning, and removed it; and confirmed JPM's missing data, unknown owner-earnings checks, failed ROE check, and memo limitation.


## Student reflection

### What does the skill make consistent, and what remains AI judgment?

The skill standardizes the data sources, five-year period, formulas, and checks. Python calculates ROE using year-end equity and the lab's owner-earnings proxy: operating cash flow minus capital spending. It consistently checks whether ROE is at least 15% every year, owner earnings are positive every year, and owner earnings grow from the first year to the last. The memo must use only the script's reported numbers.

The AI interprets those results, explains limitations, and chooses own the business, watch it, or pass. That decision requires judgment; passing the checks does not automatically make a company a good investment.

### Why is "not found" better than estimating missing data?

"Not found" honestly identifies a gap in the evidence. An estimate could look like an actual SEC-reported fact, distort the calculations, and produce a misleading conclusion. Preserving missing data makes the analysis traceable and signals where further research is needed. If a required input is missing, the related check stays "not known" instead of receiving an unsupported pass or fail.


## Skills learning

### What is an AI skill?

An AI skill is a reusable set of instructions, sometimes bundled with scripts and reference files, that guides the AI through a particular task. Your Buffett skill defines how to gather financial data, calculate metrics, and write a supported memo. It acts like a task-specific instruction manual.

### Why read only its name and description initially?

The name and description help the AI decide whether the skill fits your request. It loads the full instructions only when relevant, saving space in its working context and avoiding unnecessary information. This approach is called progressive disclosure—like scanning a cookbook's table of contents before reading the recipe you need.
