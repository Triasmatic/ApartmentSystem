class expense:
    def __init__(self, month, day, catagory, payee, amount):
        self.month = month
        self.day = day
        self.catagory = catagory
        self.payee = payee
        self.amount = amount

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getCategory(self):
        return self.catagory

    def getAmount(self):
        return self.amount

    def getPayee(self):
        return self.payee