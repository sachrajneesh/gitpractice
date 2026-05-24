"""Demonstrates: how to create a virtual environment, install a package, and use it"""

# ---------------------------------------------------------------
# VIRTUAL ENVIRONMENTS AND PIP
#
# So far we've only used Python's built-in standard library.
# But Python has 500,000+ THIRD-PARTY packages on PyPI (pypi.org).
# pip is the tool that downloads and installs them.
#
# A VIRTUAL ENVIRONMENT (venv) is an isolated Python environment
# for a single project. This means:
#   - Each project has its own packages
#   - Installing package X for Project A doesn't affect Project B
#   - You can use different package versions in different projects
#
# This file explains the process with comments, then shows a
# runnable Python example using a common package.
# ---------------------------------------------------------------

# ============================================================
# STEP 1: Create a virtual environment
# (Run this in your terminal, NOT in Python)
# ============================================================

# Terminal commands (do NOT run these as Python code — they're shell commands):
#
#   python -m venv venv
#
# This creates a folder called 'venv' in your current directory
# containing a private copy of Python and pip.

# ============================================================
# STEP 2: Activate the virtual environment
# ============================================================

# On Mac/Linux:
#   source venv/bin/activate
#
# On Windows:
#   venv\Scripts\activate
#
# After activation you'll see (venv) at the start of your prompt:
#   (venv) ryan@laptop:~/myproject $
#
# This means your terminal is now using the venv's Python.

# ============================================================
# STEP 3: Install a package with pip
# ============================================================

# Example: install the 'requests' library (for making HTTP requests)
#
#   pip install requests
#
# pip downloads from PyPI and installs into your venv.
#
# To see all installed packages:
#   pip list
#
# To save your requirements to a file (so others can reproduce your env):
#   pip freeze > requirements.txt
#
# To install from a requirements.txt:
#   pip install -r requirements.txt

# ============================================================
# STEP 4: Use the installed package in Python
# ============================================================

# The rest of this file is RUNNABLE Python code.
# It uses only the built-in 'urllib' (no install needed) to demonstrate
# making an HTTP request — similar to what 'requests' would do.

import urllib.request
import json

print("=" * 50)
print("  Virtual Environments & pip Demo")
print("=" * 50)

# ---------------------------------------------------------------
# Runnable example: fetch public data from an API
# (This uses urllib from the standard library — no pip needed)
# ---------------------------------------------------------------

print("\nFetching a random joke from the internet...")
print("(This uses urllib — try the same with 'requests' after pip install requests)")

url = "https://official-joke-api.appspot.com/random_joke"

try:
    with urllib.request.urlopen(url, timeout=5) as response:
        data = json.loads(response.read())
    print(f"\nSetup:      {data['setup']}")
    print(f"Punchline:  {data['punchline']}")
except Exception as e:
    # If there's no internet connection, show what would happen
    print(f"(Could not reach API — check your connection): {e}")
    print("\nDemo output when it works:")
    print("  Setup:     Why do programmers prefer dark mode?")
    print("  Punchline: Because light attracts bugs!")

# ---------------------------------------------------------------
# What the same code looks like with 'requests' (after pip install):
# ---------------------------------------------------------------

print("""
# With 'requests' (after: pip install requests):
# -----------------------------------------------
# import requests
#
# response = requests.get("https://official-joke-api.appspot.com/random_joke")
# data = response.json()   # automatically parses JSON
# print(data['setup'])
# print(data['punchline'])
#
# That's it! Much cleaner than urllib.
""")

# ============================================================
# STEP 5: Deactivate when done
# ============================================================
#
# To leave the virtual environment:
#   deactivate
#
# Your prompt goes back to normal (no '(venv)' prefix).

# ============================================================
# Quick Reference
# ============================================================
print("Quick Reference:")
print("  python -m venv venv          # create venv")
print("  source venv/bin/activate     # activate (Mac/Linux)")
print("  venv\\Scripts\\activate        # activate (Windows)")
print("  pip install <package>        # install a package")
print("  pip list                     # see installed packages")
print("  pip freeze > requirements.txt # save your requirements")
print("  deactivate                   # exit the venv")
