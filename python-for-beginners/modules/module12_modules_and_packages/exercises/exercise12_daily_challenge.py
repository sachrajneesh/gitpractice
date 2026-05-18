"""
Exercise 12 🟡: Random Daily Challenge Generator

What you'll practise:
  Importing modules (random, datetime), lists, and writing your own module.

Task:
  Build a program that picks a random coding challenge for today from a list,
  displays it with today's date, and saves it to a log file.

Requirements:
  - Store at least 10 challenge descriptions in a list.
  - Use random.choice() to pick one.
  - Display: today's date (formatted nicely) + the challenge.
  - Append the chosen challenge to "challenge_log.txt" with a timestamp.
  - Bonus: put the challenge list in a separate module (challenges.py) and import it.

Example output:
  === Daily Coding Challenge ===
  Date: Monday, 15 January 2024

  Today's challenge:
  Write a function that checks whether a string is a palindrome.

  Challenge saved to challenge_log.txt

How to run:
  python modules/module12_modules_and_packages/exercises/exercise12_daily_challenge.py

Hints:
  - from random import choice
  - from datetime import datetime
  - datetime.now().strftime("%A, %d %B %Y")  gives "Monday, 15 January 2024"
  - Open challenge_log.txt in "a" mode to append.

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# TODO: Step 1 — Import random and datetime
# TODO: Step 2 — Create a list of at least 10 challenge descriptions
# TODO: Step 3 — Pick a random challenge using random.choice()
# TODO: Step 4 — Print today's date and the chosen challenge
# TODO: Step 5 — Append the challenge + timestamp to challenge_log.txt
