"""Demonstrates: nested loops — a loop inside a loop"""

# ---------------------------------------------------------------
# Nested loops are loops that contain other loops.
# The INNER loop runs completely for EACH iteration of the OUTER loop.
#
# Think of it like: for each row → for each column → do something
# ---------------------------------------------------------------

# --- Example 1: Multiplication table (1-5) ---
print("Multiplication table (1 to 5):")
print()

# Print a header row
print("     ", end="")   # indent the header
for col in range(1, 6):
    print(f"{col:>4}", end="")   # :>4 right-aligns in 4 characters
print()   # newline after header

print("     " + "----" * 5)  # separator line

# Outer loop: each ROW (multiplier on the left)
for row in range(1, 6):
    print(f"  {row}  ", end="")   # print the row label

    # Inner loop: each COLUMN (multiplier on the top)
    for col in range(1, 6):
        product = row * col
        print(f"{product:>4}", end="")   # print product, right-aligned

    print()   # move to the next line after each row is done

# ---------------------------------------------------------------
# How many times does the inner body run?
# Outer loop: 5 times (1 to 5)
# Inner loop: 5 times per outer iteration
# Total: 5 × 5 = 25 times
# ---------------------------------------------------------------

# --- Example 2: Nested loop to print a pattern ---
print("\nStar pattern:")
for row in range(1, 6):          # rows 1 to 5
    for star in range(row):      # print 'row' number of stars
        print("*", end="")       # end="" stays on the same line
    print()                      # newline at the end of each row
# Output:
# *
# **
# ***
# ****
# *****

# --- Example 3: Loop over a list of students and their scores ---
print("\nStudent report:")
students = ["Alice", "Ryan", "Marcus"]
all_scores = [
    [88, 74, 91],   # Alice's scores
    [79, 85, 92],   # Ryan's scores
    [65, 70, 88],   # Marcus's scores
]

# Outer loop: each student
for i in range(len(students)):
    name = students[i]
    scores = all_scores[i]

    total = 0
    # Inner loop: each score for this student
    for score in scores:
        total += score

    average = total / len(scores)
    print(f"  {name}: scores={scores}, average={average:.1f}")
