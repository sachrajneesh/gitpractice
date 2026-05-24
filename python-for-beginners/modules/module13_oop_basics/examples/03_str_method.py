"""Demonstrates: __str__ and __repr__ — why they matter"""

# ---------------------------------------------------------------
# Python calls __str__ when you use print() or str() on an object.
# Python calls __repr__ when you inspect an object in the REPL or
# when there is no __str__ defined.
#
# Without these, printing an object shows something like:
#   <__main__.Player object at 0x10a8b9c50>  ← not helpful!
#
# With __str__: print(player)     → "Ryan (Level 3, HP 100)"
# With __repr__: repr(player)     → "Player('Ryan', 3)"
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Without __str__ (default, unhelpful output) ---
# ---------------------------------------------------------------

class BadPlayer:
    """A player WITHOUT __str__ — hard to debug."""
    def __init__(self, name, level):
        self.name = name
        self.level = level

bad = BadPlayer("Ryan", 3)
print("Without __str__:")
print(bad)           # <__main__.BadPlayer object at 0x...>
print(repr(bad))     # same unreadable output

# ---------------------------------------------------------------
# --- With __str__ and __repr__ ---
# ---------------------------------------------------------------

class Player:
    """A player WITH __str__ and __repr__."""

    def __init__(self, name, level=1, health=100):
        self.name = name
        self.level = level
        self.health = health

    def __str__(self):
        """Human-readable description — used by print() and str()."""
        # This should be friendly and easy to read.
        return f"{self.name} (Level {self.level}, HP {self.health})"

    def __repr__(self):
        """Developer-facing description — used in the REPL and for debugging."""
        # Convention: __repr__ should look like code that recreates the object.
        return f"Player(name={self.name!r}, level={self.level}, health={self.health})"
        # !r adds quotes around the string value: "Ryan" → "'Ryan'"


ryan = Player("Ryan", level=3, health=85)

print("\nWith __str__ and __repr__:")
print(ryan)           # → Ryan (Level 3, HP 85)          ← __str__
print(str(ryan))      # → Ryan (Level 3, HP 85)          ← __str__
print(repr(ryan))     # → Player(name='Ryan', level=3, health=85)  ← __repr__

# In a list, Python uses __repr__ to display objects:
team = [Player("Ryan", 3), Player("Alice", 7), Player("Marcus", 2)]
print(f"\nTeam list: {team}")   # uses __repr__ for each player

# ---------------------------------------------------------------
# --- __str__ is used by f-strings too ---
# ---------------------------------------------------------------
print(f"\nCurrent player: {ryan}")   # f-string uses __str__

# ---------------------------------------------------------------
# --- Why have both? ---
# __str__  → for humans (nice output in print statements)
# __repr__ → for developers (accurate, recreatable, for debugging)
#
# If you only define ONE, define __str__.
# Python falls back to __repr__ if __str__ is missing.
# ---------------------------------------------------------------

class Pizza:
    """A pizza with size and toppings."""

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        topping_list = ", ".join(self.toppings)
        return f"{self.size.capitalize()} pizza with {topping_list}"

    def __repr__(self):
        return f"Pizza(size={self.size!r}, toppings={self.toppings!r})"

my_pizza = Pizza("large", ["cheese", "pepperoni", "mushrooms"])
print(f"\n{my_pizza}")        # Large pizza with cheese, pepperoni, mushrooms
print(repr(my_pizza))         # Pizza(size='large', toppings=['cheese', 'pepperoni', 'mushrooms'])
