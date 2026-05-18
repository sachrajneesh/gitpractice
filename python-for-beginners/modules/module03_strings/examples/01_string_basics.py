"""
Module 03 — Example 01: String Basics

Demonstrates:
  - String literals with single and double quotes
  - When to use one versus the other
  - Escape characters: \n, \t, \\, \", \'
  - The raw string prefix r"..." to disable escape processing

Run this file:
  python modules/module03_strings/examples/01_string_basics.py
"""

print("=== Single vs double quotes ===")

# Both are identical — use whichever you prefer
greeting_double = "Hello, world!"
greeting_single = 'Hello, world!'
print(greeting_double)
print(greeting_single)
print()

# When your string contains a double quote, use single quotes on the outside
quote = 'Albert said, "Imagination is more important than knowledge."'
print(quote)

# When your string contains an apostrophe, use double quotes on the outside
sentence = "It's a great day to learn Python."
print(sentence)
print()

# ---
print("=== Escape characters ===")
print()

# \n — newline (moves to next line)
print("Line 1\nLine 2\nLine 3")
print()

# \t — tab (adds a horizontal tab space)
print("Name:\tAlice")
print("Score:\t95")
print()

# \\ — a literal backslash
print("File path: C:\\Users\\Alice\\Documents")
print()

# \" — a double quote inside a double-quoted string
print("She said, \"Don't give up!\"")

# \' — a single quote inside a single-quoted string
print('It\'s never too late to learn.')
print()

# ---
print("=== Combining escape characters ===")

# A receipt-style output using \t and \n
receipt = "RECEIPT\n--------\nCoffee:\t$3.50\nCake:\t$4.00\nTotal:\t$7.50"
print(receipt)
print()

# ---
print("=== Raw strings (r prefix) ===")

# In a raw string, backslashes are treated literally — no escape processing.
# Useful for file paths on Windows and regular expressions.
windows_path = r"C:\Users\Alice\Documents\notes.txt"
print(windows_path)    # C:\Users\Alice\Documents\notes.txt

# Without r prefix, backslash sequences are interpreted as escape characters.
# \U starts a Unicode escape (causes SyntaxError in Python 3 if not valid).
# \n becomes a newline, \t becomes a tab. This is a common Windows path bug.
# Example (commented out — would cause a SyntaxError or produce wrong output):
# wrong_path = "C:\Users\Alice\Documents\notes.txt"
# ^^ Python sees \U as a Unicode escape and raises SyntaxError.
# Always use r"..." or double backslashes for Windows paths:
double_slash_path = "C:\\Users\\Alice\\Documents\\notes.txt"
print(double_slash_path)   # C:\Users\Alice\Documents\notes.txt  (same as raw string)
