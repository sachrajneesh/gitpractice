"""
Module 03 — Example 04: String Indexing and Slicing

Demonstrates:
  - Positive and negative indexing
  - Basic slicing with start:stop
  - Slicing with a step
  - Reversing a string with slicing
  - Practical uses of slicing

Run this file:
  python modules/module03_strings/examples/04_indexing_slicing.py
"""

# === ASCII DIAGRAM: how indices map to characters ===
#
#   String:   P  y  t  h  o  n   (6 characters)
#   Pos idx:  0  1  2  3  4  5
#   Neg idx: -6 -5 -4 -3 -2 -1
#
# Slicing syntax: string[start : stop : step]
#   - start: the index to begin at (inclusive)
#   - stop:  the index to stop BEFORE (exclusive — NOT included)
#   - step:  how many positions to advance each time (default 1)
#
# Memory trick: think of indices as pointing between characters:
#
#   | P | y | t | h | o | n |
#   0   1   2   3   4   5   6
#
# s[1:4] means "from slot 1 to slot 4", giving you y, t, h

language = "Python"

print("=== Positive indexing ===")
print(f"language = '{language}'")
print(f"language[0]  = '{language[0]}'")    # P
print(f"language[1]  = '{language[1]}'")    # y
print(f"language[2]  = '{language[2]}'")    # t
print(f"language[3]  = '{language[3]}'")    # h
print(f"language[4]  = '{language[4]}'")    # o
print(f"language[5]  = '{language[5]}'")    # n
print()

print("=== Negative indexing (count from the right) ===")
print(f"language[-1] = '{language[-1]}'")   # n  (last character)
print(f"language[-2] = '{language[-2]}'")   # o
print(f"language[-3] = '{language[-3]}'")   # h
print()

print("=== IndexError: going out of bounds ===")
# Accessing an index that does not exist raises IndexError.
# language[6] would crash — the valid range is 0 to 5 (or -6 to -1).
# Commented out here to keep the file runnable:
# print(language[6])  # ERROR: string index out of range
print("(Index 6 would cause an IndexError — valid range is 0 to 5)")
print()

# ---
print("=== Basic slicing [start:stop] ===")
s = "Python"
print(f"s = '{s}'")
print(f"s[0:3]  = '{s[0:3]}'")   # Pyt  — indices 0,1,2 (not 3)
print(f"s[1:4]  = '{s[1:4]}'")   # yth  — indices 1,2,3
print(f"s[3:6]  = '{s[3:6]}'")   # hon  — indices 3,4,5
print()

print("=== Omitting start or stop ===")
print(f"s[:3]   = '{s[:3]}'")    # Pyt  — from beginning to 3
print(f"s[3:]   = '{s[3:]}'")    # hon  — from 3 to end
print(f"s[:]    = '{s[:]}'")     # Python — entire string (a copy)
print()

print("=== Slicing with a step [start:stop:step] ===")
alphabet = "abcdefghij"
print(f"alphabet = '{alphabet}'")
print(f"alphabet[::2]   = '{alphabet[::2]}'")     # acegi  — every 2nd
print(f"alphabet[::3]   = '{alphabet[::3]}'")     # adgj   — every 3rd
print(f"alphabet[1::2]  = '{alphabet[1::2]}'")    # bdfhj  — every 2nd, starting at 1
print(f"alphabet[0:8:2] = '{alphabet[0:8:2]}'")   # aceg   — every 2nd, only first 8
print()

print("=== Reversing a string with [::-1] ===")
word = "racecar"
print(f"word = '{word}'")
print(f"word[::-1] = '{word[::-1]}'")      # racecar (palindrome!)
print()
name = "Alice"
print(f"name = '{name}'")
print(f"name[::-1] = '{name[::-1]}'")      # ecilA
print()

# ---
print("=== Practical slicing examples ===")

# Extract file extension
filename = "holiday_photo.jpg"
extension = filename[-3:]
print(f"Extension of '{filename}': {extension}")     # jpg

# Extract first and last name from a full name
full_name = "Alice Johnson"
first = full_name[:5]       # "Alice"
last = full_name[6:]        # "Johnson"
print(f"First: {first}, Last: {last}")

# Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"'racecar' palindrome? {is_palindrome('racecar')}")   # True
print(f"'hello' palindrome?   {is_palindrome('hello')}")     # False
print(f"'A man a plan a canal Panama' palindrome? {is_palindrome('A man a plan a canal Panama')}")
