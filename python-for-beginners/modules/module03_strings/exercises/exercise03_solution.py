"""
Exercise 03 Solution 🟢: Name Card Generator

Only look at this after spending at least 15 minutes genuinely attempting
the exercise. After reading, close this file and retype it from memory.
"""

# Collect input
first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()

# Build derived strings
full_name = f"{first_name} {last_name}".upper()
initials = f"{first_name[0].upper()}. {last_name[0].upper()}."

# Calculate card width — name length + padding on each side
# We add 4 characters of internal padding (2 spaces each side)
inner_width = max(len(full_name), len(initials)) + 6  # at least 6 chars of breathing room
card_width = inner_width + 2   # +2 for the "| " and " |" borders

# Build the horizontal border
border = "+" + "-" * inner_width + "+"

# Print the card
print()
print(border)
print("| " + full_name.center(inner_width - 2) + " |")
print("| " + initials.center(inner_width - 2) + " |")
print(border)
print()

# ---
# Example output for "Alice Johnson":
#
# +--------------------+
# |   ALICE JOHNSON    |
# |       A. J.        |
# +--------------------+
#
# Example output for "Amara Osei-Bonsu" (longer name):
#
# +--------------------+
# |  AMARA OSEI-BONSU  |
# |       A. O.        |
# +--------------------+
# ---

# THINGS TO NOTICE:
# - .strip() removes any accidental leading/trailing spaces from input
# - max() ensures the card is wide enough for both the name AND the initials
# - .center(width) does the centring math for us — we don't have to count spaces
# - The card adapts to any name length because inner_width is calculated, not hardcoded
