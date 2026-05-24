"""
Exercise 15 🟢: Personal Learning Roadmap

What you'll practise:
  File I/O, f-strings, user input, and reflecting on what you have learned.

Task:
  Build a program that interviews you about your goals and interests,
  then generates a personalised 90-day learning roadmap and saves it
  as a markdown file (my_roadmap.md).

Requirements:
  - Ask: What do you want to build? (web app / data project / game / automation tool / other)
  - Ask: How many hours per week can you study? (number)
  - Ask: What is your biggest Python strength so far? (free text)
  - Ask: What do you find most confusing? (free text)
  - Based on the answers, print and save a structured roadmap with:
      - Your goal
      - Recommended next 3 topics to study
      - Recommended resources (hardcode 2-3 relevant ones)
      - A 90-day milestone plan (Days 1-30, 31-60, 61-90)
  - Save the roadmap to "my_roadmap.md".

How to run:
  python modules/module15_next_steps/exercises/exercise15_roadmap.py

Hints:
  - Use a dict to map goal choices to recommended topics and resources.
  - Write the file with open("my_roadmap.md", "w").
  - Use a multi-line f-string for the roadmap content.

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

from datetime import datetime

# ---------------------------------------------------------------
# Data: goal → recommended topics, resources, and milestones
# ---------------------------------------------------------------
GOAL_DATA = {
    "web": {
        "label": "Build a web application",
        "topics": ["Flask/Django basics", "HTML & CSS fundamentals", "Databases with SQLite"],
        "resources": [
            "Flask Mega-Tutorial by Miguel Grinberg (free, miguelgrinberg.com)",
            "Django Girls Tutorial (free, tutorial.djangogirls.org)",
            "CS50's Web Programming with Python — free on edX",
        ],
        "days_1_30": "Learn Flask basics, build a 'Hello World' web app, understand routes and templates.",
        "days_31_60": "Add a database (SQLite), build a todo web app with CRUD operations.",
        "days_61_90": "Add user login, deploy your app to a free service (Render or PythonAnywhere).",
    },
    "data": {
        "label": "Work with data / data science",
        "topics": ["pandas for data analysis", "Matplotlib/seaborn for charts", "NumPy for numbers"],
        "resources": [
            "Kaggle Learn — free interactive courses with real datasets (kaggle.com/learn)",
            "'Python for Data Analysis' by Wes McKinney — the pandas bible",
            "Corey Schafer pandas playlist on YouTube",
        ],
        "days_1_30": "Install pandas and Jupyter Notebook. Load your first CSV dataset. Explore rows/columns.",
        "days_31_60": "Clean messy data, group data by category, create bar charts and line graphs.",
        "days_61_90": "Find a real dataset you care about (sports, music, etc.) and build a full analysis.",
    },
    "game": {
        "label": "Create games",
        "topics": ["pygame fundamentals", "2D game loops and sprites", "Collision detection"],
        "resources": [
            "pygame official tutorials (pygame.org/wiki/GettingStarted)",
            "CS Dojo pygame series on YouTube",
            "'Making Games with Python & Pygame' by Al Sweigart (free online)",
        ],
        "days_1_30": "Install pygame. Build a window, draw shapes, move a player with arrow keys.",
        "days_31_60": "Add sprites, images, and a basic enemy that moves towards the player.",
        "days_61_90": "Add scoring, lives, a start screen, and a game-over screen. Share it!",
    },
    "automation": {
        "label": "Automate tasks",
        "topics": ["File system automation with os/pathlib", "Web scraping with requests+BeautifulSoup", "Sending emails / scheduling"],
        "resources": [
            "'Automate the Boring Stuff with Python' by Al Sweigart (FREE online, automatetheboringstuff.com)",
            "Real Python automation tutorials (realpython.com)",
            "Python requests library docs (docs.python-requests.org)",
        ],
        "days_1_30": "Write scripts to rename files, organise a folder, and read/write CSV and JSON.",
        "days_31_60": "Scrape a website you find interesting. Automate a repetitive task from your own life.",
        "days_61_90": "Schedule a script to run daily, or add a GUI with tkinter or a web interface.",
    },
    "other": {
        "label": "General Python skills",
        "topics": ["Object-oriented programming (classes)", "Testing with pytest", "Working with APIs"],
        "resources": [
            "Real Python — comprehensive tutorials for all levels (realpython.com)",
            "Python docs official tutorial (docs.python.org/3/tutorial)",
            "Exercism Python track — free coding exercises with mentoring (exercism.org)",
        ],
        "days_1_30": "Strengthen OOP skills: build 3-5 class-based projects. Practice on Exercism.",
        "days_31_60": "Learn to write tests with pytest. Refactor your earlier projects to add tests.",
        "days_61_90": "Consume a real public API (weather, jokes, GitHub). Build something you'd use daily.",
    },
}

# ---------------------------------------------------------------
# Interview the user
# ---------------------------------------------------------------
print("=" * 50)
print("  90-Day Python Learning Roadmap Generator")
print("=" * 50)
print("\nAnswer a few questions and I'll build your personal plan.\n")

# Goal selection
print("What do you want to build?")
print("  1. web       — web apps")
print("  2. data      — data analysis")
print("  3. game      — games")
print("  4. automation — scripts that automate tasks")
print("  5. other     — general Python / not sure yet")

goal_input = input("\nYour choice (web/data/game/automation/other): ").strip().lower()

# Normalise the input — accept number shortcuts too
goal_map = {"1": "web", "2": "data", "3": "game", "4": "automation", "5": "other"}
if goal_input in goal_map:
    goal_input = goal_map[goal_input]
if goal_input not in GOAL_DATA:
    goal_input = "other"   # default if unexpected input

goal_data = GOAL_DATA[goal_input]

# Hours per week
while True:
    try:
        hours = int(input("\nHow many hours per week can you study? "))
        if hours > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a whole number.")

# Free-text questions
strength = input("\nWhat's your biggest Python strength so far? ").strip() or "core syntax and problem-solving"
confusion = input("What do you find most confusing right now? ").strip() or "not sure yet"

# ---------------------------------------------------------------
# Build the roadmap content
# ---------------------------------------------------------------
today = datetime.now().strftime("%d %B %Y")
daily_hrs = hours / 7

# Calculate rough times based on hours/week
wks_30 = 30 // 7 + 1
wks_60 = 60 // 7 + 1
wks_90 = 90 // 7 + 1

topics_bullet = "\n".join(f"- {t}" for t in goal_data["topics"])
resources_bullet = "\n".join(f"- {r}" for r in goal_data["resources"])

roadmap = f"""# My 90-Day Python Learning Roadmap

