from tenant import *
import userInterface as UI

class Client:
    
    def __init__(self) -> None:
        self.tenantList = {}
        self.expenseList = []
        self.rentPayments = []
        return
    
    
    def input_tenant(self) -> None:
        name = input("Enter tenant name: ")
        apt_num = input("Enter apt number: ")
        
        if apt_num not in self.tenantList:
            self.tenantList[apt_num] = Tenant(name, apt_num)
        else:
            print("Room is occupied")
            
        
        return
   
#test run    
# driver = Client()

# while True:
#     option = input(UI.main_menu())
    
#     if option == "i": #input data 
#         option = input(UI.input_menu())
#         if option == "t":
#             driver.input_tenant()
#         elif option == "r":
#             pass #record rent
#         elif option == "e":
#             pass #record expense
     
#     elif option == "d": #display report
#         UI.display_tenants(driver)
        
#     elif option == "q": #quit program
#         break
    
# print("Logging out...")