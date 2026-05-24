"""Demonstrates: basic if/else statement"""

# ---------------------------------------------------------------
# An if/else statement lets your program make decisions.
# If the condition is True → run the if block.
# Otherwise            → run the else block.
# ---------------------------------------------------------------

# --- Example: Did Ryan pass the exam? ---

score = 74          # change this number and run again to see the difference
passing_mark = 60   # the minimum score needed to pass

# The condition goes right after the keyword "if"
# The colon (:) at the end is required — don't forget it!
if score >= passing_mark:
    # Everything INDENTED under the if runs only when condition is True
    print("Congratulations — you passed!")
    print(f"Your score was {score}. Well done!")
else:
    # The else block runs when the condition is False
    print("Sorry — not quite this time.")
    print(f"You scored {score}. The passing mark is {passing_mark}.")

# ---------------------------------------------------------------
# The code AFTER the if/else always runs (it's not indented)
# ---------------------------------------------------------------
print("Thanks for taking the exam.")   # this line always prints

# ---------------------------------------------------------------
# Another example: checking the weather to decide what to wear
# ---------------------------------------------------------------
temperature = 8    # degrees Celsius

if temperature < 10:
    print("\nIt's cold — wear a jacket!")
else:
    print("\nNice day — no jacket needed.")

# ---------------------------------------------------------------
# A note on indentation:
# Python uses indentation (4 spaces) to define code blocks.
# Code inside an if/else MUST be indented consistently.
# If you mix tabs and spaces Python will give you an IndentationError.
# ---------------------------------------------------------------
