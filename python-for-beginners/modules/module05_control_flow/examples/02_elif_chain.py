"""Demonstrates: if/elif/else chain (grade classifier)"""

# ---------------------------------------------------------------
# When you have MORE than two possible outcomes, use elif.
# Python checks each condition TOP TO BOTTOM and runs the FIRST
# one that is True — then skips all the rest.
# ---------------------------------------------------------------

score = 83     # try changing this to 95, 73, 65, 40, or 105

# Step-by-step grade classifier:

if score > 100 or score < 0:
    # Check for invalid input first — before any grade logic.
    print("Invalid score! Please enter a number between 0 and 100.")

elif score >= 90:
    # This only runs if the score is valid AND >= 90.
    grade = "A"
    message = "Outstanding!"

elif score >= 80:
    # Only reached if above conditions were False (score is 80-89)
    grade = "B"
    message = "Great work!"

elif score >= 70:
    # Score is 70-79
    grade = "C"
    message = "Solid effort."

elif score >= 60:
    # Score is 60-69
    grade = "D"
    message = "Passing, but aim higher."

else:
    # Everything else — score is 0-59
    grade = "F"
    message = "Let's review and try again."

# Only print the grade if the score was valid.
# We use 'grade' in a variable so we only define the output once.
if 0 <= score <= 100:
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(message)

# ---------------------------------------------------------------
# Why put the highest range first?
# If we put score >= 60 first, a score of 95 would match that
# condition AND stop — it would never reach score >= 90.
# Always go from HIGHEST to LOWEST (or most specific to least).
# ---------------------------------------------------------------

print("\n--- Checking a few scores ---")
for test_score in [95, 83, 71, 65, 42]:
    if test_score >= 90:
        g = "A"
    elif test_score >= 80:
        g = "B"
    elif test_score >= 70:
        g = "C"
    elif test_score >= 60:
        g = "D"
    else:
        g = "F"
    print(f"  {test_score:>3} → {g}")   # :>3 right-aligns in 3 characters
