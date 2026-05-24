"""Demonstrates: the math module — sqrt, ceil, floor, pi, pow"""

# ---------------------------------------------------------------
# The math module provides mathematical functions and constants.
# It's part of Python's standard library — always available.
# ---------------------------------------------------------------

import math

# ---------------------------------------------------------------
# --- Constants ---
# ---------------------------------------------------------------
print("=== Constants ===")
print(f"math.pi  = {math.pi}")     # 3.141592653589793 — the ratio of circumference to diameter
print(f"math.e   = {math.e}")      # 2.718281828459045 — Euler's number (base of natural log)
print(f"math.inf = {math.inf}")    # positive infinity
print(f"math.tau = {math.tau}")    # 2 * pi

# ---------------------------------------------------------------
# --- sqrt — square root ---
# ---------------------------------------------------------------
print("\n=== math.sqrt() ===")
print(f"sqrt(16)  = {math.sqrt(16)}")   # 4.0
print(f"sqrt(2)   = {math.sqrt(2):.4f}")  # 1.4142 — useful in geometry

# Pythagoras: hypotenuse of right triangle with sides 3 and 4
a, b = 3, 4
hypotenuse = math.sqrt(a**2 + b**2)
print(f"Hypotenuse of {a}-{b} triangle: {hypotenuse}")   # 5.0

# ---------------------------------------------------------------
# --- ceil and floor — rounding ---
# ---------------------------------------------------------------
print("\n=== ceil and floor ===")
price = 4.30
print(f"price = {price}")
print(f"math.ceil({price})  = {math.ceil(price)}")    # 5  — ALWAYS rounds UP
print(f"math.floor({price}) = {math.floor(price)}")   # 4  — ALWAYS rounds DOWN

# Practical: how many full boxes of 12 do you need for 50 items?
items = 50
box_size = 12
boxes_needed = math.ceil(items / box_size)   # can't have partial boxes!
print(f"\n{items} items, {box_size} per box: need {boxes_needed} boxes")  # 5

# ---------------------------------------------------------------
# --- math.pow — exponentiation ---
# ---------------------------------------------------------------
print("\n=== math.pow() ===")
# math.pow(x, y) is like x ** y but ALWAYS returns a float
print(f"math.pow(2, 10) = {math.pow(2, 10)}")    # 1024.0
print(f"2 ** 10         = {2 ** 10}")             # 1024 (int)

# Compound interest: A = P(1 + r)^t
principal = 1000
rate = 0.05    # 5% annual interest
years = 10
final_amount = principal * math.pow(1 + rate, years)
print(f"\n£{principal} invested at {rate*100:.0f}% for {years} years: £{final_amount:.2f}")

# ---------------------------------------------------------------
# --- Other useful math functions ---
# ---------------------------------------------------------------
print("\n=== Other functions ===")
print(f"math.abs(-5)   via abs(-5)   = {abs(-5)}")   # abs() is a built-in, not in math
print(f"math.log(100)               = {math.log(100):.4f}")   # natural log
print(f"math.log10(100)             = {math.log10(100)}")     # log base 10 → 2.0
print(f"math.factorial(5)           = {math.factorial(5)}")   # 5! = 120
print(f"math.gcd(12, 8)             = {math.gcd(12, 8)}")     # greatest common divisor → 4
print(f"math.degrees(math.pi)       = {math.degrees(math.pi)}")   # radians → degrees: 180.0
print(f"math.radians(180)           = {math.radians(180):.4f}")   # degrees → radians: pi
