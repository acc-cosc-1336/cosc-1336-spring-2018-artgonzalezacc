from transaction import Transaction

class CashTransaction(Transaction):

    def __init__(self, trans_type, amount):

        Transaction.__init__(self, trans_type, amount)

    def display(self):

        print(self.trans_type, format(self.amount, '.2f'))
