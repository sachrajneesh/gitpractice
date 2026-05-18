# Module 12 Concepts: Modules & Packages

> This is a stub. Full content will be added in a future revision.

---

## import

```python
import math
import random
import datetime
import os
import sys

math.sqrt(16)          # 4.0
math.pi                # 3.14159...
math.floor(3.7)        # 3
math.ceil(3.2)         # 4

random.randint(1, 10)            # random int from 1 to 10
random.choice(["a", "b", "c"])  # pick one at random
random.shuffle(my_list)         # shuffle list in place
random.random()                  # float between 0.0 and 1.0

datetime.date.today()
datetime.datetime.now()
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

os.getcwd()            # current working directory
os.listdir(".")        # list files in current directory
os.path.exists("file.txt")

sys.argv               # command-line arguments
sys.exit(0)            # exit the program
```

---

## from X import Y

```python
from math import sqrt, pi
from random import randint, choice
from datetime import date, datetime

# Now use without the module prefix
sqrt(25)      # 5.0
randint(1, 6) # simulated dice roll
date.today()
```

---

## Writing your own module

Any `.py` file is a module. Create `utils.py`:

```python
# utils.py
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9/5 + 32

def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0
```

Import and use it:

```python
# main.py (same folder as utils.py)
import utils

print(utils.celsius_to_fahrenheit(100))  # 212.0
print(utils.is_even(7))                  # False
```

---

## if __name__ == "__main__":

```python
# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # This only runs when you execute mymodule.py directly.
    # It does NOT run when another file imports mymodule.
    greet("World")
```

---

## pip and virtual environments

```bash
# Install a package
pip install requests

# Save dependencies to a file
pip freeze > requirements.txt

# Install from requirements file (e.g. on a new computer)
pip install -r requirements.txt

# Create a virtual environment
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

---

## Next steps

Run the exercise. Then move to Module 13: OOP Basics.
