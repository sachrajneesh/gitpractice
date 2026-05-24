"""Demonstrates: instance methods, self, and calling methods"""

# ---------------------------------------------------------------
# A METHOD is a function defined INSIDE a class.
# Instance methods automatically receive the instance as their
# first argument — by convention this is always named 'self'.
#
# You call methods with: instance.method_name(arguments)
# Python passes 'self' automatically — you never pass it manually.
# ---------------------------------------------------------------

class Player:
    """A player with health, score, and game actions."""

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.health = 100
        self.score = 0
        self.alive = True

    # --- A method that DOES something (no return value) ---
    def take_damage(self, amount):
        """Reduce health by amount. Player dies if health reaches 0."""
        self.health -= amount    # modify the instance's own attribute via self
        print(f"{self.name} took {amount} damage. Health: {self.health}")

        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self.name} has been defeated!")

    # --- A method that RETURNS a value ---
    def is_alive(self):
        """Return True if the player is still alive."""
        return self.alive

    # --- A method that MODIFIES an attribute ---
    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points
        print(f"{self.name} earned {points} points! Total: {self.score}")

    # --- A method that USES other attributes ---
    def level_up(self):
        """Increase level and restore health."""
        self.level += 1
        self.health = 100    # full heal on level up
        self.alive = True
        print(f"{self.name} levelled up to Level {self.level}! Full health restored.")

    # --- A method that uses multiple attributes ---
    def status(self):
        """Print a summary of the player's current status."""
        status = "alive" if self.alive else "DEFEATED"
        print(f"[ {self.name} | Level {self.level} | HP {self.health} | Score {self.score} | {status} ]")


# ---------------------------------------------------------------
# --- Using the methods ---
# ---------------------------------------------------------------
ryan = Player("Ryan", level=3)
ryan.status()

print()
ryan.add_score(500)
ryan.take_damage(30)
ryan.take_damage(25)
ryan.status()

print()
ryan.level_up()
ryan.status()

print()
ryan.take_damage(60)
ryan.take_damage(50)   # this one should defeat Ryan
ryan.status()

# --- Checking alive status ---
print(f"\nIs Ryan alive? {ryan.is_alive()}")   # False

# ---------------------------------------------------------------
# Key points:
#   - Every method's first parameter is 'self' (the instance)
#   - You call methods with dot notation: ryan.take_damage(30)
#   - Python passes the instance as 'self' automatically
#   - Methods can READ and WRITE the instance's attributes via self.attr
# ---------------------------------------------------------------
