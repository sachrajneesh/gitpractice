# Module 03: Strings

> **30/70 reminder** — Strings have a lot of methods to learn. Resist the urge to
> read them all and memorise them. Read CONCEPTS.md once, then spend the majority
> of your time in the exercises, looking up methods as you need them.

---

## Learning objectives

By the end of this module you will be able to:

- Write string literals using single quotes, double quotes, and triple quotes
- Use escape characters: `\n`, `\t`, `\\`, `\"`
- Build strings with f-strings (modern, preferred approach)
- Access individual characters with indexing (`s[0]`, `s[-1]`)
- Extract substrings with slicing (`s[1:4]`, `s[::2]`)
- Use common string methods: `upper`, `lower`, `strip`, `replace`, `split`, `join`, `find`, `len`

---

## Topics covered

1. String literals — single vs double quotes
2. Escape characters (`\n`, `\t`, `\\`, `\"`, `\'`)
3. Multi-line strings with triple quotes
4. f-strings — the modern way to embed values in strings
5. String indexing — accessing one character by position
6. String slicing — extracting a range of characters
7. Common string methods

---

## Files in this module

### Examples (run and read these first)
- `examples/01_string_basics.py` — literals, quotes, escape characters
- `examples/02_multiline.py` — triple-quoted strings
- `examples/03_fstrings.py` — f-strings with expressions inside `{}`
- `examples/04_indexing_slicing.py` — indexing and slicing with ASCII diagram
- `examples/05_string_methods.py` — all common methods with real examples

### Exercises (your 70%)
- `exercises/exercise03_namecard.py` 🟢 — **start here**
- `exercises/exercise03_solution.py` — only after 15 min of genuine effort

---

## Exercise checklist

- [ ] exercise03_namecard.py — build a formatted name card with a border

---

## How to work through this module

1. Read CONCEPTS.md — run each example file as you reach its section.
2. Try modifying the examples slightly (change a slice, try a different method).
3. Attempt `exercise03_namecard.py` without looking at any hints first.
4. If genuinely stuck after 15 minutes, check the hints in the exercise file.
5. Only open the solution after 15 minutes of real effort.
6. Mark the checkbox, then update `COURSE_CATALOG.md`.
