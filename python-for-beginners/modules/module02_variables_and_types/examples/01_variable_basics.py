"""
Module 02 — Example 01: Variable Basics

Demonstrates:
  - Creating variables of each basic type (int, float, str, bool, None)
  - Printing variable values
  - Using type() to check what type a value is
  - Reassigning a variable (changing its value)

Run this file:
  python modules/module02_variables_and_types/examples/01_variable_basics.py
"""

# --- int (integer) ---
score = 95
year_born = 2007
negative_temp = -12

print("=== Integers ===")
print("score:", score)            # score: 95
print("year_born:", year_born)    # year_born: 2007
print("type:", type(score))       # type: <class 'int'>
print()

# --- float (floating-point number) ---
height_metres = 1.75
price = 4.99
pi_approx = 3.14159

print("=== Floats ===")
print("height_metres:", height_metres)
print("price:", price)
print("type:", type(height_metres))    # <class 'float'>
print()

# --- str (string) ---
first_name = "Maria"
city = "Nairobi"
favourite_food = 'jollof rice'         # single quotes work too

print("=== Strings ===")
print("first_name:", first_name)
print("city:", city)
print("favourite_food:", favourite_food)
print("type:", type(first_name))       # <class 'str'>
print()

# --- bool (boolean) ---
is_logged_in = True
has_won = False
game_over = False

print("=== Booleans ===")
print("is_logged_in:", is_logged_in)
print("has_won:", has_won)
print("type:", type(is_logged_in))     # <class 'bool'>
print()

# --- None ---
middle_name = None          # Maria has no middle name on file
last_result = None          # no result calculated yet

print("=== None ===")
print("middle_name:", middle_name)     # None
print("type:", type(middle_name))      # <class 'NoneType'>
print()

# --- Reassigning a variable ---
# A variable's value can change. The name stays; the contents change.
print("=== Reassignment ===")
lives = 3
print("lives:", lives)      # 3

lives = lives - 1           # player lost a life
print("lives:", lives)      # 2

lives = 0                   # game over
print("lives:", lives)      # 0
print()

# --- Multiple assignment on one line ---
# You can assign the same value to multiple variables at once
x = y = z = 0
print("x, y, z:", x, y, z)  # x, y, z: 0 0 0

# Or unpack multiple values at once
first, second, third = "gold", "silver", "bronze"
print("first:", first)       # gold
print("second:", second)     # silver
print("third:", third)       # bronze
