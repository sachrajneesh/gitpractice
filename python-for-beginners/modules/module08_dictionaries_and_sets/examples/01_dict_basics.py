"""Demonstrates: creating dictionaries, accessing values, get(), and updating"""

# ---------------------------------------------------------------
# A dictionary stores KEY → VALUE pairs.
# Keys must be unique. Values can be anything.
# Dictionaries use curly braces {} and a colon to separate key:value.
#
# Think of it like a real dictionary: you look up a WORD (key)
# to find its DEFINITION (value).
# ---------------------------------------------------------------

# --- Creating a dictionary ---
player = {
    "name": "Ryan",
    "level": 12,
    "health": 95,
    "favourite_weapon": "sword",
}

print("Player:", player)
print("Type:", type(player))   # <class 'dict'>

# --- Accessing values by key ---
# Use square brackets: dict[key]
print("\nPlayer name:", player["name"])      # Ryan
print("Player level:", player["level"])     # 12
print("Player health:", player["health"])   # 95

# --- KeyError: what happens when the key doesn't exist ---
# player["mana"]  ← would crash with KeyError: 'mana'

# --- Safe access with get() ---
# get(key) returns None if the key doesn't exist (no crash!)
mana = player.get("mana")
print("\nMana (using get):", mana)           # None — key doesn't exist

# get(key, default) returns the default value instead of None
mana_with_default = player.get("mana", 0)
print("Mana (with default 0):", mana_with_default)   # 0

health = player.get("health", 100)
print("Health (with default):", health)     # 95 — key exists, returns actual value

# --- Updating values ---
print("\nBefore level up:", player["level"])
player["level"] = 13     # just assign to an existing key to update it
print("After level up:", player["level"])

# --- Adding new key-value pairs ---
player["mana"] = 80       # this key didn't exist before — now it does
player["guild"] = "The Python Knights"
print("\nAfter adding mana and guild:", player)

# --- Checking if a key exists ---
print("\n'health' in player:", "health" in player)    # True
print("'strength' in player:", "strength" in player)  # False

# ---------------------------------------------------------------
# --- Another example: food calorie tracker ---
# ---------------------------------------------------------------
calories = {
    "pizza": 285,      # calories per slice
    "burger": 354,
    "salad": 98,
    "cola": 139,
}

meal = ["pizza", "pizza", "cola"]
total_calories = 0

for food in meal:
    # get() with a default of 0 protects against unknown foods
    total_calories += calories.get(food, 0)

print(f"\nMeal: {meal}")
print(f"Total calories: {total_calories}")
