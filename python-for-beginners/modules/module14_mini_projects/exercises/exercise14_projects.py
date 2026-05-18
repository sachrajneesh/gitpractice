"""
Exercise 14 🔴: Mini Projects

What you'll practise:
  Everything from Modules 01-13, applied to building complete programs.

This file contains starter outlines for all three projects.
Build them one at a time. Start with Project 1.

How to run:
  python modules/module14_mini_projects/exercises/exercise14_projects.py
  (then uncomment the project you want to work on)

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Re-read the relevant module's CONCEPTS.md,
    then try again before looking for hints online.
"""

# ============================================================
# PROJECT 1: Number Quiz (Easy) 🟢
# ============================================================
# Uncomment and complete this section to work on Project 1.

"""
import random

def generate_question():
    # TODO: Pick two random numbers (1-20) and a random operator (+, -, *)
    # TODO: Return the question string and the correct answer
    pass

def ask_question(question, correct_answer):
    # TODO: Print the question, get input, convert to int
    # TODO: Return True if correct, False if wrong
    pass

def show_results(score, total):
    # TODO: Print score as X/Y
    # TODO: Map score to letter grade and print it
    pass

def main():
    score = 0
    total_questions = 10
    # TODO: Loop total_questions times
    # TODO: Generate a question, ask it, update score
    show_results(score, total_questions)

if __name__ == "__main__":
    main()
"""

# ============================================================
# PROJECT 2: Expense Tracker (Medium) 🟡
# ============================================================
# Uncomment and complete this section to work on Project 2.

"""
import csv
from datetime import datetime

CATEGORIES = ["food", "transport", "entertainment", "other"]
EXPENSES_FILE = "expenses.csv"

def load_expenses():
    # TODO: Read expenses from EXPENSES_FILE if it exists
    # TODO: Return a list of dicts: [{date, amount, category, note}, ...]
    pass

def save_expenses(expenses):
    # TODO: Write all expenses to EXPENSES_FILE
    pass

def add_expense(expenses):
    # TODO: Ask for amount, category, and note
    # TODO: Append a new dict to expenses with today's date
    pass

def show_summary(expenses):
    # TODO: Print total spent
    # TODO: Print breakdown by category
    pass

def main():
    expenses = load_expenses()
    # TODO: Main menu loop: Add / Summary / Quit
    pass

if __name__ == "__main__":
    main()
"""

# ============================================================
# PROJECT 3: Text-Based Adventure (Hard) 🔴
# ============================================================
# Uncomment and complete this section to work on Project 3.

"""
ROOMS = {
    "entrance": {
        "description": "You stand at the entrance of a crumbling castle.",
        "exits": {"north": "hallway"},
        "items": ["torch"],
    },
    "hallway": {
        "description": "A long dark hallway. Suits of armour line the walls.",
        "exits": {"south": "entrance", "north": "throne_room", "east": "library"},
        "items": [],
    },
    "library": {
        "description": "Dusty shelves filled with ancient books.",
        "exits": {"west": "hallway"},
        "items": ["key"],
    },
    "throne_room": {
        "description": "A vast room with a locked iron door to the north.",
        "exits": {"south": "hallway"},
        "items": [],
        "locked_exit": {"direction": "north", "requires": "key", "leads_to": "treasure_room"},
    },
    "treasure_room": {
        "description": "Gold and jewels everywhere. You have won!",
        "exits": {},
        "items": [],
        "win": True,
    },
}

def describe_room(room):
    # TODO: Print room description, exits, and items
    pass

def handle_command(command, current_room_id, inventory):
    # TODO: Parse command: go <direction>, pick up <item>, use <item>, look, quit
    # TODO: Return (new_room_id, inventory, game_over)
    pass

def main():
    current_room_id = "entrance"
    inventory = []
    game_over = False
    # TODO: Main loop — describe room, get command, handle command
    pass

if __name__ == "__main__":
    main()
"""

# ============================================================
# To start: uncomment ONE project section above and complete it.
# ============================================================
print("Uncomment a project section above to start building!")
