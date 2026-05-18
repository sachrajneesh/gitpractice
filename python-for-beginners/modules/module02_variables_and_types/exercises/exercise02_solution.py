"""
Exercise 02 Solution 🟢: Profile Card

Only look at this after spending at least 15 minutes genuinely attempting
the exercise. After reading, close this file and retype it from memory.
"""

CURRENT_YEAR = 2024

# Collect input from the user
first_name = input("What is your first name? ")
age = int(input("How old are you? "))

# Calculate derived values
birth_year = CURRENT_YEAR - age
age_in_10_years = age + 10

# Print the profile card
border = "-" * 30
print()
print(border)
print("       PROFILE CARD")
print(border)
print(f"  Name        : {first_name}")
print(f"  Age         : {age}")
print(f"  Born approx.: {birth_year}")
print(f"  Age in 2034 : {age_in_10_years}")
print(border)
print()

# ---
# Example output when user enters "Amara" and "17":
#
# ------------------------------
#        PROFILE CARD
# ------------------------------
#   Name        : Amara
#   Age         : 17
#   Born approx.: 2007
#   Age in 2034 : 27
# ------------------------------
# ---

# THINGS TO NOTICE:
# - CURRENT_YEAR is ALL_CAPS because it's a constant (won't change during the run)
# - We convert age to int immediately after input() — not later
# - f-strings make it easy to embed variable values inside strings
# - The border variable is reused three times — one definition, multiple uses
