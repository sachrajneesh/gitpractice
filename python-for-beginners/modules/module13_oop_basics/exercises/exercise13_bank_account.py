"""
Exercise 13 🔴: BankAccount & SavingsAccount

What you'll practise:
  Classes, __init__, instance methods, __str__, inheritance, and super().

Task:
  Part A — BankAccount class:
    Attributes: owner (str), balance (float, default 0.0)
    Methods:
      deposit(amount)   — add amount to balance; print confirmation
      withdraw(amount)  — deduct amount; print confirmation; refuse if insufficient funds
      get_balance()     — return current balance
      __str__           — "BankAccount(owner=Alice, balance=£150.00)"

  Part B — SavingsAccount subclass:
    Inherits from BankAccount.
    Additional attribute: interest_rate (float, e.g. 0.05 for 5%)
    Additional method: apply_interest() — multiply balance by (1 + interest_rate),
                       print how much interest was added.
    Override __str__ — include the interest rate.

Requirements:
  - deposit() and withdraw() must validate: amounts must be positive.
  - withdraw() must print "Insufficient funds" if amount > balance.
  - Create at least two BankAccount objects and one SavingsAccount.
  - Demonstrate all methods.

How to run:
  python modules/module13_oop_basics/exercises/exercise13_bank_account.py

Hints:
  - class SavingsAccount(BankAccount):
  - In SavingsAccount.__init__: call super().__init__(owner, balance)
  - apply_interest: interest = self.balance * self.interest_rate; self.balance += interest

Rules:
  - TYPE every line yourself — no copy-paste, ever.
  - Stuck for 15+ min? Peek at the solution, then CLOSE it and retype from memory.
"""

# === Your code goes below this line ===

# --- Part A: BankAccount ---

# TODO: Step 1 — Define class BankAccount with __init__(self, owner, balance=0.0)
# TODO: Step 2 — Add deposit(self, amount) method
# TODO: Step 3 — Add withdraw(self, amount) method with balance check
# TODO: Step 4 — Add get_balance(self) method
# TODO: Step 5 — Add __str__(self) method

# --- Part B: SavingsAccount ---

# TODO: Step 6 — Define class SavingsAccount(BankAccount)
# TODO: Step 7 — Override __init__ to add interest_rate attribute (call super().__init__)
# TODO: Step 8 — Add apply_interest(self) method
# TODO: Step 9 — Override __str__(self)

# --- Demo ---

# TODO: Step 10 — Create two BankAccount objects, deposit/withdraw, print
# TODO: Step 11 — Create one SavingsAccount, apply interest, print
