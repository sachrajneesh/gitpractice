"""Demonstrates: list methods — append, extend, insert, remove, pop, sort, reverse"""

# ---------------------------------------------------------------
# Lists come with built-in methods (functions attached to the list).
# Call them with: my_list.method_name(arguments)
# ---------------------------------------------------------------

shopping = ["bread", "milk", "eggs"]
print("Starting list:", shopping)

# ---------------------------------------------------------------
# --- append() — add ONE item to the END ---
# ---------------------------------------------------------------
shopping.append("butter")   # adds "butter" at the end
print("\nAfter append('butter'):", shopping)

shopping.append("cheese")
print("After append('cheese'):", shopping)

# ---------------------------------------------------------------
# --- extend() — add MULTIPLE items from another list to the end ---
# ---------------------------------------------------------------
more_items = ["apples", "pasta", "sauce"]
shopping.extend(more_items)   # adds all three items at once
print("\nAfter extend(...):", shopping)

# ---------------------------------------------------------------
# --- insert() — add ONE item at a SPECIFIC position ---
# ---------------------------------------------------------------
shopping.insert(1, "jam")   # insert "jam" at index 1 (pushes others right)
print("\nAfter insert(1, 'jam'):", shopping)

# ---------------------------------------------------------------
# --- remove() — remove the FIRST occurrence of a value ---
# ---------------------------------------------------------------
shopping.remove("milk")   # removes "milk" by VALUE (not by index)
print("\nAfter remove('milk'):", shopping)
# Note: if the item isn't in the list, remove() raises a ValueError

# ---------------------------------------------------------------
# --- pop() — remove and RETURN item at index (default: last item) ---
# ---------------------------------------------------------------
last_item = shopping.pop()     # removes and returns the last item
print(f"\nAfter pop() — removed '{last_item}':", shopping)

first_item = shopping.pop(0)   # removes and returns item at index 0
print(f"After pop(0) — removed '{first_item}':", shopping)

# ---------------------------------------------------------------
# --- sort() — sort IN PLACE (alphabetically or numerically) ---
# ---------------------------------------------------------------
scores = [88, 43, 95, 61, 79, 12, 55]
print("\nOriginal scores:", scores)
scores.sort()                 # sorts lowest to highest (in place — modifies the list!)
print("After sort():", scores)

scores.sort(reverse=True)     # sorts highest to lowest
print("After sort(reverse=True):", scores)

names = ["Zara", "Alice", "Ryan", "Marcus"]
names.sort()                  # alphabetical order
print("\nSorted names:", names)

# ---------------------------------------------------------------
# --- reverse() — reverse the order IN PLACE ---
# ---------------------------------------------------------------
shopping.reverse()
print("\nAfter reverse():", shopping)

# ---------------------------------------------------------------
# --- len(), min(), max(), sum() — useful built-in functions ---
# ---------------------------------------------------------------
scores = [88, 43, 95, 61, 79]
print(f"\nScores: {scores}")
print(f"  Count:   {len(scores)}")     # number of items
print(f"  Minimum: {min(scores)}")     # lowest value
print(f"  Maximum: {max(scores)}")     # highest value
print(f"  Sum:     {sum(scores)}")     # total
print(f"  Average: {sum(scores)/len(scores):.1f}")  # calculated average
