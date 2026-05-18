"""
Module 01 — Example 04: Common Mistakes

Demonstrates:
  - What SyntaxError looks like and why it happens
  - What NameError looks like and why it happens
  - How to read Python's error messages
  - The most frequent beginner mistakes in this module

IMPORTANT: The broken lines are commented out with # so this file runs without errors.
           Each broken line is followed by an explanation and the correct version.

Run this file to see the correct versions working:
  python modules/module01_getting_started/examples/04_common_mistakes.py
"""

print("=== SyntaxError examples ===")
print()

# --- Mistake 1: Missing closing parenthesis ---
# ERROR: SyntaxError — '(' was never closed
# pint("Hello"

# FIXED: Add the closing parenthesis
print("Hello")


# --- Mistake 2: Forgetting quotes around a string ---
# ERROR: NameError — 'Hello' is not defined (Python thinks it's a variable name)
# print(Hello)

# FIXED: Wrap the text in quotes
print("Hello")


# --- Mistake 3: Wrong quote style — mixing single and double ---
# ERROR: SyntaxError — invalid syntax
# print("Hello')

# FIXED: Use the same type of quote to open and close
print("Hello")
print('Hello')  # both work, but be consistent


# --- Mistake 4: Calling the function with the wrong name ---
# ERROR: NameError — name 'pint' is not defined
# pint("Hello!")

# FIXED: The function is called print, not pint
print("Hello!")


# --- Mistake 5: Forgetting parentheses entirely ---
# In Python 3, print is a function — it MUST have parentheses.
# ERROR: This would print the function object itself, not your text.
# In Python 2 (old!), print "Hello" was valid. In Python 3, it is not.
# print "Hello"

# FIXED:
print("Hello")


print()
print("=== How to read an error message ===")
print()

# Python error messages have three useful parts:
#
# Traceback (most recent call last):
#   File "example.py", line 23, in <module>
#     pint("Hello!")         <-- the line that caused the error
# NameError: name 'pint' is not defined   <-- what went wrong
#
# Read it bottom-up:
#   1. Bottom line: what type of error it is and a short description
#   2. Middle lines: which file and line number the error occurred on
#   3. The indented line: shows you the actual code that failed
#
# Armed with this, you can usually find and fix the problem in under a minute.

print("Tips for fixing errors:")
print("  1. Read the LAST line of the error message first.")
print("  2. Note the line number — Python tells you exactly where to look.")
print("  3. Compare your code with a working example character by character.")
print("  4. Check for typos, missing quotes, and missing parentheses.")
print()
print("Errors are normal. Every programmer sees them every day.")
print("Getting good at fixing errors is as important as writing code.")
