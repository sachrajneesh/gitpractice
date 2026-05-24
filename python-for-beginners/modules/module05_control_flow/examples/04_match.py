"""Demonstrates: Python 3.10+ match statement (structural pattern matching)"""

# ---------------------------------------------------------------
# The match statement (introduced in Python 3.10) is like a
# powerful switch/case from other languages.
# It's great when you're comparing ONE variable against several
# EXACT values — much cleaner than a long if/elif chain.
# ---------------------------------------------------------------

# --- Example: game menu command handler ---

command = "attack"    # try changing to: "defend", "run", "inventory", "help", "xyz"

# Using match/case:
match command:
    case "attack":
        print("You swing your sword! -15 HP to the enemy.")
    case "defend":
        print("You raise your shield. Defence +10 for this turn.")
    case "run":
        print("You flee the battle! Coward... but alive.")
    case "inventory":
        print("Inventory: [sword, shield, 2x health potion]")
    case "help":
        print("Commands: attack, defend, run, inventory, heal")
    case _:
        # case _ is the default — matches ANYTHING not caught above
        print(f"Unknown command: '{command}'. Type 'help' for options.")

# ---------------------------------------------------------------
# Equivalent if/elif chain — notice how much longer it is:
# ---------------------------------------------------------------
print("\n--- Same thing using if/elif ---")

if command == "attack":
    print("You swing your sword!")
elif command == "defend":
    print("You raise your shield.")
elif command == "run":
    print("You flee the battle!")
elif command == "inventory":
    print("Inventory: [sword, shield, 2x health potion]")
elif command == "help":
    print("Commands: attack, defend, run, inventory, heal")
else:
    print(f"Unknown command: '{command}'.")

# ---------------------------------------------------------------
# match can also match on multiple values at once using |
# ---------------------------------------------------------------
print("\n--- Matching multiple values with | ---")

day = "Saturday"    # try: "Monday", "Saturday", "Sunday", "Friday"

match day:
    case "Saturday" | "Sunday":
        # | means "or" inside a case
        print(f"{day} is a weekend — sleep in!")
    case "Friday":
        print("TGIF! Weekend is almost here.")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday":
        print(f"{day} is a school day.")
    case _:
        print(f"'{day}' is not a recognised day of the week.")

# ---------------------------------------------------------------
# When to use match vs if/elif:
#   Use match  — when comparing ONE variable against exact values
#   Use if/elif — when conditions involve ranges, comparisons, or complex logic
#   e.g. score >= 90 is NOT suitable for match — use if/elif for that
# ---------------------------------------------------------------
