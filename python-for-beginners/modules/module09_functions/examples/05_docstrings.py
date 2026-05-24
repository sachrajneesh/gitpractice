"""Demonstrates: writing good docstrings and using the help() function"""

# ---------------------------------------------------------------
# A docstring is a string literal placed as the FIRST statement
# inside a function (or class/module).
# It explains what the function does, its parameters, and what
# it returns.
#
# Python stores the docstring in the function's __doc__ attribute,
# and the built-in help() function displays it automatically.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- The simplest form: one-line docstring ---
# ---------------------------------------------------------------
def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"

# Access the docstring directly:
print(greet.__doc__)
print(greet("Ryan"))

# ---------------------------------------------------------------
# --- Multi-line docstring for more complex functions ---
# ---------------------------------------------------------------
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): Weight in kilograms.
        height_m  (float): Height in metres.

    Returns:
        float: BMI value rounded to 1 decimal place.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.9
    """
    if height_m <= 0:
        return None   # guard against invalid input
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

print("\n" + "-" * 40)
print("calculate_bmi docstring:")
print(calculate_bmi.__doc__)

# Calculate a real BMI
bmi_value = calculate_bmi(70, 1.75)
print(f"BMI for 70kg / 1.75m: {bmi_value}")

# ---------------------------------------------------------------
# --- Using help() to display docstrings ---
# ---------------------------------------------------------------
def find_high_score(scores):
    """
    Find the highest score in a list.

    Parameters:
        scores (list): A list of numeric scores.

    Returns:
        int or float: The maximum score. Returns None for empty lists.
    """
    if not scores:
        return None
    return max(scores)

# help() prints a nicely formatted version of the docstring:
print("\n" + "=" * 40)
help(find_high_score)   # shows the docstring in a formatted way

# ---------------------------------------------------------------
# --- Why write docstrings? ---
# ---------------------------------------------------------------
# 1. Future you will thank present you — code you wrote 3 months
#    ago feels like someone else wrote it.
# 2. Your teammates (or course instructors) can understand your code.
# 3. Tools like IDEs and linters use docstrings for auto-complete hints.
# 4. help() works on your functions just like on built-ins:
help(len)    # see how Python's own len() is documented

# ---------------------------------------------------------------
# --- Docstring conventions ---
# ---------------------------------------------------------------
# One-liner: use for simple functions, keep it on one line.
# Multi-line: use for complex functions with multiple params.
#
# The most common format is Google style (used above) or NumPy style.
# The key rule: ALWAYS start with a verb: "Return...", "Calculate...", "Find..."
# ---------------------------------------------------------------