Generated: {today}

---

## My Goal

{goal_data['label']}

## My Starting Point

- **Biggest strength:** {strength}
- **Current challenge:** {confusion}
- **Study time:** {hours} hours/week (~{daily_hrs:.1f} hours/day)

---

## Next 3 Topics to Learn

{topics_bullet}

---

## Recommended Resources

{resources_bullet}

---

## 90-Day Milestone Plan

### Days 1–30 (~{wks_30} weeks)
{goal_data['days_1_30']}

### Days 31–60 (~{wks_60} weeks)
{goal_data['days_31_60']}

### Days 61–90 (~{wks_90} weeks)
{goal_data['days_61_90']}

---

## General Tips

- **Consistency beats intensity.** 30 minutes every day beats 4 hours once a week.
- **Build things.** Every tutorial should end with you making something of your own.
- **Get stuck.** Struggling with a problem for 20 minutes teaches more than reading for 2 hours.
- **Share your work.** Push to GitHub. Show someone what you built.

---

*You've completed Python for Beginners. The hard work starts now — and it's worth it.*
"""

# ---------------------------------------------------------------
# Print and save
# ---------------------------------------------------------------
print("\n" + "=" * 50)
print(roadmap)
print("=" * 50)

output_file = "my_roadmap.md"
with open(output_file, "w") as f:
    f.write(roadmap)

print(f"Roadmap saved to {output_file}")
print("Open it in VS Code or any markdown viewer for a nicely formatted version.")
