"""
Module 02 — Example 04: Type Gotchas

Demonstrates:
  - The classic error: trying to add a number and a string
  - How to fix it using int(), float(), or str()
  - Other surprising type behaviours beginners often hit
  - Using type() to investigate before assuming

Run this file:
  python modules/module02_variables_and_types/examples/04_type_gotchas.py
"""

print("=== Gotcha 1: adding a number and a string ===")
print()

# This looks like it should work, but it crashes with TypeError:
# user_input = "5"          # input() always returns a string
# total = 10 + user_input   # ERROR: unsupported operand type(s) for +: 'int' and 'str'

# Why? Because "5" (string) and 5 (integer) are completely different types.
# Python does not automatically guess what you meant.

# THE FIX: convert the string to an integer first
user_input = "5"            # pretend this came from input()
total = 10 + int(user_input)
print("10 + int('5') =", total)   # 15
print()

# ---
print("=== Gotcha 2: joining a string and a number with + ===")
print()

player_name = "Alice"
score = 95

# This crashes:
# message = "Score: " + score    # ERROR: can only concatenate str (not "int") to str

# THE FIX: convert the integer to a string first
message = "Score: " + str(score)
print(message)    # Score: 95

# Better fix (Module 03): use an f-string
message_v2 = f"Score: {score}"
print(message_v2)  # Score: 95
print()

# ---
print("=== Gotcha 3: integer division vs float division ===")
print()

# Regular division (/) always returns a float
print(10 / 2)     # 5.0   — not 5 (it's a float!)
print(7 / 2)      # 3.5

# Floor division (//) returns an integer (rounds down)
print(10 // 2)    # 5     — integer result
print(7 // 2)     # 3     — rounds DOWN (not rounds to nearest)
print(-7 // 2)    # -4    — still rounds DOWN (away from zero for negatives)
print()

# ---
print("=== Gotcha 4: float precision ===")
print()

# Floats are not always exactly what you expect due to how computers store them
print(0.1 + 0.2)           # 0.30000000000000004  (not 0.3!)
print(0.1 + 0.2 == 0.3)    # False  — surprising but correct!

# For currency, use the round() function or the decimal module (covered later)
result = round(0.1 + 0.2, 2)
print("Rounded:", result)  # 0.3
print()

# ---
print("=== Gotcha 5: int() does not round — it truncates ===")
print()

print(int(3.9))    # 3   — NOT 4! int() strips the decimal, it does NOT round
print(int(3.1))    # 3
print(int(-3.9))   # -3  — strips the decimal (towards zero)

# To round properly, use round()
print(round(3.9))  # 4
print(round(3.5))  # 4   (Python uses "banker's rounding" — rounds to nearest even)
print(round(2.5))  # 2   (banker's rounding: 2 is the nearest even)
print()

# ---
print("=== Use type() when in doubt ===")
print()

mystery = "42"
print("mystery:", mystery)
print("type(mystery):", type(mystery))

# Always check the type before doing arithmetic with values from input()
# or from external sources.
