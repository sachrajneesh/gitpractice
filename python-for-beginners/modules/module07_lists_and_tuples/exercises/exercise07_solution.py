"""
Exercise 07 🟡: To-Do List App

What you'll practise:
  Lists, list methods (append, remove), loops, and conditional logic
  to build a simple interactive menu-driven application.

Task:
  Build a command-line to-do list manager where the user can:
    - Add a new task
    - View all tasks (numbered)
    - Remove a task by number
    - Quit the program

Requirements:
  - Store tasks in a Python list.
  - Show a menu after each action (loop back to menu until user quits).
  - Number the tasks starting from 1 when displaying (list stores from index 0).
  - If no tasks exist, print a friendly "No tasks yet" message.
  - Handle invalid input (e.g. removing a task number that does not exist).

Example interaction:
  === To-Do List ===
  1. Add task
  2. View tasks
  3. Remove task
  4. Quit
  Choice: 1
  New task: Buy groceries
  Task added!

  Choice: 2
  Your tasks:
    1. Buy groceries

How to run:
  python modules/module07_lists_and_tuples/exercises/exercise07_todo_list.py

Hints:
  - Use a while True loop for the menu and break when the user quits.
  - To number items: for i, task in enumerate(tasks, start=1): print(f"{i}. {task}")
  - To remove by number: tasks.pop(number - 1)  (user sees 1-based, list is 0-based)
  - Wrap the remove in a try/except IndexError to handle out-of-range numbers.

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

tasks = []   # empty list to store all tasks

while True:
    # Print the menu every iteration so the user always knows their options.
    print("\n=== To-Do List ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Choice: ").strip()   # .strip() removes accidental whitespace

    if choice == "1":
        task = input("New task: ").strip()
        if task:   # only add if the user typed something
            tasks.append(task)
            print("Task added!")
        else:
            print("No task entered.")

    elif choice == "2":
        if not tasks:   # empty list is falsy in Python
            print("No tasks yet — add one first!")
        else:
            print("Your tasks:")
            # enumerate(tasks, start=1) gives pairs: (1, task1), (2, task2), ...
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            # Show tasks first so the user knows what numbers to use.
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"  {i}. {task}")

            try:
                number = int(input("Remove task number: "))
                removed = tasks.pop(number - 1)   # convert 1-based to 0-based index
                print(f"Removed: '{removed}'")
            except (ValueError, IndexError):
                # ValueError: user typed something that isn't a number
                # IndexError: number was valid int but out of range
                print("Invalid number. Please enter a number from the list.")

    elif choice == "4":
        print("Goodbye!")
        break   # exit the while True loop

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
