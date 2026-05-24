"""Demonstrates: creating lists, indexing, and negative indexing"""

# ---------------------------------------------------------------
# A list is an ORDERED collection of items.
# Lists use square brackets [] and can hold any type of value.
# Items are separated by commas.
# Lists are MUTABLE — you can change them after creation.
# ---------------------------------------------------------------

# --- Creating lists ---
games = ["Minecraft", "FIFA", "Fortnite", "Zelda", "Pokemon"]
scores = [88, 74, 95, 61, 79]
mixed = ["Ryan", 17, True, 3.14]   # lists can hold mixed types (though unusual)
empty_list = []                     # an empty list — you can add to it later

print("Games:", games)
print("Scores:", scores)
print("Length of games list:", len(games))   # len() counts items

# ---------------------------------------------------------------
# --- Indexing — accessing ONE item ---
#
# Index:   0          1          2          3          4
# Item:  "Minecraft" "FIFA"  "Fortnite"  "Zelda"  "Pokemon"
# ---------------------------------------------------------------

# Indexes START at 0 (not 1!) — this is called zero-based indexing
print("\nFirst game (index 0):", games[0])    # Minecraft
print("Second game (index 1):", games[1])   # FIFA
print("Third game (index 2):", games[2])    # Fortnite

# ---------------------------------------------------------------
# --- Negative indexing — count from the END ---
#
# Index:    -5         -4         -3         -2         -1
# Item:  "Minecraft" "FIFA"  "Fortnite"  "Zelda"  "Pokemon"
# ---------------------------------------------------------------

# -1 is always the LAST item — very useful!
print("\nLast game (index -1):", games[-1])    # Pokemon
print("Second to last (-2):", games[-2])      # Zelda

# ---------------------------------------------------------------
# --- Modifying items by index ---
# ---------------------------------------------------------------
print("\nBefore change:", games)
games[1] = "Cyberpunk"   # replace FIFA with Cyberpunk at index 1
print("After change:", games)

# ---------------------------------------------------------------
# --- Checking if an item is in the list ---
# ---------------------------------------------------------------
print("\n'Zelda' in games:", "Zelda" in games)        # True
print("'FIFA' in games:", "FIFA" in games)            # False (we replaced it)
print("'Minecraft' in games:", "Minecraft" in games)  # True

# ---------------------------------------------------------------
# --- Common beginner mistake: index out of range ---
# ---------------------------------------------------------------
# games[10] would crash with IndexError because games only has 5 items
# Always use len() to check before accessing unknown indexes.
print("\nSafe access example:")
target_index = 2
if target_index < len(games):
    print(f"Item at index {target_index}: {games[target_index]}")
else:
    print(f"Index {target_index} is out of range!")
