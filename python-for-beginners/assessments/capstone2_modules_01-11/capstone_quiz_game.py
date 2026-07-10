"""
CAPSTONE #2 🔴: Quiz Game (Modules 01–11)

This is a second knowledge check at the same level as the Expense Tracker, but a
completely different problem. If you understood the *ideas* (not just memorised
the first capstone), you will be able to build this. There are few hints on
purpose.

--------------------------------------------------------------------------------
WHAT YOU ARE BUILDING
--------------------------------------------------------------------------------
A command-line Quiz Game. It shows a menu in a loop and lets the user:

    1. Add a question       (topic, question text, answer)
    2. View all questions
    3. Take the quiz        (get asked each question, get scored)
    4. Save questions to a file
    5. Load questions from a file
    6. Quit

Each question is stored as a DICTIONARY, for example:
    {"topic": "Geography", "question": "Capital of France?", "answer": "Paris"}

All questions are stored together in a LIST of those dictionaries (the "question
bank").

--------------------------------------------------------------------------------
HOW "TAKE THE QUIZ" SHOULD WORK
--------------------------------------------------------------------------------
  - Ask the user how many questions they want (a number). If they type a blank
    line or a number bigger than the bank, just use ALL questions.
  - Loop through the questions. For each one:
        * print the question
        * read the user's answer with input()
        * compare it to the correct answer, IGNORING case and spaces
          (so "  paris " counts as correct for "Paris")
  - Keep a running score.
  - At the end, print:
        * the score and a percentage
        * a letter grade band  (A/B/C/D/F — you choose the cut-offs)
        * a per-topic breakdown, e.g.  "Geography: 2/3 correct"

--------------------------------------------------------------------------------
REQUIREMENTS  (this is how your work will be graded)
--------------------------------------------------------------------------------
Structure & functions (Module 9):
  [ ] Organised into FUNCTIONS, each doing one job, each with a docstring.
  [ ] A main() function runs the menu loop.

Menu loop (Modules 5 & 6):
  [ ] A while loop shows the menu until the user chooses Quit.
  [ ] if / elif / else (or match) dispatches each menu choice.

Adding a question (Modules 2, 3, 7, 8):
  [ ] Read topic, question, and answer with input(); clean them with .strip().
  [ ] Store the question as a dictionary appended to the list.

Taking the quiz (Modules 2, 3, 4, 5, 6, 8):
  [ ] Ask how many questions — convert that text to an int.
  [ ] Loop through the questions and compare answers case-insensitively
      (.strip().lower() on both sides).
  [ ] Track score with arithmetic; print a percentage.
  [ ] Use if/elif/else to turn the percentage into a letter grade.
  [ ] Build a dictionary to count correct/total PER TOPIC and print it.

Save & load (Module 10):
  [ ] Save the question bank to a CSV file (one row per question).
  [ ] Load it back from that CSV into the list.

Error handling (Module 11):
  [ ] If the user types a non-number when asked how many questions, don't crash
      — either re-ask or fall back to all questions.
  [ ] If the user loads a file that does not exist, catch it and print a
      friendly message instead of a traceback.

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
  python assessments/capstone2_modules_01-11/capstone_quiz_game.py

--------------------------------------------------------------------------------
RULES
--------------------------------------------------------------------------------
  - TYPE every line yourself — no copy-paste.
  - You may look back at earlier modules, but do NOT open a solution until you
    have genuinely tried.
  - Get it working first, then make it neat.

--------------------------------------------------------------------------------
STRETCH GOALS (only if the above all works)
--------------------------------------------------------------------------------
  - Shuffle the questions before each quiz (see the random module).
  - Let the user filter the quiz to a single topic.
  - Save each quiz result (date, score) to a separate "scores" file.
  - Give a second chance on a wrong answer before revealing the correct one.
"""

# =============================================================================
# Your code goes below. The TODOs are a suggested order — you decide the details.
# =============================================================================

# TODO: A place to store all questions (a list). Where should it live?

# TODO: def add_question(questions):   ask user, build a dict, append it
# TODO: def view_questions(questions): print every question (hide the answers!)
# TODO: def take_quiz(questions):      ask, score, print grade + per-topic result
# TODO: def save_questions(questions, filename):  write to CSV
# TODO: def load_questions(filename):             read from CSV, return a list
# TODO: def print_menu():              print the 6 options
# TODO: def main():                    the while-loop menu that ties it together


# TODO: At the very bottom, start the program.
#       (Bonus: use the  if __name__ == "__main__":  guard from Module 09.)
