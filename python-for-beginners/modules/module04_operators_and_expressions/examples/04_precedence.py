"""Demonstrates: operator precedence and how brackets change results"""

# ---------------------------------------------------------------
# Operator Precedence — Who goes first?
#
# Just like in maths, Python follows a specific order when
# evaluating expressions. This is called PEMDAS / BODMAS:
#
#   1. ()    — Parentheses (brackets) — HIGHEST priority
#   2. **    — Exponentiation
#   3. *, /, //, %  — Multiplication, Division (left to right)
#   4. +, -  — Addition, Subtraction (left to right) — LOWEST
#
# When in doubt: USE BRACKETS. They make your intent clear.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Example 1 — Addition before multiplication? No!
# ---------------------------------------------------------------
# Without brackets, * happens BEFORE +
result_a = 2 + 3 * 4       # Python does: 2 + (3 * 4) = 2 + 12 = 14
print(f"2 + 3 * 4 = {result_a}")   # 14

# With brackets we force addition first
result_b = (2 + 3) * 4     # Python does: (5) * 4 = 20
print(f"(2 + 3) * 4 = {result_b}")  # 20

# ---------------------------------------------------------------
# Example 2 — Calculating a game score
# ---------------------------------------------------------------
base_points = 100
multiplier = 3
bonus = 50

# WRONG interpretation (no brackets): bonus added AFTER multiplying
score_wrong = base_points + bonus * multiplier
# Python sees: 100 + (50 * 3) = 100 + 150 = 250
print(f"Without brackets: {score_wrong}")   # 250

# CORRECT interpretation (with brackets): add bonus to base THEN multiply
score_correct = (base_points + bonus) * multiplier
# Python sees: (100 + 50) * 3 = 150 * 3 = 450
print(f"With brackets:    {score_correct}")  # 450

# ---------------------------------------------------------------
# Example 3 — Exponentiation has higher priority than unary minus
# ---------------------------------------------------------------
# This is a classic surprise!
result_no_brackets = -2 ** 2    # Python does: -(2**2) = -(4) = -4  ← not 4!
result_with_brackets = (-2) ** 2 # Python does: (-2)*(-2) = 4
print(f"\n-2 ** 2    = {result_no_brackets}")    # -4
print(f"(-2) ** 2  = {result_with_brackets}")   # 4

# ---------------------------------------------------------------
# Example 4 — Mixed arithmetic in a real calculation
# ---------------------------------------------------------------
# Average test score: add all scores, divide by count
# With three scores: 88, 74, 95
# WRONG — without brackets:
avg_wrong = 88 + 74 + 95 / 3   # Python: 88 + 74 + (95/3) = 193.67
print(f"\nWrong average: {avg_wrong:.2f}")     # 193.67

# CORRECT — brackets force the addition first:
avg_correct = (88 + 74 + 95) / 3   # (257) / 3 = 85.67
print(f"Correct average: {avg_correct:.2f}")  # 85.67

# ---------------------------------------------------------------
# Example 5 — Logical operators have lower precedence than comparisons
# ---------------------------------------------------------------
age = 17
score = 88

# Python evaluates comparisons first, THEN logical operators
# So this works as expected:
result = age >= 16 and score > 80
# Python sees: (age >= 16) and (score > 80) = True and True = True
print(f"\nAge >= 16 AND score > 80: {result}")   # True

# ---------------------------------------------------------------
# Golden rule: when unsure, add brackets.
# Extra brackets never hurt — they only add clarity!
# ---------------------------------------------------------------
tip = 15.00
meal = 42.50
tax_rate = 0.08

# Clear and unambiguous with brackets:
total = (meal * (1 + tax_rate)) + tip
print(f"\nMeal total with tax and tip: ${total:.2f}")  # $60.90
