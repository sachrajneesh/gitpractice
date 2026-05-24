"""Demonstrates: import, from X import Y, and aliasing with as"""

# ---------------------------------------------------------------
# A MODULE is a Python file containing functions, classes, and
# variables you can reuse. Python ships with hundreds of modules
# in its standard library — no installation needed.
#
# Three ways to import:
#   import module_name               — import the whole module
#   from module_name import thing    — import just one thing
#   import module_name as alias      — give the module a short name
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Style 1: import the whole module ---
# ---------------------------------------------------------------
import math   # import the entire math module

# Access functions with: module_name.function_name()
circumference = 2 * math.pi * 5    # math.pi is a constant
root = math.sqrt(144)              # math.sqrt() is a function
print(f"Circumference of circle r=5: {circumference:.2f}")
print(f"Square root of 144: {root}")

# ---------------------------------------------------------------
# --- Style 2: from X import Y — import specific items ---
# ---------------------------------------------------------------
from math import sqrt, pi, ceil, floor
# Now we can use sqrt(), pi, ceil(), floor() WITHOUT the 'math.' prefix

area = pi * 5 ** 2         # no 'math.' needed
print(f"\nArea of circle r=5: {area:.2f}")
print(f"ceil(4.3):  {ceil(4.3)}")    # 5 — round UP
print(f"floor(4.7): {floor(4.7)}")  # 4 — round DOWN

# ---------------------------------------------------------------
# --- Style 3: import as — give the module an alias ---
# ---------------------------------------------------------------
import random as rnd       # 'rnd' is a shorter alias for 'random'
import datetime as dt      # 'dt' is a common alias for 'datetime'

# Now use the alias instead of the full module name
lucky_number = rnd.randint(1, 100)
print(f"\nYour lucky number: {lucky_number}")

today = dt.datetime.now().strftime("%A, %d %B %Y")
print(f"Today is: {today}")

# ---------------------------------------------------------------
# --- from X import Y as Z — import a specific item with alias ---
# ---------------------------------------------------------------
from datetime import datetime as DateTime   # alias specific import

now = DateTime.now()
print(f"\nCurrent time: {now.strftime('%H:%M:%S')}")

# ---------------------------------------------------------------
# Which style to use?
#
# import math           → best when you need many things from a module
#                         (makes it clear where each function comes from)
#
# from math import sqrt → best when you only need one or two things
#                         (shorter code, but harder to see which module
#                          'sqrt' came from)
#
# import numpy as np    → conventional for well-known libraries
#                         (np, pd, plt are widely recognised aliases)
# ---------------------------------------------------------------
