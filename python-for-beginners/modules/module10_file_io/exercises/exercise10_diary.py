"""
Exercise 10 🟡: Diary App

What you'll practise:
  Writing to files, appending, reading files, and the with statement.

Task:
  Build a simple diary app where the user can:
    1. Write a new diary entry (appends to diary.txt)
    2. Read all diary entries (reads diary.txt)
    3. Quit

  Bonus: save and load a contacts list to/from contacts.csv using the csv module.

Requirements:
  - New entries are appended to "diary.txt" (not overwritten).
  - Each entry should be saved with a date/time stamp.
  - Reading displays all past entries.
  - If diary.txt does not exist yet, reading should print a friendly message.

Example diary.txt content:
  [2024-01-15 09:30] Finished Module 09 today. Functions are starting to click!
  [2024-01-16 08:45] Wrote my first file I/O program. Really satisfying.

How to run:
  python modules/module10_file_io/exercises/exercise10_diary.py

Hints:
  - from datetime import datetime; datetime.now().strftime("%Y-%m-%d %H:%M")
  - Open in "a" mode to append without overwriting.
  - Check if file exists: from pathlib import Path; Path("diary.txt").exists()

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# TODO: Step 1 — Import datetime (from datetime import datetime)
# TODO: Step 2 — Define a function write_entry() that appends to diary.txt
# TODO: Step 3 — Define a function read_entries() that prints diary.txt contents
# TODO: Step 4 — Write the main menu loop: Write / Read / Quit
