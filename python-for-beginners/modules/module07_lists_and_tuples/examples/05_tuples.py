"""Demonstrates: tuples, immutability, and when to use tuples vs lists"""

# ---------------------------------------------------------------
# A tuple is like a list but IMMUTABLE — you cannot change it
# after it's created. Tuples use parentheses () instead of [].
#
# Use a LIST  when: items will change (add, remove, edit)
# Use a TUPLE when: items are fixed and should not change
# ---------------------------------------------------------------

# --- Creating tuples ---
coordinates = (51.5074, -0.1278)      # London's latitude and longitude
rgb_red = (255, 0, 0)                 # RGB colour — won't change
player_start = (0, 0)                 # starting position in a game

print("Coordinates:", coordinates)
print("RGB red:", rgb_red)
print("Player start:", player_start)

# --- Accessing tuple items — same as lists (indexing works the same) ---
print("\nLatitude:", coordinates[0])      # 51.5074
print("Longitude:", coordinates[1])     # -0.1278
print("Red channel:", rgb_red[0])       # 255

# --- Tuples are IMMUTABLE — you CANNOT modify them ---
# This would cause a TypeError:
# rgb_red[0] = 100    ← ERROR: 'tuple' object does not support item assignment
print("\nTrying to modify a tuple raises TypeError (don't try it!)")
print("That's by design — it protects the data from accidental changes.")

# --- You CAN still iterate over a tuple ---
print("\nRGB values:")
for channel in rgb_red:
    print(f"  {channel}")

# --- Tuple unpacking — assign each value to a separate variable ---
# This is one of the most useful features of tuples!
x, y = player_start      # unpack both values at once
print(f"\nPlayer position: x={x}, y={y}")

latitude, longitude = coordinates
print(f"London: lat={latitude}, long={longitude}")

# A common use: returning multiple values from a function
def get_screen_size():
    return (1920, 1080)   # return a tuple

width, height = get_screen_size()   # unpack the returned tuple
print(f"\nScreen: {width} x {height}")

# --- Tuples vs Lists side by side ---
print("\n--- Tuples vs Lists ---")

# Use a LIST for a collection that changes:
shopping_cart = ["pizza", "cola", "chips"]  # you'll add/remove items
shopping_cart.append("ice cream")
print("Shopping cart (list):", shopping_cart)

# Use a TUPLE for fixed data:
week_days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")  # never changes
print("Week days (tuple):", week_days)

# --- A single-item tuple needs a trailing comma ---
single = ("Minecraft",)   # the comma makes it a tuple, not just parentheses
not_a_tuple = ("Minecraft")  # WITHOUT comma: just a string in brackets!
print(f"\nType with comma: {type(single)}")       # <class 'tuple'>
print(f"Type without comma: {type(not_a_tuple)}") # <class 'str'>

# --- Named tuples preview (for later) ---
# Tuples are great for fixed records where order matters.
# e.g. player = ("Ryan", 17, 1500)  → (name, age, score)
player = ("Ryan", 17, 1500)
name, age, score = player
print(f"\nPlayer: {name}, age {age}, score {score}")
