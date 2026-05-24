"""Demonstrates: for loop with range() — counting up, down, and with step"""

# ---------------------------------------------------------------
# The for loop repeats code a set number of times.
# range() generates a sequence of numbers to loop over.
#
# range(stop)           → 0, 1, 2, ..., stop-1
# range(start, stop)    → start, start+1, ..., stop-1
# range(start, stop, step) → start, start+step, ..., up to stop
# ---------------------------------------------------------------

# --- Counting up from 1 to 5 ---
print("Counting up from 1 to 5:")
for number in range(1, 6):   # range(1, 6) gives 1, 2, 3, 4, 5 (NOT 6)
    print(f"  {number}")

# --- Counting down from 10 to 1 ---
print("\nCountdown:")
for number in range(10, 0, -1):   # start=10, stop=0 (not included), step=-1
    print(f"  {number}")
print("  Blast off!")

# --- Counting in steps of 2 (even numbers) ---
print("\nEven numbers from 2 to 10:")
for number in range(2, 11, 2):   # step=2 means skip every other number
    print(f"  {number}")

# --- Printing a simple level progress bar ---
print("\nLoading game levels:")
total_levels = 5
for level in range(1, total_levels + 1):   # +1 so we include level 5
    print(f"  Level {level} of {total_levels}... loaded!")

# --- Using range() to repeat something N times ---
# range(3) gives 0, 1, 2 — we use _ when we don't care about the value
print("\nReady? Go!")
for _ in range(3):   # the underscore _ is a convention meaning "I won't use this variable"
    print("  Beep!")

# --- Summing numbers with a for loop ---
print("\nSum of 1 to 100:")
total = 0                    # start with an accumulator at 0
for number in range(1, 101): # 1 to 100 inclusive
    total = total + number   # add each number to the running total
print(f"  Total = {total}")  # 5050

# ---------------------------------------------------------------
# Key points about range():
#   - range(stop) starts at 0
#   - The stop value is NEVER included
#   - Negative step counts DOWN
#   - range() doesn't create a list — it generates numbers one at a time
# ---------------------------------------------------------------
