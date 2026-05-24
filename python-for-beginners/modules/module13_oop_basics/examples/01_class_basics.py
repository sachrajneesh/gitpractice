"""Demonstrates: defining a class, __init__, creating instances, accessing attributes"""

# ---------------------------------------------------------------
# A CLASS is a blueprint for creating objects.
# An INSTANCE (or OBJECT) is a specific thing built from that blueprint.
#
# Example: 'Player' is a class (the blueprint).
#          'ryan_player' is an instance of Player (one specific player).
#
# __init__ is the INITIALISER (constructor) — it runs automatically
# every time you create a new instance. Use it to set up attributes.
# ---------------------------------------------------------------

class Player:
    """A player in a simple game."""

    def __init__(self, name, level=1):
        # 'self' refers to the specific instance being created.
        # self.name creates an ATTRIBUTE called 'name' on this instance.
        self.name = name
        self.level = level
        self.health = 100        # default health for all players
        self.score = 0           # everyone starts at 0 points

# ---------------------------------------------------------------
# --- Creating instances ---
# ---------------------------------------------------------------

# Calling the class like a function creates a new instance.
# Python calls __init__ automatically and passes the new object as 'self'.
ryan = Player("Ryan")            # name="Ryan", level=1 (default)
alice = Player("Alice", level=5) # name="Alice", level=5

# ---------------------------------------------------------------
# --- Accessing attributes with dot notation ---
# ---------------------------------------------------------------
print(f"Name:   {ryan.name}")    # Ryan
print(f"Level:  {ryan.level}")   # 1
print(f"Health: {ryan.health}")  # 100
print(f"Score:  {ryan.score}")   # 0

print(f"\nAlice: level {alice.level}")

# ---------------------------------------------------------------
# --- Each instance is independent ---
# ---------------------------------------------------------------
ryan.score = 1500     # change Ryan's score
alice.score = 2100    # change Alice's score

print(f"\nRyan's score:  {ryan.score}")    # 1500
print(f"Alice's score: {alice.score}")   # 2100 — totally separate!

# ---------------------------------------------------------------
# --- Adding attributes after creation ---
# ---------------------------------------------------------------
ryan.weapon = "sword"     # you can add new attributes on the fly
print(f"Ryan's weapon: {ryan.weapon}")

# ---------------------------------------------------------------
# --- type() and isinstance() ---
# ---------------------------------------------------------------
print(f"\ntype(ryan):           {type(ryan)}")          # <class '__main__.Player'>
print(f"isinstance(ryan, Player): {isinstance(ryan, Player)}")  # True

# ---------------------------------------------------------------
# --- Creating many instances from the same class ---
# ---------------------------------------------------------------
print("\n=== Team ===")
team = [
    Player("Ryan", level=3),
    Player("Alice", level=7),
    Player("Marcus", level=2),
]

for player in team:
    print(f"  {player.name} — Level {player.level}")
