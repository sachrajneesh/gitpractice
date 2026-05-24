"""
Exercise 04 🟢: Simple Calculator

What you'll practise:
  Arithmetic operators, user input, type conversion, and string comparison.

Task:
  Build a calculator that asks the user for two numbers and an operator,
  then prints the result.

Requirements:
  - Ask the user for a first number (convert to float).
  - Ask the user for an operator: +, -, *, /, //, %, **
  - Ask the user for a second number (convert to float).
  - Compute and print the result with a clear label.
  - Handle division by zero gracefully (print an error message, not a crash).

Example interaction:
  Enter first number: 10
  Enter operator (+, -, *, /, //, %, **): *
  Enter second number: 7
  Result: 10.0 * 7.0 = 70.0

How to run:
  python modules/module04_operators_and_expressions/exercises/exercise04_calculator.py

Hints:
  - Use if/elif chains to check which operator was entered.
  - For division by zero: check if num2 == 0 before dividing.
  - An else at the end can catch unknown operators.

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# Get the two numbers from the user and convert them to floats.
# float() lets the user type decimals like 3.5 as well as whole numbers.
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))

# Use if/elif to pick the right operation based on what the user typed.
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    # Division by zero would crash with ZeroDivisionError — check first.
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

elif operator == "//":
    # Floor division also needs a zero check.
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 // num2
        print(f"Result: {num1} // {num2} = {result}")

elif operator == "%":
    # Modulo (remainder) also cannot have a zero divisor.
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

elif operator == "**":
    result = num1 ** num2
    print(f"Result: {num1} ** {num2} = {result}")

else:
    # The else catches anything that didn't match above.
    print(f"Unknown operator: '{operator}'. Please use +, -, *, /, //, %, or **")
