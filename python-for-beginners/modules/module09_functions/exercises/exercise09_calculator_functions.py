"""
Exercise 09 🟡: Calculator Functions & BMI Calculator

What you'll practise:
  Defining functions, parameters, return values, default args, and docstrings.

Task:
  Part A — Calculator with functions:
    Rewrite the calculator from Module 04 using separate functions:
    add(a, b), subtract(a, b), multiply(a, b), divide(a, b).
    Each function should return the result (not print it).
    Add a calculate(a, operator, b) dispatcher function that calls the right one.

  Part B — BMI Calculator:
    Write a function bmi(weight_kg, height_m) that returns the BMI value.
    Write a function bmi_category(bmi_value) that returns the category string:
      Under 18.5 → "Underweight"
      18.5–24.9  → "Normal weight"
      25–29.9    → "Overweight"
      30+        → "Obese"
    Ask the user for weight and height and print their BMI and category.

Requirements:
  - Every function must have a one-line docstring.
  - divide() must return None (or raise an error) for division by zero.
  - bmi() should round to 1 decimal place.

How to run:
  python modules/module09_functions/exercises/exercise09_calculator_functions.py

Hints:
  - def add(a, b): return a + b
  - For the dispatcher: if operator == "+": return add(a, b)
  - bmi = weight_kg / (height_m ** 2)

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# --- Part A: Calculator functions ---

# TODO: Step 1 — Define add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# TODO: Step 2 — Define calculate(a, operator, b) that calls the right function
# TODO: Step 3 — Ask user for two numbers and an operator, call calculate(), print result

# --- Part B: BMI Calculator ---

# TODO: Step 4 — Define bmi(weight_kg, height_m) — returns rounded BMI
# TODO: Step 5 — Define bmi_category(bmi_value) — returns category string
# TODO: Step 6 — Ask user for weight and height, print BMI and category
