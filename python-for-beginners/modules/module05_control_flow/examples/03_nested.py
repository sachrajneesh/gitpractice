"""Demonstrates: nested if statements"""

# ---------------------------------------------------------------
# Nested if statements are if/else blocks INSIDE other if/else blocks.
# Each level of nesting adds another layer of indentation.
# Use nested ifs when a decision depends on a PREVIOUS decision.
# ---------------------------------------------------------------

is_weekend = True      # change these and run again to see different paths
is_sunny = False
homework_done = True

# First decision: is it a weekend?
if is_weekend:
    print("It's the weekend!")

    # Second decision (INSIDE the first): is it sunny?
    if is_sunny:
        print("It's sunny — let's go to the park!")

        # Third decision (INSIDE the second): is homework done?
        if homework_done:
            print("Homework is done. Full day of fun!")
        else:
            print("Finish your homework first, then enjoy the park.")

    else:
        # We're still inside "is_weekend" block
        print("It's cloudy — Netflix and chill it is.")

        if homework_done:
            print("Homework done — pure guilt-free relaxing!")
        else:
            print("Good time to get that homework done.")

else:
    # Back at the top level — it's a school day
    print("It's a school day — time to focus.")

    if homework_done:
        print("Homework ready — great start to the day!")
    else:
        print("Better rush — homework isn't done yet!")

# ---------------------------------------------------------------
# Warning: deeply nested code can get hard to read.
# If you're 4+ levels deep, consider using 'and'/'or' instead.
#
# Compare: nested version vs flat version
# ---------------------------------------------------------------
print("\n--- Same logic, flattened with 'and' ---")

# Nested version checks is_weekend first, then is_sunny, then homework
# The flat version collapses all three into one condition:
if is_weekend and is_sunny and homework_done:
    print("Weekend + sunny + homework done = park time!")
elif is_weekend and not is_sunny:
    print("Weekend but cloudy — indoor day.")
elif not is_weekend:
    print("School day — focus up.")

# Both approaches are valid — choose whichever is easier to read.
