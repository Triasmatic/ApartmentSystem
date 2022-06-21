from unittest import case
from tenant import *
# from TenantList import *

class Client:
    
    def __init__(self) -> None:
        self.tenantList = {}
        self.expenseList = []
        self.rentPayments = []
        pass
    
    
    def input_tenant(self) -> None:
        name = input("Enter tenant name: ")
        apt_num = input("Enter apt number: ")
        
        if apt_num not in self.tenantList:
            self.tenantList[apt_num] = Tenant(name, apt_num)
        else:
            print("Room is occupied")
            
        
        return
    
     
    
class UI:
    def main_menu() -> None:
        return "i - input data\nd - display report\nq - quit program\n"
    
    def input_menu() -> None:
        return "t - add tenant\nr - record rent\ne - record expense\n"
    
    def display_tenants(prog):
        print("Room - Name")
        print("-----------")
        for element in prog.tenantList:
            print(prog.tenantList.get(element))
            
        return 
   
        
driver = Client()

while True:
    option = input(UI.main_menu())
    
    if option == "i": #input data 
        option = input(UI.input_menu())
        if option == "t":
            driver.input_tenant()
        elif option == "r":
            pass #record rent
        elif option == "e":
            pass #record expense
     
    elif option == "d": #display report
        UI.display_tenants(driver)
        
    elif option == "q": #quit program
        break
    
print("Logging out...")