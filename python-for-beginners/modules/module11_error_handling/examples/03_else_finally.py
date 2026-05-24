"""Demonstrates: try/except/else/finally — when each block runs"""

# ---------------------------------------------------------------
# The full try/except structure has four optional blocks:
#
#   try:
#       # code that might raise an exception
#   except SomeError:
#       # runs ONLY if SomeError was raised in try
#   else:
#       # runs ONLY if NO exception was raised in try
#   finally:
#       # runs ALWAYS — whether or not an exception occurred
#       # great for cleanup (close files, print "done", etc.)
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Walkthrough: all four blocks ---
# ---------------------------------------------------------------

def safe_divide(a, b):
    """Demonstrate try/except/else/finally."""
    print(f"\nDividing {a} / {b}:")
    try:
        result = a / b        # this is the risky operation

    except ZeroDivisionError:
        print("  except: caught ZeroDivisionError — cannot divide by zero!")
        result = None

    else:
        # Only runs if try succeeded with NO exception
        print(f"  else: division worked! result = {result}")

    finally:
        # ALWAYS runs — even if we hit except, even if we hit return
        print("  finally: this always runs (cleanup goes here)")

    return result

safe_divide(10, 2)   # try succeeds → else runs → finally runs
safe_divide(10, 0)   # try fails   → except runs → finally runs (else is skipped)

# ---------------------------------------------------------------
# --- Practical example: file reading with all four blocks ---
# ---------------------------------------------------------------

import os

def read_score_file(filename):
    """Read a high score from a file, with full try/except/else/finally."""
    f = None
    try:
        f = open(filename, "r")    # might raise FileNotFoundError
        score = int(f.read().strip())  # might raise ValueError

    except FileNotFoundError:
        print(f"  File '{filename}' not found.")
        return None

    except ValueError:
        print("  File content is not a valid number.")
        return None

    else:
        # Only reached if open() AND int() both succeeded
        print(f"  High score loaded: {score}")
        return score

    finally:
        # Close the file whether or not there was an error.
        # This is exactly what 'with open(...)' does for you automatically!
        if f:
            f.close()
            print("  File closed in finally block.")

# Test with a file that doesn't exist
read_score_file("highscore.txt")

# Create a test file and try again
with open("highscore.txt", "w") as f:
    f.write("9999")

read_score_file("highscore.txt")

# Test with bad content
with open("highscore.txt", "w") as f:
    f.write("not_a_number")

read_score_file("highscore.txt")

# Clean up
os.remove("highscore.txt")

# ---------------------------------------------------------------
# Summary: when each block runs
# ---------------------------------------------------------------
print("""
Block      | try succeeds | try raises exception
-----------|-------------|---------------------
try        | YES         | YES (until error)
except     | NO          | YES (matching type)
else       | YES         | NO
finally    | YES         | YES (always!)
""")

# ---------------------------------------------------------------
# Key insight: use 'with open(...)' in real code — it handles
# the finally-close automatically and is cleaner than writing
# try/finally yourself.
# ---------------------------------------------------------------
