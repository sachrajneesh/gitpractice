# Module 03 Concepts: Strings

Strings are one of the most-used types in Python. You will work with them in
almost every program you write. Take time with this module.

---

## String literals

A **string literal** is a piece of text written directly in your code, surrounded
by quotation marks. The quotation marks tell Python "this is text, not code".

```python
greeting = "Hello, world!"
name = 'Alice'
```

Single quotes and double quotes work identically. Pick one style and stick to it.
The only time you need to mix them is when your text contains quote characters.

```python
# Text contains a double quote — use single quotes on the outside
line = 'She said, "Hello!"'

# Text contains a single quote/apostrophe — use double quotes on the outside
line = "It's a beautiful day."

# Or use the same type of quote but escape it with backslash
line = "She said, \"Hello!\""
line = 'It\'s a beautiful day.'
```

---

## Escape characters

An **escape character** is a backslash (`\`) followed by a letter that represents
a special character you cannot type directly.

| Escape | Meaning          | Example                    |
|--------|------------------|----------------------------|
| `\n`   | newline          | `"Line 1\nLine 2"`         |
| `\t`   | tab              | `"Name:\tAlice"`           |
| `\\`   | literal backslash| `"C:\\Users\\Alice"`       |
| `\"`   | double quote     | `"She said \"Hi\""`        |
| `\'`   | single quote     | `'It\'s fine'`             |

```python
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

print("Name:\tAlice")
# Output:
# Name:   Alice

print("Path: C:\\Users\\Alice\\Desktop")
# Output:
# Path: C:\Users\Alice\Desktop
```

---

## Multi-line strings (triple quotes)

If you need a string that spans multiple lines, use triple quotes:
either `"""..."""` or `'''...'''`.

```python
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

print(poem)
```

Output:
```
Roses are red,
Violets are blue,
Python is great,
And so are you.
```

Triple-quoted strings are also used for **docstrings** — the explanatory comments
at the top of functions and files (you will see these in every example file in
this course).

---

## f-strings — the modern way to embed values

An **f-string** (formatted string literal) lets you embed variable values and
expressions directly inside a string. Put `f` before the opening quote, then
use `{}` curly braces to insert values.

```python
name = "Alice"
age = 17

# Old way (do not use)
message = "Hello, " + name + ". You are " + str(age) + " years old."

# f-string (modern, preferred)
message = f"Hello, {name}. You are {age} years old."
print(message)
# Output: Hello, Alice. You are 17 years old.
```

**Expressions inside {}**

You can put any expression inside the curly braces, not just variable names:

```python
score = 85
print(f"Score: {score}")               # Score: 85
print(f"Next year: {2024 + 1}")        # Next year: 2025
print(f"Double score: {score * 2}")    # Double score: 170
print(f"Upper: {name.upper()}")        # Upper: ALICE

# Formatting numbers
pi = 3.14159
print(f"Pi to 2dp: {pi:.2f}")         # Pi to 2dp: 3.14
price = 9.5
print(f"Price: ${price:.2f}")          # Price: $9.50

# Padding for alignment
print(f"{'Name':<10} {'Score':>5}")    # Name       Score
print(f"{'Alice':<10} {95:>5}")        # Alice         95
```

f-strings are fast, readable, and the Python community's preferred way to format
strings. Use them everywhere. You do not need to learn `%` formatting or `.format()`.

---

## String indexing

Every character in a string has a position, called an **index**.
Indexing starts at 0 (not 1).

```
String:    P  y  t  h  o  n
Index:     0  1  2  3  4  5
           (positive indices, from the left)

Index:    -6 -5 -4 -3 -2 -1
           (negative indices, from the right)
```

Use square brackets `[]` to access a single character:

```python
language = "Python"
print(language[0])     # P   (first character)
print(language[1])     # y
print(language[5])     # n   (last character)
print(language[-1])    # n   (last character, using negative index)
print(language[-2])    # o   (second from last)
```

Strings are **immutable** — you cannot change a single character.
`language[0] = "J"` would raise a TypeError.
To "change" a string, you create a new one.

---

## String slicing

**Slicing** extracts a portion of a string.
Syntax: `string[start:stop:step]`

- `start` — index to begin at (inclusive), default is 0
- `stop` — index to stop before (exclusive, not included), default is end
- `step` — how many positions to advance each time, default is 1

```
String:    P  y  t  h  o  n
Index:     0  1  2  3  4  5
```

```python
s = "Python"
print(s[0:3])    # "Pyt"   — indices 0, 1, 2 (not 3)
print(s[2:5])    # "tho"   — indices 2, 3, 4
print(s[:3])     # "Pyt"   — from beginning to index 3
print(s[3:])     # "hon"   — from index 3 to end
print(s[:])      # "Python" — the whole string
print(s[::2])    # "Pto"   — every 2nd character
print(s[::-1])   # "nohtyP" — reversed! (step of -1 goes backwards)
```

---

## Common string methods

A **method** is a function that belongs to a specific type. You call it using
dot notation: `variable.method()`.

String methods do not modify the original string — they return a new one.

```python
text = "  Hello, World!  "

# Case conversion
text.upper()           # "  HELLO, WORLD!  "
text.lower()           # "  hello, world!  "
text.title()           # "  Hello, World!  "

# Whitespace removal
text.strip()           # "Hello, World!"   (removes both ends)
text.lstrip()          # "Hello, World!  " (removes left only)
text.rstrip()          # "  Hello, World!" (removes right only)

# Searching
"Python".find("th")    # 2   (index where "th" starts; -1 if not found)
"Python".find("xyz")   # -1  (not found)
"Python".count("t")    # 1   (how many times "t" appears)
"Hello".startswith("He")  # True
"Hello".endswith("lo")    # True

# Replacing and splitting
"hello world".replace("world", "Python")  # "hello Python"
"apple,banana,cherry".split(",")          # ["apple", "banana", "cherry"]
",".join(["apple", "banana", "cherry"])   # "apple,banana,cherry"

# Checking content
"  ".isspace()       # True
"abc123".isalnum()   # True  (all alphanumeric)
"abc".isalpha()      # True  (all letters)
"123".isdigit()      # True  (all digits)

# Length (this is a built-in function, not a method)
len("Python")        # 6
```

**Important:** these methods return new values. The original string is unchanged.

```python
name = "alice"
upper_name = name.upper()
print(name)         # "alice"       — original unchanged
print(upper_name)   # "ALICE"       — new string returned
```
