"""
Module 03 — Example 05: String Methods

Demonstrates:
  - Case methods: upper, lower, title, capitalize, swapcase
  - Stripping whitespace: strip, lstrip, rstrip
  - Searching: find, rfind, count, startswith, endswith, in
  - Replacing: replace
  - Splitting and joining: split, rsplit, splitlines, join
  - Checking content: isalpha, isdigit, isalnum, isspace, isupper, islower
  - len() (built-in function, not a method)
  - Important: methods return new strings — originals are unchanged

Run this file:
  python modules/module03_strings/examples/05_string_methods.py
"""

print("=== Case methods ===")

text = "hello, world!"
print(text.upper())        # HELLO, WORLD!
print(text.lower())        # hello, world!  (already lower, no change)
print(text.title())        # Hello, World!  (capitalise first letter of each word)
print(text.capitalize())   # Hello, world!  (only first letter of entire string)
print(text.swapcase())     # HELLO, WORLD!  → actually same since all lower

mixed = "hElLo WoRlD"
print(mixed.swapcase())    # HeLlO wOrLd
print()

# ---
print("=== Stripping whitespace ===")

padded = "   hello, world!   "
print(repr(padded))               # '   hello, world!   '
print(repr(padded.strip()))       # 'hello, world!'    — both ends
print(repr(padded.lstrip()))      # 'hello, world!   ' — left end only
print(repr(padded.rstrip()))      # '   hello, world!' — right end only

# strip() with an argument removes those specific characters
messy = "***hello***"
print(messy.strip("*"))           # hello
print()

# ---
print("=== Searching ===")

sentence = "the cat sat on the mat"

# find() returns the index of the first occurrence, or -1 if not found
print(sentence.find("cat"))       # 4
print(sentence.find("xyz"))       # -1
print(sentence.find("at"))        # 5  (first occurrence)

# rfind() finds the LAST occurrence
print(sentence.rfind("at"))       # 21  (the "at" in "mat")

# count() counts non-overlapping occurrences
print(sentence.count("at"))       # 3  ("cat", "sat", "mat")
print(sentence.count("the"))      # 2

# startswith / endswith
print(sentence.startswith("the"))  # True
print(sentence.endswith("mat"))    # True
print(sentence.endswith("cat"))    # False

# The 'in' operator — simplest way to check if something exists
print("cat" in sentence)           # True
print("dog" in sentence)           # False
print("cat" not in sentence)       # False
print()

# ---
print("=== Replacing ===")

# replace(old, new) — replaces ALL occurrences by default
message = "I like cats. Cats are great. My cat is named Whiskers."
print(message.replace("cat", "dog"))
# I like dogs. Cats are great. My dog is named Whiskers.
# NOTE: "Cats" (capital C) was NOT replaced — case-sensitive!

# replace(old, new, count) — replace only the first N occurrences
print(message.replace("cat", "dog", 1))
# I like dogs. Cats are great. My cat is named Whiskers.
print()

# ---
print("=== Splitting and joining ===")

# split() — splits a string into a list of substrings
csv_line = "Alice,17,Lagos,student"
parts = csv_line.split(",")
print(parts)              # ['Alice', '17', 'Lagos', 'student']
print(parts[0])           # Alice
print(parts[1])           # 17

# split() with no argument splits on any whitespace
sentence2 = "  too   many   spaces  "
words = sentence2.split()
print(words)              # ['too', 'many', 'spaces']  (strips leading/trailing too)

# splitlines() splits on newlines
poem_lines = "Line one\nLine two\nLine three"
print(poem_lines.splitlines())   # ['Line one', 'Line two', 'Line three']

# join() — the reverse of split: glues a list of strings together
words_list = ["Python", "is", "great"]
print(" ".join(words_list))     # Python is great
print("-".join(words_list))     # Python-is-great
print(", ".join(words_list))    # Python, is, great
print("".join(words_list))      # Pythonisgreat
print()

# ---
print("=== Checking content ===")

print("abc".isalpha())     # True  — all letters
print("123".isdigit())     # True  — all digits
print("abc123".isalnum())  # True  — all alphanumeric
print("   ".isspace())     # True  — all whitespace
print("HELLO".isupper())   # True  — all uppercase
print("hello".islower())   # True  — all lowercase
print("Hello World".istitle())  # True  — title case
print()

# ---
print("=== len() — length of a string ===")

print(len("Python"))       # 6
print(len(""))             # 0  (empty string)
print(len("  hello  "))   # 9  (spaces count too)
print()

# ---
print("=== IMPORTANT: methods return new strings ===")

original = "hello"
upper_version = original.upper()

print("original:", original)       # hello    — unchanged!
print("upper_version:", upper_version)  # HELLO   — new string

# A common mistake:
original.upper()   # this is fine but useless — the result is thrown away
print("After calling .upper() without saving:", original)  # still "hello"

# Always capture the result:
original = original.upper()   # NOW original is updated
print("After reassigning:", original)   # HELLO
