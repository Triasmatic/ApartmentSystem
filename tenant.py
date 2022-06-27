class Tenant:

    def __init__(self, name, aptNumber, phoneNumber):
        self.name = name
        self.aptNumber = aptNumber
        self.phoneNumber = phoneNumber

    def getName(self):
        return self.name

    def getAptNumber(self):
        return self.aptNo

    def getPhoneNumber(self):
        return self.phoneNumber

    def __repr__(self):
        return f'{self.aptNumber} - {self.name}'