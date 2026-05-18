# Course-in-a-box: Python for Beginners (coding-first)

Give this file to **Claude Code** (claude.ai/code) in an empty directory. Claude will scaffold a 15-module, hands-on Python course for absolute beginners — per-module READMEs, runnable examples, and TODO-style exercises paired with solutions.

Designed for someone who just finished high school and has never written a line of code. No math beyond what you learned in school. Every concept is introduced through things you can run immediately.

---

## Quick start

1. **Install Claude Code** if you haven't: https://claude.com/claude-code
2. Open a terminal in the parent directory where you want the course to live:
   ```bash
   cd ~/workspace/learning
   ```
3. Start Claude Code and paste the prompt below (everything between the `>>>` markers).
4. Answer Claude's one clarifying question (directory name).
5. Let Claude scaffold — it creates ~80 files.
6. Install Python, run the smoke test, then open module 1.

> **Why Python first?** Python reads almost like English, runs on every platform, and is the #1 language for data science, web backends, automation, and AI. It's the best first language to learn — and the skills transfer everywhere.

---

## Prompt to paste into Claude Code

>>> START OF PROMPT >>>

I want you to scaffold a coding-first Python course on my machine for a complete beginner who just finished high school. The style is "hands-on exercises with TODO markers, paired with solutions, so I can code step by step."

Please follow the spec in the rest of this message exactly.

### Learning principles (embed these everywhere)

The student must internalize three rules. Reference them explicitly in `LEARNING_APPROACH.md`, in the top-level `README.md`, and in every module `README.md`:

1. **30/70 rule** — 30% watching/reading, 70% hands-on coding. Every module README should remind the student of this ratio.
2. **Daily consistency over long sessions** — 1.5–2 hours/day, 6 days/week. The `QUICK_START.md` resume guide should open with this schedule.
3. **Type every line — never copy-paste** — exercises must reinforce this with a reminder at the top of every starter file.

### Course goals
- 15 modules covering Python from absolute zero through real mini-projects
- Every module has runnable examples *and* fill-in-the-blank exercises with solutions
- No hand-holding prose — short READMEs, code does the teaching
- Assumes no prior programming experience whatsoever
- Uses only the Python standard library for Modules 1–12; third-party packages only from Module 13 onward

### Before you scaffold, ask me
- **Directory name** — default to `python-for-beginners` in the current working directory.

Then create the layout below.

### Directory layout

```
<course-dir>/
├── README.md                # install guide, how to run code, smoke test
├── COURSE_CATALOG.md        # 15-module outline with status markers
├── LEARNING_APPROACH.md     # coding-first teaching style
├── QUICK_START.md           # resume guide (how to pick up where you left off)
├── PROJECT_STRUCTURE.md     # file layout reference
├── CHEATSHEET.md            # one-page Python syntax quick reference
├── .python-version          # 3.12
├── .gitignore               # __pycache__, .venv, *.pyc
└── modules/
    ├── README.md            # index table
    ├── module01_getting_started/
    ├── module02_variables_and_types/
    ├── module03_strings/
    ├── module04_operators_and_expressions/
    ├── module05_control_flow/
    ├── module06_loops/
    ├── module07_lists_and_tuples/
    ├── module08_dictionaries_and_sets/
    ├── module09_functions/
    ├── module10_file_io/
    ├── module11_error_handling/
    ├── module12_modules_and_packages/
    ├── module13_oop_basics/
    ├── module14_mini_projects/
    └── module15_next_steps/
```

Each module directory contains:
- `README.md` — objectives, topics covered, exercise list with checkboxes
- `CONCEPTS.md` — plain-English explanation of every new concept with code snippets
- `examples/` — numbered runnable files (`01_*.py`, `02_*.py`, …) — one concept per file, heavily commented
- `exercises/` — `exerciseNN_<topic>.py` (starter with `# TODO:` markers) + `exerciseNN_solution.py`

### 15-module curriculum

