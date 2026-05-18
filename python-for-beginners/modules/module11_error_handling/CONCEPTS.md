# Module 11 Concepts: Error Handling

> This is a stub. Full content will be added in a future revision.

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
```

---

## else and finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")    # only runs if no exception
finally:
    print("This always runs.")    # cleanup code goes here
```

---

## Catching multiple exceptions at once

```python
try:
    value = int(input("Enter a number: "))
except (ValueError, TypeError) as e:
    print(f"Input error: {e}")
```

The `as e` part gives you the exception object, which you can print for details.

---

## raise — throwing exceptions

```python
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}")
    return age
```

---

## Common built-in exceptions

| Exception          | Cause                                          |
|--------------------|------------------------------------------------|
| `ValueError`       | Wrong value type (e.g. int("hello"))           |
| `TypeError`        | Wrong type (e.g. "3" + 5)                     |
| `NameError`        | Name not defined                               |
| `IndexError`       | List index out of range                        |
| `KeyError`         | Dictionary key not found                       |
| `FileNotFoundError`| File does not exist                            |
| `ZeroDivisionError`| Division by zero                               |
| `AttributeError`   | Object has no such attribute/method            |

---

## Next steps

Run the exercise. Then move to Module 12: Modules & Packages.
