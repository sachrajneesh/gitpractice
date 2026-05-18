# Python for Beginners

```
+----------------------------------------------------------+
|                   THREE LEARNING PRINCIPLES              |
|                                                          |
|  1. 30/70 RULE — 30% reading/watching, 70% coding.      |
|     Every module reminds you. Take this seriously.       |
|                                                          |
|  2. DAILY CONSISTENCY — 1.5 to 2 hours/day, 6 days/week.|
|     Short daily sessions beat long weekend marathons.    |
|                                                          |
|  3. TYPE EVERY LINE — never copy-paste. Ever.            |
|     If stuck, peek at the solution, then close it and    |
|     retype it from memory.                               |
+----------------------------------------------------------+
```

A hands-on, coding-first Python course for complete beginners.
No prior programming experience required.

---

## Installing Python 3.12

### Option A — python.org (recommended for all platforms)
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.12.x" (the big yellow button).
3. Run the installer.
   - **Windows**: check "Add Python to PATH" before clicking Install.
   - **macOS/Linux**: follow the standard installer steps.

### Option B — Windows Store
1. Open the Microsoft Store.
2. Search for "Python 3.12".
3. Click Get / Install.

### Option C — Homebrew (macOS only)
```bash
brew install python@3.12
```

---

## Verify your installation

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run:

```bash
python --version
```

You should see something like:
```
Python 3.12.x
```

If you see `Python 2.x.x`, try `python3 --version` instead, and use `python3` everywhere in this course.

---

## How to run any example

```bash
python modules/moduleXX_<name>/examples/01_<name>.py
```

Replace `moduleXX_<name>` with the actual module folder name.

---

## Smoke test — run these right now to confirm everything works

```bash
python modules/module01_getting_started/examples/01_hello_world.py
python modules/module01_getting_started/exercises/exercise01_solution.py
```

Both should print output without errors. If they do, you are ready to go.

---

## VS Code setup (recommended editor)

1. Download VS Code from https://code.visualstudio.com/
2. Open VS Code.
3. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS) to open Extensions.
4. Search for **Python** (publisher: Microsoft) and click Install.
5. Open this course folder: File > Open Folder > select `python-for-beginners/`.
6. VS Code will detect the `.python-version` file and suggest using Python 3.12.
7. Press `Ctrl+Shift+P` / `Cmd+Shift+P`, type "Python: Select Interpreter", choose 3.12.

To run a file: open it, then press `F5` or right-click > "Run Python File in Terminal".

---

## Creating a virtual environment

A virtual environment keeps your project's packages separate from system Python.
Run these commands inside the `python-for-beginners/` folder:

```bash
# Create the virtual environment (only do this once)
python -m venv .venv

# Activate it — macOS/Linux:
source .venv/bin/activate

# Activate it — Windows (Command Prompt):
.venv\Scripts\activate.bat

# Activate it — Windows (PowerShell):
.venv\Scripts\Activate.ps1

# You should see (.venv) at the start of your prompt now.
# To deactivate later:
deactivate
```

---

## Course structure at a glance

See `COURSE_CATALOG.md` for the full 15-module table.
See `QUICK_START.md` to jump straight in.
See `CHEATSHEET.md` when you need a syntax reminder.
See `LEARNING_APPROACH.md` to understand the philosophy behind this course.
