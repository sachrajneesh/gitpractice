# Module 10 Concepts: File I/O

> This is a stub. Full content will be added in a future revision.

---

## Opening files

```python
# Basic syntax
file = open("notes.txt", "r")   # open for reading
content = file.read()
file.close()                    # MUST close manually

# Better: use 'with' — closes automatically, even if an error occurs
with open("notes.txt", "r") as f:
    content = f.read()
# File is automatically closed here
```

### File modes

| Mode | Meaning                                          |
|------|--------------------------------------------------|
| `"r"` | Read (default). File must exist.               |
| `"w"` | Write. Creates file; overwrites if exists.     |
| `"a"` | Append. Creates file; adds to end if exists.   |
| `"x"` | Create. Creates file; errors if already exists.|

---

## Reading

```python
with open("story.txt", "r") as f:
    # Read the entire file as one big string
    content = f.read()

with open("story.txt", "r") as f:
    # Read all lines into a list of strings (each includes \n)
    lines = f.readlines()

with open("story.txt", "r") as f:
    # Read line by line (memory-efficient for large files)
    for line in f:
        print(line.strip())   # strip() removes the trailing \n
```

---

## Writing

```python
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Append (does not overwrite)
with open("output.txt", "a") as f:
    f.write("Third line\n")
```

---

## csv module

```python
import csv

# Write a CSV file
with open("contacts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Phone"])          # header row
    writer.writerow(["Alice", "555-0101"])
    writer.writerow(["Bob", "555-0202"])

# Read a CSV file
with open("contacts.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)    # row is a list of strings
```

---

## pathlib.Path

```python
from pathlib import Path

# Create a path object
p = Path("notes.txt")
data_dir = Path("data") / "logs" / "today.txt"  # cross-platform path building

# Common operations
p.exists()       # True if file/folder exists
p.is_file()      # True if it is a file
p.is_dir()       # True if it is a directory
p.suffix         # ".txt"
p.stem           # "notes"
p.parent         # Path(".") — the containing directory

# Read/write directly (no open() needed)
p.write_text("Hello, file!")
content = p.read_text()
```

---

## Next steps

Run the exercise. Then move to Module 11: Error Handling.
