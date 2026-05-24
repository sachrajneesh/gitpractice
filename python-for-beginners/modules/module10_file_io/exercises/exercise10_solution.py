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

from datetime import datetime
from pathlib import Path

DIARY_FILE = "diary.txt"


def write_entry():
    """Ask the user for a diary entry and append it with a timestamp."""
    entry = input("What's on your mind today?\n> ").strip()
    if not entry:
        print("No entry written — you didn't type anything.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"[{timestamp}] {entry}\n"

    # "a" mode appends — previous entries are never overwritten.
    with open(DIARY_FILE, "a") as f:
        f.write(line)
    print("Entry saved!")


def read_entries():
    """Print all diary entries, or a message if none exist yet."""
    if not Path(DIARY_FILE).exists():
        print("No diary entries yet. Start writing!")
        return

    print(f"\n--- Your Diary ({DIARY_FILE}) ---")
    with open(DIARY_FILE, "r") as f:
        content = f.read()

    if content.strip():
        print(content)
    else:
        print("The diary file is empty.")


# --- Main menu loop ---
print("=== Personal Diary ===")

while True:
    print("\n1. Write new entry")
    print("2. Read all entries")
    print("3. Quit")

    choice = input("Choice: ").strip()

    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("Goodbye! Keep writing.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
