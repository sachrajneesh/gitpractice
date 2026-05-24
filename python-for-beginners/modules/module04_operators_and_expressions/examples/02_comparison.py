"""Demonstrates: comparison operators (==, !=, <, >, <=, >=)"""

# ---------------------------------------------------------------
# Comparison operators compare two values and ALWAYS return
# a boolean: either True or False.
# ---------------------------------------------------------------

# Let's use game scores and ages as our examples.

ryan_score = 88
passing_score = 70
perfect_score = 100

# --- Equal to (==) ---
# Two equals signs! One = assigns, two == compares.
print(ryan_score == perfect_score)   # False  (88 is not 100)
print(ryan_score == 88)              # True

# --- Not equal to (!=) ---
print(ryan_score != passing_score)   # True  (88 is not 70)
print(ryan_score != 88)              # False

# --- Greater than (>) ---
print(ryan_score > passing_score)    # True  (88 > 70)
print(ryan_score > perfect_score)    # False (88 is not > 100)

# --- Less than (<) ---
print(ryan_score < perfect_score)    # True  (88 < 100)
print(ryan_score < passing_score)    # False (88 is not < 70)

# --- Greater than or equal to (>=) ---
print(ryan_score >= passing_score)   # True  (88 >= 70)
print(ryan_score >= 88)              # True  (88 >= 88, equal counts!)

# --- Less than or equal to (<=) ---
print(ryan_score <= perfect_score)   # True  (88 <= 100)
print(ryan_score <= 88)              # True  (88 <= 88, equal counts!)

# ---------------------------------------------------------------
# Comparing strings — Python compares them alphabetically
# ---------------------------------------------------------------
favourite_game = "Minecraft"
print(favourite_game == "Minecraft")   # True
print(favourite_game == "minecraft")   # False — case matters!

# ---------------------------------------------------------------
# Storing the result in a variable
# ---------------------------------------------------------------
did_pass = ryan_score >= passing_score  # this stores True or False
print(f"Did Ryan pass? {did_pass}")     # Did Ryan pass? True

# ---------------------------------------------------------------
# Using comparisons inside if statements (preview of Module 05)
# ---------------------------------------------------------------
age = 17
driving_age = 16
print(f"Old enough to drive: {age >= driving_age}")   # True

high_score = 95
if high_score > 90:
    print("New high score! Excellent!")   # this prints because 95 > 90

# ---------------------------------------------------------------
# Common beginner mistake: using = instead of ==
# ---------------------------------------------------------------
# WRONG:  if score = 100:    <- this is assignment, not comparison (will error)
# RIGHT:  if score == 100:   <- this is comparison
# ---------------------------------------------------------------
