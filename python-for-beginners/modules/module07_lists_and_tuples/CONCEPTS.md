# Module 07 Concepts: Lists & Tuples

> This is a stub. Full content will be added in a future revision.

---

## Lists

A list is an ordered, mutable (changeable) collection of items.
Items can be any type and can be mixed.

```python
fruits = ["apple", "banana", "cherry"]
scores = [95, 82, 78, 91]
mixed = [1, "hello", True, None]
empty = []
```

### Indexing and slicing

Works exactly like strings (see Module 03).

```python
fruits[0]      # "apple"
fruits[-1]     # "cherry"
fruits[1:3]    # ["banana", "cherry"]
```

### Common methods

```python
fruits.append("date")           # add to end
fruits.insert(1, "avocado")     # insert at index
fruits.extend(["fig", "grape"]) # add multiple items
fruits.remove("banana")         # remove by value (first occurrence)
fruits.pop()                    # remove and return last item
fruits.pop(0)                   # remove and return item at index 0
fruits.sort()                   # sort in place (ascending)
fruits.sort(reverse=True)       # sort descending
fruits.reverse()                # reverse in place
fruits.index("cherry")          # find index of a value
fruits.count("apple")           # count occurrences
len(fruits)                     # number of items
"apple" in fruits               # True/False membership check
```

---

## List comprehensions

A concise way to create a new list by transforming or filtering another list.

```python
# Regular loop version:
squares = []
for n in range(10):
    squares.append(n ** 2)

# Comprehension version (preferred):
squares = [n ** 2 for n in range(10)]

# With a filter:
evens = [n for n in range(20) if n % 2 == 0]

# Transforming strings:
names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
```

---

## Tuples

A tuple is an ordered, **immutable** (unchangeable) sequence.
Use tuples for data that should not change: coordinates, RGB colour values, database records.

```python
point = (3, 7)
colour = (255, 128, 0)   # RGB orange
empty_tuple = ()
single = (42,)           # note the trailing comma — required for single-item tuples

point[0]       # 3 — indexing works the same
# point[0] = 5 # ERROR: tuples cannot be changed
```

### Tuple unpacking

```python
x, y = (3, 7)
print(x)   # 3
print(y)   # 7

first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

---

## Next steps

Run the exercise. Then move to Module 08: Dictionaries & Sets.
