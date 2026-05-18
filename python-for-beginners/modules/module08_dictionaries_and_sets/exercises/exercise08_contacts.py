"""
Exercise 08 🟡: Contacts Book

What you'll practise:
  Dictionaries, nested dicts, loops, and menu-driven programs.

Task:
  Build a contacts book where the user can add a contact (name + phone),
  look up a contact by name, list all contacts, and delete a contact.

Requirements:
  - Store contacts in a dictionary: keys are names, values are phone numbers.
  - Menu options: 1) Add  2) Look up  3) List all  4) Delete  5) Quit
  - Look up should be case-insensitive (store names in a consistent format).
  - Searching for a non-existent contact should print a helpful message.
  - Deleting a non-existent contact should not crash.

Example interaction:
  1. Add contact
  2. Look up contact
  3. List all contacts
  4. Delete contact
  5. Quit
  Choice: 1
  Name: Alice
  Phone: 555-0101
  Contact saved!

  Choice: 2
  Search name: alice
  Alice: 555-0101

How to run:
  python modules/module08_dictionaries_and_sets/exercises/exercise08_contacts.py

Hints:
  - Store keys as name.title() to normalise capitalisation.
  - Use contacts.get(name, None) to avoid KeyError on lookup.
  - To list all: for name, phone in contacts.items(): ...

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# TODO: Step 1 — Create an empty dictionary to store contacts
# TODO: Step 2 — Write the main menu loop (while True)
# TODO: Step 3 — Handle "Add": get name and phone, store in dict
# TODO: Step 4 — Handle "Look up": get name, print phone or "not found"
# TODO: Step 5 — Handle "List all": iterate and print all contacts
# TODO: Step 6 — Handle "Delete": remove by name, or print "not found"
# TODO: Step 7 — Handle "Quit": break
