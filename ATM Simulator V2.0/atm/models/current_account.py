from atm.models.account import BankAccount
from atm.exceptions.banking_exceptions import InsufficientFundsError


class CurrentAccount(BankAccount):

    OVERDRAFT_LIMIT = 2000

    def withdraw(self, amount: float):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self._balance + self.OVERDRAFT_LIMIT:
            raise InsufficientFundsError("Overdraft limit exceeded")

        self._balance -= amount