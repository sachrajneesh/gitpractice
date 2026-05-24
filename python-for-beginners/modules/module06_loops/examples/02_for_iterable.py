"""Demonstrates: for loop over a list and a string"""

# ---------------------------------------------------------------
# A for loop can iterate over ANY "iterable" — something that
# contains multiple items you can step through one by one.
# Lists and strings are both iterables.
# ---------------------------------------------------------------

# --- Looping over a list ---
favourite_games = ["Minecraft", "FIFA", "Fortnite", "Zelda", "Pokemon"]

print("My favourite games:")
for game in favourite_games:   # 'game' gets each item in turn
    print(f"  - {game}")

# --- Looping over a list of numbers ---
scores = [88, 74, 95, 61, 79]

print("\nExam scores:")
total = 0
for score in scores:
    print(f"  {score}")
    total += score   # += is shorthand for total = total + score

average = total / len(scores)   # len() gives the number of items
print(f"Average: {average:.1f}")

# --- enumerate() — get the index AND the value at the same time ---
print("\nNumbered game list:")
for index, game in enumerate(favourite_games, start=1):
    # enumerate() gives pairs: (0, 'Minecraft'), (1, 'FIFA'), etc.
    # start=1 makes it count from 1 instead of 0
    print(f"  {index}. {game}")

# --- Looping over a string ---
# A string is a sequence of characters — you can loop over each one.
name = "Ryan"

print(f"\nLetters in '{name}':")
for letter in name:    # 'letter' gets each character one at a time
    print(f"  {letter}")

# --- Counting specific characters ---
sentence = "Minecraft is the best game ever"
vowels = "aeiou"    # a string we'll check against
vowel_count = 0

for char in sentence.lower():   # .lower() so 'E' and 'e' both count
    if char in vowels:           # 'in' checks if char is in the vowels string
        vowel_count += 1

print(f"\nVowels in '{sentence}': {vowel_count}")

# --- Looping over a list of food items and building a new sentence ---
toppings = ["cheese", "pepperoni", "mushrooms", "olives"]

print("\nPizza order:")
for topping in toppings:
    print(f"  Adding {topping}...")
print("  Pizza is ready!")
