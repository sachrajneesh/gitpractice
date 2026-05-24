"""
Exercise 05 🟡: Grade Classifier

What you'll practise:
  if/elif/else chains, comparison operators, and printing conditional messages.

Task:
  Build a program that asks for a numeric exam score (0-100) and prints
  the corresponding letter grade and an encouraging message.

Requirements:
  - Ask for a score using input() and convert to int.
  - Use if/elif/else to determine the grade:
      90-100 → A ("Outstanding!")
      80-89  → B ("Great work!")
      70-79  → C ("Solid effort.")
      60-69  → D ("Passing, but aim higher.")
      0-59   → F ("Let's review and try again.")
  - If the score is outside 0-100, print an error message.
  - Print the grade and message on separate lines.

Example interaction:
  Enter your score (0-100): 87
  Grade: B
  Great work!

How to run:
  python modules/module05_control_flow/exercises/exercise05_grade_classifier.py

Hints:
  - Start with the highest range (90-100) and work down.
  - An elif score < 0 or score > 100 check can catch invalid input.
  - You can store the grade in a variable and print it at the end.

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# Get the score and convert to int (int because scores are whole numbers).
score = int(input("Enter your score (0-100): "))

# Validate first — reject anything outside the valid range.
if score < 0 or score > 100:
    print("Invalid score! Please enter a number between 0 and 100.")

# Check from highest to lowest so ranges don't overlap.
elif score >= 90:
    print("Grade: A")
    print("Outstanding!")

elif score >= 80:
    print("Grade: B")
    print("Great work!")

elif score >= 70:
    print("Grade: C")
    print("Solid effort.")

elif score >= 60:
    print("Grade: D")
    print("Passing, but aim higher.")

else:
    # Catches 0-59 — the only remaining valid range.
    print("Grade: F")
    print("Let's review and try again.")
