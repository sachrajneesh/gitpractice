# Module 02 Concepts: Variables & Data Types

---

## What is a variable?

Imagine a labelled storage box. You write a name on the outside — "score" — and put
a value inside — the number 95. Whenever you want that value, you look at the box
labelled "score" and take out what is inside.

A **variable** is exactly that: a named container for storing a value.

```python
score = 95
player_name = "Alice"
lives_remaining = 3
```

The `=` sign is called the **assignment operator**. It means "store the value on the
right into the variable named on the left."

Variables are useful because:
- You can refer to a value by name instead of repeating the raw value everywhere.
- If the value changes, you update it in one place and the rest of the program
  automatically uses the new value.

---

## The five basic data types

A **data type** describes the kind of value a variable holds.
Python has five basic types you will use constantly.

### int (integer)

An **int** is a whole number — no decimal point.

```python
age = 17
year = 2024
temperature = -5
score = 0
```

### float (floating-point number)

A **float** is a number with a decimal point.

```python
height = 1.72          # in metres
price = 9.99
pi = 3.14159
average = 87.5
```

### str (string)

A **str** (string) is a sequence of characters — text.
Always wrapped in quotes (single or double — both are fine).

```python
name = "Alice"
city = 'Lagos'
message = "Hello, world!"
empty = ""             # an empty string is valid
```

### bool (boolean)

A **bool** (boolean) is either `True` or `False`. Nothing else.
Notice the capital first letter — that is required.

```python
is_logged_in = True
has_finished = False
game_over = False
```

Booleans are used when you need to track yes/no or on/off situations.
You will use them heavily in Module 05 (Control Flow).

### None (NoneType)

`None` is a special value that means "no value" or "empty" or "not set yet".
It is its own type: NoneType.

```python
result = None           # not calculated yet
user_input = None       # nothing entered yet
```

`None` is not zero, not an empty string, not False. It is explicitly "nothing".

---

## Variable naming rules

Python has strict rules about variable names. Break them and you get a SyntaxError
or NameError.

**Rules (must follow):**
- Names can contain letters, digits, and underscores: `score_2024`
- Names cannot contain spaces: `my score` is illegal — use `my_score`
- Names cannot start with a digit: `1player` is illegal — use `player1`
- Names are case-sensitive: `score`, `Score`, and `SCORE` are three different variables

**Conventions (strongly recommended):**
- Use **snake_case**: all lowercase with underscores between words
  - `player_name`, `high_score`, `is_game_over`
- Make names descriptive: `x` tells you nothing; `player_score` tells you everything
- Single-letter names are only acceptable for short loop counters (covered in Module 06)

**Valid names:**
```python
name = "Alice"
player_1_score = 100
is_game_over = False
total_items_in_cart = 5
```

**Invalid names (these cause errors):**
```python
# 1st_place = "Alice"     # ERROR: cannot start with a digit
# my score = 95           # ERROR: no spaces allowed
# class = "Math"          # ERROR: 'class' is a Python keyword (reserved word)
```

---

## The type() function

`type()` is a built-in function that tells you the data type of any value or variable.

```python
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
print(type(None))       # <class 'NoneType'>

age = 17
print(type(age))        # <class 'int'>
```

Use `type()` whenever you are not sure what kind of value you are working with.
It is especially useful for debugging.

---

## input() — getting text from the user

`input()` is a built-in function that pauses your program and waits for the user
to type something and press Enter. It then returns whatever they typed as a string.

```python
name = input("What is your name? ")
print("Hello,", name)
```

When Python runs `input("What is your name? ")`:
1. It prints the message `What is your name? ` in the terminal.
2. It waits for the user to type something and press Enter.
3. It returns the typed text as a string.
4. That string is stored in the variable `name`.

**Critical rule: input() ALWAYS returns a string.**

Even if the user types a number, `input()` gives you a string:

```python
age_text = input("How old are you? ")
print(type(age_text))   # <class 'str'>  — even if they typed "17"
```

This means you cannot do maths with `age_text` yet. You need to convert it first.

---

## Type conversion

To convert between types, use these built-in functions:

### int() — convert to integer

```python
age_text = input("How old are you? ")   # user types "17"
age = int(age_text)                      # now age is the integer 17
print(type(age))                         # <class 'int'>
print(age + 1)                           # 18
```

You can combine both steps:
```python
age = int(input("How old are you? "))
```

### float() — convert to float

```python
height = float(input("Your height in metres: "))   # user types "1.72"
print(height + 0.05)                               # 1.77
```

### str() — convert to string

```python
score = 95
message = "Your score is " + str(score)
print(message)                           # Your score is 95
```

You need `str()` when you want to join a number to a string using `+`.
(In Module 03 you will learn a cleaner way to do this with f-strings.)

---

## Summary table

| Type    | Example         | Use case                       |
|---------|-----------------|--------------------------------|
| int     | `42`            | Counting, whole numbers        |
| float   | `3.14`          | Measurements, decimals         |
| str     | `"Alice"`       | Text, names, messages          |
| bool    | `True`/`False`  | Yes/no decisions               |
| None    | `None`          | "Not set yet", missing values  |
