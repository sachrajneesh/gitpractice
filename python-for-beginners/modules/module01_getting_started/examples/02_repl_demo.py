"""
Module 01 — Example 02: REPL Demo

Demonstrates:
  - What the Python REPL (interactive mode) is
  - The kinds of expressions you can type directly
  - Why the REPL is useful for quick experiments

This file is written in REPL style — each block shows what you would type
at the >>> prompt and what Python would show back.

To actually try the REPL:
  1. Open a terminal
  2. Type: python
  3. You'll see the >>> prompt
  4. Type the expressions below and press Enter after each one
  5. Type exit() when you want to leave

Run this file normally to see the same results:
  python modules/module01_getting_started/examples/02_repl_demo.py
"""

# In the REPL, if you type a simple expression, Python shows its value.
# In a script file, you need print() to see it.

# --- Simple arithmetic ---
# REPL: >>> 2 + 2         Output: 4
print(2 + 2)              # 4

# REPL: >>> 10 * 5        Output: 50
print(10 * 5)             # 50

# REPL: >>> 7 / 2         Output: 3.5
print(7 / 2)              # 3.5

# REPL: >>> 7 // 2        Output: 3  (floor division — rounds down)
print(7 // 2)             # 3

# --- String expressions ---
# REPL: >>> "hello"       Output: 'hello'
print("hello")

# REPL: >>> "hello" + " " + "world"     Output: 'hello world'
print("hello" + " " + "world")

# REPL: >>> "ha" * 3      Output: 'hahaha'
print("ha" * 3)           # hahaha

# --- Built-in functions you can explore in the REPL ---
# REPL: >>> len("Python")  Output: 6
print(len("Python"))      # 6

# REPL: >>> type(42)       Output: <class 'int'>
print(type(42))

# REPL: >>> type("hello")  Output: <class 'str'>
print(type("hello"))

# REPL: >>> type(3.14)     Output: <class 'float'>
print(type(3.14))

# --- The REPL is perfect for quick experiments ---
# Try things like:
#   >>> "Python".upper()
#   >>> abs(-15)
#   >>> round(3.7)
#   >>> max(3, 7, 2, 9, 1)
#   >>> min(3, 7, 2, 9, 1)

print()
print("The REPL is your playground. Experiment freely.")
print("You cannot break anything permanently by typing in the REPL.")
