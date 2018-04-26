from customer import Customer

class CustomerRepository:

    def __init__(self):

        self.customers = {}
        self.__init_account_data()

    def __init_account_data(self):

        self.customers[1] = Customer()
        self.customers[2] = Customer()
        self.customers[3] = Customer()
        self.customers[4] = Customer()
        
