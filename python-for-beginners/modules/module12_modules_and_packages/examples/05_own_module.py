"""Demonstrates: creating and importing your own module"""

# ---------------------------------------------------------------
# Any Python file is a MODULE. You can import it into another
# file just like you'd import math or random.
#
# This file imports from 'helpers.py' which is in the same folder.
# When Python sees 'import helpers' it looks for helpers.py in:
#   1. The current directory
#   2. Directories listed in sys.path
#
# File layout:
#   examples/
#     helpers.py          ← the module we created
#     05_own_module.py    ← this file (imports helpers)
# ---------------------------------------------------------------

import helpers    # imports our helpers.py — no .py extension in the import!

# ---------------------------------------------------------------
# --- Using functions from our module ---
# ---------------------------------------------------------------
print("=== Using helpers module ===")

# Call functions using: module_name.function_name()
message = helpers.greet("Ryan")
print(message)

scores = [88, 74, 95, 61, 79]
avg = helpers.calculate_average(scores)
print(f"Average score: {avg:.1f}")

# ---------------------------------------------------------------
# --- Access module-level constants ---
# ---------------------------------------------------------------
print(f"\nModule version: {helpers.VERSION}")
print(f"Course: {helpers.COURSE_NAME}")

# ---------------------------------------------------------------
# --- Test the palindrome checker ---
# ---------------------------------------------------------------
print("\n=== Palindrome tests ===")
words = ["racecar", "python", "level", "Ryan", "madam", "hello"]
for word in words:
    result = helpers.is_palindrome(word)
    tick = "✓" if result else "✗"
    print(f"  {tick} '{word}' is {'a' if result else 'not a'} palindrome")

# ---------------------------------------------------------------
# --- Test clamp ---
# ---------------------------------------------------------------
print("\n=== Clamp tests ===")
# clamp keeps a value within a min/max range — great for game stats!
health = helpers.clamp(150, 0, 100)   # can't go over 100
print(f"Health after damage: {health}")  # 100

volume = helpers.clamp(-5, 0, 100)    # can't go below 0
print(f"Volume (min 0): {volume}")    # 0

speed = helpers.clamp(55, 0, 120)     # within range — stays the same
print(f"Speed (0-120): {speed}")      # 55

# ---------------------------------------------------------------
# --- from helpers import ... (specific items) ---
# ---------------------------------------------------------------
from helpers import greet, is_palindrome

# Now we can call these without the 'helpers.' prefix
print("\n" + greet("Alice"))
print(f"Is 'level' a palindrome? {is_palindrome('level')}")

# ---------------------------------------------------------------
# --- Checking a module's contents with dir() ---
# ---------------------------------------------------------------
print("\nEverything in helpers module:")
public_items = [item for item in dir(helpers) if not item.startswith("_")]
print(" ", public_items)

# ---------------------------------------------------------------
# Key takeaway:
# Any .py file you create can be imported as a module!
# This lets you split your code across multiple files and reuse it.
# ---------------------------------------------------------------
