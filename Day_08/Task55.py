# Task 55: Simulate a bank system with deposit, withdraw, and balance operations.

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self._balance = initial_balance # Private attribute

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f" Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f" Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        else:
            print(f" Invalid withdrawal. Available: ${self._balance:.2f}")

# Demonstration
account = BankAccount("Sarah Jenkins", 500.00)
account.deposit(150.00)
account.withdraw(600.00)
account.withdraw(100.00)