| # | Module | Focus | Deliverable exercise |
|---|--------|-------|----------------------|
| 01 | Getting Started | What Python is; installing Python; running the REPL; writing and running your first `.py` file; `print()`; comments. | `hello.py` — print your name, age, and a favourite quote |
| 02 | Variables & Data Types | `int`, `float`, `str`, `bool`, `None`; variable naming rules; `type()`; `input()`. | A personal profile script that asks your name and age, then prints a formatted summary |
| 03 | Strings | String literals; quotes; escape characters; multi-line strings; f-strings; common string methods (`upper`, `lower`, `strip`, `replace`, `split`, `join`, `find`, `len`). | A "name card generator" that takes first and last name and prints a formatted card |
| 04 | Operators & Expressions | Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`); comparison (`==`, `!=`, `<`, `>`, `<=`, `>=`); logical (`and`, `or`, `not`); operator precedence. | A simple calculator that takes two numbers and an operator from the user and prints the result |
| 05 | Control Flow | `if`, `elif`, `else`; truthiness; nested conditions; `match` statement (Python 3.10+). | A grade classifier: reads a score, prints the letter grade and a personalised message |
| 06 | Loops | `for` loop; `range()`; `while` loop; `break`; `continue`; `else` on loops; nested loops. | A times-table printer and a number-guessing game (using `while`) |
| 07 | Lists & Tuples | Creating, indexing, slicing; `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`; list comprehensions; tuples and immutability. | A to-do list app (add, view, remove tasks) using a list |
| 08 | Dictionaries & Sets | Creating dicts; getting and setting values; `keys()`, `values()`, `items()`; nested dicts; sets and set operations (`union`, `intersection`, `difference`). | A contacts book: add, look up, and delete contacts stored in a dictionary |
| 09 | Functions | Defining functions; parameters and return values; default arguments; keyword arguments; variable scope (`local` vs `global`); docstrings. | Refactor the Module 4 calculator into clean functions; add a `BMI calculator` function |
| 10 | File I/O | Opening files with `open()`; `read()`, `readlines()`, `write()`; `with` statement; working with CSV using `csv` module; file paths with `pathlib`. | A diary app: write entries to a file and read them back; save contacts from Module 8 to a CSV |
| 11 | Error Handling | `try`, `except`, `else`, `finally`; common built-in exceptions; raising exceptions with `raise`; writing helpful error messages. | Harden the Module 10 diary app so it never crashes on bad input or missing files |
| 12 | Modules & Packages | `import`; `from X import Y`; the standard library tour (`math`, `random`, `datetime`, `os`, `sys`); `pip` and virtual environments; writing your own module. | A "random daily challenge" generator using `random` and `datetime`; package your helper functions as a module |
| 13 | OOP Basics | Classes and objects; `__init__`; instance attributes; methods; `__str__`; inheritance; `super()`. | A `BankAccount` class with deposit, withdraw, and statement methods; a `SavingsAccount` subclass with interest |
| 14 | Mini Projects | Apply everything: three self-contained projects at increasing difficulty — choose to do all or just the one at your level. | Project A (easy): number quiz game; Project B (medium): expense tracker with file persistence; Project C (hard): text-based adventure game with OOP |
| 15 | Next Steps | What comes after: web dev (`Flask`/`FastAPI`), data science (`pandas`/`numpy`), automation (`requests`), AI/ML; reading docs; finding help; where to practice. | A one-page personal learning roadmap `.md` file you fill in for yourself |

### Depth of authoring

- **Fully flesh out Modules 01–03** (README + CONCEPTS + examples + starter exercise + solution). These are the foundation — the student must feel confident and successful before continuing.
- **Scaffold Modules 04–15** with README + CONCEPTS stub + a single placeholder exercise file. The student fleshes these out as they progress.

### Module 1 specifics (critical)

Module 1 must:
- Have a `CONCEPTS.md` that explains what a program is in plain English (no assumed knowledge)
- Show three ways to run Python: the REPL, a script, and VS Code / any editor
- Explain `print()` thoroughly — multiple arguments, `sep`, `end`
- Explain comments (`#`) and why they matter
- Have an example that fails intentionally (`01_common_mistakes.py`) showing `SyntaxError` and `NameError` with friendly explanations in comments
- The exercise must be achievable in under 5 minutes by a complete beginner

### Module 2 specifics (critical)

Module 2 must:
- Show how Python decides what "type" something is, with `type()` output in comments
- Demonstrate `input()` and the fact that it always returns a `str` — and show how to convert with `int()` / `float()`
- Have a dedicated example (`04_type_gotchas.py`) showing the classic "adding a number and a string" error and how to fix it

### Module 3 specifics (critical)

Module 3 must:
- Dedicate a full example to f-strings (`03_fstrings.py`) — this is the modern way; old `%` formatting is not taught
- Show indexing and slicing with a visual ASCII diagram in comments
- Have the exercise produce real-looking output (formatted card with borders)

### Shared conventions

- All examples runnable standalone: `python modules/<module>/examples/<file>.py`
- Every example file starts with a docstring explaining what it demonstrates
- No third-party imports in Modules 1–12 — standard library only
- Every exercise has a matching `*_solution.py`
- Difficulty indicators in exercise filenames: `🟢` easy, `🟡` medium, `🔴` hard

### Exercise file template

```python
"""
Exercise N 🟢|🟡|🔴: <title>

What you'll practise:
  <one sentence>

Task:
  <what to build, in plain English>

Requirements:
  - <bullet>
  - <bullet>

How to run:
  python modules/<module>/exercises/<file>.py

Hints:
  - <one helpful pointer per gotcha>

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# TODO: Step 1 — <first small step>

# TODO: Step 2 — <next step>

# TODO: Step 3 — <final step>
```

