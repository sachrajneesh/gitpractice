"""Demonstrates: break and continue inside loops"""

# ---------------------------------------------------------------
# break    — EXIT the loop immediately, regardless of the condition
# continue — SKIP the rest of this iteration, go to the next one
#
# Both work inside for loops AND while loops.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# BREAK — stop the loop early
# ---------------------------------------------------------------

# Example: search a list and stop once found
print("Searching for 'Zelda' in game library:")
game_library = ["Minecraft", "FIFA", "Fortnite", "Zelda", "Pokemon", "Halo"]

for game in game_library:
    print(f"  Checking '{game}'...")
    if game == "Zelda":
        print("  Found it!")
        break   # stop looping — no point checking the rest
print("Search complete.\n")

# Example: while loop with break for "quit" command
print("Type game commands (or 'quit' to exit):")
while True:     # True means "loop forever" — we control exit with break
    command = input("  Command: ")
    if command == "quit":
        print("  Exiting game. Bye!")
        break   # break exits the while True loop
    else:
        print(f"  You typed: '{command}'")

# ---------------------------------------------------------------
# CONTINUE — skip this iteration, move to the next
# ---------------------------------------------------------------

print("\nPrinting only odd numbers from 1 to 10:")
for number in range(1, 11):
    if number % 2 == 0:   # if the number is even...
        continue           # ...skip it and go to the next iteration
    print(f"  {number}")   # only prints if we didn't hit continue

# Example: skip banned words in a list
print("\nFiltering message words:")
words = ["Hello", "spam", "how", "spam", "are", "you", "spam"]
banned = "spam"

for word in words:
    if word == banned:
        continue    # skip banned words
    print(f"  {word}", end=" ")   # end=" " puts words on the same line
print()  # newline at the end

# Example: process scores but skip invalid ones
print("\nValid scores only:")
raw_scores = [88, -5, 74, 101, 95, 0, 61]

for score in raw_scores:
    if score < 0 or score > 100:
        print(f"  Skipping invalid score: {score}")
        continue    # skip to next score — don't process this one
    print(f"  Score: {score}")

# ---------------------------------------------------------------
# Summary:
#   break    — "I'm done with this loop entirely, exit now"
#   continue — "Skip this item, but keep going with the rest"
# ---------------------------------------------------------------
