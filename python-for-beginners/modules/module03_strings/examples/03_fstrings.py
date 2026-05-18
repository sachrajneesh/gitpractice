"""
Module 03 — Example 03: f-strings

Demonstrates:
  - Basic f-string syntax
  - Embedding variables
  - Embedding expressions and function calls
  - Number formatting: decimal places, padding, commas
  - String alignment for neat output columns
  - Nested quotes inside f-strings

Run this file:
  python modules/module03_strings/examples/03_fstrings.py
"""

print("=== Basic f-strings ===")

name = "Kofi"
age = 18
city = "Accra"

# Prefix with f, then use {variable_name} to embed
print(f"Hello, my name is {name}.")
print(f"I am {age} years old and I live in {city}.")
print()

# ---
print("=== Expressions inside {} ===")

# You can put any expression, not just a variable name
print(f"Next year I will be {age + 1}.")
print(f"My name in uppercase: {name.upper()}")
print(f"The product of 12 and 7 is {12 * 7}.")
print(f"Is name longer than 3 chars? {len(name) > 3}")
print()

# ---
print("=== Number formatting ===")

pi = 3.14159265
price = 1234567.89
score = 95

# :.Nf — fixed decimal places
print(f"Pi to 2 decimal places: {pi:.2f}")    # 3.14
print(f"Pi to 4 decimal places: {pi:.4f}")    # 3.1416 (rounds)

# :, — thousands separator
print(f"Price with commas: ${price:,.2f}")    # $1,234,567.89

# :% — percentage
rate = 0.875
print(f"Pass rate: {rate:.1%}")               # 87.5%

# :e — scientific notation
big_number = 1234567890
print(f"Scientific: {big_number:.2e}")        # 1.23e+09

print()

# ---
print("=== String alignment and padding ===")

# :<N — left-align in a field of width N
# :>N — right-align in a field of width N
# :^N — centre in a field of width N

print(f"{'Name':<15} {'Score':>5} {'Grade':^7}")
print("-" * 30)
print(f"{'Alice':<15} {95:>5} {'A':^7}")
print(f"{'Bob':<15} {82:>5} {'B':^7}")
print(f"{'Carol':<15} {78:>5} {'C':^7}")
print(f"{'Damilola':<15} {91:>5} {'A':^7}")
print()

# ---
print("=== Using quotes inside f-strings ===")

# If your f-string uses double quotes, use single quotes inside {}
language = "Python"
print(f"I am learning {'Python'!r}.")   # !r adds repr() — shows quotes

# Or just use the variable
print(f"Language: {language}")

# Using an expression that returns a string
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {', '.join(fruits)}")
print()

# ---
print("=== Multi-line f-string ===")

first_name = "Amara"
last_name = "Okafor"
gpa = 3.87

card = f"""
Student Report
--------------
Name  : {first_name} {last_name}
GPA   : {gpa:.2f}
Status: {"Honours" if gpa >= 3.5 else "Good standing"}
"""
print(card)
