"""Demonstrates: list comprehensions — compact list creation"""

# ---------------------------------------------------------------
# A list comprehension is a concise way to create a new list
# by transforming or filtering another list (or range).
#
# Basic syntax:
#   new_list = [expression for item in iterable]
#
# With a filter:
#   new_list = [expression for item in iterable if condition]
#
# It's equivalent to a for loop that builds a list, but shorter.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Example 1 — Double every score in a list
# ---------------------------------------------------------------
scores = [40, 55, 70, 85, 90]

# The old way — for loop:
doubled_old = []
for score in scores:
    doubled_old.append(score * 2)

# The list comprehension way — one line!
doubled = [score * 2 for score in scores]

print("Original scores:", scores)
print("Doubled (for loop):", doubled_old)
print("Doubled (comprehension):", doubled)   # same result!

# ---------------------------------------------------------------
# Example 2 — Convert temperatures from Celsius to Fahrenheit
# ---------------------------------------------------------------
celsius = [0, 10, 20, 30, 37, 100]

# formula: F = (C * 9/5) + 32
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("\nCelsius:    ", celsius)
print("Fahrenheit: ", fahrenheit)

# ---------------------------------------------------------------
# Example 3 — Extract first letters of names (make initials)
# ---------------------------------------------------------------
names = ["Alice", "Ryan", "Marcus", "Zara"]

initials = [name[0] for name in names]   # name[0] is the first character
print("\nNames:", names)
print("Initials:", initials)

# ---------------------------------------------------------------
# Example 4 — FILTERING with if
# ---------------------------------------------------------------
all_scores = [88, 43, 95, 61, 79, 12, 55, 71]

# Only keep scores above 60 (passing scores)
passing = [score for score in all_scores if score >= 60]
print("\nAll scores:", all_scores)
print("Passing (>= 60):", passing)

# Only keep even numbers
evens = [n for n in range(1, 21) if n % 2 == 0]
print("\nEven numbers 1-20:", evens)

# ---------------------------------------------------------------
# Example 5 — Combine transformation AND filtering
# ---------------------------------------------------------------
game_names = ["minecraft", "fortnite", "zelda", "fifa", "pokemon"]

# Capitalize names that are longer than 5 characters
long_names = [name.capitalize() for name in game_names if len(name) > 5]
print("\nLong game names (capitalised):", long_names)

# ---------------------------------------------------------------
# Example 6 — Creating a list from a range
# ---------------------------------------------------------------
squares = [n ** 2 for n in range(1, 11)]   # 1², 2², 3², ..., 10²
print("\nSquares 1 to 10:", squares)

# ---------------------------------------------------------------
# Tip: if your comprehension is hard to read, use a for loop instead.
# Readability matters more than being clever!
# ---------------------------------------------------------------
