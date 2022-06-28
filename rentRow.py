class rentRow:
    def __init__(self,  aptNum, month, amount):
        self.rent = amount
        self.aptNumber = aptNum
        self.datePaid = month


    def setRent(self, month, rent):
        self.rent[month - 1] = rent

    def getApt(self):
        return self.aptNumber

    def getDatePaid(self):
        return self.datePaid

    def getAmount(self):
        return self.rent

    def getSumOfRow(self):
        return sum(self.rent)
