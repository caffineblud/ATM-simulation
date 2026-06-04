from atm.models.savings_account import SavingsAccount
from atm.models.current_account import CurrentAccount
from atm.models.transactions import Transaction
from atm.services.storage_service import StorageService
from atm.exceptions.banking_exceptions import AccountNotFoundError


class ATMService:

    def __init__(self):

        self.accounts = {}
        self.current_account = None
        self.load_accounts()

    def create_account(
        self,
        account_type,
        account_number,
        holder_name,
        pin,
        balance
    ):

        if account_type == "savings":

            account = SavingsAccount(
                account_number,
                holder_name,
                pin,
                balance
            )

        else:

            account = CurrentAccount(
                account_number,
                holder_name,
                pin,
                balance
            )

        self.accounts[account_number] = account
        self.save_accounts()

    def load_accounts(self):

        data = StorageService.load_data()

        for item in data:

            if item["type"] == "savings":

                account = SavingsAccount(
                    item["account_number"],
                    item["holder_name"],
                    item["pin"],
                    item["balance"]
                )

            else:

                account = CurrentAccount(
                    item["account_number"],
                    item["holder_name"],
                    item["pin"],
                    item["balance"]
                )

            self.accounts[item["account_number"]] = account

    def save_accounts(self):

        data = []

        for account in self.accounts.values():

            account_type = (
                "savings"
                if isinstance(account, SavingsAccount)
                else "current"
            )

            data.append({
                "type": account_type,
                "account_number": account.account_number,
                "holder_name": account.holder_name,
                "pin": account._pin,
                "balance": account.get_balance()
            })

        StorageService.save_data(data)

    def select_account(self, account_number):

        if account_number not in self.accounts:
            raise AccountNotFoundError("Account not found")

        self.current_account = self.accounts[account_number]

    def deposit(self, amount):

        self.current_account.deposit(amount)

        transaction = Transaction.create(
            "Deposit",
            amount,
            self.current_account.get_balance()
        )

        self.current_account.add_transaction(transaction)

        self.save_accounts()

    def withdraw(self, amount):

        self.current_account.withdraw(amount)

        transaction = Transaction.create(
            "Withdrawal",
            amount,
            self.current_account.get_balance()
        )

        self.current_account.add_transaction(transaction)

        self.save_accounts()

    def get_balance(self):

        return self.current_account.get_balance()

    def get_transactions(self):

        return self.current_account.get_transactions()