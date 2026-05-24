"""Demonstrates: appending to files vs overwriting"""

# ---------------------------------------------------------------
# The difference between "w" and "a" mode:
#
#   "w" (write)  — opens file, DELETES all existing content,
#                  then writes from the beginning.
#                  Like a blank page every time.
#
#   "a" (append) — opens file, keeps existing content,
#                  adds new content at the END.
#                  Like writing in a journal — previous entries stay.
#
# Use "a" for logs, diaries, any ongoing record.
# Use "w" when you want to replace the file contents entirely.
# ---------------------------------------------------------------

import os   # for cleanup at the end

# ---------------------------------------------------------------
# --- Demonstrate "w" mode (overwrite) ---
# ---------------------------------------------------------------
log_file = "game_log.txt"

# First write
with open(log_file, "w") as f:
    f.write("Game started.\n")
    f.write("Player joined: Ryan\n")
print("First write done.")

# Second "w" write — this REPLACES everything from the first write!
with open(log_file, "w") as f:
    f.write("This OVERWRITES the previous content.\n")

with open(log_file, "r") as f:
    print("\nContents after two 'w' opens:")
    print(f.read())
# You only see the second write — the first is gone!

# ---------------------------------------------------------------
# --- Demonstrate "a" mode (append) ---
# ---------------------------------------------------------------
diary_file = "diary.txt"

# First entry
with open(diary_file, "a") as f:
    f.write("Day 1: Started learning Python. It's pretty fun!\n")
print("First diary entry appended.")

# Second entry — "a" mode KEEPS the previous entry
with open(diary_file, "a") as f:
    f.write("Day 2: Learned about for loops and lists. Brain is full.\n")
print("Second diary entry appended.")

# Third entry
with open(diary_file, "a") as f:
    f.write("Day 3: File I/O today. My notes are saved to a real file!\n")
print("Third diary entry appended.")

# Read the entire diary — should have all 3 entries
print("\n--- Your Diary ---")
with open(diary_file, "r") as f:
    print(f.read())

# ---------------------------------------------------------------
# --- Practical pattern: append a timestamped entry ---
# ---------------------------------------------------------------
from datetime import datetime

def append_log_entry(filename, message):
    """Append a timestamped message to a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(filename, "a") as f:
        f.write(entry)
    print(f"Logged: {entry.strip()}")

append_log_entry("game_log.txt", "Level 3 completed.")
append_log_entry("game_log.txt", "Achievement unlocked: Python Padawan")

print("\nGame log contents:")
with open("game_log.txt", "r") as f:
    print(f.read())

# Clean up demo files
os.remove(diary_file)
os.remove("game_log.txt")
print("Demo files removed.")
