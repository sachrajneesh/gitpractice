"""Demonstrates: the datetime module — now(), strftime(), timedelta"""

# ---------------------------------------------------------------
# The datetime module provides classes for working with dates
# and times. The three most useful parts:
#
#   datetime.now()     — current date and time
#   strftime()         — format a datetime as a string
#   timedelta          — represent a duration (e.g. "3 days")
# ---------------------------------------------------------------

from datetime import datetime, timedelta, date

# ---------------------------------------------------------------
# --- datetime.now() — get the current date and time ---
# ---------------------------------------------------------------
print("=== datetime.now() ===")
now = datetime.now()    # returns a datetime object with today's date and time
print(f"Full datetime: {now}")
print(f"Year:   {now.year}")
print(f"Month:  {now.month}")
print(f"Day:    {now.day}")
print(f"Hour:   {now.hour}")
print(f"Minute: {now.minute}")

# ---------------------------------------------------------------
# --- strftime() — format datetime as a string ---
# ---------------------------------------------------------------
print("\n=== strftime() — formatting ===")
# strftime uses format codes starting with %
# Common codes:
#   %Y — 4-digit year      (2024)
#   %m — 2-digit month     (01-12)
#   %d — 2-digit day       (01-31)
#   %H — 24-hour hour      (00-23)
#   %M — minutes           (00-59)
#   %A — full weekday name (Monday)
#   %B — full month name   (January)
#   %I — 12-hour hour      (01-12)
#   %p — AM or PM

print(now.strftime("%Y-%m-%d"))                    # 2024-01-15
print(now.strftime("%d/%m/%Y"))                    # 15/01/2024
print(now.strftime("%A, %d %B %Y"))               # Monday, 15 January 2024
print(now.strftime("%H:%M"))                       # 14:30
print(now.strftime("%-d %B %Y at %I:%M %p"))       # 15 January 2024 at 02:30 PM

# ---------------------------------------------------------------
# --- timedelta — arithmetic with dates ---
# ---------------------------------------------------------------
print("\n=== timedelta ===")

# A timedelta represents a duration
one_week = timedelta(weeks=1)
three_days = timedelta(days=3)
two_hours = timedelta(hours=2)

print(f"One week:   {one_week}")
print(f"Three days: {three_days}")

# Add/subtract timedeltas to dates
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"\nToday:      {now.strftime('%d %B %Y')}")
print(f"Tomorrow:   {tomorrow.strftime('%d %B %Y')}")
print(f"Last week:  {last_week.strftime('%d %B %Y')}")

# ---------------------------------------------------------------
# --- How many days until an event? ---
# ---------------------------------------------------------------
print("\n=== Days until an event ===")
# date.today() gives just the date (no time component)
today = date.today()

# Christmas this year (or next, if it's past)
christmas = date(today.year, 12, 25)
if christmas < today:
    christmas = date(today.year + 1, 12, 25)  # next year's Christmas

days_until = (christmas - today).days   # subtraction gives a timedelta
print(f"Today:    {today}")
print(f"Christmas: {christmas}")
print(f"Days until Christmas: {days_until}")

# ---------------------------------------------------------------
# --- Comparing datetimes ---
# ---------------------------------------------------------------
print("\n=== Comparing datetimes ===")
start = datetime(2024, 1, 1, 0, 0)    # January 1st, 2024 midnight
end = datetime(2024, 12, 31, 23, 59)  # December 31st, 2024 11:59pm
duration = end - start
print(f"Duration of 2024: {duration.days} days")
