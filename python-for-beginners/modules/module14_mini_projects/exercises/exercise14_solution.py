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

import random
import csv
import os
from datetime import datetime


# ============================================================
# PROJECT 1: Number Quiz
# ============================================================

def generate_question():
    """Pick two random numbers and a random operator. Return (question_str, answer)."""
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    else:
        answer = a * b

    question = f"What is {a} {operator} {b}?"
    return question, answer


def ask_question(question, correct_answer):
    """Ask the question, get the player's answer. Return True if correct."""
    try:
        user_answer = int(input(f"  {question} "))
    except ValueError:
        print("  (Please enter a whole number)")
        return False
    return user_answer == correct_answer


def quiz_grade(score, total):
    """Return a letter grade based on score/total."""
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def run_quiz():
    """Run a 10-question number quiz."""
    print("\n" + "=" * 40)
    print("  PROJECT 1: Number Quiz")
    print("=" * 40)
    print("Answer 10 random maths questions.\n")

    score = 0
    total = 10

    for i in range(total):
        print(f"Question {i + 1}/{total}:")
        question, answer = generate_question()
        if ask_question(question, answer):
            print("  Correct!")
            score += 1
        else:
            print(f"  Wrong. The answer was {answer}.")

    grade = quiz_grade(score, total)
    print(f"\nFinal score: {score}/{total} — Grade: {grade}")
    if grade == "A":
        print("Outstanding! Maths wizard!")
    elif grade in ("B", "C"):
        print("Good effort! Keep practising.")
    else:
        print("Keep at it — maths takes practice!")


# ============================================================
# PROJECT 2: Expense Tracker
# ============================================================

EXPENSES_FILE = "expenses.csv"
CATEGORIES = ["food", "transport", "entertainment", "other"]


def load_expenses():
    """Load expenses from CSV. Returns a list of dicts."""
    if not os.path.exists(EXPENSES_FILE):
        return []
    expenses = []
    with open(EXPENSES_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses


def save_expenses(expenses):
    """Write all expenses to CSV."""
    with open(EXPENSES_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    """Prompt the user and add a new expense."""
    try:
        amount = float(input("Amount (£): "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    print(f"Categories: {', '.join(CATEGORIES)}")
    category = input("Category: ").strip().lower()
    if category not in CATEGORIES:
        category = "other"

    note = input("Note (optional): ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append({"date": date, "category": category, "amount": amount, "note": note})
    save_expenses(expenses)
    print(f"Saved: £{amount:.2f} ({category})")


def show_expense_summary(expenses):
    """Print total and per-category breakdown."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal: £{total:.2f}")

    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat, 0) + e["amount"]

    print("Breakdown:")
    for cat, amount in sorted(by_category.items()):
        pct = (amount / total) * 100
        print(f"  {cat:15} £{amount:7.2f}  ({pct:.0f}%)")


def run_expense_tracker():
    """Run the expense tracker menu loop."""
    print("\n" + "=" * 40)
    print("  PROJECT 2: Expense Tracker")
    print("=" * 40)

    expenses = load_expenses()

    while True:
        print("\n1. Add expense")
        print("2. Show summary")
        print("3. Back to main menu")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expense_summary(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# ============================================================
# PROJECT 3: Text Adventure
# ============================================================

ROOMS = {
    "entrance": {
        "description": "You stand at the entrance of Crumbling Castle. Vines cover the walls.",
        "exits": {"north": "hallway"},
        "items": ["torch"],
    },
    "hallway": {
        "description": "A long dark hallway. Suits of armour line the walls.",
        "exits": {"south": "entrance", "north": "throne_room", "east": "library"},
        "items": [],
    },
    "library": {
        "description": "Dusty shelves filled with ancient books. Something glints on a shelf.",
        "exits": {"west": "hallway"},
        "items": ["key"],
    },
    "throne_room": {
        "description": "A vast hall with a cracked throne. A heavy iron door blocks the north.",
        "exits": {"south": "hallway"},
        "items": [],
        "locked_exit": {"direction": "north", "requires": "key", "leads_to": "treasure_room"},
    },
    "treasure_room": {
        "description": "Gold and jewels fill every corner. You have found the legendary treasure!",
        "exits": {},
        "items": [],
        "win": True,
    },
}


def describe_room(room_id):
    """Print description, items, and exits for the current room."""
    room = ROOMS[room_id]
    print(f"\n{room['description']}")
    if room["items"]:
        print(f"Items: {', '.join(room['items'])}")
    exits = list(room.get("exits", {}).keys())
    locked = room.get("locked_exit")
    if locked:
        exits.append(f"{locked['direction']} (locked — needs {locked['requires']})")
    if exits:
        print(f"Exits: {', '.join(exits)}")
    else:
        print("There is no way out.")


def handle_adventure_command(command, current_room_id, inventory):
    """Parse command and return (new_room_id, inventory, game_over)."""
    words = command.lower().strip().split()
    if not words:
        return current_room_id, inventory, False

    action = words[0]

    if action == "go" and len(words) > 1:
        direction = words[1]
        room = ROOMS[current_room_id]

        # Check regular exits
        if direction in room.get("exits", {}):
            return room["exits"][direction], inventory, False

        # Check locked exit
        locked = room.get("locked_exit")
        if locked and direction == locked["direction"]:
            if locked["requires"] in inventory:
                print(f"You use the {locked['requires']} to unlock the door.")
                return locked["leads_to"], inventory, False
            else:
                print(f"The door is locked. You need a {locked['requires']}.")
        else:
            print("You can't go that way.")

    elif action in ("pick", "take", "get") and len(words) > 1:
        item = words[-1]
        room_items = ROOMS[current_room_id]["items"]
        if item in room_items:
            inventory.append(item)
            room_items.remove(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} here.")

    elif action == "look":
        describe_room(current_room_id)

    elif action in ("inventory", "inv", "i"):
        print(f"Carrying: {', '.join(inventory)}" if inventory else "Nothing in inventory.")

    elif action == "quit":
        print("You flee the castle. Until next time!")
        return current_room_id, inventory, True

    else:
        print("Commands: go <direction>, pick up <item>, look, inventory, quit")

    return current_room_id, inventory, False


def run_adventure():
    """Run the text adventure main loop."""
    print("\n" + "=" * 40)
    print("  PROJECT 3: Crumbling Castle Adventure")
    print("=" * 40)
    print("Commands: go <direction>, pick up <item>, look, inventory, quit\n")

    current_room = "entrance"
    inventory = []
    game_over = False

    describe_room(current_room)

    while not game_over:
        command = input("\n> ").strip()
        current_room, inventory, game_over = handle_adventure_command(
            command, current_room, inventory
        )

        if ROOMS[current_room].get("win"):
            describe_room(current_room)
            print("\nYOU WIN! Congratulations, adventurer!")
            break
        elif not game_over:
            # Only re-describe the room if the player moved (detect by checking
            # if describe was called in handle). Simplest approach: always describe.
            pass


# ============================================================
# Main launcher — choose which project to run
# ============================================================

if __name__ == "__main__":
    print("=" * 40)
    print("  Module 14 — Mini Projects")
    print("=" * 40)
    print("1. Number Quiz")
    print("2. Expense Tracker")
    print("3. Text Adventure")

    choice = input("Which project? (1/2/3): ").strip()

    if choice == "1":
        run_quiz()
    elif choice == "2":
        run_expense_tracker()
    elif choice == "3":
        run_adventure()
    else:
        print("Invalid choice.")
