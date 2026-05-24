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

from datetime import datetime
from pathlib import Path

DIARY_FILE = "diary.txt"


def validate_entry(text):
    """Raise ValueError if the entry text is empty or only whitespace."""
    if not text.strip():
        raise ValueError("Entry cannot be empty.")


def write_entry():
    """Ask the user for an entry, validate it, and append with a timestamp."""
    try:
        entry = input("What's on your mind today?\n> ")
        validate_entry(entry)   # raises ValueError if empty

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        line = f"[{timestamp}] {entry.strip()}\n"

        with open(DIARY_FILE, "a") as f:
            f.write(line)
        print("Entry saved!")

    except ValueError as e:
        print(f"Could not save entry: {e}")
    except IOError as e:
        # IOError covers disk full, permission denied, etc.
        print(f"File write error: {e}")
    finally:
        # finally always runs — good for a status message
        print("(write_entry complete)")


def read_entries():
    """Print all diary entries, handling missing or unreadable files."""
    try:
        if not Path(DIARY_FILE).exists():
            print("No diary entries yet. Write your first one!")
            return

        with open(DIARY_FILE, "r") as f:
            content = f.read()

    except FileNotFoundError:
        print("Diary file not found.")
        return
    except IOError as e:
        print(f"Could not read diary: {e}")
        return
    else:
        # Only runs if no exception was raised
        print(f"\n--- Your Diary ---")
        print(content if content.strip() else "(empty)")


# ---------------------------------------------------------------
# Main loop wrapped in try/except KeyboardInterrupt.
# This catches Ctrl+C so the program exits cleanly.
# ---------------------------------------------------------------
print("=== Hardened Diary App ===")

try:
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
            print("Goodbye!")
            break
        else:
            # No crash — just a friendly message for invalid input
            print("Invalid choice. Please enter 1, 2, or 3.")

except KeyboardInterrupt:
    # User pressed Ctrl+C — exit cleanly
    print("\nProgram interrupted. Goodbye!")
except Exception as e:
    # Last-resort catch: something genuinely unexpected happened
    print(f"\nUnexpected error: {e}")
    print("Please report this to your instructor.")
