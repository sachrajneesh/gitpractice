"""Demonstrates: the random module — randint, choice, shuffle, seed"""

# ---------------------------------------------------------------
# The random module generates pseudo-random numbers and makes
# random selections. Great for games, simulations, and quizzes.
# ---------------------------------------------------------------

import random

# ---------------------------------------------------------------
# --- randint(a, b) — random INTEGER between a and b (inclusive) ---
# ---------------------------------------------------------------
print("=== random.randint() ===")
dice_roll = random.randint(1, 6)   # simulates a die (1 to 6, both included)
print(f"Dice roll: {dice_roll}")

secret_number = random.randint(1, 100)   # for a number guessing game
print(f"Secret number (1-100): {secret_number}")

# Roll 5 dice and show them all
print("Rolling 5 dice:", [random.randint(1, 6) for _ in range(5)])

# ---------------------------------------------------------------
# --- choice(seq) — pick ONE random item from a sequence ---
# ---------------------------------------------------------------
print("\n=== random.choice() ===")
pizza_toppings = ["cheese", "pepperoni", "mushrooms", "olives", "pineapple"]
todays_pizza = random.choice(pizza_toppings)
print(f"Today's pizza topping: {todays_pizza}")

directions = ["north", "south", "east", "west"]
random_direction = random.choice(directions)
print(f"The monster moves: {random_direction}")

# ---------------------------------------------------------------
# --- choices(seq, k=n) — pick MULTIPLE items (with replacement) ---
# ---------------------------------------------------------------
print("\n=== random.choices() ===")
# k=3 means pick 3 items; items can be repeated (with replacement)
topping_combo = random.choices(pizza_toppings, k=3)
print(f"3 random toppings (repeats allowed): {topping_combo}")

# ---------------------------------------------------------------
# --- sample(seq, k=n) — pick MULTIPLE unique items (no replacement) ---
# ---------------------------------------------------------------
print("\n=== random.sample() ===")
# sample() picks without replacement — no duplicates!
cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7"]
hand = random.sample(cards, k=5)   # deal 5 unique cards
print(f"Your hand: {hand}")

# ---------------------------------------------------------------
# --- shuffle(seq) — randomly reorder a list IN PLACE ---
# ---------------------------------------------------------------
print("\n=== random.shuffle() ===")
playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(f"Original: {playlist}")
random.shuffle(playlist)    # modifies the list in place (like list.sort())
print(f"Shuffled: {playlist}")

# ---------------------------------------------------------------
# --- seed(n) — make "random" results reproducible ---
# ---------------------------------------------------------------
print("\n=== random.seed() ===")
# Setting a seed means the same sequence will be generated every time.
# Useful for testing, tutorials, or making reproducible results.
random.seed(42)   # any number works as the seed
print("With seed 42:")
print([random.randint(1, 10) for _ in range(5)])   # always the same 5 numbers

random.seed(42)   # reset to the same seed
print("With seed 42 again (same!):")
print([random.randint(1, 10) for _ in range(5)])   # identical output

# ---------------------------------------------------------------
# --- uniform(a, b) — random FLOAT between a and b ---
# ---------------------------------------------------------------
print("\n=== random.uniform() ===")
reaction_time = random.uniform(0.2, 1.5)   # random float in range
print(f"Simulated reaction time: {reaction_time:.3f} seconds")
