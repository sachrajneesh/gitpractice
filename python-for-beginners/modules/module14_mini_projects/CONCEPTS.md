# Module 14 Concepts: Mini Projects

> This module is mostly coding. This file covers project planning strategy.

---

## How to plan a program before you write it

1. **Define the problem in one sentence.**
   "A quiz game that asks 10 random maths questions and grades the player."

2. **List the data you need to store.**
   - A score counter (int)
   - The 10 questions (generated randomly)
   - The player's answers

3. **List the actions (functions) your program needs.**
   - `generate_question()` — return a random question and its answer
   - `ask_question(question, answer)` — show question, get input, return True/False
   - `show_results(score, total)` — print final score and grade

4. **Sketch the main loop in plain English before writing code.**
   ```
   score = 0
   repeat 10 times:
       question = generate_question()
       if player answered correctly:
           score += 1
   show_results(score, 10)
   ```

5. **Write the simplest possible version first.**
   Get it working with hardcoded data. Add randomness and features after.

---

## Project specs

### Project 1: Number Quiz (Easy) 🟢

- Generate 10 random arithmetic questions (addition, subtraction, multiplication).
- Use numbers between 1 and 20.
- Time limit per question is optional (stretch goal).
- Score out of 10. Map score to grade: 9-10=A, 7-8=B, 5-6=C, 3-4=D, 0-2=F.
- Print a congratulations or encouragement message based on grade.

Key modules: `random`, functions, loops, f-strings.

### Project 2: Expense Tracker (Medium) 🟡

- Let user log expenses: amount, category (food/transport/entertainment/other), note.
- Store all expenses in a list of dicts.
- Show: total spent, breakdown by category.
- Save to expenses.csv and load from it on startup.
- Bonus: filter by date range.

Key modules: `csv`, `datetime`, dicts, lists, file I/O, functions.

### Project 3: Text-Based Adventure (Hard) 🔴

- Define at least 5 rooms as dicts with: description, exits (dict of direction → room_id), items.
- Player has an inventory (list).
- Commands: go north/south/east/west, pick up item, use item, look, quit.
- At least one puzzle (e.g. need a key to open a door).
- Win condition and lose condition.
- Bonus: save/load game state to a JSON file.

Key modules: dicts, lists, functions, OOP (optional), file I/O, loops.

---

## Next steps

After completing all three projects, move to Module 15: Next Steps.
