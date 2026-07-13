"""
CAPSTONE #3 SOLUTION: Sales Data Analyzer & Report Generator (Modules 01–11)

Reference solution. Many correct versions exist — this is one clean one that
satisfies every requirement. Keep it back until the learner has finished (or
genuinely got stuck on) their own attempt.

Run it:
  python assessments/capstone3_modules_01-11/capstone_solution.py
"""

import csv
from pathlib import Path

HERE = Path(__file__).parent
DEFAULT_INPUT = HERE / "sample_sales.csv"
REPORT_FILE = HERE / "report.txt"
SUMMARY_FILE = HERE / "summary.csv"

EXPECTED_COLUMNS = 6  # date, salesperson, region, product, quantity, unit_price


def get_settings():
    """Ask the user for the input file and Top N, with sensible fallbacks."""
    raw_name = input(f"Data file [{DEFAULT_INPUT.name}]: ").strip()
    filename = HERE / raw_name if raw_name else DEFAULT_INPUT

    raw_n = input("How many salespeople in the Top N ranking? [all]: ").strip()
    try:
        top_n = int(raw_n)
        if top_n < 1:
            top_n = None  # treat as "all"
    except ValueError:
        top_n = None  # blank or non-number -> all
    return filename, top_n


def clean_row(row):
    """Turn one raw CSV row into a sale dict, or return None if it is broken."""
    if len(row) != EXPECTED_COLUMNS:
        return None
    date, salesperson, region, product, quantity, unit_price = row
    salesperson = salesperson.strip().title()
    region = region.strip().title()
    product = product.strip().title()
    if not salesperson or not region or not product:
        return None
    try:
        quantity = int(quantity.strip())
        unit_price = float(unit_price.strip())
    except ValueError:
        return None
    if quantity < 0 or unit_price < 0:
        return None
    return {
        "date": date.strip(),
        "salesperson": salesperson,
        "region": region,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "total": quantity * unit_price,
    }


def load_sales(filename):
    """Read and clean the CSV. Return (list_of_sales, skipped_count)."""
    sales = []
    skipped = 0
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the header row
        for row in reader:
            if not row:
                continue  # ignore fully blank lines
            sale = clean_row(row)
            if sale is None:
                skipped += 1
            else:
                sales.append(sale)
    return sales, skipped


def revenue_by(sales, key):
    """Build a {field_value: total_revenue} dictionary for the given field."""
    totals = {}
    for sale in sales:
        name = sale[key]
        totals[name] = totals.get(name, 0.0) + sale["total"]
    return totals


def units_by_product(sales):
    """Build a {product: total_quantity} dictionary."""
    units = {}
    for sale in sales:
        product = sale["product"]
        units[product] = units.get(product, 0) + sale["quantity"]
    return units


def tier_for(revenue):
    """Return the performance tier for a salesperson's revenue."""
    if revenue >= 200:
        return "Gold"
    elif revenue >= 100:
        return "Silver"
    else:
        return "Bronze"


def rank_salespeople(sales):
    """Return a list of (name, revenue, tier) sorted by revenue, highest first."""
    per_person = revenue_by(sales, "salesperson")
    ranking = []
    for name, revenue in per_person.items():
        ranking.append((name, revenue, tier_for(revenue)))
    ranking.sort(key=lambda item: item[1], reverse=True)
    return ranking


def top_key(totals):
    """Return the key with the largest value in a dict (or None if empty)."""
    if not totals:
        return None
    best = None
    best_value = None
    for key, value in totals.items():
        if best_value is None or value > best_value:
            best = key
            best_value = value
    return best


def build_report_text(sales, skipped, ranking, top_n):
    """Build the full human-readable report as one big string."""
    total_revenue = sum(sale["total"] for sale in sales)
    count = len(sales)
    average = total_revenue / count if count else 0.0

    region_rev = revenue_by(sales, "region")
    product_units = units_by_product(sales)
    best_product = top_key(product_units)
    top_person = ranking[0][0] if ranking else None

    lines = []
    lines.append("=" * 52)
    lines.append("SALES REPORT")
    lines.append("=" * 52)
    lines.append(f"Valid sales : {count}")
    lines.append(f"Skipped rows: {skipped}")
    lines.append(f"Total revenue: ${total_revenue:,.2f}")
    lines.append(f"Average sale : ${average:,.2f}")
    lines.append(f"Top salesperson : {top_person}")
    lines.append(f"Best-selling product: {best_product}")
    lines.append("")

    lines.append("-" * 52)
    lines.append("REVENUE BY REGION")
    lines.append("-" * 52)
    for region, revenue in sorted(region_rev.items(), key=lambda x: x[1], reverse=True):
        share = (revenue / total_revenue * 100) if total_revenue else 0
        lines.append(f"  {region:<10} ${revenue:>10,.2f}   ({share:4.1f}%)")
    lines.append("")

    lines.append("-" * 52)
    lines.append("UNITS SOLD BY PRODUCT")
    lines.append("-" * 52)
    for product, units in sorted(product_units.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"  {product:<10} {units:>6} units")
    lines.append("")

    shown = ranking if top_n is None else ranking[:top_n]
    heading = "ALL SALESPEOPLE" if top_n is None else f"TOP {top_n} SALESPEOPLE"
    lines.append("-" * 52)
    lines.append(f"{heading} (by revenue)")
    lines.append("-" * 52)
    lines.append(f"  {'Rank':<5}{'Name':<12}{'Revenue':>12}   Tier")
    for i, (name, revenue, tier) in enumerate(shown, start=1):
        lines.append(f"  {i:<5}{name:<12}${revenue:>10,.2f}   {tier}")
    lines.append("=" * 52)

    return "\n".join(lines)


def write_report(text, filename=REPORT_FILE):
    """Write the report text to a file."""
    with open(filename, "w") as f:
        f.write(text + "\n")


def write_summary_csv(ranking, filename=SUMMARY_FILE):
    """Write one row per salesperson: name, revenue, tier."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["salesperson", "revenue", "tier"])
        for name, revenue, tier in ranking:
            writer.writerow([name, f"{revenue:.2f}", tier])


def main():
    """Run the whole analysis pipeline."""
    filename, top_n = get_settings()

    try:
        sales, skipped = load_sales(filename)
    except FileNotFoundError:
        print(f"  Could not find '{filename}'. Nothing to analyse.")
        return

    if not sales:
        print("  No valid sales found in the file.")
        return

    ranking = rank_salespeople(sales)
    report = build_report_text(sales, skipped, ranking, top_n)

    print(report)
    write_report(report)
    write_summary_csv(ranking)
    print(f"\nWrote {REPORT_FILE.name} and {SUMMARY_FILE.name}.")


if __name__ == "__main__":
    main()
