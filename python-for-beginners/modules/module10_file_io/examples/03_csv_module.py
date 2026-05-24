"""Demonstrates: reading and writing CSV files with the csv module"""

# ---------------------------------------------------------------
# CSV = Comma-Separated Values
# It's one of the most common file formats for storing tabular data
# (like a spreadsheet saved as plain text).
#
# Example contents of scores.csv:
#   name,score,grade
#   Ryan,88,B
#   Alice,95,A
#   Marcus,74,C
#
# Python's built-in csv module handles quoting, escaping, and
# different delimiters automatically — much safer than splitting
# lines on commas manually.
# ---------------------------------------------------------------

import csv   # built-in module — no install needed
import os    # for cleanup

scores_file = "scores.csv"

# ---------------------------------------------------------------
# --- Writing a CSV file ---
# ---------------------------------------------------------------
print("Writing scores.csv...")

# The data we want to save — a list of lists (rows)
students = [
    ["name", "score", "grade"],   # header row
    ["Ryan", 88, "B"],
    ["Alice", 95, "A"],
    ["Marcus", 74, "C"],
    ["Zara", 61, "D"],
    ["Sam", 42, "F"],
]

# newline="" is important on Windows — prevents extra blank lines
with open(scores_file, "w", newline="") as f:
    writer = csv.writer(f)          # create a writer object
    writer.writerows(students)       # writerows writes ALL rows at once
    # (use writer.writerow(row) to write one row at a time)

print(f"Wrote {len(students) - 1} student records (+ header).")

# ---------------------------------------------------------------
# --- Reading a CSV file ---
# ---------------------------------------------------------------
print("\nReading scores.csv:")

with open(scores_file, "r", newline="") as f:
    reader = csv.reader(f)          # create a reader object
    header = next(reader)           # next() reads ONE row — we get the header
    print(f"Header: {header}")
    print()

    for row in reader:              # loop over remaining rows
        name, score, grade = row    # unpack each row into variables
        print(f"  {name}: {score} (Grade {grade})")

# ---------------------------------------------------------------
# --- DictReader — read rows as dictionaries ---
# ---------------------------------------------------------------
print("\nUsing DictReader (rows as dicts):")

with open(scores_file, "r", newline="") as f:
    reader = csv.DictReader(f)      # header row becomes the dict keys automatically
    for row in reader:
        # Each row is a dict: {"name": "Ryan", "score": "88", "grade": "B"}
        # Note: all values come back as STRINGS — convert numbers as needed
        print(f"  {row['name']} scored {int(row['score'])} → Grade {row['grade']}")

# ---------------------------------------------------------------
# --- DictWriter — write using field names ---
# ---------------------------------------------------------------
expenses_file = "expenses.csv"
print(f"\nWriting {expenses_file}...")

fieldnames = ["date", "item", "amount"]
expenses = [
    {"date": "2024-01-15", "item": "Pizza", "amount": 12.99},
    {"date": "2024-01-15", "item": "Bus pass", "amount": 3.50},
    {"date": "2024-01-16", "item": "Game", "amount": 29.99},
]

with open(expenses_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()            # writes the header row automatically
    writer.writerows(expenses)      # writes all data rows

print(f"Expenses saved to {expenses_file}.")

# Read it back to confirm
with open(expenses_file, "r", newline="") as f:
    print("\nContents of expenses.csv:")
    print(f.read())

# Clean up
os.remove(scores_file)
os.remove(expenses_file)
print("Demo files removed.")
