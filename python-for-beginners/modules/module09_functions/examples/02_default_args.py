"""Demonstrates: default parameter values"""

# ---------------------------------------------------------------
# Default parameters let you define a function where some
# arguments are OPTIONAL — the caller can leave them out and
# the function will use the default value instead.
#
# Syntax:
#   def function_name(required_param, optional_param="default_value"):
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Basic example: greeting with optional language ---
# ---------------------------------------------------------------
def greet(name, language="English"):
    """Greet a player in their preferred language."""
    if language == "English":
        print(f"Hello, {name}!")
    elif language == "Spanish":
        print(f"¡Hola, {name}!")
    elif language == "French":
        print(f"Bonjour, {name}!")
    else:
        print(f"Hello, {name}! (language '{language}' not supported)")

# Calling WITH the default — don't pass the second argument
greet("Ryan")              # → Hello, Ryan!  (uses default "English")

# Calling WITH a custom value — override the default
greet("Carlos", "Spanish") # → ¡Hola, Carlos!
greet("Marie", "French")   # → Bonjour, Marie!

# ---------------------------------------------------------------
# --- Game stats with multiple defaults ---
# ---------------------------------------------------------------
def create_player(name, level=1, health=100, weapon="fists"):
    """Create and display a new player character."""
    print(f"\n--- New Player ---")
    print(f"  Name:   {name}")
    print(f"  Level:  {level}")
    print(f"  Health: {health}")
    print(f"  Weapon: {weapon}")

# Only the name is required — all others have defaults
create_player("Ryan")                          # uses all defaults
create_player("Alice", level=5)                # override just level
create_player("Marcus", level=3, weapon="sword")  # override level + weapon
create_player("Zara", 10, 150, "magic staff")  # override all

# ---------------------------------------------------------------
# --- Default for a list/count operation ---
# ---------------------------------------------------------------
def show_top_scores(scores, top_n=3):
    """Print the top N scores from a list (default: top 3)."""
    sorted_scores = sorted(scores, reverse=True)   # sort highest first
    limit = min(top_n, len(sorted_scores))         # don't exceed list length
    print(f"\nTop {limit} scores:")
    for i, score in enumerate(sorted_scores[:limit], start=1):
        print(f"  #{i}: {score}")

all_scores = [88, 74, 95, 61, 79, 42, 85, 100, 67]
show_top_scores(all_scores)        # shows top 3 (default)
show_top_scores(all_scores, top_n=5)  # shows top 5

# ---------------------------------------------------------------
# IMPORTANT RULE: parameters WITH defaults must come AFTER
# parameters WITHOUT defaults.
#
# VALID:   def func(required, optional="default")
# INVALID: def func(optional="default", required)  ← SyntaxError!
# ---------------------------------------------------------------
