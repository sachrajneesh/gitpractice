"""Demonstrates: catching multiple exception types and the Exception base class"""

# ---------------------------------------------------------------
# You can catch different exception types in several ways:
#
# 1. Multiple except clauses — one per exception type
#    (best when each error needs different handling)
#
# 2. Tuple of types in one except clause
#    (when several errors should be handled the same way)
#
# 3. except Exception — catches almost everything
#    (use as a last resort / safety net)
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# --- Multiple except clauses ---
# ---------------------------------------------------------------

def parse_score(value):
    """Convert a string to a score between 0 and 100."""
    try:
        score = int(value)         # might raise ValueError if not numeric

        if score < 0 or score > 100:
            raise ValueError(f"Score must be 0-100, got {score}")

        result = 100 / score       # might raise ZeroDivisionError if score=0
        return score

    except ValueError as e:
        print(f"Invalid value: {e}")
        return None

    except ZeroDivisionError:
        print("Score cannot be zero (would cause division by zero).")
        return None

print("=== parse_score tests ===")
print(parse_score("88"))       # 88 — works fine
print(parse_score("hello"))   # ValueError: invalid literal...
print(parse_score("150"))     # ValueError: must be 0-100
print(parse_score("0"))       # ZeroDivisionError caught

# ---------------------------------------------------------------
# --- Catching multiple exceptions in ONE clause using a tuple ---
# ---------------------------------------------------------------

def load_config(filename, key):
    """Load a value from a simple config file by key."""
    try:
        with open(filename, "r") as f:
            data = {}
            for line in f:
                k, v = line.strip().split("=")  # might raise ValueError (no '=')
                data[k.strip()] = v.strip()
            return data[key]           # might raise KeyError

    except (FileNotFoundError, KeyError, ValueError) as e:
        # All three errors get the same user-friendly response
        print(f"Could not load config: {e}")
        return None

print("\n=== load_config tests ===")
print(load_config("settings.cfg", "username"))   # FileNotFoundError

# ---------------------------------------------------------------
# --- except Exception — the broad catch-all ---
# ---------------------------------------------------------------
# Exception is the base class for almost all exceptions.
# It's useful as a final safety net but don't overuse it —
# catching too broadly hides bugs.

def risky_operation(items):
    """Demonstrate a broad exception catch."""
    try:
        total = sum(items)    # fails if items contains non-numbers
        avg = total / len(items)   # fails if list is empty
        return avg
    except ZeroDivisionError:
        print("Cannot average an empty list.")
        return None
    except TypeError:
        print("List contains non-numeric values.")
        return None
    except Exception as e:
        # Last resort: catch anything unexpected
        print(f"Unexpected error ({type(e).__name__}): {e}")
        return None

print("\n=== risky_operation tests ===")
print(risky_operation([10, 20, 30]))    # 20.0 — works
print(risky_operation([]))              # ZeroDivisionError caught
print(risky_operation([1, "two", 3]))  # TypeError caught

# ---------------------------------------------------------------
# Exception hierarchy (simplified):
#   BaseException
#   └── Exception
#       ├── ValueError      (wrong value type/format)
#       ├── TypeError       (wrong argument type)
#       ├── KeyError        (dict key not found)
#       ├── IndexError      (list index out of range)
#       ├── FileNotFoundError (file not found)
#       ├── ZeroDivisionError (division by zero)
#       └── ... many more
# ---------------------------------------------------------------
