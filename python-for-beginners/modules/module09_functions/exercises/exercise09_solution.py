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

# ============================================================
# Part A: Calculator functions
# ============================================================

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return a divided by b, or None if b is zero."""
    if b == 0:
        return None   # signal division by zero to the caller
    return a / b

def calculate(a, operator, b):
    """Dispatch to the correct arithmetic function based on operator string."""
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return None   # unknown operator

# --- Calculator interaction ---
print("=== Function Calculator ===")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = calculate(num1, op, num2)

if result is None:
    if op in ("+", "-", "*", "/"):
        print("Error: Cannot divide by zero.")
    else:
        print(f"Unknown operator: '{op}'")
else:
    print(f"Result: {num1} {op} {num2} = {result}")


# ============================================================
# Part B: BMI Calculator
# ============================================================

def bmi(weight_kg, height_m):
    """Return BMI value rounded to 1 decimal place."""
    return round(weight_kg / (height_m ** 2), 1)

def bmi_category(bmi_value):
    """Return the BMI category string for a given BMI value."""
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal weight"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

# --- BMI interaction ---
print("\n=== BMI Calculator ===")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres (e.g. 1.75): "))

bmi_val = bmi(weight, height)
category = bmi_category(bmi_val)

print(f"\nYour BMI: {bmi_val}")
print(f"Category: {category}")
