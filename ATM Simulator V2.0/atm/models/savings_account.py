from atm.models.account import BankAccount
from atm.exceptions.banking_exceptions import InsufficientFundsError


class SavingsAccount(BankAccount):

    MIN_BALANCE = 500

    def withdraw(self, amount: float):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if self._balance - amount < self.MIN_BALANCE:
            raise InsufficientFundsError(
                f"Minimum balance of ₹{self.MIN_BALANCE} required"
            )

        self._balance -= amount