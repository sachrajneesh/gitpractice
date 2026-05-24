"""Demonstrates: the quiz pattern — a 3-question mini-quiz"""

# ---------------------------------------------------------------
# This is a simplified version of Project 1 (Number Quiz).
# It shows the core pattern:
#   - Store questions in a data structure
#   - Loop through questions, collect answers
#   - Track score and show results
# ---------------------------------------------------------------

# Store each question as a dict with "question" and "answer" keys.
# This makes it easy to add more questions later — just add more dicts!
questions = [
    {
        "question": "What keyword defines a function in Python?",
        "answer": "def",
    },
    {
        "question": "What is 2 ** 8?",
        "answer": "256",
    },
    {
        "question": "What method adds an item to the end of a list?",
        "answer": "append",
    },
]

score = 0
total = len(questions)   # count questions automatically — easier to update later

print("=== Python Quiz ===")
print(f"Answer {total} questions. Good luck!\n")

# Loop through each question dict
for i, q in enumerate(questions, start=1):
    user_answer = input(f"Q{i}: {q['question']}\nYour answer: ").strip().lower()
    correct = q["answer"].lower()   # normalise case for fair comparison

    if user_answer == correct:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The answer was: {q['answer']}\n")

# Show final score
print(f"=== Results: {score}/{total} ===")
percentage = (score / total) * 100

if percentage == 100:
    print("Perfect score! You're a Python wizard!")
elif percentage >= 66:
    print("Great job! You know your stuff.")
else:
    print("Good try — review the modules and have another go!")
