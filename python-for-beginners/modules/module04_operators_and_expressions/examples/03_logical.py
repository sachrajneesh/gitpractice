"""Demonstrates: logical operators (and, or, not)"""

# ---------------------------------------------------------------
# Logical operators combine or flip boolean (True/False) values.
# They let you check multiple conditions at once.
#
#   and  — both conditions must be True
#   or   — at least one condition must be True
#   not  — flips True to False and False to True
# ---------------------------------------------------------------

age = 17
has_licence = False
is_raining = True
is_weekend = True
homework_done = True
score = 82
passing = 60

# ---------------------------------------------------------------
# --- and --- (BOTH sides must be True)
# ---------------------------------------------------------------

# Can Ryan drive? He needs to be old enough AND have a licence.
can_drive = age >= 16 and has_licence
print(f"Can Ryan drive? {can_drive}")   # False — has_licence is False

# Is it a perfect study day? Weekend AND homework already done.
perfect_study_day = is_weekend and homework_done
print(f"Perfect study day? {perfect_study_day}")   # True

# Passed AND scored over 80? (both must be true)
great_result = score >= passing and score > 80
print(f"Great result? {great_result}")   # True (82 >= 60 AND 82 > 80)

# ---------------------------------------------------------------
# --- or --- (AT LEAST ONE side must be True)
# ---------------------------------------------------------------

# Is a jacket needed? If it's raining OR cold outside.
temperature = 14
needs_jacket = is_raining or temperature < 15
print(f"Needs jacket? {needs_jacket}")   # True (both are actually true here)

# Can eat pizza for dinner? If there's money OR the friend is paying.
has_money = False
friend_paying = True
can_eat_pizza = has_money or friend_paying
print(f"Can eat pizza? {can_eat_pizza}")   # True — friend is paying!

# ---------------------------------------------------------------
# --- not --- (FLIPS the boolean value)
# ---------------------------------------------------------------

is_school_night = True
print(f"Is school night? {is_school_night}")       # True
print(f"Not school night? {not is_school_night}")  # False

is_tired = False
print(f"Is tired? {is_tired}")         # False
print(f"Not tired? {not is_tired}")    # True  (flipped!)

# ---------------------------------------------------------------
# Combining operators — more complex conditions
# ---------------------------------------------------------------

# Can Ryan go to the gaming café tonight?
# He can go if: it's not a school night AND (homework is done OR he's already finished early)
finished_early = False
can_go_out = (not is_school_night) and (homework_done or finished_early)
print(f"\nCan Ryan go to the café? {can_go_out}")
# is_school_night is True, so not is_school_night is False
# False and anything = False, so no café tonight!

is_school_night = False   # let's say it's Friday
can_go_out = (not is_school_night) and (homework_done or finished_early)
print(f"Friday night café? {can_go_out}")   # True!

# ---------------------------------------------------------------
# Truth table summary:
#   True  and True  = True
#   True  and False = False
#   False and True  = False
#   False and False = False
#
#   True  or True  = True
#   True  or False = True
#   False or True  = True
#   False or False = False
#
#   not True  = False
#   not False = True
# ---------------------------------------------------------------
