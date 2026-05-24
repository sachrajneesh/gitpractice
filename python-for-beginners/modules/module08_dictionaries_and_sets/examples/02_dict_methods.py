"""Demonstrates: dict methods — keys(), values(), items(), iteration, nested dicts"""

# ---------------------------------------------------------------
# Dictionaries have several useful methods for accessing their
# contents and iterating over them.
# ---------------------------------------------------------------

game_scores = {
    "Alice": 1450,
    "Ryan": 2100,
    "Marcus": 870,
    "Zara": 1980,
}

# ---------------------------------------------------------------
# --- keys() — all the keys ---
# ---------------------------------------------------------------
print("Players:", list(game_scores.keys()))   # convert to list to see the values

# ---------------------------------------------------------------
# --- values() — all the values ---
# ---------------------------------------------------------------
print("Scores:", list(game_scores.values()))

# ---------------------------------------------------------------
# --- items() — all (key, value) pairs as tuples ---
# ---------------------------------------------------------------
print("Items:", list(game_scores.items()))

# ---------------------------------------------------------------
# --- Iterating over a dictionary ---
# ---------------------------------------------------------------

# Method 1: loop over keys (simplest)
print("\nAll players (loop over keys):")
for player in game_scores:     # loops over keys by default
    print(f"  {player}")

# Method 2: loop over keys and look up values
print("\nLeaderboard:")
for player in game_scores:
    score = game_scores[player]
    print(f"  {player}: {score}")

# Method 3: loop over items() — most common and cleanest
print("\nLeaderboard (using items):")
for player, score in game_scores.items():   # unpack each (key, value) tuple
    print(f"  {player}: {score:,}")         # :, adds comma separator (2,100)

# ---------------------------------------------------------------
# --- Finding the highest score ---
# ---------------------------------------------------------------
top_player = max(game_scores, key=game_scores.get)
print(f"\nTop player: {top_player} with {game_scores[top_player]} points")

# ---------------------------------------------------------------
# --- Nested dictionaries ---
# A dictionary whose values are themselves dictionaries.
# ---------------------------------------------------------------
contacts = {
    "Ryan": {
        "phone": "555-0101",
        "email": "ryan@example.com",
        "city": "London",
    },
    "Alice": {
        "phone": "555-0202",
        "email": "alice@example.com",
        "city": "Manchester",
    },
}

# Access nested values: outer_key → inner_key
print("\nRyan's phone:", contacts["Ryan"]["phone"])
print("Alice's city:", contacts["Alice"]["city"])

# Iterate nested dict
print("\nAll contacts:")
for name, info in contacts.items():
    print(f"  {name}:")
    for field, value in info.items():
        print(f"    {field}: {value}")

# ---------------------------------------------------------------
# --- Updating with update() ---
# ---------------------------------------------------------------
game_scores.update({"Sam": 1200, "Ryan": 2350})   # adds Sam, updates Ryan
print("\nAfter update:", game_scores)

# ---------------------------------------------------------------
# --- Removing with pop() ---
# ---------------------------------------------------------------
removed_score = game_scores.pop("Marcus")   # removes Marcus and returns his score
print(f"\nRemoved Marcus (score was {removed_score}):", game_scores)
