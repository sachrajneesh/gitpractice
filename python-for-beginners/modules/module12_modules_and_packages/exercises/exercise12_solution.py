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

from random import choice
from datetime import datetime

# A list of 12 beginner-friendly Python coding challenges.
CHALLENGES = [
    "Write a function that checks whether a string is a palindrome.",
    "Write a function that counts how many vowels are in a sentence.",
    "Create a list of 10 random numbers and print the min, max, and average.",
    "Write a function that reverses a list without using .reverse().",
    "Build a simple number guessing game with a maximum of 5 tries.",
    "Write a function that returns True if a number is prime.",
    "Create a dictionary that maps each letter in your name to its position.",
    "Write a function that takes a list of scores and returns the letter grade average.",
    "Build a simple password generator using the random module.",
    "Write a function that removes all duplicate items from a list.",
    "Create a temperature converter (Celsius ↔ Fahrenheit) with a menu.",
    "Write a function that finds the two numbers in a list that add up to a target.",
]

# Pick today's challenge randomly.
todays_challenge = choice(CHALLENGES)

# Format today's date nicely.
today_str = datetime.now().strftime("%A, %d %B %Y")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# Display the challenge in the terminal.
print("=" * 40)
print("  Daily Coding Challenge")
print("=" * 40)
print(f"Date: {today_str}")
print()
print("Today's challenge:")
print(f"  {todays_challenge}")
print()

# Append the challenge to the log file with a timestamp.
log_entry = f"[{timestamp}] {todays_challenge}\n"
log_file = "challenge_log.txt"

with open(log_file, "a") as f:
    f.write(log_entry)

print(f"Challenge saved to {log_file}")
