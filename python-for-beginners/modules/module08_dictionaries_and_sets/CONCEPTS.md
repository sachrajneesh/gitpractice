# Module 08 Concepts: Dictionaries & Sets

> This is a stub. Full content will be added in a future revision.

---

## Dictionaries

A dictionary stores key-value pairs. Keys must be unique and immutable (usually strings).
Values can be anything.

```python
contact = {
    "name": "Alice",
    "phone": "555-0101",
    "email": "alice@example.com"
}
```

### Accessing values

```python
contact["name"]                      # "Alice"
contact.get("phone")                 # "555-0101"
contact.get("address", "no address") # "no address" (safe — no KeyError)
```

### Setting and deleting

```python
contact["city"] = "Lagos"       # add new key or update existing
del contact["email"]            # remove a key
contact.pop("phone")            # remove and return the value
```

### Checking existence

```python
"name" in contact               # True
"fax" in contact                # False
```

### Iterating

```python
for key in contact:
    print(key)

for key, value in contact.items():
    print(f"{key}: {value}")

list(contact.keys())            # ["name", "city"]
list(contact.values())          # ["Alice", "Lagos"]
```

---

## Nested dictionaries

```python
people = {
    "alice": {"age": 17, "city": "Lagos"},
    "bob":   {"age": 16, "city": "Accra"},
}

people["alice"]["age"]          # 17
```

---

## Sets

A set is an unordered collection of unique values. Duplicates are automatically removed.

```python
colours = {"red", "blue", "green", "red"}   # "red" only stored once
print(colours)   # {'red', 'blue', 'green'}  (order not guaranteed)

colours.add("yellow")
colours.discard("red")   # safe remove (no error if not present)
```

### Set operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # union:        {1, 2, 3, 4, 5, 6}
a & b    # intersection: {3, 4}
a - b    # difference:   {1, 2}  (in a but not b)
a ^ b    # symmetric difference: {1, 2, 5, 6}  (in one but not both)
```

---

## Next steps

Run the exercise. Then move to Module 09: Functions.
