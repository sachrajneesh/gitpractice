"""Demonstrates: defining functions with def, parameters, return, and calling"""

# ---------------------------------------------------------------
# A function is a NAMED block of code that you can run whenever
# you need it by "calling" it.
#
# Why use functions?
#   - Avoid repeating the same code (DRY: Don't Repeat Yourself)
#   - Break big problems into small named pieces
#   - Make code easier to read and test
#
# Syntax:
#   def function_name(parameter1, parameter2):
#       # code block (indented)
#       return result     ← sends a value back to the caller
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- A simple function with no parameters ---
# ---------------------------------------------------------------
def say_hello():
    """Print a greeting."""
    print("Hello, Ryan! Ready to code?")

# Calling the function (nothing happens until you call it!)
say_hello()   # → Hello, Ryan! Ready to code?
say_hello()   # call it again — runs the same code twice

# ---------------------------------------------------------------
# --- A function with ONE parameter ---
# ---------------------------------------------------------------
def greet(name):
    """Print a personalised greeting."""
    print(f"Hey {name}, welcome to Python!")

greet("Ryan")    # → Hey Ryan, welcome to Python!
greet("Alice")   # → Hey Alice, welcome to Python!

# ---------------------------------------------------------------
# --- A function with TWO parameters ---
# ---------------------------------------------------------------
def describe_score(player, score):
    """Print a player's score."""
    print(f"{player} scored {score} points.")

describe_score("Ryan", 1500)
describe_score("Alice", 2100)

# ---------------------------------------------------------------
# --- A function that RETURNS a value ---
# ---------------------------------------------------------------
def add_scores(score1, score2):
    """Add two scores and return the total."""
    total = score1 + score2
    return total   # sends the result back to whoever called the function

# Store the returned value in a variable
result = add_scores(800, 700)
print(f"\nCombined score: {result}")   # 1500

# Or use it directly in an expression
print(f"Double score: {add_scores(500, 300) * 2}")   # 1600

# ---------------------------------------------------------------
# --- A function that does a calculation and returns the result ---
# ---------------------------------------------------------------
def calculate_average(scores):
    """Calculate and return the average of a list of scores."""
    if len(scores) == 0:
        return 0   # guard against empty list (can't divide by zero)
    total = sum(scores)
    return total / len(scores)

my_scores = [88, 74, 95, 61, 79]
avg = calculate_average(my_scores)
print(f"\nScores: {my_scores}")
print(f"Average: {avg:.1f}")

# ---------------------------------------------------------------
# Key points:
#   - def defines the function — it doesn't run it yet
#   - Parameters are the variable names in the def line
#   - Arguments are the actual values you pass when calling
#   - return sends a value back; without return, function returns None
# ---------------------------------------------------------------