The matching `*_solution.py` has the same docstring header, then the full implementation — one clean approach with a few comments explaining key choices.

### Beginner-friendliness rules

- CONCEPTS.md files must assume zero prior knowledge — define every term the first time it appears
- Error messages in examples must be explained in plain English right in the comments
- Every `examples/` file demonstrates exactly one concept — no mixing
- Use real-world analogies in CONCEPTS.md (a variable is like a labelled box; a function is like a recipe)
- Example programs should be things a teenager would find interesting: names, scores, games, messages — not abstract `foo`/`bar` placeholders

### Verification (tell me these commands at the end)

```bash
cd <course-dir>
python --version            # should print Python 3.12.x
python modules/module01_getting_started/examples/01_hello_world.py
python modules/module01_getting_started/exercises/exercise01_solution.py
```

Now ask for the directory name, then scaffold the whole thing.

>>> END OF PROMPT >>>

---

## What your son ends up with

- **~80 files**, runnable the moment Python is installed — no extra packages needed for the first 12 modules
- A working, fun first program by end of module 1 — instant confidence
- **3 modules of real, heavily-guided exercises** to start coding immediately
- **12 more scaffolded modules** with READMEs and concept stubs, ready to work through at his own pace
- Every exercise has a `*_solution.py` next to it — code first, peek second
- A final module that maps out what to learn next so he's never lost

## How to learn (non-negotiable principles)

### 1. Avoid tutorial-watching traps
The biggest mistake beginners make is watching videos and feeling like they understand — then sitting down to code and drawing a blank. Videos are useful, but they are **not** the work.

Stick to this split every session:
- **30%** watching / reading
- **70%** actually writing code

If you catch yourself re-watching a video instead of attempting the exercise, stop and open your editor instead.

### 2. Daily practice beats marathon sessions
Your brain consolidates skills during sleep. A short daily session is worth far more than a long weekly one.

Target schedule:
- **1.5–2 hours per day**
- **6 days a week** (one rest day is fine)

Consistency is the skill. Missing one day is fine; missing a week undoes the week before it.

### 3. Type every line yourself — no exceptions
Never copy-paste code. Not from this course, not from Stack Overflow, not from anywhere.

Why it matters:
- Typing forces your brain to process each character
- You will make typos — that's the point. Debugging your own mistakes is how you learn to read code
- Copy-pasting produces confidence that disappears the moment you face a blank file

If you genuinely can't figure out a step after 15 minutes of trying, look at the solution — then **close it and retype the answer from memory**.

---

## Tips for the student

- **Run every example before reading it** — see what it does, then figure out how.
- **When something breaks, read the error message first.** Python's errors are usually very descriptive.
- **Google is part of the job.** Even senior engineers search "how to do X in Python" dozens of times a day.
- **Finish the exercise before looking at the solution.** Even a broken attempt teaches more than a perfect copy.

## Troubleshooting

- **`python` not found** → Try `python3` instead. On Windows, use the Microsoft Store Python or installer from python.org.
- **`SyntaxError`** → Check for missing colons (`:`) after `if`/`for`/`def`, mismatched quotes, or bad indentation.
- **`IndentationError`** → Python uses 4 spaces per indent level. Don't mix spaces and tabs — use spaces everywhere.
- **`NameError: name 'x' is not defined`** → You used a variable before assigning it, or you made a typo in the name.
- **`TypeError`** → You tried to do an operation between incompatible types (e.g. adding a string and a number). Use `int()` or `str()` to convert.
- **VS Code shows red squiggles** → Install the **Python** extension by Microsoft in VS Code for syntax highlighting and error detection.

## Customising the course

- **Slower pace**: split each module into two sessions — first half: read CONCEPTS + examples; second half: exercise.
- **Faster pace**: skip the exercises you find trivial and jump to the Module 14 mini-projects after finishing Module 9.
- **Different projects**: edit the Module 14 project descriptions in the prompt — swap in topics your son cares about (sport stats, music, games).

The prompt is the source of truth. Edit it, hand it to Claude Code, and you get a fresh course in ~15 minutes.

---

## What comes after this course

Once your son finishes Module 14, he'll be ready for any of these paths:

| Interest | What to learn next |
|----------|--------------------|
| Web apps | Flask or FastAPI — build a backend; then HTML/CSS for the frontend |
| Data & AI | `pandas`, `matplotlib`, then `scikit-learn` for machine learning |
| Automation | `requests` to call APIs; `selenium` to automate browsers |
| Games | `pygame` — 2D games entirely in Python |
| Command-line tools | `argparse`, `rich`, `typer` — beautiful terminal apps |
