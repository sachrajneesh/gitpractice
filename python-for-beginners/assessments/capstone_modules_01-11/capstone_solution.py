"""
CAPSTONE SOLUTION: Expense Tracker (Modules 01–11)

Reference solution. There are many correct ways to write this — the goal is to
show one clean version that satisfies every requirement. Do not hand this to
Ryan until he has finished (or genuinely got stuck on) his own attempt.

Run it:
  python assessments/capstone_modules_01-11/capstone_solution.py
"""

import csv
from pathlib import Path

DEFAULT_FILE = Path(__file__).parent / "expenses.csv"


def print_menu():
    """Print the main menu of options."""
    print("\n===== Expense Tracker =====")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View totals by category")
    print("4. Save expenses to file")
    print("5. Load expenses from file")
    print("6. Quit")


def ask_amount():
    """Ask for a positive number, re-asking until the input is valid."""
    while True:
        raw = input("Amount: ").strip()
        try:
            amount = float(raw)
        except ValueError:
            print("  That is not a number. Try again (e.g. 12.50).")
            continue
        if amount < 0:
            print("  Amount cannot be negative. Try again.")
            continue
        return amount


def add_expense(expenses):
    """Ask the user for expense details and append them as a dict."""
    description = input("Description: ").strip().title()
    category = input("Category: ").strip().title()
    amount = ask_amount()
    expenses.append({
        "description": description,
        "category": category,
        "amount": amount,
    })
    print(f"  Added: {description} ({category}) - ${amount:.2f}")


def view_expenses(expenses):
    """Print every expense in a table, plus the grand total."""
    if not expenses:
        print("  No expenses yet. Add one first!")
        return
    print(f"\n{'#':<3}{'Description':<20}{'Category':<15}{'Amount':>10}")
    print("-" * 48)
    grand_total = 0.0
    for i, exp in enumerate(expenses, start=1):
        print(f"{i:<3}{exp['description']:<20}{exp['category']:<15}${exp['amount']:>9.2f}")
        grand_total += exp["amount"]
    print("-" * 48)
    print(f"{'TOTAL':<38}${grand_total:>9.2f}")


def totals_by_category(expenses):
    """Print the total amount spent in each category."""
    if not expenses:
        print("  No expenses yet.")
        return
    totals = {}
    for exp in expenses:
        category = exp["category"]
        totals[category] = totals.get(category, 0.0) + exp["amount"]
    print("\nTotals by category:")
    for category, total in totals.items():
        print(f"  {category:<15} ${total:.2f}")


def save_expenses(expenses, filename=DEFAULT_FILE):
    """Write all expenses to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["description", "category", "amount"])
        for exp in expenses:
            writer.writerow([exp["description"], exp["category"], exp["amount"]])
    print(f"  Saved {len(expenses)} expense(s) to {filename}")


def load_expenses(filename=DEFAULT_FILE):
    """Read expenses from a CSV file and return them as a list of dicts."""
    expenses = []
    try:
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the header row
            for row in reader:
                if len(row) != 3:
                    continue  # skip malformed rows
                description, category, amount = row
                expenses.append({
                    "description": description,
                    "category": category,
                    "amount": float(amount),
                })
        print(f"  Loaded {len(expenses)} expense(s) from {filename}")
    except FileNotFoundError:
        print(f"  No saved file found at {filename}. Starting empty.")
    return expenses


def main():
    """Run the menu loop until the user quits."""
    expenses = []
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            totals_by_category(expenses)
        elif choice == "4":
            save_expenses(expenses)
        elif choice == "5":
            expenses = load_expenses()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
