from tenant import *

class Client:
    
    def __init__(self) -> None:
        self.tenantList = []
        self.expenseList = []
        pass
    
    def display_main_menu(self) -> None:
        print("i - input data\nd - display report\nq - quit program\n")
        return
    
    def display_input_menu(self) -> None:
        print("t - add tenant\nr - record rent\ne - record expense\n")
        return
    
    def input_tenant(self) -> None:
        name = input("Enter tenant name: ")
        apt_num = input("Enter apt number: ")
        self.tenantList.append(Tenant(name, apt_num))
        return
    
   
        
driver = Client()
driver.main_menu()
driver.input_tenant()

    
    