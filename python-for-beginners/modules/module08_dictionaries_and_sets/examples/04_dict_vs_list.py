"""Demonstrates: when to use a dict vs a list — side-by-side comparison"""

# ---------------------------------------------------------------
# LISTS  are best when:
#   - You have an ORDERED sequence of items
#   - You access items by POSITION (first, second, third...)
#   - You need to iterate over everything
#
# DICTS are best when:
#   - You need to look up items by a meaningful NAME (key)
#   - You're storing LABELLED data (like a form or record)
#   - You want fast lookup without looping through everything
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# SCENARIO 1: Top 5 game scores on a leaderboard
# Use a LIST — because ORDER matters (rank 1, 2, 3...)
# ---------------------------------------------------------------
print("=== Leaderboard (List) ===")
leaderboard = [("Ryan", 2100), ("Zara", 1980), ("Alice", 1450), ("Sam", 1200), ("Marcus", 870)]

for rank, (name, score) in enumerate(leaderboard, start=1):
    print(f"  #{rank}  {name:10} {score:,}")

# To find the top scorer: it's just leaderboard[0] — easy!
print(f"\nTop scorer: {leaderboard[0][0]}")

# ---------------------------------------------------------------
# SCENARIO 2: A single player's profile
# Use a DICT — because we're labelling data (name, level, health...)
# ---------------------------------------------------------------
print("\n=== Player Profile (Dict) ===")
player = {
    "name": "Ryan",
    "level": 12,
    "health": 95,
    "mana": 60,
    "class": "Warrior",
}

print(f"  Name:   {player['name']}")
print(f"  Level:  {player['level']}")
print(f"  Health: {player['health']}/100")

# Much cleaner than a list: player[0], player[1], player[2]... would be confusing!

# ---------------------------------------------------------------
# SCENARIO 3: Counting how many times each food appears in an order
# Use a DICT — keys=food, values=count
# ---------------------------------------------------------------
print("\n=== Order Summary (Dict) ===")
order = ["pizza", "cola", "pizza", "burger", "cola", "pizza", "water"]

# Build a count dictionary
counts = {}
for item in order:
    if item in counts:
        counts[item] += 1   # already seen this item, increment count
    else:
        counts[item] = 1    # first time seeing it, start at 1

for item, count in counts.items():
    print(f"  {item}: x{count}")

# Alternative: Python has a built-in Counter for this — see Module 12!

# ---------------------------------------------------------------
# SCENARIO 4: A list of scores — easy iteration
# Use a LIST — simple collection of numbers, no labels needed
# ---------------------------------------------------------------
print("\n=== Score Summary (List) ===")
scores = [88, 74, 95, 61, 79, 42, 85]
print(f"  Scores: {scores}")
print(f"  Average: {sum(scores)/len(scores):.1f}")
print(f"  Highest: {max(scores)}")
print(f"  Lowest:  {min(scores)}")

# ---------------------------------------------------------------
# SUMMARY TABLE
# ---------------------------------------------------------------
print("""
  Structure  | Access by     | Ordered? | Duplicates? | Best for
  -----------|---------------|----------|-------------|------------------
  List       | index (0,1,2) | Yes      | Yes         | sequences, rankings
  Dict       | key (name)    | Yes*     | Keys: No    | labelled records, lookups
  Set        | (can't index) | No       | No          | unique items, membership
  Tuple      | index (0,1,2) | Yes      | Yes         | fixed records, coordinates

  *Dicts preserve insertion order since Python 3.7
""")
