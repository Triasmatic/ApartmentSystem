class rentRow:
    def __init__(self, aptNumber):
        self.rent = [0] * 12
        self.aptNumber = aptNumber

    def setRent(self, month, rent):
        self.rent[month - 1] = rent

    def getSumOfRow(self):
        return sum(self.rent)
