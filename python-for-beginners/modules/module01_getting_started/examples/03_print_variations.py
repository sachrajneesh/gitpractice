"""
Module 01 — Example 03: print() Variations

Demonstrates:
  - Printing multiple arguments with default separator (space)
  - Changing the separator with sep=
  - Changing the line ending with end=
  - Combining sep and end together
  - Printing blank lines

Run this file:
  python modules/module01_getting_started/examples/03_print_variations.py
"""

print("=== Default behaviour ===")

# Default: Python puts a space between arguments and a newline at the end
print("apple", "banana", "cherry")
# Output: apple banana cherry

print("Name:", "Alice")
# Output: Name: Alice

print()  # prints a blank line

# ---

print("=== Changing sep ===")

# Use a comma-space as the separator
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

# Use a dash
print("2024", "01", "15", sep="-")
# Output: 2024-01-15

# Use no separator at all (empty string)
print("J", "a", "m", "e", "s", sep="")
# Output: James

# Use a newline as separator — each item on its own line
print("First", "Second", "Third", sep="\n")
# Output:
# First
# Second
# Third

print()

# ---

print("=== Changing end ===")

# Default end is "\n" (newline). Change it to stay on the same line.
print("Loading", end="")
print("...", end="")
print(" Done!")
# Output: Loading... Done!

# Use a space instead of newline to join lines
print("Step 1", end=" -> ")
print("Step 2", end=" -> ")
print("Step 3")
# Output: Step 1 -> Step 2 -> Step 3

print()

# ---

print("=== Combining sep and end ===")

print("Mon", "Tue", "Wed", sep=" | ", end=" (weekdays)\n")
# Output: Mon | Tue | Wed (weekdays)

print("R", "G", "B", sep="+", end="=colour\n")
# Output: R+G+B=colour

print()

# ---

print("=== Practical uses ===")

# Building a simple table header
print("Name", "Age", "Score", sep="\t")
print("Alice", 17, 95, sep="\t")
print("Bob", 16, 88, sep="\t")
print("Carol", 18, 92, sep="\t")
