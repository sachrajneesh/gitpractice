# Capstone Assessment #3 — Modules 01–11 (Sales Data Analyzer) — ADVANCED

The **hardest** of the three capstones and a deliberately **different kind of
program**. Capstones #1 (Expense Tracker) and #2 (Quiz Game) were both
interactive menu apps where data is typed in one record at a time. This one is a
**batch data pipeline**: it reads a whole file of raw, partly-broken data,
cleans it, runs several aggregations across the entire dataset, ranks and tiers
the results, and writes finished report files. The difficulty is in the
*analysis*, not the menu.

## Files
- `capstone_sales_analyzer.py` — hand this to the learner (brief + requirements
  + TODO pipeline).
- `sample_sales.csv` — the input dataset. **It contains 3 broken rows on
  purpose** (a non-numeric quantity, a missing region+price, and a short row).
  A correct program skips them and reports "3 skipped".
- `capstone_solution.py` — reference solution (tested). Keep it back until they
  finish.
- `report.txt` / `summary.csv` — *generated* when the program runs; not part of
  the assignment (git-ignored / safe to delete).

## How to give it
1. Give this **after** they've completed capstones #1 and #2.
2. Ask them to open `capstone_sales_analyzer.py` and read the brief.
3. Suggested time: 2.5–3 hours (it is meant to stretch them).
4. Run with:
   ```
   python assessments/capstone3_modules_01-11/capstone_sales_analyzer.py
   ```

## Why this is harder than #1 and #2
- **Whole-dataset thinking**, not one record at a time.
- **Dirty input**: must validate and skip broken rows without crashing.
- **Multiple aggregations** into several dictionaries at once.
- **Sorting by a key** and finding the **max of a dict** (ranking, top product).
- **Derived categories** (performance tiers) and **percentages**.
- **Generates two output files** in different formats (text report + CSV).

## What each part is really testing

| Module | Concept | Where it shows up |
|--------|---------|-------------------|
| 01 | `print`, comments | on-screen summary, progress |
| 02 | `input`, `int()`/`float()` | settings prompt; parsing quantity & price |
| 03 | strings, f-strings, methods | `.strip()/.title()`, aligned report columns |
| 04 | operators | line totals, average, percentage shares |
| 05 | `if/elif/else` | performance tiers, validation branches |
| 06 | loops | iterating rows and building every aggregate |
| 07 | lists | list of sale dicts; sorting; Top-N slicing |
| 08 | dictionaries | per-region / per-person / per-product totals |
| 09 | functions | a pipeline of small functions + `main()` |
| 10 | file I/O | read CSV; write `report.txt` and `summary.csv` |
| 11 | error handling | skip broken rows; bad Top-N; missing file |

## Grading rubric (100 points)

| Area | Points | Look for |
|------|-------:|----------|
| Runs without crashing on the messy file | 10 | Handles the 3 bad rows, no traceback |
| Functions & structure | 15 | Small single-job functions, docstrings, a `main()` pipeline |
| Reading & cleaning data | 15 | csv + `with open`; int/float conversion; **counts** skipped rows |
| Per-region / per-person / per-product dicts | 15 | Correct aggregation with loops into dictionaries |
| Totals, average, percentages | 10 | Arithmetic correct; average = revenue / valid count |
| Ranking & tiers | 15 | Sorted highest-first; Gold/Silver/Bronze via if/elif/else; max product/person |
| Output files | 15 | `report.txt` readable & aligned; `summary.csv` has header + one row per person |
| Error handling (settings & file) | 5 | Bad Top-N falls back; missing file caught |

**Grade bands:** 90+ excellent · 75–89 solid · 60–74 passing with gaps ·
below 60 revisit the weak modules.

### Expected numbers from `sample_sales.csv` (for quick checking)
- Valid sales: **14**, Skipped rows: **3**
- Total revenue: **$673.93**, Average sale: **$48.14**
- Top salesperson: **Carol ($276.13, Gold)**; Best-selling product: **Widget (55 units)**
- Ranking: Carol → Dave ($174.16) → Bob ($124.67) → Alice ($98.97, Bronze)

(Exact totals may differ slightly if they round mid-calculation — that's fine;
the ranking and skip-count are the important signals.)

## Questions to confirm real understanding
- How did you decide a row was "broken", and why skip instead of crash?
- Why use a dictionary for the per-region totals instead of a list?
- Explain the line that sorts the salespeople. What is the sort *key*?
- Why is the average computed as revenue ÷ **valid** count, not ÷ total rows?
- If the file had 10,000 rows, would your code still work? Why?

## The three capstones together
| # | Project | Shape | New challenge |
|---|---------|-------|---------------|
| 1 | Expense Tracker | interactive CRUD | list of dicts + CSV + try/except |
| 2 | Quiz Game | interactive scoring | case-insensitive matching, per-topic tally |
| 3 | Sales Analyzer | **batch pipeline** | dirty data, multi-aggregation, ranking, report files |

If Ryan clears all three, he can not only recall the module 1–11 concepts but
**apply them to unfamiliar problem shapes** — which is the real goal.
