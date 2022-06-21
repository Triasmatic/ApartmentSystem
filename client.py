from unittest import case
from tenant import *
# from TenantList import *

class Client:
    
    def __init__(self) -> None:
        self.tenantList = {}
        self.expenseList = []
        pass
    
    def display_main_menu(self) -> None:
        print("i - input data\nd - display report\nq - quit program\n")
        return 0
    
    def display_input_menu(self) -> None:
        print("t - add tenant\nr - record rent\ne - record expense\n")
        return
    
    def input_tenant(self) -> None:
        name = input("Enter tenant name: ")
        apt_num = input("Enter apt number: ")
        
        if apt_num not in self.tenantList:
            self.tenantList[apt_num] = Tenant(name, apt_num)
        else:
            print("Room is occupied")
            
        
        return
    
    def display_tenants(self):
        print("Room - Name")
        print("-----------")
        for element in self.tenantList:
            print(self.tenantList.get(element))
            
        return  
    
    
   
        
driver = Client()

