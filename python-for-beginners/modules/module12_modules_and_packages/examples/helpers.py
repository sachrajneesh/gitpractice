"""
A simple helper module for the Python for Beginners course.

This file is imported by 05_own_module.py to demonstrate how to
create and use your own modules.
"""


def greet(name):
    """Return a personalised greeting string."""
    return f"Hey {name}, welcome to Python!"


def calculate_average(numbers):
    """Return the average of a list of numbers, or 0.0 for empty lists."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards (ignoring case/spaces)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]    # compare string with its reverse


def clamp(value, minimum, maximum):
    """Return value clamped between minimum and maximum."""
    return max(minimum, min(value, maximum))


# MODULE-LEVEL constant — available as helpers.VERSION
VERSION = "1.0.0"
COURSE_NAME = "Python for Beginners"
