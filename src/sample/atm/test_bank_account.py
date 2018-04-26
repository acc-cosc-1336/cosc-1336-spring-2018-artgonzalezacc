import unittest
from bank_account import BankAccount

class Test_BankAccount(unittest.TestCase):

    account = BankAccount(500)
    
    def test_begin_balance_w_500(self):
        self.assertEqual(500, self.account.get_balance())

    def test_deposit_100(self):
        self.account.deposit(100)
        self.assertEqual(600, self.account.get_balance())

    def test_withdraw_200(self):
        self.account.withdraw(200)
        self.assertEqual(400, self.account.get_balance())

    def test_withdraw_500(self):
        self.account.withdraw(500)
        self.assertEqual(400, self.account.get_balance())
       

unittest.main(verbosity=2)
        
