"""Demonstrates: list slicing with start, stop, step"""

# ---------------------------------------------------------------
# Slicing extracts a PORTION of a list (or string) into a new list.
# Syntax: my_list[start : stop : step]
#
# - start  — index where the slice BEGINS (included)
# - stop   — index where the slice ENDS   (NOT included)
# - step   — how many positions to jump each time (default: 1)
#
# Any part can be omitted and Python fills in defaults.
# ---------------------------------------------------------------

playlist = ["Song A", "Song B", "Song C", "Song D", "Song E", "Song F", "Song G"]
#  index:      0         1         2         3         4         5         6

print("Full playlist:", playlist)
print(f"Length: {len(playlist)}")

# ---------------------------------------------------------------
# --- Basic slices ---
# ---------------------------------------------------------------

# First three songs [0, 1, 2]
print("\nFirst 3 songs:", playlist[0:3])    # start=0, stop=3 (3 not included)

# Same thing — omitting start defaults to 0
print("First 3 (shorthand):", playlist[:3])

# Songs from index 4 to the end
print("From index 4 onwards:", playlist[4:])  # omitting stop goes to the end

# Middle section [2, 3, 4]
print("Middle section [2:5]:", playlist[2:5])

# ---------------------------------------------------------------
# Visual diagram:
#
# playlist = ["Song A", "Song B", "Song C", "Song D", "Song E", "Song F", "Song G"]
# index:          0         1         2         3         4         5         6
#
# playlist[1:4]  → items at 1, 2, 3  → ["Song B", "Song C", "Song D"]
#                         ^start        ^stop (not included)
# ---------------------------------------------------------------

print("\nDiagram check:")
print("playlist[1:4]:", playlist[1:4])   # ["Song B", "Song C", "Song D"]

# ---------------------------------------------------------------
# --- Step — skip items ---
# ---------------------------------------------------------------

# Every other song (step=2)
print("\nEvery other song:", playlist[::2])   # 0, 2, 4, 6

# Every third song
print("Every third song:", playlist[::3])    # 0, 3, 6

# ---------------------------------------------------------------
# --- Negative indexes in slices ---
# ---------------------------------------------------------------

# Last two songs
print("\nLast 2 songs:", playlist[-2:])       # index -2 to end

# All but the last one
print("All but last:", playlist[:-1])         # from 0 up to (not including) -1

# ---------------------------------------------------------------
# --- Reverse with step=-1 ---
# ---------------------------------------------------------------
reversed_playlist = playlist[::-1]   # start=end, stop=beginning, step=-1
print("\nReversed playlist:", reversed_playlist)

# ---------------------------------------------------------------
# --- Slicing does NOT modify the original list ---
# ---------------------------------------------------------------
first_half = playlist[:4]
print("\nSlice:", first_half)
print("Original unchanged:", playlist)   # still has all 7 songs

# ---------------------------------------------------------------
# --- Slicing works on strings too! ---
# ---------------------------------------------------------------
song_title = "Bohemian Rhapsody"
print(f"\nFirst 8 chars of '{song_title}': '{song_title[:8]}'")
print(f"Last 8 chars: '{song_title[-8:]}'")
print(f"Every other char: '{song_title[::2]}'")
