"""
Module 03 — Example 02: Multi-line Strings

Demonstrates:
  - Triple-quoted strings spanning multiple lines
  - How leading/trailing newlines work in triple quotes
  - Using triple-quoted strings for docstrings
  - Practical uses: email templates, menus, banners

Run this file:
  python modules/module03_strings/examples/02_multiline.py
"""

print("=== Basic triple-quoted string ===")

poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

print(poem)
print()

# ---
print("=== Triple single quotes work too ===")

haiku = '''An old silent pond...
A frog jumps into the pond.
Splash! Silence again.'''

print(haiku)
print()

# ---
print("=== Watch out for leading newlines ===")

# If you open with """ and immediately press Enter, there's a leading newline
with_leading_newline = """
This starts with a blank line."""

print(repr(with_leading_newline))  # repr() shows the actual characters
# Output: '\nThis starts with a blank line.'

# To avoid it, start the text immediately after the opening quotes
no_leading_newline = """This does NOT start with a blank line."""
print(repr(no_leading_newline))
print()

# ---
print("=== Practical use: email template ===")

recipient = "Alice"
sender = "Bob"
subject = "Python Progress"

email = f"""Hi {recipient},

Just wanted to let you know I finished Module 03 of the Python course!

Strings are making a lot more sense now. The f-string section was
especially useful.

Best,
{sender}"""

print(email)
print()

# ---
print("=== Practical use: text menu ===")

menu = """
============================
       MAIN MENU
============================
  1. New Game
  2. Load Game
  3. Settings
  4. Quit
============================
"""

print(menu)

# ---
print("=== Docstrings ===")

# Triple-quoted strings at the top of a function or file are called docstrings.
# Python stores them and tools use them for documentation.
# Every example file in this course has a docstring — look at the top of this file.

def calculate_average(numbers):
    """
    Calculate and return the average of a list of numbers.

    This is a docstring — it describes what the function does,
    what it takes as input, and what it returns.
    """
    return sum(numbers) / len(numbers)

# You can access the docstring programmatically:
print("Function docstring:")
print(calculate_average.__doc__)
