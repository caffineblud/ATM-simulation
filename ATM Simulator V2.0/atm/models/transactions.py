from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:

    transaction_type: str
    amount: float
    balance_after: float
    timestamp: str

    @staticmethod
    def create(transaction_type, amount, balance_after):

        return Transaction(
            transaction_type=transaction_type,
            amount=amount,
            balance_after=balance_after,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )