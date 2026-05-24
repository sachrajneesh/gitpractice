"""Demonstrates: a learning-path menu that prints descriptions of each path"""

# ---------------------------------------------------------------
# After finishing this course, there are many directions you can
# take your Python skills. This program lets you explore them.
# ---------------------------------------------------------------

# Store each learning path as a dictionary with details.
# This makes it easy to add new paths later.
PATHS = {
    "1": {
        "name": "Web Development",
        "emoji": "🌐",
        "description": "Build websites and web apps using Python on the backend.",
        "tools": ["Flask", "Django", "FastAPI"],
        "first_step": "Build a simple Flask web app that serves a webpage.",
        "resources": [
            "Flask Mega-Tutorial (Miguel Grinberg) — free online",
            "Django Girls Tutorial — beginner-friendly",
            "Real Python Flask tutorials — realpython.com",
        ],
        "timeline": "~3-6 months to build your first real web app",
    },
    "2": {
        "name": "Data Science & Analysis",
        "emoji": "📊",
        "description": "Analyse data, spot trends, and make visualisations.",
        "tools": ["pandas", "NumPy", "Matplotlib", "Jupyter Notebooks"],
        "first_step": "Install pandas and load a CSV file into a DataFrame.",
        "resources": [
            "Kaggle Learn — free courses with datasets",
            "'Python for Data Analysis' (Wes McKinney) — the pandas bible",
            "Corey Schafer pandas playlist — YouTube",
        ],
        "timeline": "~2-4 months to analyse your first real dataset",
    },
    "3": {
        "name": "Game Development",
        "emoji": "🎮",
        "description": "Create 2D games with sprites, physics, and sound.",
        "tools": ["pygame", "pyglet", "Arcade"],
        "first_step": "Follow the pygame tutorial to make a bouncing ball.",
        "resources": [
            "pygame.org — official tutorials",
            "CS Dojo pygame series — YouTube",
            "The Python Arcade Library docs — api.arcade.academy",
        ],
        "timeline": "~1-3 months to build your first playable game",
    },
    "4": {
        "name": "Automation & Scripting",
        "emoji": "🤖",
        "description": "Automate boring tasks: rename files, scrape websites, send emails.",
        "tools": ["selenium", "requests", "BeautifulSoup", "schedule"],
        "first_step": "Write a script that renames all files in a folder.",
        "resources": [
            "'Automate the Boring Stuff with Python' (Al Sweigart) — free online!",
            "Real Python automation tutorials — realpython.com",
            "Python requests library docs",
        ],
        "timeline": "~1-2 months to automate your first real task",
    },
}


def show_path(path_data):
    """Print a detailed description of a learning path."""
    print(f"\n{'='*50}")
    print(f"  {path_data['name']}")
    print(f"{'='*50}")
    print(f"\n{path_data['description']}")
    print(f"\nKey tools: {', '.join(path_data['tools'])}")
    print(f"\nYour first step: {path_data['first_step']}")
    print(f"\nTimeline: {path_data['timeline']}")
    print(f"\nRecommended resources:")
    for resource in path_data["resources"]:
        print(f"  - {resource}")


# --- Main menu loop ---
print("=" * 50)
print("  Where will Python take you next?")
print("=" * 50)
print()
for key, path in PATHS.items():
    print(f"  {key}. {path['name']}")
print("  5. Show all paths")
print("  q. Quit")

while True:
    choice = input("\nChoose a path (1-5 or q): ").strip().lower()

    if choice in PATHS:
        show_path(PATHS[choice])

    elif choice == "5":
        for path_data in PATHS.values():
            show_path(path_data)

    elif choice == "q":
        print("\nWhatever path you choose — keep coding. You've got this!")
        break

    else:
        print("Please enter 1, 2, 3, 4, 5, or q.")
