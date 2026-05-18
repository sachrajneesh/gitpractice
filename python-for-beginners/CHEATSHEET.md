# Python Cheatsheet — One-Page Syntax Reference

---

## Variables & Types

```python
name = "Alice"          # str
age = 17                # int
height = 1.72           # float
is_student = True       # bool
nothing = None          # NoneType

type(age)               # <class 'int'>
```

---

## Strings & f-strings

```python
greeting = "Hello, world!"
multi = """Line one
Line two"""

# f-string (modern, preferred)
f"My name is {name} and I am {age} years old."
f"Next year I'll be {age + 1}."

# Escape characters
"\n"   # newline
"\t"   # tab
"\\"   # backslash
"\""   # double quote

# Common methods
"hello".upper()            # "HELLO"
"  hi  ".strip()           # "hi"
"a,b,c".split(",")         # ["a", "b", "c"]
"-".join(["a", "b", "c"])  # "a-b-c"
"hello".replace("l", "r")  # "herro"
len("hello")               # 5

# Indexing & slicing
s = "Python"
s[0]      # "P"
s[-1]     # "n"
s[0:3]    # "Pyt"
s[::2]    # "Pto"
```

---

## Operators

```python
# Arithmetic
+   -   *   /   //   %   **
10 // 3    # 3   (floor division)
10 % 3     # 1   (remainder)
2 ** 8     # 256 (power)

# Comparison  (returns True/False)
==   !=   <   >   <=   >=

# Logical
and   or   not
not True       # False
True and False # False
True or False  # True
```

---

## if / elif / else

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Below C")
```

---

## for loop

```python
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for i in range(1, 11, 2):  # 1, 3, 5, 7, 9
    print(i)
```

---

## while loop

```python
count = 0
while count < 5:
    print(count)
    count += 1

# break exits the loop early
# continue skips to the next iteration
```

---

## Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]              # "apple"
fruits[-1]             # "cherry"
fruits[1:3]            # ["banana", "cherry"]

fruits.append("date")
fruits.insert(1, "avocado")
fruits.remove("banana")
fruits.pop()           # removes and returns last item
fruits.sort()
fruits.reverse()
len(fruits)            # number of items

# List comprehension
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

---

## Tuples

```python
point = (3, 7)         # immutable — cannot change after creation
x, y = point           # unpacking
```

---

## Dictionaries

```python
person = {"name": "Alice", "age": 17, "city": "Lagos"}

person["name"]          # "Alice"
person.get("phone", "no phone")  # safe access with default

person["email"] = "alice@example.com"  # add/update
del person["city"]

for key, value in person.items():
    print(f"{key}: {value}")

person.keys()    # dict_keys(["name", "age", "email"])
person.values()  # dict_values(["Alice", 17, "alice@example.com"])
```

---

## Sets

```python
colours = {"red", "blue", "green"}
colours.add("yellow")
colours.discard("red")

a = {1, 2, 3}
b = {2, 3, 4}
a | b    # union:        {1, 2, 3, 4}
a & b    # intersection: {2, 3}
a - b    # difference:   {1}
```

---

## Functions

```python
def greet(name, greeting="Hello"):
    """Return a greeting string."""
    return f"{greeting}, {name}!"

greet("Alice")             # "Hello, Alice!"
greet("Bob", "Hi")         # "Hi, Bob!"
greet(greeting="Hey", name="Carol")  # keyword args
```

---

## File I/O

```python
# Write to a file
with open("notes.txt", "w") as f:
    f.write("First line\n")

# Read entire file
with open("notes.txt", "r") as f:
    content = f.read()

# Read line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# Append to a file
with open("notes.txt", "a") as f:
    f.write("Another line\n")
```

---

## try / except

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")   # runs if no exception
finally:
    print("Done.")               # always runs
```

---

## Imports

```python
import math
import random
import datetime

math.sqrt(16)          # 4.0
math.pi                # 3.14159...
random.randint(1, 10)  # random int between 1 and 10
random.choice(["a","b","c"])
datetime.date.today()

from math import sqrt, pi    # import specific names
from random import randint
```
