# reference links
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk


class RentApp:
    def __int__(self):
        # basic window setup
        window = tk.Tk()
        tenantBtn = tk.Button(window, text="Tenant Management", bg='orange')
        rentBtn = tk.Button(window, text="Rent Management")
        reportBtn = tk.Button(window, text="Finanacial")
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