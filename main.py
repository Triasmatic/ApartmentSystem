# reference links
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

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