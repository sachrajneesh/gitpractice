# Module 06 Concepts: Loops

> This is a stub. Full content will be added in a future revision.

---

## for loop

```python
# Iterate over a range of numbers
for i in range(5):
    print(i)      # prints 0, 1, 2, 3, 4

# range(start, stop, step)
for i in range(1, 11):      # 1 to 10
    print(i)

for i in range(0, 20, 2):   # even numbers 0-18
    print(i)

for i in range(10, 0, -1):  # countdown 10 to 1
    print(i)
```

---

## Iterating over a string

```python
for letter in "Python":
    print(letter)     # P, y, t, h, o, n  (one per line)
```

---

## while loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
# prints 0, 1, 2, 3, 4
```

Use `while` when you do not know in advance how many iterations you need.

---

## break and continue

```python
# break — exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)        # prints 0, 1, 2, 3, 4

# continue — skip the rest of this iteration
for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)        # prints 1, 3, 5, 7, 9
```

---

## else on a loop

The `else` block runs only if the loop completed without hitting a `break`.

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop finished without break")   # this runs
```

---

## Nested loops

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row},{col}", end="  ")
    print()   # newline after each row
```

Output:
```
1,1  1,2  1,3
2,1  2,2  2,3
3,1  3,2  3,3
```

---

## Next steps

Run the exercise. Then move to Module 07: Lists & Tuples.
