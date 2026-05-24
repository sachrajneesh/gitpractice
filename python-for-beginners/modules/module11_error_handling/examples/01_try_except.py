"""Demonstrates: basic try/except, catching specific exceptions"""

# ---------------------------------------------------------------
# When Python encounters an error it raises an EXCEPTION.
# Without error handling the program CRASHES and shows a traceback.
#
# try/except lets you CATCH exceptions and handle them gracefully
# instead of crashing.
#
# Structure:
#   try:
#       # code that might fail
#   except SomeError:
#       # code that runs if SomeError happens
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Example 1: Handling invalid input (ValueError) ---
# ---------------------------------------------------------------
# ValueError is raised when you pass the wrong type to a conversion,
# e.g. int("hello") fails because "hello" isn't a number.

print("=== Safe number input ===")
try:
    age = int(input("Enter your age: "))   # this might fail!
    print(f"Your age is {age}. You were born around {2025 - age}.")
except ValueError:
    # This runs only if int() fails (user typed something non-numeric)
    print("That's not a valid number! Please enter digits only.")

# ---------------------------------------------------------------
# --- Example 2: Handling division by zero (ZeroDivisionError) ---
# ---------------------------------------------------------------
print("\n=== Safe division ===")

def safe_divide(a, b):
    """Divide a by b, returning None if b is zero."""
    try:
        result = a / b       # might raise ZeroDivisionError
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

print(safe_divide(10, 2))    # 5.0 — works fine
print(safe_divide(10, 0))    # prints error, returns None

# ---------------------------------------------------------------
# --- Example 3: Handling missing files (FileNotFoundError) ---
# ---------------------------------------------------------------
print("\n=== Safe file read ===")
try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("That file doesn't exist — nothing to read.")

# ---------------------------------------------------------------
# --- Example 4: Handling wrong dictionary key (KeyError) ---
# ---------------------------------------------------------------
print("\n=== Safe dict lookup ===")
scores = {"Ryan": 88, "Alice": 95, "Marcus": 74}
name = "Zara"

try:
    score = scores[name]    # Zara isn't in the dict — KeyError!
    print(f"{name}'s score: {score}")
except KeyError:
    print(f"'{name}' is not in the scores dictionary.")

# Note: for dicts, .get() is often simpler than try/except for this case.

# ---------------------------------------------------------------
# --- Example 5: Using the exception object for details ---
# ---------------------------------------------------------------
print("\n=== Catching exception details ===")
try:
    result = int("not_a_number")
except ValueError as e:
    # 'e' holds the exception object — you can print it for details
    print(f"Caught a ValueError: {e}")
