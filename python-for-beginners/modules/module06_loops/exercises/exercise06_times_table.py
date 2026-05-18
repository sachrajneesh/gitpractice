"""
Exercise 06 🟡: Times Table & Number Guessing Game

What you'll practise:
  for loops, range(), while loops, break, and user input inside a loop.

Task:
  Part A — Times Table Printer:
    Ask the user which times table they want (e.g. 7),
    then print the full 1-to-12 times table for that number.

  Part B — Number Guessing Game:
    Pick a secret number between 1 and 20 (hardcode it for now, or use random).
    Let the user guess repeatedly until they get it right.
    After each wrong guess, tell them if the secret is higher or lower.
    Count the attempts and report the total when they win.

Requirements:
  - Part A: use a for loop with range().
  - Part B: use a while loop with break, and keep a guess counter.

Example output (Part A, user enters 7):
  7 x 1  =  7
  7 x 2  = 14
  ...
  7 x 12 = 84

Example output (Part B):
  Guess the number (1-20): 10
  Too low! Try again.
  Guess the number (1-20): 15
  Too high! Try again.
  Guess the number (1-20): 13
  Correct! You got it in 3 guesses.

How to run:
  python modules/module06_loops/exercises/exercise06_times_table.py

Hints:
  - For Part A: print(f"{n} x {i} = {n * i}")
  - For Part B: use a while True loop, increment a counter each guess,
    break when the guess is correct.
  - Bonus: import random and use random.randint(1, 20) for the secret number.

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# --- Part A: Times Table ---

# TODO: Step 1 — Ask the user which times table they want (convert to int)
# TODO: Step 2 — Use a for loop over range(1, 13) to print each line

print()  # spacer between parts

# --- Part B: Number Guessing Game ---

# TODO: Step 3 — Set a secret_number (e.g. 13, or use random.randint)
# TODO: Step 4 — Set a guess_count variable to 0
# TODO: Step 5 — Use a while True loop: ask for a guess, increment count
# TODO: Step 6 — If correct, print success + count and break
# TODO: Step 7 — If wrong, print "Too low!" or "Too high!" and continue
