"""
Exercise 11 🟡: Harden the Diary App

What you'll practise:
  try/except/else/finally, FileNotFoundError, ValueError, and raise.

Task:
  Take the diary app from Module 10 and add proper error handling so that
  it never crashes unexpectedly, no matter what the user types.

Requirements:
  - Wrap file operations in try/except blocks for FileNotFoundError and IOError.
  - Wrap all input() conversions in try/except ValueError.
  - If an unexpected error occurs, print a user-friendly message (not a traceback).
  - Use finally where appropriate for cleanup messages.
  - Add a function validate_entry(text) that raises ValueError if the text is empty.

Example behaviour (robust):
  > Choice: 5
  Invalid choice. Please enter 1, 2, or 3.

  > (user types Ctrl+C)
  Program interrupted. Goodbye!

How to run:
  python modules/module11_error_handling/exercises/exercise11_harden_diary.py

Hints:
  - Wrap the entire main loop in try/except KeyboardInterrupt for Ctrl+C handling.
  - Use except Exception as e: print(f"Unexpected error: {e}") as a last resort.
  - validate_entry: if not text.strip(): raise ValueError("Entry cannot be empty")

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# TODO: Step 1 — Copy or rewrite the diary app from Module 10
# TODO: Step 2 — Add try/except around file reads (FileNotFoundError)
# TODO: Step 3 — Add try/except around file writes (IOError)
# TODO: Step 4 — Add try/except KeyboardInterrupt around the main loop
# TODO: Step 5 — Add validate_entry(text) that raises ValueError for empty input
# TODO: Step 6 — Use finally for any cleanup messages
