# reference links
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

from tkinter import *


class RentApp:
    def __int__(self):
        # basic window setup
        def leave():
            nope = Button(window, text="don't press", command=exit)
            nope.pack()
        window = Tk()
        tenantBtn = Button(window, text="Tenant Management", bg='orange', command=leave)
        rentBtn = Button(window, text="Rent Management")
        reportBtn = Button(window, text="Finanacial")
        # tenantBtn.grid(column=0, row=0)
        # rentBtn.grid(column=1, row=0)
        # reportBtn.grid(column=2, row=0)
        tenantBtn.pack()
        rentBtn.pack()
        reportBtn.pack()
        window.title("Tenant Management System")
        window.geometry('700x550')

        windowFrames = []


        window.mainloop()

class landingPage:
    def __int__(self):
        print("landing page window")



if __name__ == '__main__':
    RentApp().__int__()