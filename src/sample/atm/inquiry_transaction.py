from transaction import Transaction

class InquiryTransaction(Transaction):

    def __init__(self, trans_type):

        Transaction.__init__(self, trans_type)

    def display(self):

        print(self.trans_type)

    
