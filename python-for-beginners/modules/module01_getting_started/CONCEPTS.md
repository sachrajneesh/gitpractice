# Module 01 Concepts: Getting Started

Work through this slowly. Run every example as you go.

---

## What is a program?

A **program** is a set of instructions that tells a computer exactly what to do,
in what order, one step at a time.

Think of it like a recipe. A recipe says: "First, boil the water. Then, add the pasta.
Then, wait 10 minutes. Then, drain and serve." A program says the same kind of thing,
but to a computer, and in a language the computer can follow.

Computers are extremely fast and extremely literal. They do exactly what you tell them,
nothing more, nothing less. If your instructions are wrong, the result will be wrong.
This is not a flaw — it is what makes programming powerful. You are in complete control.

---

## What is Python?

**Python** is a programming language — a way of writing instructions that a computer
can understand. It was created in 1991 by Guido van Rossum and is now one of the most
popular languages in the world.

**Why learn Python?**

- It reads almost like plain English, which makes it great for beginners.
- It is used everywhere: web development, data science, artificial intelligence,
  automation, game development, and scientific research.
- It has a massive community, so help is always easy to find.
- The same skills you learn here apply to nearly every other programming language.

---

## Three ways to run Python

### Way 1: The REPL (interactive mode)

**REPL** stands for Read-Eval-Print Loop. It is a live conversation with Python —
you type one line, Python runs it immediately and shows you the result.

Open a terminal and type:
```
python
```

You will see something like:
```
Python 3.12.0 (...)
>>> 
```

The `>>>` is Python waiting for your input. Try typing:
```python
>>> print("Hello!")
Hello!
>>> 2 + 2
4
>>> "hello".upper()
'HELLO'
```

To exit the REPL, type `exit()` and press Enter.

The REPL is excellent for experimenting and testing small ideas. You will use it often.

### Way 2: A script file

A **script** is a `.py` file that contains Python code. You run the whole file at once.

1. Create a file called `hello.py`.
2. Type `print("Hello, world!")` inside it.
3. Save it.
4. In a terminal, navigate to the folder containing the file and run:
   ```
   python hello.py
   ```
5. Python reads the file top to bottom and executes every line.

This is how real programs work. You will write all exercises as script files.

### Way 3: VS Code

VS Code is a code editor with Python support built in. Once the Python extension is
installed (see README.md), you can open any `.py` file and press `F5` to run it, or
right-click in the file and choose "Run Python File in Terminal".

VS Code also shows you errors as you type, which is very helpful.

---

## print() — your most-used function

A **function** is a named action you can trigger. You will learn to write your own
functions in Module 09. For now, you will use built-in functions that Python provides.

`print()` is a function that displays text (or anything else) in the terminal.

```python
print("Hello, world!")
```

Run this. You will see:
```
Hello, world!
```

The text inside the parentheses is called an **argument**. You are passing the text
`"Hello, world!"` as an argument to `print()`.

The quotation marks around the text tell Python that this is a **string** — a sequence
of characters. You can use single quotes (`'`) or double quotes (`"`) — both work.

### Printing multiple values

You can give `print()` multiple arguments separated by commas:

```python
print("My name is", "Alice", "and I am", 17, "years old.")
```

Output:
```
My name is Alice and I am 17 years old.
```

Python automatically puts a space between each argument. That default space is
controlled by the `sep` parameter.

### The sep parameter

`sep` stands for "separator". It controls what Python puts between arguments.

```python
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print("2024", "01", "15", sep="-")
# Output: 2024-01-15

print("a", "b", "c", sep="")
# Output: abc
```

### The end parameter

By default, `print()` adds a newline character (`\n`) at the end, which moves the
cursor to the next line. The `end` parameter lets you change this.

```python
print("Loading", end="")
print("...", end="")
print(" Done!")
# Output: Loading... Done!

print("Step 1", end=" | ")
print("Step 2", end=" | ")
print("Step 3")
# Output: Step 1 | Step 2 | Step 3
```

---

## Comments

A **comment** is a line (or part of a line) that Python ignores completely.
Comments are for humans — they explain what the code is doing.

```python
# This is a comment. Python skips this line entirely.
print("Hello!")  # This is an inline comment — runs after the print

# Use comments to:
# - Explain WHY you wrote the code this way (not just what it does)
# - Leave notes for your future self
# - Temporarily disable a line while debugging
```

Good comment:
```python
# Convert the score to a letter grade because the report needs a letter, not a number
grade = convert_score(score)
```

Not-so-useful comment:
```python
# Print hello
print("hello")
```

The second comment just repeats what the code already says. Aim for comments that
add information the code itself does not convey.

---

## Common beginner errors

Errors are a normal, expected part of programming. Even experienced developers make
them constantly. The skill is reading the error message to understand what went wrong.

### SyntaxError

A **SyntaxError** means Python cannot understand what you typed — the code is
grammatically wrong, like a sentence missing punctuation.

```python
# ERROR: missing closing parenthesis
print("Hello"
```

Python's message:
```
SyntaxError: '(' was never closed
```

### NameError

A **NameError** means you tried to use a name (variable or function) that Python
does not know about — either because you spelled it wrong or forgot to define it.

```python
# ERROR: 'pint' is not defined — the function is called 'print'
pint("Hello!")
```

Python's message:
```
NameError: name 'pint' is not defined
```

**How to approach errors:**
1. Read the last line of the error message first — it tells you what went wrong.
2. Read the line number — Python tells you exactly where the problem is.
3. Look at your code on that line. Compare carefully with the working examples.

Errors are not failures. They are feedback. Every error you fix teaches you something.
