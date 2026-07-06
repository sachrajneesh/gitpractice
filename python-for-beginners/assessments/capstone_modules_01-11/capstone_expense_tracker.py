"""
CAPSTONE 🔴: Expense Tracker (Modules 01–11)

This is a knowledge check, not a guided lesson. There are fewer hints than a
normal exercise on purpose. You already have every tool you need — this asks you
to combine skills from Modules 1 through 11 into one working program.

--------------------------------------------------------------------------------
WHAT YOU ARE BUILDING
--------------------------------------------------------------------------------
A command-line Expense Tracker. It shows a menu in a loop and lets the user:

    1. Add an expense       (description, category, amount)
    2. View all expenses    (nicely formatted table)
    3. View totals by category
    4. Save expenses to a file
    5. Load expenses from a file
    6. Quit

Each expense is stored as a DICTIONARY, for example:
    {"description": "Coffee", "category": "Food", "amount": 3.5}

All expenses are stored together in a LIST of those dictionaries.

--------------------------------------------------------------------------------
REQUIREMENTS  (this is how your work will be graded)
--------------------------------------------------------------------------------
Structure & functions (Module 9):
  [ ] The program is organised into FUNCTIONS. Each function does one job.
  [ ] Every function has a one-line docstring.
  [ ] There is a main() function that runs the menu loop.

Menu loop (Modules 5 & 6):
  [ ] A while loop keeps showing the menu until the user chooses Quit.
  [ ] if / elif / else (or match) dispatches each menu choice.

Adding an expense (Modules 2, 3, 4):
  [ ] Ask for description, category, and amount using input().
  [ ] Convert the amount to a float. Clean up text with .strip()/.title().
  [ ] Store the expense as a dictionary appended to the list (Modules 7 & 8).

Viewing expenses (Modules 3, 6, 7):
  [ ] Loop over the list and print each expense with an f-string.
  [ ] Print a grand total of all amounts at the bottom.
  [ ] If the list is empty, print a friendly "no expenses yet" message.

Totals by category (Module 8):
  [ ] Build a dictionary of {category: total_amount} and print it.

Save & load (Module 10):
  [ ] Save the expenses to a CSV file (one row per expense).
  [ ] Load them back from that CSV file into the list.

Error handling (Module 11):
  [ ] If the user types a non-number for the amount, catch it and re-ask
      (do NOT let the program crash).
  [ ] If the user tries to load a file that does not exist, catch the error
      and print a friendly message.

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
  python assessments/capstone_modules_01-11/capstone_expense_tracker.py

--------------------------------------------------------------------------------
RULES
--------------------------------------------------------------------------------
  - TYPE every line yourself — no copy-paste.
  - You may look back at earlier module exercises, but do NOT open a solution
    until you have genuinely tried.
  - Get it working first, then make it neat. A messy program that runs beats a
    beautiful one that doesn't.

--------------------------------------------------------------------------------
STRETCH GOALS (only if the above all works)
--------------------------------------------------------------------------------
  - Add a menu option to delete an expense by its number.
  - When viewing, sort expenses from highest amount to lowest.
  - Use pathlib.Path for the file path instead of a plain string.
  - Prevent adding an expense with a negative amount (raise or re-ask).
"""

# =============================================================================
# Your code goes below. The TODOs are a suggested order — you decide the details.
# =============================================================================

# TODO: A place to store all expenses (a list). Where should it live?

# TODO: def add_expense(expenses):        ask user, build a dict, append it
# TODO: def view_expenses(expenses):      print a table + grand total
# TODO: def totals_by_category(expenses): build & print {category: total}
# TODO: def save_expenses(expenses, filename):   write to CSV
# TODO: def load_expenses(filename):             read from CSV, return a list
# TODO: def print_menu():                 print the 6 options
# TODO: def main():                       the while-loop menu that ties it together


# TODO: At the very bottom, call main() so the program actually starts.
#       (Bonus: use the  if __name__ == "__main__":  guard you saw in Module 09.)
