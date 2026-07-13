"""
CAPSTONE #3 🔴🔴 (ADVANCED): Sales Data Analyzer & Report Generator
Modules 01–11

This is the HARDEST of the three capstones and a deliberately different kind of
program. The first two were interactive menu apps where you typed data in one
record at a time. This one is a *data pipeline*: it reads a whole file of raw,
partly-broken data, cleans it, crunches numbers across the entire dataset, and
writes out finished report files. Almost no menu — the work is in the analysis.

You are given a data file to work with: `sample_sales.csv`.

--------------------------------------------------------------------------------
WHAT YOU ARE BUILDING
--------------------------------------------------------------------------------
A program that reads `sample_sales.csv` (columns below), analyses it, prints a
summary to the screen, and writes TWO output files:
    - report.txt   — a nicely formatted human-readable report
    - summary.csv  — one row per salesperson with their totals

The input columns are:
    date, salesperson, region, product, quantity, unit_price

IMPORTANT: the data file is realistic — some rows are BROKEN on purpose
(a non-numeric quantity, a missing price, a row with too few columns). Your
program must SKIP bad rows, count how many it skipped, and keep going. It must
never crash on bad data.

--------------------------------------------------------------------------------
WHAT THE ANALYSIS MUST PRODUCE
--------------------------------------------------------------------------------
For every VALID row, compute the line total:  quantity * unit_price.
Then compute across the whole dataset:

  1. Total revenue (sum of all line totals).
  2. Number of valid sales and number of skipped/broken rows.
  3. Average sale value.
  4. Revenue per REGION            -> a dictionary {region: revenue}.
  5. Revenue per SALESPERSON       -> a dictionary {name: revenue}.
  6. Units sold per PRODUCT        -> a dictionary {product: total_quantity}.
  7. The best-selling product (most units) and the top salesperson (most $).
  8. A ranking of salespeople from highest revenue to lowest.
  9. A performance TIER for each salesperson based on their revenue:
         >= 200      -> "Gold"
         100–199.99  -> "Silver"
         under 100   -> "Bronze"

--------------------------------------------------------------------------------
SMALL INTERACTIVE PART (keep it minimal)
--------------------------------------------------------------------------------
At the start, ask the user two things with input():
  - Which data file to read (pressing Enter should default to sample_sales.csv).
  - How many salespeople to show in the "Top N" ranking (a number; if they type
    something that isn't a number, fall back to showing all of them).

--------------------------------------------------------------------------------
REQUIREMENTS  (this is how your work will be graded)
--------------------------------------------------------------------------------
Structure & functions (Module 9):
  [ ] Split into FUNCTIONS, each doing ONE job, each with a docstring.
  [ ] A main() function runs the whole pipeline top to bottom.
  [ ] No giant do-everything function.

Reading & cleaning data (Modules 2, 3, 10, 11):
  [ ] Read the CSV with the csv module inside a `with open(...)`.
  [ ] Convert quantity to int and unit_price to float.
  [ ] Skip rows that are broken (wrong length, empty field, non-numeric) using
      try/except — and COUNT how many you skipped.
  [ ] Clean text fields with .strip() (and .title() where it makes sense).

Crunching the numbers (Modules 4, 5, 6, 7, 8):
  [ ] Store valid sales as a LIST of dictionaries.
  [ ] Use loops to build the per-region / per-person / per-product dictionaries.
  [ ] Use arithmetic for totals, the average, and percentages.
  [ ] Use if/elif/else for the performance tiers.
  [ ] SORT the salespeople by revenue (highest first) for the ranking.
  [ ] Find the max product and max salesperson from your dictionaries.

Output (Modules 3, 10):
  [ ] Print a readable summary to the screen with f-strings.
  [ ] Write report.txt with the full report (aligned columns look great).
  [ ] Write summary.csv: header + one row per salesperson
      (name, revenue, tier).

--------------------------------------------------------------------------------
HOW TO RUN
--------------------------------------------------------------------------------
  python assessments/capstone3_modules_01-11/capstone_sales_analyzer.py

--------------------------------------------------------------------------------
RULES
--------------------------------------------------------------------------------
  - TYPE every line yourself — no copy-paste.
  - Build it in stages and RUN it often: first just read + count rows, then add
    one aggregation at a time, then the report files last.
  - Do NOT open the solution until you have genuinely tried.

--------------------------------------------------------------------------------
STRETCH GOALS (only if everything above works)
--------------------------------------------------------------------------------
  - Add a per-region average sale value.
  - Let the user filter the report to a single region or product.
  - Sort summary.csv by revenue and add a "rank" column.
  - Print a tiny text bar chart of revenue per region (e.g. "North | #######").
  - Use pathlib.Path for all file paths.
"""

# =============================================================================
# Your code goes below. The TODOs are a suggested pipeline order — you decide
# the details and the exact function signatures.
# =============================================================================

# TODO: def get_settings():        ask for the input filename + Top N (with a
#                                   sensible default and error handling)
# TODO: def load_sales(filename):  read + clean the CSV; return (sales, skipped)
# TODO: def revenue_by(sales, key):    build a {value: revenue} dict for a field
# TODO: def units_by_product(sales):   build a {product: total_quantity} dict
# TODO: def tier_for(revenue):         return "Gold" / "Silver" / "Bronze"
# TODO: def rank_salespeople(sales):   return salespeople sorted by revenue desc
# TODO: def build_report_text(...):    return the big report string
# TODO: def write_report(text, filename)
# TODO: def write_summary_csv(ranking, filename)
# TODO: def main():                    run the whole pipeline and print a summary


# TODO: At the very bottom, start the program.
#       (Bonus: use the  if __name__ == "__main__":  guard from Module 09.)
