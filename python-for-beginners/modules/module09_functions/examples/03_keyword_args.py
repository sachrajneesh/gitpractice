"""Demonstrates: keyword arguments and mixing positional with keyword"""

# ---------------------------------------------------------------
# When calling a function, you can pass arguments in two ways:
#
# POSITIONAL: arguments matched by their ORDER in the def line
#   order_pizza("large", "pepperoni", True)
#
# KEYWORD: arguments matched by NAME — order doesn't matter
#   order_pizza(size="large", topping="pepperoni", extra_cheese=True)
#
# You can MIX them, but positional args must come FIRST.
# ---------------------------------------------------------------

def order_pizza(size, topping, extra_cheese=False, delivery=True):
    """Print a pizza order summary."""
    cheese_str = " + extra cheese" if extra_cheese else ""
    delivery_str = "delivery" if delivery else "collection"
    print(f"Order: {size} pizza, {topping}{cheese_str} — {delivery_str}")

# --- Positional arguments (order matches the def line) ---
order_pizza("large", "pepperoni")
order_pizza("medium", "mushroom", True, False)   # extra_cheese=True, delivery=False

print()

# --- Keyword arguments (use the parameter names) ---
# Order doesn't matter when you name them:
order_pizza(topping="pineapple", size="small")     # reversed order — still works!
order_pizza(size="large", topping="cheese", extra_cheese=True)

print()

# --- Mixing positional and keyword ---
# Positional args MUST come before keyword args
order_pizza("large", "pepperoni", extra_cheese=True)       # size and topping positional, extra_cheese keyword
order_pizza("small", "veggie", delivery=False)             # first two positional, last keyword

print()

# ---------------------------------------------------------------
# --- When keyword args are especially useful ---
# ---------------------------------------------------------------

def create_character(name, cls, level=1, health=100, strength=10, agility=10):
    """Create a game character with stats."""
    print(f"{name} the {cls} — Lvl {level} | HP {health} | STR {strength} | AGI {agility}")

# Positional only — you must remember the ORDER:
create_character("Ryan", "Warrior", 5, 120, 18, 12)   # easy to make mistakes

# Keyword args — crystal clear what each value is:
create_character("Alice", "Mage", level=7, health=80, strength=5, agility=15)

# Keyword args also let you skip defaults you don't want to change:
create_character("Marcus", "Rogue", agility=20)   # only change agility

# ---------------------------------------------------------------
# --- Why keywords improve readability ---
# ---------------------------------------------------------------

# Which is clearer?
print()
print("Calling with positionals:", end=" ")
print("create_character('Zara', 'Archer', 3, 90, 8, 18)")

print("Calling with keywords:   ", end=" ")
print("create_character('Zara', 'Archer', level=3, health=90, strength=8, agility=18)")

# The second form is longer but far easier to read and maintain!
