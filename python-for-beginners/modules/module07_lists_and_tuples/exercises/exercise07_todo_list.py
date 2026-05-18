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

# === Your code goes below this line ===

# TODO: Step 1 — Create an empty list to store tasks
# TODO: Step 2 — Write a while True loop that shows the menu
# TODO: Step 3 — Handle choice "1": append a new task
# TODO: Step 4 — Handle choice "2": display all tasks with numbers
# TODO: Step 5 — Handle choice "3": ask for task number and remove it
# TODO: Step 6 — Handle choice "4": break out of the loop
# TODO: Step 7 — Handle invalid menu choices with an else clause
