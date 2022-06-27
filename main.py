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
        # tenantTable.column("tenent_id", anchor=CENTER, width=80)
        tenantTable.column("tenent_name", anchor=CENTER, width=80)
        tenantTable.column("tenent_apt_numbner", anchor=CENTER, width=80)
        tenantTable.column("tenent_phone_number", anchor=CENTER, width=80)

        tenantTable.heading('#0', text="", anchor=CENTER)
        # tenantTable.heading("tenent_id", text="Tenent ID", anchor=CENTER)
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
            def tempAddT():
                tenantTable.insert("", 'end', values=(nameText.get('1.0','end'), aptText.get('1.0','end'), phoneText.get('1.0','end')))
                addTWindow.destroy()
            tAddBtn = tk.Button(addTWindow, text="Add this tenant", command=tempAddT).grid(column=0, row=4)

        def editT():
            editTWindow = tk.Tk()
            selctedItem = tenantTable.selection()
            nameText = tk.Text(editTWindow, height=1, width=50, text=selctedItem)
            nameText.grid(column=1, row=0)
            aptText = tk.Text(editTWindow, height=1, width=50, text=selctedItem)
            aptText.grid(column=1, row=1)
            phoneText = tk.Text(editTWindow, height=1, width=50, text=selctedItem)
            phoneText.grid(column=1, row=2)
            nameLabel = tk.Label(editTWindow, text="Name ").grid(column=0, row=0)
            aptLabel = tk.Label(editTWindow, text="Apt ").grid(column=0, row=1)
            phoneLabel = tk.Label(editTWindow, text="Phone ").grid(column=0, row=2)
            def tempEditT():
                tenantTable.item(selctedItem, text="bulb", values=(nameText.get('1.0','end'), aptText.get('1.0','end'), phoneText.get('1.0','end')))
                editTWindow.destroy()
            tEditBtn = tk.Button(editTWindow, text="Edit this tenant", command=tempEditT).grid(column=0, row=4)

        def remT():
            selectedItem = tenantTable.selection()[0]
            tenantTable.delete(selectedItem)


        tb1 = tk.Frame(tenantTab)
        tb1.grid(column=0,row=1)
        tenantAddBtn = Button(tb1, text="Add Tenant", command=addT)
        tenantAddBtn.grid(column=0, row=0)

        tenantEditBtn = Button(tb1, text="Edit Tenant", command=editT)
        tenantEditBtn.grid(column=1, row=0)

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