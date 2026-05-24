"""Demonstrates: arithmetic operators (+, -, *, /, //, %, **)"""

# ---------------------------------------------------------------
# Python has 7 arithmetic operators.
# Let's explore each one using real-life examples.
# ---------------------------------------------------------------

# --- Addition (+) ---
game_score = 1500          # Ryan's current score in a game
bonus_points = 250         # bonus collected this level
total_score = game_score + bonus_points  # add them together
print(f"Score after bonus: {total_score}")  # 1750

# --- Subtraction (-) ---
wallet = 50.00             # money in wallet (dollars)
pizza_cost = 12.99         # cost of a large pizza
remaining = wallet - pizza_cost
print(f"Money left after pizza: ${remaining:.2f}")  # $37.01

# --- Multiplication (*) ---
hours_per_day = 2          # study hours each day
days_per_week = 7          # days in a week
weekly_hours = hours_per_day * days_per_week
print(f"Weekly study hours: {weekly_hours}")  # 14

# --- Division (/) ---
# Regular division ALWAYS returns a float (decimal number)
total_candy = 10           # candy bars to share
friends = 4                # number of friends
candy_each = total_candy / friends
print(f"Candy per friend: {candy_each}")  # 2.5  (float, not int)

# --- Floor Division (//) ---
# Floor division divides and rounds DOWN to the nearest whole number.
# Great for "how many whole items fit?"
full_bags = total_candy // friends   # how many WHOLE candy bars each friend gets
print(f"Whole candy bars per friend: {full_bags}")  # 2

# --- Modulo (%) ---
# The modulo operator gives you the REMAINDER after division.
# "10 candy bars shared by 4 friends — what's left over?"
leftover_candy = total_candy % friends
print(f"Leftover candy bars: {leftover_candy}")  # 2

# Another classic use: check if a number is even or odd
age = 17
if age % 2 == 0:
    print(f"{age} is even")
else:
    print(f"{age} is odd")   # 17 is odd

# --- Exponentiation (**) ---
# ** means "to the power of"
base = 2
exponent = 10
result = base ** exponent   # 2 to the power of 10
print(f"2 to the power of 10 = {result}")  # 1024

# Real example: compound interest
# If Ryan invests $1000 at 5% annual interest for 3 years:
principal = 1000
rate = 1.05        # 1 + 5% = 1.05
years = 3
future_value = principal * (rate ** years)
print(f"Investment value after {years} years: ${future_value:.2f}")  # $1157.63

# ---------------------------------------------------------------
# Summary of all 7 operators:
#   +   addition           5 + 3  = 8
#   -   subtraction        5 - 3  = 2
#   *   multiplication     5 * 3  = 15
#   /   division (float)   5 / 3  = 1.666...
#   //  floor division     5 // 3 = 1
#   %   modulo (remainder) 5 % 3  = 2
#   **  exponentiation     5 ** 3 = 125
# ---------------------------------------------------------------
