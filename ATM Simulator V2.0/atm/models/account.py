from abc import ABC, abstractmethod
from datetime import datetime


class BankAccount(ABC):

    def __init__(
        self,
        account_number: str,
        holder_name: str,
        pin: str,
        balance: float = 0
    ):
        self._account_number = account_number
        self._holder_name = holder_name
        self._pin = pin
        self._balance = balance
        self._transactions = []
        self.created_at = datetime.now()

    @property
    def account_number(self):
        return self._account_number

    @property
    def holder_name(self):
        return self._holder_name

    def authenticate(self, pin: str) -> bool:
        return self._pin == pin

    def deposit(self, amount: float):

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    def get_balance(self):
        return self._balance

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def get_transactions(self):
        return self._transactions