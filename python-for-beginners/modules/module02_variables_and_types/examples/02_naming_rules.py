"""
Module 02 — Example 02: Naming Rules

Demonstrates:
  - Valid variable names (these work)
  - Invalid variable names (commented out — these cause errors)
  - The snake_case convention
  - Why descriptive names matter

Run this file:
  python modules/module02_variables_and_types/examples/02_naming_rules.py
"""

print("=== Valid variable names ===")

# Letters, digits, and underscores — all fine
player_name = "Kofi"
score_1 = 100
high_score_2024 = 9999
_private_note = "internal use"    # leading underscore is valid (convention: private)
GRAVITY = 9.81                    # ALL_CAPS convention means "constant, don't change"

print("player_name:", player_name)
print("score_1:", score_1)
print("high_score_2024:", high_score_2024)
print("GRAVITY:", GRAVITY)
print()

# ---
print("=== Invalid names (commented out — would cause errors) ===")

# ERROR: cannot start with a digit
# 1st_place = "Kofi"
# Output: SyntaxError: invalid decimal literal

# ERROR: no spaces in variable names
# player name = "Kofi"
# Output: SyntaxError: invalid syntax

# ERROR: hyphens are not allowed (Python sees it as subtraction)
# player-score = 100
# Output: SyntaxError: cannot assign to expression here

# ERROR: Python reserved keywords cannot be used as variable names
# Keywords include: if, else, for, while, def, class, return, True, False, None, and, or, not, in, is, ...
# class = "Math"
# Output: SyntaxError: invalid syntax

print("(All invalid names are commented out — they would cause errors)")
print()

# ---
print("=== The snake_case convention ===")

# Bad: hard to read
s = "Alice"
hn = "Alice Johnson"
hsc = 9999

# Better: single words are fine as-is
name = "Alice"
score = 100

# Best: multiple words use underscores (snake_case)
full_name = "Alice Johnson"
high_score = 9999
is_game_over = False
total_items_in_cart = 5
player_1_score = 80
player_2_score = 95

print("full_name:", full_name)
print("high_score:", high_score)
print("is_game_over:", is_game_over)
print()

# ---
print("=== Case sensitivity ===")

# These are THREE DIFFERENT variables
score = 10
Score = 20
SCORE = 30

print("score:", score)     # 10
print("Score:", Score)     # 20
print("SCORE:", SCORE)     # 30

print()
print("Convention: use all-lowercase snake_case for regular variables.")
print("Reserve ALL_CAPS for constants (values that should never change).")
