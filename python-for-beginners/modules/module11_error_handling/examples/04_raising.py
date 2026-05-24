"""Demonstrates: raise, custom error messages, and re-raising exceptions"""

# ---------------------------------------------------------------
# You can RAISE your own exceptions using the 'raise' keyword.
# This is useful for:
#   - Enforcing rules in your functions ("if input is wrong, crash loudly")
#   - Providing clear, descriptive error messages to the caller
#   - Re-raising caught exceptions after logging them
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Raising a standard exception with a custom message ---
# ---------------------------------------------------------------

def set_volume(level):
    """Set the game volume. Must be 0-100."""
    if not isinstance(level, int):
        raise TypeError(f"Volume must be an integer, got {type(level).__name__}")
    if level < 0 or level > 100:
        raise ValueError(f"Volume must be between 0 and 100, got {level}")
    print(f"Volume set to {level}%")

try:
    set_volume(75)      # fine
    set_volume(150)     # raises ValueError
except ValueError as e:
    print(f"Caught ValueError: {e}")

try:
    set_volume("loud")  # raises TypeError
except TypeError as e:
    print(f"Caught TypeError: {e}")

# ---------------------------------------------------------------
# --- Raising inside a validation function ---
# ---------------------------------------------------------------

def validate_username(username):
    """
    Validate a username string.
    Raises ValueError with a descriptive message if invalid.
    """
    if not username:
        raise ValueError("Username cannot be empty.")
    if len(username) < 3:
        raise ValueError(f"Username must be at least 3 characters (got {len(username)}).")
    if len(username) > 20:
        raise ValueError(f"Username must be 20 characters or fewer (got {len(username)}).")
    if not username.isalnum():
        raise ValueError("Username can only contain letters and numbers.")
    return True   # all checks passed

print("\n=== Username validation ===")
test_usernames = ["Ryan", "Ry", "a" * 25, "bad name!", "ValidUser123"]
for name in test_usernames:
    try:
        validate_username(name)
        print(f"  '{name}' is valid.")
    except ValueError as e:
        print(f"  '{name}' is invalid: {e}")

# ---------------------------------------------------------------
# --- Re-raising an exception ---
# ---------------------------------------------------------------
# Sometimes you want to log the error AND let it bubble up.
# Use 'raise' with no argument inside an except block to re-raise.

import logging

def load_player_data(filename):
    """Load player data — log errors and re-raise so the caller knows."""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"  [LOG] Could not find {filename}: {e}")
        raise   # re-raises the same FileNotFoundError — doesn't swallow it

print("\n=== Re-raising ===")
try:
    load_player_data("nonexistent.dat")
except FileNotFoundError:
    print("  Caller caught the re-raised FileNotFoundError and handled it.")

# ---------------------------------------------------------------
# Key rules:
#   - Raise early, with a clear message — don't let bad data travel far
#   - Don't raise bare 'Exception' if a more specific type fits
#   - Re-raise when you want to log but not silence the error
# ---------------------------------------------------------------
