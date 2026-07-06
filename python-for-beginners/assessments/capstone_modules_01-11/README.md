# Capstone Assessment — Modules 01–11

A single integrated project that checks whether the learner can **combine**
everything from the first eleven modules, not just recall each piece in
isolation. Theme: a command-line **Expense Tracker**.

## Files
- `capstone_expense_tracker.py` — hand this to the learner. It contains the
  brief, requirements, and a scaffold of TODOs.
- `capstone_solution.py` — reference solution. Keep this back until they finish.

## How to give it
1. Ask the learner to open `capstone_expense_tracker.py` and read the brief.
2. Give them a fixed time (suggested: 90–120 minutes for this level).
3. They run it with:
   ```
   python assessments/capstone_modules_01-11/capstone_expense_tracker.py
   ```

## What each part is really testing

| Module | Concept | Where it shows up |
|--------|---------|-------------------|
| 01 | `print`, comments | menu output, messages |
| 02 | variables, `input`, `int/float` | reading & converting the amount |
| 03 | strings, f-strings, methods | `.strip()`, `.title()`, formatted table |
| 04 | operators | summing totals, comparisons |
| 05 | `if/elif/else` | menu dispatch |
| 06 | loops | `while` menu loop, `for` over expenses |
| 07 | lists | the list of expenses |
| 08 | dictionaries | each expense; `{category: total}` |
| 09 | functions | one function per job + `main()` |
| 10 | file I/O | save/load CSV |
| 11 | error handling | bad amount & missing file don't crash |

## Grading rubric (100 points)

| Area | Points | Look for |
|------|-------:|----------|
| Runs without crashing | 10 | Program starts and the menu loops |
| Functions & structure | 15 | Split into functions, each with a docstring, a `main()` |
| Menu loop & dispatch | 10 | `while` loop + `if/elif/else`; Quit actually exits |
| Add expense | 15 | Reads input, converts amount to float, stores a **dict** in the **list** |
| View expenses | 10 | Loops the list, f-string output, prints a grand total, handles empty list |
| Totals by category | 10 | Builds a `{category: total}` dict correctly |
| Save & load (CSV) | 15 | Writes a file and reads it back into the list |
| Error handling | 10 | Non-numeric amount re-asks; missing file caught (no traceback) |
| Code quality | 5 | Readable names, no dead code, sensible comments |

**Grade bands:** 90+ excellent · 75–89 solid · 60–74 passing with gaps ·
below 60 revisit the weak modules.

## Fast ways to probe understanding after they submit
Ask them to explain, in their own words:
- Why is each expense a **dictionary** instead of just three variables?
- What would happen if you removed the `try/except` around the amount input?
- Why does `input()` always need converting before you can do maths on it?
- What does `with open(...)` give you that a plain `open()` doesn't?

If they can answer those, the grasp is real — not copied.

## Common mistakes to watch for (and which module to revisit)
- Storing amounts as strings, so totals concatenate instead of add → **Mod 2/4**
- Using `expenses` as a global and mutating it inconsistently → **Mod 9 (scope)**
- Catching every error with a bare `except:` instead of `ValueError` → **Mod 11**
- Forgetting the empty-list case (crashes on first "view") → **Mod 5/7**
- Reloading the file but not skipping the header row → **Mod 10**
