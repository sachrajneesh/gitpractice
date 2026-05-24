"""Demonstrates: the expense tracker pattern — file + dict for persistence"""

# ---------------------------------------------------------------
# This is a simplified version of Project 2 (Expense Tracker).
# It shows the core patterns:
#   - Store expenses as a list of dicts
#   - Save/load data from a CSV file for persistence
#   - Show a category summary
# ---------------------------------------------------------------

import csv
import os
from datetime import datetime

EXPENSES_FILE = "demo_expenses.csv"   # demo file — will be deleted at end


def load_expenses():
    """Load expenses from CSV file. Returns a list of dicts."""
    if not os.path.exists(EXPENSES_FILE):
        return []   # empty list if file doesn't exist yet
    expenses = []
    with open(EXPENSES_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["amount"] = float(row["amount"])   # convert string back to float
            expenses.append(row)
    return expenses


def save_expenses(expenses):
    """Save all expenses to CSV file."""
    if not expenses:
        return
    with open(EXPENSES_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    """Add one expense entry."""
    try:
        amount = float(input("Amount (£): "))
    except ValueError:
        print("Invalid amount.")
        return
    category = input("Category (food/transport/entertainment/other): ").strip().lower()
    note = input("Note: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "note": note,
    })
    save_expenses(expenses)   # save immediately after adding
    print(f"Added: £{amount:.2f} for {category}")


def show_summary(expenses):
    """Print total and category breakdown."""
    if not expenses:
        print("No expenses yet.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: £{total:.2f}")

    # Build a category totals dict
    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat, 0) + e["amount"]

    print("By category:")
    for cat, amount in sorted(by_category.items()):
        print(f"  {cat:15} £{amount:.2f}")


# --- Demo: add a couple of expenses and show summary ---
print("=== Expense Tracker Demo ===\n")

expenses = load_expenses()

# Simulate adding two expenses automatically for the demo
print("Adding demo expenses...")
expenses.append({"date": "2024-01-15", "category": "food", "amount": 12.50, "note": "Pizza lunch"})
expenses.append({"date": "2024-01-15", "category": "transport", "amount": 3.40, "note": "Bus fare"})
save_expenses(expenses)

show_summary(expenses)

print("\n--- Interactive add ---")
add_expense(expenses)
show_summary(expenses)

# Clean up the demo file
if os.path.exists(EXPENSES_FILE):
    os.remove(EXPENSES_FILE)
    print("\nDemo file removed.")
