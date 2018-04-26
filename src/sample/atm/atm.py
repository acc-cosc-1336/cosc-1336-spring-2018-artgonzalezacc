from customer import Customer
from data.customer_repository import CustomerRepository

class ATM:

    def __init__(self):
        self.customer_repository = CustomerRepository()
        self.customer = None
        self.account = -1

    def deposit(self, amt=-1):

        if amt == -1:
            amt = float(input("Deposit amount: "))
            
        bank_account = self.customer.accounts[self.account]
        bank_account.deposit(amt)

    def withdraw(self, amt=-1):

        if amt == -1:
            amt = float(input("Withdraw amount: "))
            
        bank_account = self.customer.accounts[self.account]
        bank_account.withdraw(amt)

    def inquiry(self, amt=-1):
        bank_account = self.customer.accounts[self.account]
        print("Balance: ", bank_account.get_balance())

    def transactions(self, amt=-1):
        bank_account = self.customer.accounts[self.account]
        bank_account.view_transactions()


    def balance(self):

        bank_account = self.customer.accounts[self.account]
        return bank_account.get_balance()
        

    

    
        

    
        
