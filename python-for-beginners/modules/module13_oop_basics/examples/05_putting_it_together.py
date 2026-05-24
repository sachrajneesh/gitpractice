"""Demonstrates: a complete Student class with name, grades, and average() method"""

# ---------------------------------------------------------------
# This example brings together everything from Module 13:
#   - Class definition with __init__
#   - Multiple instance methods
#   - __str__ and __repr__
#   - Real-world use case: tracking student grades
# ---------------------------------------------------------------

class Student:
    """
    Represents a student with a name and a list of grades.

    Attributes:
        name (str): The student's name.
        subject (str): The subject being graded.
        grades (list): List of numeric grades (0-100).
    """

    def __init__(self, name, subject="General"):
        self.name = name
        self.subject = subject
        self.grades = []   # start with no grades — will add them with add_grade()

    def add_grade(self, grade):
        """Add a grade to this student's record. Must be 0-100."""
        if not 0 <= grade <= 100:
            print(f"Invalid grade {grade} — must be between 0 and 100.")
            return
        self.grades.append(grade)
        print(f"Grade {grade} added for {self.name}.")

    def average(self):
        """Return the average of all grades, or 0.0 if no grades yet."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        """Return the letter grade based on the average score."""
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def highest(self):
        """Return the highest grade, or None if no grades yet."""
        return max(self.grades) if self.grades else None

    def lowest(self):
        """Return the lowest grade, or None if no grades yet."""
        return min(self.grades) if self.grades else None

    def report(self):
        """Print a full grade report for this student."""
        print(f"\n--- Report: {self.name} ({self.subject}) ---")
        if not self.grades:
            print("  No grades recorded yet.")
            return
        print(f"  Grades:  {self.grades}")
        print(f"  Average: {self.average():.1f}")
        print(f"  Grade:   {self.letter_grade()}")
        print(f"  Highest: {self.highest()}")
        print(f"  Lowest:  {self.lowest()}")

    def __str__(self):
        """Human-readable summary."""
        if not self.grades:
            return f"{self.name} ({self.subject}) — no grades yet"
        return f"{self.name} ({self.subject}) — Average: {self.average():.1f} ({self.letter_grade()})"

    def __repr__(self):
        """Developer-facing representation."""
        return f"Student(name={self.name!r}, subject={self.subject!r}, grades={self.grades!r})"


# ---------------------------------------------------------------
# --- Demonstration ---
# ---------------------------------------------------------------

print("=== Creating students ===")
ryan = Student("Ryan", "Python Programming")
alice = Student("Alice", "Python Programming")
marcus = Student("Marcus")   # uses default subject

print(ryan)   # no grades yet
print()

# Add grades
ryan.add_grade(88)
ryan.add_grade(74)
ryan.add_grade(91)
ryan.add_grade(85)
ryan.add_grade(79)

alice.add_grade(95)
alice.add_grade(98)
alice.add_grade(92)

marcus.add_grade(55)
marcus.add_grade(62)
marcus.add_grade(58)

# Print reports
ryan.report()
alice.report()
marcus.report()

# The __str__ now shows grade info
print("\n=== Class summary ===")
class_list = [ryan, alice, marcus]
for student in class_list:
    print(f"  {student}")

# Find the top student
top = max(class_list, key=lambda s: s.average())
print(f"\nTop student: {top.name} with average {top.average():.1f}")
