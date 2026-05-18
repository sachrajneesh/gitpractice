# Module 15 Concepts: Next Steps

> This is a stub / ecosystem overview. It is intentionally brief.
> The goal is to point you toward the right tools, not to teach them here.

---

## Web development with Flask

Flask is a "micro-framework" — it gives you routing and request handling without
making too many decisions for you. Perfect for learning web development.

```python
# Install: pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

Visit http://127.0.0.1:5000 in your browser after running.

---

## Data analysis with pandas

pandas provides the DataFrame — a table structure like a spreadsheet, in Python.

```python
# Install: pip install pandas
import pandas as pd

df = pd.read_csv("expenses.csv")
print(df.head())           # first 5 rows
print(df.describe())       # statistical summary
print(df["category"].value_counts())
```

---

## Making web requests with requests

```python
# Install: pip install requests
import requests

response = requests.get("https://api.github.com/users/python")
data = response.json()
print(data["public_repos"])
```

---

## Game development with pygame

```python
# Install: pip install pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
```

---

## Command-line tools with argparse

```python
import argparse

parser = argparse.ArgumentParser(description="A simple CLI tool")
parser.add_argument("name", help="Your name")
parser.add_argument("--shout", action="store_true", help="Print in uppercase")

args = parser.parse_args()
message = f"Hello, {args.name}!"
print(message.upper() if args.shout else message)
```

Run as: `python tool.py Alice --shout`

---

## Recommended learning sequence after this course

1. Build one more command-line project entirely on your own (no tutorials).
2. Then pick one path (web / data / automation / games) and do one focused course.
3. Build something real in that domain.
4. Repeat.

The pattern is always: learn a little → build something → learn more → build more.
