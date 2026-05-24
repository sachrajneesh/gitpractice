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

# ============================================================
# Part A: BankAccount
# ============================================================

class BankAccount:
    """A basic bank account with deposit and withdraw functionality."""

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = float(balance)   # ensure it's always a float

    def deposit(self, amount):
        """Add amount to balance. Amount must be positive."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited £{amount:.2f}. New balance: £{self.balance:.2f}")

    def withdraw(self, amount):
        """Deduct amount from balance. Refuses if funds are insufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Balance: £{self.balance:.2f}, requested: £{amount:.2f}")
            return
        self.balance -= amount
        print(f"Withdrew £{amount:.2f}. New balance: £{self.balance:.2f}")

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance=£{self.balance:.2f})"


# ============================================================
# Part B: SavingsAccount (inherits from BankAccount)
# ============================================================

class SavingsAccount(BankAccount):
    """A savings account with an interest rate."""

    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        # Call parent __init__ to set up owner, balance — don't duplicate that code.
        super().__init__(owner, balance)
        self.interest_rate = interest_rate   # e.g. 0.05 = 5%

    def apply_interest(self):
        """Add interest to the balance and print how much was earned."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: £{interest:.2f} (rate {self.interest_rate*100:.1f}%). "
              f"New balance: £{self.balance:.2f}")

    def __str__(self):
        # Override to include the interest rate.
        return (f"SavingsAccount(owner={self.owner}, "
                f"balance=£{self.balance:.2f}, "
                f"rate={self.interest_rate*100:.1f}%)")


# ============================================================
# Demo
# ============================================================

print("=== BankAccount Demo ===")

acc1 = BankAccount("Ryan")
acc2 = BankAccount("Alice", balance=500.00)

print(acc1)
print(acc2)
print()

acc1.deposit(200)
acc1.deposit(150)
acc1.withdraw(80)
acc1.withdraw(300)   # should fail — insufficient funds
print(f"Ryan's balance: £{acc1.get_balance():.2f}")

print()
print("=== SavingsAccount Demo ===")

savings = SavingsAccount("Marcus", balance=1000.00, interest_rate=0.04)
print(savings)
print()

savings.deposit(500)
savings.apply_interest()   # earn 4% interest on £1500
savings.apply_interest()   # compound it again
print()
print(savings)
savings.withdraw(200)      # withdrawals still work (inherited method)
print(savings)
