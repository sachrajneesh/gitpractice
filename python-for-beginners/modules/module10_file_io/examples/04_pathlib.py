"""Demonstrates: pathlib.Path — exists(), read_text(), write_text(), parent, stem"""

# ---------------------------------------------------------------
# pathlib is a modern, object-oriented way to work with file paths.
# Instead of joining strings manually, you create Path objects and
# use their methods and properties.
#
# It handles path separators automatically (/ on Mac/Linux, \\ on Windows)
# so your code works on all platforms.
# ---------------------------------------------------------------

from pathlib import Path   # built-in module — no install needed

# ---------------------------------------------------------------
# --- Creating Path objects ---
# ---------------------------------------------------------------

# A Path is just a path — the file doesn't need to exist yet
notes_path = Path("demo_notes.txt")
nested_path = Path("data") / "scores" / "results.csv"   # / operator joins paths!

print("notes_path:", notes_path)
print("nested_path:", nested_path)

# ---------------------------------------------------------------
# --- Checking if a file/directory exists ---
# ---------------------------------------------------------------
print("\nDoes 'demo_notes.txt' exist?", notes_path.exists())   # False (not created yet)

# ---------------------------------------------------------------
# --- Writing to a file with write_text() ---
# ---------------------------------------------------------------
notes_path.write_text("Module 10 is going great!\nPathlib makes paths easy.\n")
print(f"Written to {notes_path}")
print("Does 'demo_notes.txt' exist now?", notes_path.exists())   # True

# ---------------------------------------------------------------
# --- Reading a file with read_text() ---
# ---------------------------------------------------------------
content = notes_path.read_text()
print(f"\nContents of {notes_path}:")
print(content)

# ---------------------------------------------------------------
# --- Path properties ---
# ---------------------------------------------------------------
example_path = Path("/Users/ryan/documents/homework/essay.txt")

print("Path properties:")
print(f"  Full path:  {example_path}")
print(f"  name:       {example_path.name}")       # essay.txt  (filename + extension)
print(f"  stem:       {example_path.stem}")       # essay      (filename without extension)
print(f"  suffix:     {example_path.suffix}")     # .txt       (just the extension)
print(f"  parent:     {example_path.parent}")     # /Users/ryan/documents/homework
print(f"  parents[1]: {example_path.parents[1]}") # /Users/ryan/documents

# ---------------------------------------------------------------
# --- Making directories ---
# ---------------------------------------------------------------
output_dir = Path("output_demo")
output_dir.mkdir(exist_ok=True)   # creates folder; exist_ok=True means no error if it already exists
print(f"\nCreated directory: {output_dir}")
print("Is it a directory?", output_dir.is_dir())   # True

# Write a file inside the new directory using / operator:
report_path = output_dir / "report.txt"
report_path.write_text("This report is saved inside the output folder.\n")
print(f"Written: {report_path}")

# ---------------------------------------------------------------
# --- Listing files in a directory ---
# ---------------------------------------------------------------
print(f"\nFiles in '{output_dir}':")
for file in output_dir.iterdir():   # iterdir() yields all items in the directory
    print(f"  {file.name} ({file.suffix})")

# ---------------------------------------------------------------
# --- Clean up demo files ---
# ---------------------------------------------------------------
notes_path.unlink()       # unlink() deletes a file
report_path.unlink()
output_dir.rmdir()        # rmdir() deletes an EMPTY directory
print("\nDemo files and directory removed.")
