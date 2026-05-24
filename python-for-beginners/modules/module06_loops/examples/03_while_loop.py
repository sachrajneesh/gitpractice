"""Demonstrates: while loop basics with a counter"""

# ---------------------------------------------------------------
# A while loop keeps running AS LONG AS a condition is True.
# It's used when you don't know in advance how many times to loop.
#
# Structure:
#   while <condition>:
#       # code to repeat
#
# WARNING: if the condition never becomes False, you get an
# infinite loop! Always make sure something changes each iteration.
# ---------------------------------------------------------------

# --- Basic while loop: count up to 5 ---
counter = 1       # initialise the counter BEFORE the loop

print("Counting to 5:")
while counter <= 5:          # keep looping while counter is 5 or less
    print(f"  {counter}")
    counter += 1             # IMPORTANT: increment counter each time or it loops forever!

print("Done!")

# --- Countdown with a while loop ---
print("\nRocket countdown:")
countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1    # -= 1 is shorthand for countdown = countdown - 1
print("  Blast off!")

# --- Summing numbers until the total exceeds a target ---
print("\nAdding numbers until total exceeds 20:")
total = 0
number = 1

while total <= 20:
    total += number    # add current number to total
    print(f"  Added {number}, total = {total}")
    number += 1        # move to the next number

print(f"Stopped when total reached {total}")

# --- Repeating a question until valid input is given ---
# (Preview of input validation — important in real programs!)
print("\nGuess the magic number (1-10):")
secret = 7       # the correct answer

guess = 0        # initialise to something that won't accidentally be correct
attempts = 0

while guess != secret:
    guess = int(input("  Your guess: "))
    attempts += 1
    if guess != secret:
        print("  Wrong! Try again.")

print(f"  Correct! It took you {attempts} attempt(s).")

# ---------------------------------------------------------------
# while vs for:
#   Use for   — when you know the number of iterations (or have a list to loop over)
#   Use while — when you loop until a condition changes (e.g. user input, game state)
# ---------------------------------------------------------------
