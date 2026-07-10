# Capstone Assessment #2 — Modules 01–11 (Quiz Game)

A second integrated project at the **same difficulty** as the Expense Tracker
capstone, but a **different problem**. The point is to check that the learner
understood the underlying ideas — not that they memorised the first capstone.
Same skills, new shape: this one is about interactive scoring and per-topic
tallying instead of record-keeping and totals.

## Files
- `capstone_quiz_game.py` — hand this to the learner. Brief, requirements, and a
  scaffold of TODOs.
- `capstone_solution.py` — reference solution (tested). Keep it back until they
  finish.

## How to give it
1. Ask the learner to open `capstone_quiz_game.py` and read the brief.
2. Fixed time (suggested: 90–120 minutes).
3. Run with:
   ```
   python assessments/capstone2_modules_01-11/capstone_quiz_game.py
   ```

## What each part is really testing

| Module | Concept | Where it shows up |
|--------|---------|-------------------|
| 01 | `print`, comments | menu, question output |
| 02 | variables, `input`, `int()` | reading answers; "how many questions" → int |
| 03 | strings, f-strings, methods | `.strip().lower()` answer matching, formatted output |
| 04 | operators | score + percentage arithmetic |
| 05 | `if/elif/else` | correct/wrong check, letter-grade bands |
| 06 | loops | `while` menu loop, `for` over questions |
| 07 | lists | the question bank |
| 08 | dictionaries | each question; per-topic `{correct, total}` tally |
| 09 | functions | one function per job + `main()` |
| 10 | file I/O | save/load questions as CSV |
| 11 | error handling | bad "how many" input & missing file don't crash |

## Grading rubric (100 points)

| Area | Points | Look for |
|------|-------:|----------|
| Runs without crashing | 10 | Starts, menu loops, Quit exits |
| Functions & structure | 15 | Split into functions, docstrings, a `main()` |
| Menu loop & dispatch | 10 | `while` loop + `if/elif/else` |
| Add question | 10 | Reads input, stores a **dict** in the **list** |
| Take the quiz — scoring | 20 | Loops questions, **case-insensitive** compare, running score, percentage |
| Take the quiz — grade & per-topic | 10 | `if/elif/else` grade band + `{topic: correct/total}` dict |
| Save & load (CSV) | 15 | Writes a file and reads it back into the list |
| Error handling | 10 | Non-number "how many" handled; missing file caught |
| Code quality | 5 | Readable names, no dead code |

**Grade bands:** 90+ excellent · 75–89 solid · 60–74 passing with gaps ·
below 60 revisit the weak modules.

## Questions to confirm real understanding
- Why compare answers with `.strip().lower()` on **both** sides?
- Why is the per-topic result a dictionary of dictionaries instead of two lists?
- What happens if you forget to convert the "how many" answer from text to int?
- Why does loading re-assign the list (`questions = load_questions()`) rather
  than just calling the function?

## Comparing the two capstones
Give the Expense Tracker **first**. If they solve it, this one should feel
familiar in structure (menu loop, list of dicts, CSV, try/except) but force new
thinking in the quiz-scoring and per-topic tally. Struggling on #2 after passing
#1 usually means they pattern-matched the first one rather than understanding it
— a useful signal on its own.
