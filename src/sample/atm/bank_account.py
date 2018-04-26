from cash_transaction import CashTransaction
from inquiry_transaction import InquiryTransaction

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(CashTransaction('D', amount))

    def withdraw(self, amount):
        if self.__balance >= amount:
           self.__balance -= amount
        else:
           amount = 0
           print("Insufficient funds")

        self.transactions.append(CashTransaction('W', amount))

    def get_balance(self):
        self.transactions.append(InquiryTransaction('I'))
        return self.__balance

    def view_transactions(self):
        for trans in self.transactions:
            trans.display()




