from atm.exceptions.banking_exceptions import InvalidPinError


class AuthService:

    @staticmethod
    def login(account, pin):

        if not account.authenticate(pin):
            raise InvalidPinError("Incorrect PIN")

        return True