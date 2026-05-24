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

contacts = {}   # empty dict: keys=name, values=phone number

while True:
    print("\n=== Contacts Book ===")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. List all contacts")
    print("4. Delete contact")
    print("5. Quit")

    choice = input("Choice: ").strip()

    if choice == "1":
        name = input("Name: ").strip().title()    # .title() capitalises consistently
        phone = input("Phone: ").strip()
        if name and phone:
            contacts[name] = phone
            print("Contact saved!")
        else:
            print("Name and phone cannot be empty.")

    elif choice == "2":
        search = input("Search name: ").strip().title()   # normalise the search too
        phone = contacts.get(search)    # get() returns None if not found (no crash)
        if phone:
            print(f"{search}: {phone}")
        else:
            print(f"'{search}' not found in contacts.")

    elif choice == "3":
        if not contacts:
            print("No contacts yet.")
        else:
            print(f"\nAll contacts ({len(contacts)}):")
            # Sort alphabetically for a nicer display
            for name in sorted(contacts):
                print(f"  {name}: {contacts[name]}")

    elif choice == "4":
        name = input("Delete name: ").strip().title()
        if name in contacts:
            del contacts[name]
            print(f"'{name}' deleted.")
        else:
            print(f"'{name}' not found — nothing to delete.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1–5.")
