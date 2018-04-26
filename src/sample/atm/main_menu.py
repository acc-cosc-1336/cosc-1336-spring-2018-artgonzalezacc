from main_menu_actions import MainMenuActions
import random

class MainMenu:

    def __init__(self):

        self.main_menu_actions = MainMenuActions()
        self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[random.randint(1,4)]

    def __account_menu(self):

        print("Select account: ")
        print("1) Checking")
        print("2) Savings")
        print("3) Exit")

    def __display_menu(self):
        print("ACME ATM")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Inquiry")
        print("4) Transactions")
        print("5) Exit to Account Menu")

    def run_atm(self):

        choice = -1

        self.__account_menu()
        self.main_menu_actions.atm.account = int(input("Enter choice: "))

        while self.main_menu_actions.atm.account != 3:

            while choice != 5:
                self.__display_menu()
                choice = int(input("What do you want to do?"))

                if choice == 1:
                    self.main_menu_actions.handle_deposit()
                elif choice == 2:
                    self.main_menu_actions.handle_withdraw()
                elif choice == 3:
                    self.main_menu_actions.handle_inquiry()
                elif choice == 4:
                    self.main_menu_actions.handle_transactions()

            choice = -1
            self.__account_menu()
            self.main_menu_actions.atm.account = int(input("Enter choice: "))

            if self.main_menu_actions.atm.account == 0:
                self.main_menu_actions.atm.account = 1
                self.main_menu_actions.atm.customer = self.main_menu_actions.atm.customer_repository.customers[random.randint(1,4)]

