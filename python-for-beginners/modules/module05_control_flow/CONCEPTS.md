# Module 05 Concepts: Control Flow

> This is a stub. Full content will be added in a future revision.
> The key topics are listed below with brief summaries to get you started.

---

## if / elif / else

```python
score = 85

if score >= 90:
    print("A — Excellent!")
elif score >= 80:
    print("B — Good job!")
elif score >= 70:
    print("C — Passing.")
else:
    print("Below passing. Keep practising.")
```

- `if` is the first branch. Always required.
- `elif` (else if) adds more branches. Optional. Can have as many as you need.
- `else` is the catch-all. Optional. Runs if no previous condition was True.
- The colon `:` at the end of each line is required.
- The indented block below each condition is required.

---

## Truthiness

Python evaluates any value in a boolean context (e.g. inside an `if`).
Values that are treated as `False`:

- `False`
- `0` (zero — int or float)
- `""` (empty string)
- `None`
- `[]` (empty list)
- `{}` (empty dict)

Everything else is treated as `True`.

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("No name provided.")   # This runs because "" is falsy
```

---

## Nested conditions

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("You need ID.")
else:
    print("Must be 18 or older.")
```

Keep nesting shallow (max 2-3 levels). Deep nesting makes code hard to read.

---

## The match statement (Python 3.10+)

```python
command = input("Command: ")

match command:
    case "quit":
        print("Goodbye!")
    case "help":
        print("Available commands: quit, help, start")
    case "start":
        print("Game starting...")
    case _:
        print(f"Unknown command: {command}")
```

`case _` is the default — matches anything not caught above.

---

## Next steps

Run the exercise. Then move to Module 06: Loops.
