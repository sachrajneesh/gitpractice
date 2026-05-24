"""Demonstrates: open/write/read a text file using the with statement"""

# ---------------------------------------------------------------
# Files let your program SAVE data that persists after it closes.
# Python's open() function opens a file for reading or writing.
#
# The 'with' statement (context manager) is the recommended way
# to work with files — it automatically CLOSES the file even if
# an error occurs.
#
# File modes:
#   "w"  — write (creates file; OVERWRITES if it already exists)
#   "r"  — read  (reads existing file; error if file not found)
#   "a"  — append (adds to end of existing file; creates if new)
# ---------------------------------------------------------------

import os   # used at the end to clean up the demo file

# ---------------------------------------------------------------
# --- Writing to a file ---
# ---------------------------------------------------------------
print("Writing to 'notes.txt'...")

# 'with open(...)' opens the file and assigns it to the variable 'f'
# When the with block ends, Python closes the file automatically.
with open("notes.txt", "w") as f:
    # mode "w" creates the file if it doesn't exist,
    # or OVERWRITES it completely if it does.
    f.write("Python is really fun to learn.\n")    # \n = newline character
    f.write("I finished Module 10 today!\n")
    f.write("File I/O is easier than I expected.\n")

print("File written successfully.")

# ---------------------------------------------------------------
# --- Reading the entire file at once ---
# ---------------------------------------------------------------
print("\nReading the whole file:")

with open("notes.txt", "r") as f:
    # read() returns the entire file content as a single string
    content = f.read()

print(content)   # print the whole thing at once

# ---------------------------------------------------------------
# --- Reading line by line (better for large files) ---
# ---------------------------------------------------------------
print("Reading line by line:")

with open("notes.txt", "r") as f:
    # readlines() returns a list of strings, one per line
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    # .strip() removes the trailing \n from each line
    print(f"  Line {i}: {line.strip()}")

# ---------------------------------------------------------------
# --- Reading with a for loop (most memory efficient) ---
# ---------------------------------------------------------------
print("\nIterating over file directly:")

with open("notes.txt", "r") as f:
    for line in f:              # files are iterable — loops line by line
        print(f"  > {line.strip()}")

# ---------------------------------------------------------------
# --- Clean up the demo file ---
# ---------------------------------------------------------------
os.remove("notes.txt")   # delete the file so it doesn't clutter the folder
print("\nDemo file removed.")
