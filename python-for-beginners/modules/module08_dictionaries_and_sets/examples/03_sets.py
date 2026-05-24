"""Demonstrates: sets — creating, add/remove, union, intersection, difference"""

# ---------------------------------------------------------------
# A set is an UNORDERED collection of UNIQUE items.
# Sets use curly braces {} but WITHOUT key:value pairs.
#
# Key properties:
#   - No duplicates — adding the same item twice has no effect
#   - Unordered — you cannot index a set (no set[0])
#   - Very fast for "is X in this collection?" checks
# ---------------------------------------------------------------

# --- Creating a set ---
# Notice the duplicate "cheese" — sets automatically remove duplicates!
pizza_toppings = {"cheese", "pepperoni", "mushrooms", "cheese", "olives", "cheese"}
print("Pizza toppings:", pizza_toppings)   # only one "cheese" will appear
print("Type:", type(pizza_toppings))

# --- Creating a set from a list (useful for removing duplicates) ---
scores_with_duplicates = [88, 74, 88, 95, 74, 61, 88]
unique_scores = set(scores_with_duplicates)   # duplicates removed!
print("\nOriginal list:", scores_with_duplicates)
print("Unique scores:", unique_scores)

# --- Checking membership — this is where sets SHINE ---
# Much faster than checking a list for large collections.
print("\n'pepperoni' in pizza_toppings:", "pepperoni" in pizza_toppings)   # True
print("'pineapple' in pizza_toppings:", "pineapple" in pizza_toppings)   # False

# --- add() — add a single item ---
pizza_toppings.add("pineapple")   # (controversial choice...)
print("\nAfter adding pineapple:", pizza_toppings)

pizza_toppings.add("cheese")      # cheese is already there — nothing changes
print("After adding cheese again:", pizza_toppings)   # still the same

# --- remove() and discard() ---
pizza_toppings.remove("pineapple")   # removes pineapple; raises KeyError if not found
print("\nAfter removing pineapple:", pizza_toppings)

pizza_toppings.discard("anchovies")  # safe version: no error if item doesn't exist
print("After discard('anchovies'):", pizza_toppings)   # unchanged

# ---------------------------------------------------------------
# --- Set operations — comparing two sets ---
# ---------------------------------------------------------------
ryan_games = {"Minecraft", "FIFA", "Zelda", "Fortnite", "Halo"}
alice_games = {"FIFA", "Pokemon", "Zelda", "Stardew Valley", "Fortnite"}

print("\nRyan's games:", ryan_games)
print("Alice's games:", alice_games)

# --- union (|) — all games either of them owns ---
both = ryan_games | alice_games
print("\nUnion (all games):", both)

# --- intersection (&) — games BOTH own ---
shared = ryan_games & alice_games
print("Intersection (shared games):", shared)   # FIFA, Zelda, Fortnite

# --- difference (-) — games Ryan owns that Alice doesn't ---
ryan_only = ryan_games - alice_games
print("Difference (Ryan only):", ryan_only)   # Minecraft, Halo

alice_only = alice_games - ryan_games
print("Difference (Alice only):", alice_only)  # Pokemon, Stardew Valley

# --- symmetric difference (^) — games that only ONE of them owns ---
exclusive = ryan_games ^ alice_games
print("Symmetric diff (not shared):", exclusive)

# ---------------------------------------------------------------
# Sets vs Lists quick comparison:
#   Lists  → ordered, allows duplicates, supports indexing
#   Sets   → unordered, no duplicates, fast membership checks
# ---------------------------------------------------------------
