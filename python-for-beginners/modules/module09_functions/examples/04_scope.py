"""Demonstrates: local vs global scope, and why globals are usually bad"""

# ---------------------------------------------------------------
# SCOPE is about WHERE a variable can be "seen" and used.
#
# LOCAL scope:   variables created INSIDE a function
#                — they only exist while the function is running
#
# GLOBAL scope:  variables created at the TOP LEVEL of the file
#                — they exist for the lifetime of the program
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Example 1: Local variables stay inside the function ---
# ---------------------------------------------------------------
def calculate_bonus(score):
    """Calculate a bonus based on score."""
    bonus = score * 0.1    # 'bonus' is a LOCAL variable
    print(f"  Inside function: bonus = {bonus}")
    return bonus

result = calculate_bonus(500)
# print(bonus)   ← This would crash with NameError: 'bonus' is not defined
# 'bonus' only exists inside calculate_bonus, not out here.
print(f"Returned value: {result}")

# ---------------------------------------------------------------
# --- Example 2: Functions can READ global variables ---
# ---------------------------------------------------------------
GAME_NAME = "Python Quest"   # global — accessible everywhere

def show_title():
    """Print the game title."""
    # Reading a global is fine — Python looks it up in the outer scope.
    print(f"Welcome to {GAME_NAME}!")

show_title()

# ---------------------------------------------------------------
# --- Example 3: global keyword — modifying a global (avoid this!) ---
# ---------------------------------------------------------------
player_score = 0   # global variable

def add_points_bad(points):
    """BAD practice: modifying a global variable."""
    global player_score          # declares we want to modify the global
    player_score += points       # this changes the module-level variable
    print(f"  [bad] Score is now: {player_score}")

add_points_bad(100)
add_points_bad(250)
print(f"Global player_score: {player_score}")

# Why is this bad?
# - Hard to test: the function's behaviour depends on a variable defined elsewhere
# - Hard to debug: any function could change player_score from anywhere
# - Hard to understand: you need to hunt down every 'global' statement

# ---------------------------------------------------------------
# --- Example 4: The BETTER way — pass values in and return them ---
# ---------------------------------------------------------------
def add_points_good(current_score, points):
    """GOOD practice: take the score in, return the new score."""
    new_score = current_score + points   # local variable — clean!
    return new_score

score = 0
score = add_points_good(score, 100)
score = add_points_good(score, 250)
print(f"\nScore using the good approach: {score}")

# This function is PURE — it doesn't touch anything outside itself.
# You can test it independently: add_points_good(0, 100) always returns 100.

# ---------------------------------------------------------------
# --- Example 5: Name collision — local shadows global ---
# ---------------------------------------------------------------
message = "global message"   # global

def confusing():
    message = "local message"   # this creates a NEW local variable!
    print(f"  Inside function: '{message}'")

confusing()
print(f"Outside function: '{message}'")   # global is unchanged

# ---------------------------------------------------------------
# Summary:
#   - Functions can READ globals but shouldn't WRITE them
#   - Instead: pass values as parameters, return results
#   - Constants (ALL_CAPS) at the top of a file are fine as globals
# ---------------------------------------------------------------
