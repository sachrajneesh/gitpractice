# Project Structure

Annotated directory tree for the entire course.

```
python-for-beginners/
│
├── .python-version          # Tells pyenv (and VS Code) to use Python 3.12
├── .gitignore               # Files Git should ignore (__pycache__, .venv, etc.)
│
├── README.md                # Installation guide + smoke test commands
├── QUICK_START.md           # Daily schedule + how to resume + stuck strategy
├── LEARNING_APPROACH.md     # Philosophy: why 30/70, no copy-paste, daily habit
├── COURSE_CATALOG.md        # 15-module table with progress checkboxes
├── PROJECT_STRUCTURE.md     # This file — annotated directory tree
├── CHEATSHEET.md            # One-page Python syntax reference
│
└── modules/
    ├── README.md            # Index table linking to all 15 module READMEs
    │
    ├── module01_getting_started/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Teaching content: print, REPL, comments
    │   ├── examples/
    │   │   ├── 01_hello_world.py      # Classic hello world + print variations
    │   │   ├── 02_repl_demo.py        # REPL-style expressions with comments
    │   │   ├── 03_print_variations.py # sep, end, multiple arguments
    │   │   └── 04_common_mistakes.py  # Commented-out errors with explanations
    │   └── exercises/
    │       ├── exercise01_hello_you.py      # Starter file with TODOs
    │       └── exercise01_solution.py       # Full solution with comments
    │
    ├── module02_variables_and_types/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Teaching content: types, naming, input()
    │   ├── examples/
    │   │   ├── 01_variable_basics.py  # Creating vars of each type
    │   │   ├── 02_naming_rules.py     # Valid vs invalid names
    │   │   ├── 03_input_basics.py     # Using input(), always a string
    │   │   └── 04_type_gotchas.py     # The number+string error + fix
    │   └── exercises/
    │       ├── exercise02_profile.py        # Starter: name + age profile
    │       └── exercise02_solution.py       # Full solution
    │
    ├── module03_strings/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Teaching content: f-strings, slicing, methods
    │   ├── examples/
    │   │   ├── 01_string_basics.py    # Literals, quotes, escape chars
    │   │   ├── 02_multiline.py        # Triple-quoted strings
    │   │   ├── 03_fstrings.py         # f-strings with expressions
    │   │   ├── 04_indexing_slicing.py # Index and slice with ASCII diagram
    │   │   └── 05_string_methods.py   # upper, lower, strip, split, etc.
    │   └── exercises/
    │       ├── exercise03_namecard.py       # Starter: formatted name card
    │       └── exercise03_solution.py       # Full solution with bordered output
    │
    ├── module04_operators_and_expressions/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — arithmetic, comparison, logical, precedence
    │   └── exercises/
    │       └── exercise04_calculator.py     # Starter: simple calculator
    │
    ├── module05_control_flow/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — if/elif/else, truthiness, match
    │   └── exercises/
    │       └── exercise05_grade_classifier.py  # Starter: score to letter grade
    │
    ├── module06_loops/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — for, range, while, break, continue
    │   └── exercises/
    │       └── exercise06_times_table.py    # Starter: times table + guessing game
    │
    ├── module07_lists_and_tuples/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — create, slice, methods, comprehensions
    │   └── exercises/
    │       └── exercise07_todo_list.py      # Starter: to-do list app
    │
    ├── module08_dictionaries_and_sets/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — dicts, keys/values, nested, sets
    │   └── exercises/
    │       └── exercise08_contacts.py       # Starter: contacts book
    │
    ├── module09_functions/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — def, parameters, return, scope, docstrings
    │   └── exercises/
    │       └── exercise09_calculator_functions.py  # Starter: calculator + BMI
    │
    ├── module10_file_io/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — open(), read/write, with, csv, pathlib
    │   └── exercises/
    │       └── exercise10_diary.py          # Starter: diary app + CSV contacts
    │
    ├── module11_error_handling/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — try/except/else/finally, raise
    │   └── exercises/
    │       └── exercise11_harden_diary.py   # Starter: add error handling to diary
    │
    ├── module12_modules_and_packages/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — import, stdlib, pip, venv, own module
    │   └── exercises/
    │       └── exercise12_daily_challenge.py  # Starter: random challenge generator
    │
    ├── module13_oop_basics/
    │   ├── README.md        # Objectives, topics, exercise checklist
    │   ├── CONCEPTS.md      # Stub — classes, __init__, methods, inheritance
    │   └── exercises/
    │       └── exercise13_bank_account.py   # Starter: BankAccount + SavingsAccount
    │
    ├── module14_mini_projects/
    │   ├── README.md        # Objectives + project descriptions
    │   ├── CONCEPTS.md      # Stub — project planning notes
    │   └── exercises/
    │       └── exercise14_projects.py       # Starter: three project outlines
    │
    └── module15_next_steps/
        ├── README.md        # Objectives + ecosystem overview
        ├── CONCEPTS.md      # Stub — Flask, pandas, requests, pygame, argparse
        └── exercises/
            └── exercise15_roadmap.py        # Starter: personal learning roadmap
```

---

## File naming conventions

- `examples/` files: `NN_descriptive_name.py` (two-digit number prefix)
- `exercises/` starter files: `exerciseNN_topic.py`
- `exercises/` solution files: `exerciseNN_solution.py`
- All Python files: snake_case, no spaces
- All docs: UPPER_CASE.md for root docs, README.md / CONCEPTS.md inside modules
