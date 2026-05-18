"""
Module 02 — Example 03: input() Basics

Demonstrates:
  - Using input() to get text from the user
  - Why input() ALWAYS returns a string
  - Converting user input to int and float
  - Combining input() and conversion in one line

INTERACTIVE: This file asks for your input. Run it and type your answers.

Run this file:
  python modules/module02_variables_and_types/examples/03_input_basics.py
"""

print("=== Basic input() ===")
print()

# input() pauses the program and waits for the user to type something.
# Whatever they type (and press Enter) is returned as a STRING.
name = input("What is your name? ")

print("Hello,", name)
print("Type of name:", type(name))     # always <class 'str'>
print()

# ---
print("=== input() always returns a string ===")
print()

age_as_string = input("How old are you? ")

# age_as_string is a STRING, even if the user typed a number
print("You typed:", age_as_string)
print("Type:", type(age_as_string))   # <class 'str'>  — not int!

# We CANNOT do maths with it yet:
# print(age_as_string + 1)    # ERROR: TypeError — can't add int to str
print()

# ---
print("=== Converting input to a number ===")
print()

age_text = input("Enter your age again: ")
age = int(age_text)                    # convert the string "17" to the integer 17

print("As a string:", age_text, "  type:", type(age_text))
print("As an integer:", age, "  type:", type(age))
print("In ten years you will be:", age + 10)
print()

# ---
print("=== Shorthand: convert immediately ===")
print()

# Combine input() and int() in one step — very common in real code
birth_year = int(input("What year were you born? "))
current_year = 2024
approximate_age = current_year - birth_year

print(f"You were born in {birth_year}.")
print(f"You are approximately {approximate_age} years old.")
print()

# ---
print("=== float() for decimal input ===")
print()

height = float(input("Enter your height in metres (e.g. 1.72): "))
print(f"Height: {height} m")
print(f"Type: {type(height)}")         # <class 'float'>

# Now we can do float arithmetic
height_cm = height * 100
print(f"That is {height_cm} cm.")
