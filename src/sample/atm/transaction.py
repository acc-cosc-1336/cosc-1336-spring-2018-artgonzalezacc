class Transaction:

    def __init__(self, trans_type, amount=0):

        self.trans_type = trans_type
        self.amount = amount

    def display(self):

        print('Super class display')
