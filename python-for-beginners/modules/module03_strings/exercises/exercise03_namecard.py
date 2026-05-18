"""
Exercise 03 🟢: Name Card Generator

What you'll practise:
  f-strings, string methods (upper, center, len), and building formatted
  multi-line output with a visible border.

Task:
  Build a program that asks the user for their first name and last name,
  then prints a formatted name card — like a business card — in the terminal.

Requirements:
  - Ask for first name and last name using input().
  - Display the full name in UPPERCASE in the centre of the card.
  - Display the initials below the name (e.g. "A. J." for Alice Johnson).
  - Add a decorative border around the card using "+" corners and "-"/"| " sides.
  - The border width should adapt to the length of the name (not hardcoded).

Expected output (for "Alice Johnson"):
  +--------------------+
  |   ALICE JOHNSON    |
  |       A. J.        |
  +--------------------+

How to run:
  python modules/module03_strings/exercises/exercise03_namecard.py

Hints:
  - str.upper() converts to uppercase.
  - str.center(width) centres text in a field of given width.
  - Initials: first_name[0] and last_name[0] give you the first letters.
  - Card width: len(full_name) + some padding (e.g. + 6).
  - Border line: "+" + "-" * (width) + "+"
  - Side line:   "| " + text.center(width - 2) + " |"   (adjust padding to taste)

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# TODO: Step 1 — Ask for first name and last name using input()
# TODO: Step 2 — Build the full name string and initials string
# TODO: Step 3 — Calculate the card width based on the name length
# TODO: Step 4 — Print the top border
# TODO: Step 5 — Print the name row (centred, uppercase, with side borders)
# TODO: Step 6 — Print the initials row (centred, with side borders)
# TODO: Step 7 — Print the bottom border
