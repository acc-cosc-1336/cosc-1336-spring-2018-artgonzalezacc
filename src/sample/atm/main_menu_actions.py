from atm import ATM

class MainMenuActions:

    def __init__(self):

        self.atm = ATM()

    def handle_deposit(self, amt=-1):

        if amt == -1:
            self.atm.deposit()
        else:
            self.atm.deposit(amt)

    def handle_withdraw(self, amt=-1):

        if amt == -1:
            self.atm.withdraw()
        else:
            self.atm.withdraw(amt)

    def handle_inquiry(self):
        self.atm.inquiry()

    def handle_transactions(self):
        self.atm.transactions()

    def get_inquiry_balance(self):

        return self.atm.balance()
