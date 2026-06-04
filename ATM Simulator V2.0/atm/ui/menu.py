from atm.services.atm_service import ATMService
from atm.services.auth_service import AuthService


class ATMMenu:

    def __init__(self):

        self.atm_service = ATMService()
        self.logged_in = False

    # ==========================
    # GUEST MENU
    # ==========================

    def show_login_menu(self):

        print("\n" + "=" * 40)
        print("         ATM SYSTEM")
        print("=" * 40)

        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

    # ==========================
    # USER MENU
    # ==========================

    def show_user_menu(self):

        account = self.atm_service.current_account

        print("\n" + "=" * 40)
        print(f" Welcome, {account.holder_name}")
        print("=" * 40)

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Logout")

    # ==========================
    # ACCOUNT CREATION
    # ==========================

    def create_account(self):

        print("\nCreate New Account")

        account_type = input(
            "Account Type (savings/current): "
        ).lower()

        account_number = input("Account Number: ")

        holder_name = input("Holder Name: ")

        pin = input("Set 4-digit PIN: ")

        balance = float(
            input("Initial Balance: ₹")
        )

        self.atm_service.create_account(
            account_type,
            account_number,
            holder_name,
            pin,
            balance
        )

        print("\nAccount created successfully!")

    # ==========================
    # LOGIN
    # ==========================

    def login(self):

        account_number = input(
            "\nEnter Account Number: "
        )

        pin = input("Enter PIN: ")

        self.atm_service.select_account(
            account_number
        )

        account = self.atm_service.current_account

        AuthService.login(
            account,
            pin
        )

        self.logged_in = True

        print(
            f"\nLogin Successful! Welcome {account.holder_name}"
        )

    # ==========================
    # LOGOUT
    # ==========================

    def logout(self):

        self.atm_service.current_account = None

        self.logged_in = False

        print("\nLogged out successfully!")

    # ==========================
    # DEPOSIT
    # ==========================

    def deposit(self):

        amount = float(
            input("\nEnter Amount: ₹")
        )

        self.atm_service.deposit(amount)

        print("\nDeposit Successful!")

        print(
            f"Current Balance: ₹{self.atm_service.get_balance()}"
        )

    # ==========================
    # WITHDRAW
    # ==========================

    def withdraw(self):

        amount = float(
            input("\nEnter Amount: ₹")
        )

        self.atm_service.withdraw(amount)

        print("\nWithdrawal Successful!")

        print(
            f"Remaining Balance: ₹{self.atm_service.get_balance()}"
        )

    # ==========================
    # BALANCE
    # ==========================

    def balance(self):

        balance = self.atm_service.get_balance()

        print(
            f"\nCurrent Balance: ₹{balance}"
        )

    # ==========================
    # HISTORY
    # ==========================

    def history(self):

        transactions = (
            self.atm_service.get_transactions()
        )

        print("\n" + "=" * 60)
        print("       TRANSACTION HISTORY")
        print("=" * 60)

        if not transactions:

            print(
                "No transactions available."
            )

            return

        for transaction in transactions:

            print(
                f"{transaction.timestamp} | "
                f"{transaction.transaction_type} | "
                f"₹{transaction.amount} | "
                f"Balance: ₹{transaction.balance_after}"
            )

    # ==========================
    # MAIN LOOP
    # ==========================

    def run(self):

        while True:

            try:

                # --------------------
                # BEFORE LOGIN
                # --------------------

                if not self.logged_in:

                    self.show_login_menu()

                    choice = input(
                        "\nEnter Choice: "
                    )

                    if choice == "1":

                        self.create_account()

                    elif choice == "2":

                        self.login()

                    elif choice == "3":

                        print(
                            "\nThank you for using ATM!"
                        )

                        break

                    else:

                        print(
                            "\nInvalid Choice"
                        )

                # --------------------
                # AFTER LOGIN
                # --------------------

                else:

                    self.show_user_menu()

                    choice = input(
                        "\nEnter Choice: "
                    )

                    if choice == "1":

                        self.deposit()

                    elif choice == "2":

                        self.withdraw()

                    elif choice == "3":

                        self.balance()

                    elif choice == "4":

                        self.history()

                    elif choice == "5":

                        self.logout()

                    else:

                        print(
                            "\nInvalid Choice"
                        )

            except Exception as error:

                print(
                    f"\nError: {error}"
                )