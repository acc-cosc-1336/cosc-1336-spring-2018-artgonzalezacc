from bank_account import BankAccount
import random

class Customer:

    def __init__(self):
        self.id = 1
        self.name = 'John Doe'
        self.accounts = {1: BankAccount(random.randint(1, 10000)), \
                         2:BankAccount(random.randint(1, 50000))}
