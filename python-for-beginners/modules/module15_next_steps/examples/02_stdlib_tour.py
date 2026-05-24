"""Demonstrates: a quick tour of 5 useful stdlib modules — os, sys, json, re, pathlib"""

# ---------------------------------------------------------------
# Python ships with a huge standard library — "batteries included".
# This file demos 5 modules you'll reach for constantly.
# All are built-in: no pip install needed.
# ---------------------------------------------------------------

import os
import sys
import json
import re
from pathlib import Path

print("=" * 50)
print("  Standard Library Tour")
print("=" * 50)

# ---------------------------------------------------------------
# 1. os — interact with the operating system
# ---------------------------------------------------------------
print("\n--- os ---")
print(f"Current directory:     {os.getcwd()}")
print(f"User home directory:   {os.path.expanduser('~')}")
print(f"PATH env variable:     {os.environ.get('HOME', 'not set')}")

# List files in the current directory
files = os.listdir(".")
print(f"Files in '.': {files[:5]}...")   # show first 5

# Join paths safely (handles / vs \ automatically)
config_path = os.path.join(os.path.expanduser("~"), ".config", "settings.json")
print(f"Joined path:  {config_path}")

# ---------------------------------------------------------------
# 2. sys — Python interpreter info and runtime tools
# ---------------------------------------------------------------
print("\n--- sys ---")
print(f"Python version:  {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"Platform:        {sys.platform}")
print(f"Script name:     {sys.argv[0]}")   # sys.argv[0] is the current script
print(f"Python path (first 2): {sys.path[:2]}")

# sys.exit() stops the program — useful in scripts
# sys.exit(0)  ← would exit here with code 0 (success)

# ---------------------------------------------------------------
# 3. json — read and write JSON data
# ---------------------------------------------------------------
print("\n--- json ---")

# Python dict → JSON string
player_data = {
    "name": "Ryan",
    "level": 12,
    "scores": [88, 74, 95],
    "active": True,
}

json_string = json.dumps(player_data, indent=2)   # indent makes it pretty
print("Dict → JSON:")
print(json_string)

# JSON string → Python dict
loaded = json.loads(json_string)
print(f"\nJSON → Dict: {loaded['name']} at level {loaded['level']}")

# Save to file / load from file
json_path = Path("player_demo.json")
json_path.write_text(json_string)
print(f"\nSaved to {json_path}")

loaded_from_file = json.loads(json_path.read_text())
print(f"Loaded: {loaded_from_file['name']}")

json_path.unlink()   # clean up

# ---------------------------------------------------------------
# 4. re — regular expressions for pattern matching
# ---------------------------------------------------------------
print("\n--- re ---")

text = "Ryan scored 88 points on 2024-01-15. Alice scored 95 points."

# Find all numbers in the string
numbers = re.findall(r"\d+", text)
print(f"All numbers in text: {numbers}")

# Find a date pattern (YYYY-MM-DD)
date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
if date_match:
    print(f"Date found: {date_match.group()}")

# Replace a pattern
cleaned = re.sub(r"\d+", "##", text)   # replace all numbers with ##
print(f"Numbers replaced: {cleaned}")

# Validate an email address (simplified pattern)
email = "ryan@example.com"
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print(f"'{email}' looks like a valid email address.")

# ---------------------------------------------------------------
# 5. pathlib — modern path handling (you've seen this in Module 10!)
# ---------------------------------------------------------------
print("\n--- pathlib ---")

p = Path(__file__)   # __file__ is the path to the current script
print(f"This script:  {p.name}")
print(f"Directory:    {p.parent}")
print(f"Stem:         {p.stem}")    # filename without extension
print(f"Suffix:       {p.suffix}")  # .py

# Find all .py files in this directory
py_files = list(p.parent.glob("*.py"))
print(f"\n.py files in this folder: {len(py_files)}")
for f in sorted(py_files):
    print(f"  {f.name}")

print("\nThat's the stdlib tour! These 5 modules will serve you well.")
