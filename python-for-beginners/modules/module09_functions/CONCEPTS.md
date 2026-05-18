# Module 09 Concepts: Functions

> This is a stub. Full content will be added in a future revision.

---

## Defining and calling functions

```python
def greet(name):
    """Print a personalised greeting."""
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!
```

- `def` starts the function definition.
- The function name follows snake_case convention.
- Parameters are in the parentheses.
- The colon `:` ends the `def` line.
- The function body is indented.

---

## Return values

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(3, 4)   # result = 7
print(add(10, 20))   # 30
```

Without `return`, a function returns `None`.

---

## Default parameter values

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")            # "Hello, Alice!"
greet("Bob", "Hi")        # "Hi, Bob!"
```

Default values must come after non-default parameters.

---

## Keyword arguments

```python
def describe_person(name, age, city):
    print(f"{name} is {age} and lives in {city}.")

describe_person("Alice", 17, "Lagos")                # positional
describe_person(age=17, name="Alice", city="Lagos")  # keyword (order doesn't matter)
```

---

## Variable scope

Variables created inside a function are **local** — they only exist during
that function call. They are destroyed when the function returns.

```python
def calculate():
    result = 42    # local variable
    return result

calculate()
# print(result)   # ERROR: result is not defined here (local scope)
```

---

## Docstrings

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: weight in kilograms
        height_m: height in metres

    Returns:
        BMI as a float, rounded to 1 decimal place
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)
```

---

## Next steps

Run the exercise. Then move to Module 10: File I/O.
