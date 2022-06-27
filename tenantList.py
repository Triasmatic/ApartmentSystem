from tenant import *

class tenantList:

    def __init__(self):
        self.tenantList = {}

    # def insertTenant(self, tenant):
    #     self.tenants.append(tenant)
        
    def input_tenant(self) -> None:
        name = input("Enter tenant name: ")
        apt_num = input("Enter apt number: ")
        
        if apt_num not in self.tenantList:
            self.tenantList[apt_num] = Tenant(name, apt_num)
        else:
            print("Room is occupied")
            
        return

    def getAptNumber(self, string):
        for key, value in self.tenantList.items():
            if string == value:
                return key
        return "Tenant doesn't exist. Pleases check input."

    def display(self):
        for t in self.tenantList:
            print(t) # if this doesnt work, make __str__ in tenant class