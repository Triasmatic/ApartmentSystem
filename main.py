# reference links
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from functools import partial

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

        tenantBtn = tk.Button(mainTab, text="Tenant Management", bg='orange')
        rentBtn = tk.Button(mainTab, text="Rent Management")
        reportBtn = tk.Button(mainTab, text="Financial")
        tenantBtn.grid(column=0, row=0)
        rentBtn.grid(column=1, row=0)
        reportBtn.grid(column=2, row=0)
        window.title("Tenant Management System")
        window.geometry('700x550')

        windowFrames = []


        window.mainloop()

class landingPage:
    def __int__(self):
        print("landing page window")



if __name__ == '__main__':
    RentApp().__int__()