"""
CAPSTONE #2 SOLUTION: Quiz Game (Modules 01–11)

Reference solution. Many correct versions exist — this is one clean one that
satisfies every requirement. Keep it back until the learner has finished (or
genuinely got stuck on) their own attempt.

Run it:
  python assessments/capstone2_modules_01-11/capstone_solution.py
"""

import csv
from pathlib import Path

DEFAULT_FILE = Path(__file__).parent / "questions.csv"


def print_menu():
    """Print the main menu of options."""
    print("\n===== Quiz Game =====")
    print("1. Add a question")
    print("2. View all questions")
    print("3. Take the quiz")
    print("4. Save questions to file")
    print("5. Load questions from file")
    print("6. Quit")


def add_question(questions):
    """Ask the user for a question and append it as a dict."""
    topic = input("Topic: ").strip().title()
    text = input("Question: ").strip()
    answer = input("Answer: ").strip()
    if not text or not answer:
        print("  Question and answer cannot be empty. Cancelled.")
        return
    questions.append({"topic": topic, "question": text, "answer": answer})
    print(f"  Added a {topic} question. Bank now has {len(questions)}.")


def view_questions(questions):
    """Print every question (without revealing the answers)."""
    if not questions:
        print("  No questions yet. Add one first!")
        return
    print(f"\n{'#':<3}{'Topic':<15}Question")
    print("-" * 50)
    for i, q in enumerate(questions, start=1):
        print(f"{i:<3}{q['topic']:<15}{q['question']}")


def ask_how_many(maximum):
    """Ask how many questions to use; blank or bad input means all of them."""
    raw = input(f"How many questions? (1-{maximum}, blank for all): ").strip()
    if raw == "":
        return maximum
    try:
        count = int(raw)
    except ValueError:
        print("  Not a number — using all questions.")
        return maximum
    if count < 1:
        return maximum
    return min(count, maximum)


def grade_for(percent):
    """Turn a percentage into a letter grade."""
    if percent >= 90:
        return "A"
    elif percent >= 75:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"


def take_quiz(questions):
    """Ask the questions, score them, and print a per-topic breakdown."""
    if not questions:
        print("  No questions yet. Add some first!")
        return

    how_many = ask_how_many(len(questions))
    selected = questions[:how_many]

    score = 0
    results = {}  # topic -> {"correct": int, "total": int}

    for i, q in enumerate(selected, start=1):
        print(f"\nQ{i}. [{q['topic']}] {q['question']}")
        answer = input("Your answer: ").strip().lower()
        correct = q["answer"].strip().lower()

        topic = q["topic"]
        if topic not in results:
            results[topic] = {"correct": 0, "total": 0}
        results[topic]["total"] += 1

        if answer == correct:
            print("  Correct!")
            score += 1
            results[topic]["correct"] += 1
        else:
            print(f"  Wrong. The answer was: {q['answer']}")

    total = len(selected)
    percent = score / total * 100
    print("\n===== Results =====")
    print(f"Score: {score}/{total}  ({percent:.0f}%)  Grade: {grade_for(percent)}")
    print("By topic:")
    for topic, r in results.items():
        print(f"  {topic:<15} {r['correct']}/{r['total']} correct")


def save_questions(questions, filename=DEFAULT_FILE):
    """Write all questions to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["topic", "question", "answer"])
        for q in questions:
            writer.writerow([q["topic"], q["question"], q["answer"]])
    print(f"  Saved {len(questions)} question(s) to {filename}")


def load_questions(filename=DEFAULT_FILE):
    """Read questions from a CSV file and return them as a list of dicts."""
    questions = []
    try:
        with open(filename, newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the header row
            for row in reader:
                if len(row) != 3:
                    continue  # skip malformed rows
                topic, text, answer = row
                questions.append({
                    "topic": topic,
                    "question": text,
                    "answer": answer,
                })
        print(f"  Loaded {len(questions)} question(s) from {filename}")
    except FileNotFoundError:
        print(f"  No saved file found at {filename}. Starting empty.")
    return questions


def main():
    """Run the menu loop until the user quits."""
    questions = []
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_question(questions)
        elif choice == "2":
            view_questions(questions)
        elif choice == "3":
            take_quiz(questions)
        elif choice == "4":
            save_questions(questions)
        elif choice == "5":
            questions = load_questions()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("  Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
