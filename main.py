# reference links
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from functools import partial
import rentRecord
import rentRow
import tenant
import tenantList
import tenantInputScreen
import userInterface

# from https://pythonexamples.org/python-tkinter-login-form/
def valLogin(username, password):
    print('username entered: ', username)
    print('password enterd:', password)
    if (username == 'admin' and password == 'pass'):
        return True
    return False

class loginWindow:
    def __int__(self):
        window = tk.Tk()
        window.geometry( '400x200')
        window.title('RentApp login')

        userLabel =tk.Label(window, text='Username: ').grid(row=1,column=0)
        username = StringVar()
        usernameEntry = tk.Entry(window, textvariable=username).grid(row=1,column=1)

        passLabel = tk.Label(window, text='Password: ').grid(row=2,column=0)
        password = StringVar()
        passEntry = tk.Entry(window, textvariable=password, show='*').grid(row=2, column=1)
        window.mainloop()



        loginButton = tk.Button(window, text='Validate Login', command=valLogin(usernameEntry.get(),password)).grid(row=3, column=1)




    # def validate():
    #     if (valLogin(username, password)):
    #         self.quitLogin()
    def quitLogin(self):
        self.window.destroy()
        RentApp().__int__()
        
        
class RentApp:
    def __int__(self):
        # basic window setup
        window = tk.Tk()

        window.title("Rent Application")
        noteStyle = ttk.Style(window)
        noteStyle.theme_use('clam')
        noteStyle.configure("TNotebook", tabposition='n')
        tabControl = ttk.Notebook(window)

        print(noteStyle.theme_names())

        mainTab = ttk.Frame(tabControl)
        tenantTab = ttk.Frame(tabControl)
        rentTab = ttk.Frame(tabControl)
        reportTab = ttk.Frame(tabControl)

        tabControl.add(mainTab, text="Home Page")
        tabControl.add(tenantTab, text="Tenants")
        tabControl.add(rentTab, text="Rent Management")
        tabControl.add(reportTab, text="Annual Report")
        tabControl.pack(expand=1,fill='both')

        tenantTab.grid_rowconfigure(0, weight=1)
        tenantTab.grid_columnconfigure(0, weight=1)

        tenantBtn = tk.Button(mainTab, text="Tenant Management", bg='orange')
        rentBtn = tk.Button(mainTab, text="Rent Management")
        reportBtn = tk.Button(mainTab, text="Financial")
        tenantBtn.grid(column=0, row=0)
        rentBtn.grid(column=1, row=0)
        reportBtn.grid(column=2, row=0)

        tenantTable = ttk.Treeview(tenantTab)
        tenantTable['columns'] = ('tenent_name', 'tenent_apt_numbner', 'tenent_phone_number')
        tenantTable['show'] = 'headings'
        tenantTable.column('#0', width=0, stretch=YES)
        tenantTable.column("tenent_name", anchor=CENTER, width=80)
        tenantTable.column("tenent_apt_numbner", anchor=CENTER, width=80)
        tenantTable.column("tenent_phone_number", anchor=CENTER, width=80)

        tenantTable.heading('#0', text="", anchor=CENTER)
        tenantTable.heading("tenent_name", text="Tenent Name", anchor=CENTER)
        tenantTable.heading("tenent_apt_numbner", text="Apartment Number", anchor=CENTER)
        tenantTable.heading("tenent_phone_number", text="Phone Number", anchor=CENTER)

        tenantTable.grid(column=0, row=0, sticky="nsew")

        def addT():
            addTWindow = tk.Tk()
            nameText = tk.Text(addTWindow, height=1, width=50)
            nameText.grid(column=1,row=0)
            aptText = tk.Text(addTWindow, height=1, width=50)
            aptText.grid(column=1,row=1)
            phoneText = tk.Text(addTWindow, height=1, width=50)
            phoneText.grid(column=1,row=2)
            nameLabel = tk.Label(addTWindow, text="Name ").grid(column=0,row=0)
            aptLabel = tk.Label(addTWindow, text="Apt ").grid(column=0, row=1)
            phoneLabel = tk.Label(addTWindow, text="Phone ").grid(column=0, row=2)

            btnPlusLabFrame= tk.Frame(addTWindow)
            errorLabel = tk.Label(btnPlusLabFrame, text="")
            errorLabel.grid(column=1, row=0)

            def checkDupApartment(comparevalue):
                children = tenantTable.get_children('')
                for child in children:
                    values = tenantTable.item(child, 'values')
                    if(comparevalue == values[1] and str(comparevalue) == str(values[1])):
                        return True
                return False

            def tempAddT():
                t = tenant.Tenant(nameText.get('1.0','end'), aptText.get('1.0','end'), phoneText.get('1.0','end'))
                if(checkDupApartment(t.getAptNumber())):
                    errorLabel.config(text="ERROR: Apartment is occupied!", fg='RED')
                    return
                tenantTable.insert("", 'end', values=(t.getName(), t.getAptNumber(),t.getPhoneNumber()))
                addTWindow.destroy()
            tAddBtn = tk.Button(btnPlusLabFrame, text="Add this tenant", command=tempAddT).grid(column=0, row=0)
            btnPlusLabFrame.grid(column=0, row=4)

        def remT():
            selectedItem = tenantTable.selection()[0]
            tenantTable.delete(selectedItem)


        tb1 = tk.Frame(tenantTab)
        tb1.grid(column=0,row=1)
        tenantAddBtn = Button(tb1, text="Add Tenant", command=addT)
        tenantAddBtn.grid(column=0, row=0)

        tenantRemoveBtn = Button(tb1, text="Remove Tenant", command=remT)
        tenantRemoveBtn.grid(column=2, row=0)

        window.title("Tenant Management System")
        window.geometry('700x550')

        windowFrames = []

        l = landingPage.__int__(self)
        t = tenantPage.__init__(self)
        r = rentPage.__init__(self)
        e = expensesPage.__init__(self)


        window.mainloop()


class landingPage:
    def __int__(self):
        print("landing page window")

class tenantPage:
    def __init__(self):
        print("Tenant page")

class rentPage:
    def __init__(self):
        print("rent page")

class expensesPage:
    def __init__(self):
        print("expense page")



if __name__ == '__main__':
    RentApp().__int__()