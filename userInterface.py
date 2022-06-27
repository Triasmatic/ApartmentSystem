from tenant import *
from tenantList import *

class UI:
    def main_menu() -> None:
        return "i - input data\nd - display report\nq - quit program\n"
    
    def input_menu() -> None:
        return "t - add tenant\nr - record rent\ne - record expense\n"
    
    def display_tenants(tList):
        print("Room - Name")
        print("-----------")
        for element in tList.tenantList:
            print(tList.tenantList.get(element))
            
        return 
   