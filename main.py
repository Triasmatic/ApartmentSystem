# reference links
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from functools import partial
from PIL import ImageTk, Image
import expense
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
        noteStyle.configure("TNotebook", tabposition='n', background='white')
        tabControl = ttk.Notebook(window)

        print(noteStyle.theme_names())

        # Setup of tkinter Notebooks (Tabs)
        mainTab = ttk.Frame(tabControl)
        tenantTab = ttk.Frame(tabControl)
        rentTab = ttk.Frame(tabControl)
        reportTab = ttk.Frame(tabControl, style="TNotebook")

        tabControl.add(mainTab, text="Home Page")
        tabControl.add(tenantTab, text="Tenants")
        tabControl.add(rentTab, text="Rent Management")
        tabControl.add(reportTab, text="Annual Report")
        tabControl.pack(expand=1,fill='both')
        img = ImageTk.PhotoImage(Image.open("RentAppShark.png"))
        imgLabel = tk.Label(mainTab, image = img)
        imgLabel.pack()

        tenantTab.grid_rowconfigure(0, weight=1)
        tenantTab.grid_columnconfigure(0, weight=1)
        rentTab.grid_rowconfigure(0, weight=1)
        rentTab.grid_columnconfigure(0, weight=1)

        # setup of tables for tenant
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

        # add tenant window
        def addT():
            addTWindow = tk.Tk()
            nameText = tk.Entry(addTWindow)
            nameText.grid(column=1,row=0)
            aptText = tk.Entry(addTWindow)
            aptText.grid(column=1,row=1)
            phoneText = tk.Entry(addTWindow)
            phoneText.grid(column=1,row=2)
            nameLabel = tk.Label(addTWindow, text="Name ").grid(column=0,row=0)
            aptLabel = tk.Label(addTWindow, text="Apt ").grid(column=0, row=1)
            phoneLabel = tk.Label(addTWindow, text="Phone ").grid(column=0, row=2)

            btnPlusLabFrame= tk.Frame(addTWindow)
            errorLabel = tk.Label(btnPlusLabFrame, text="")
            errorLabel.grid(column=0, row=1)
            # check if apartment is occupied
            def checkDupApartment(comparevalue):
                children = tenantTable.get_children('')
                for child in children:
                    values = tenantTable.item(child, 'values')
                    if comparevalue == values[1] and str(comparevalue) == str(values[1]):
                        return True
                return False
            # insert tenant to table
            def tempAddT():
                t = tenant.Tenant(nameText.get(), aptText.get(), phoneText.get())
                if checkDupApartment(t.getAptNumber()):
                    errorLabel.config(text="ERROR: Apartment is occupied!", fg='RED')
                    return
                tenantTable.insert("", 'end', values=(t.getName(), t.getAptNumber(),t.getPhoneNumber()))
                addTWindow.destroy()
            tAddBtn = tk.Button(btnPlusLabFrame, text="Add this tenant", command=tempAddT).grid(column=0, row=0)
            btnPlusLabFrame.grid(column=0, row=4)
        # remove selected tenant
        def remT():
            selectedItem = tenantTable.selection()[0]
            tenantTable.delete(selectedItem)

        tb1 = tk.Frame(tenantTab)
        tb1.grid(column=0,row=1)

        # tennant add/remove buttons
        tenantAddBtn = Button(tb1, text="Add Tenant", command=addT)
        tenantAddBtn.grid(column=0, row=0)

        tenantRemoveBtn = Button(tb1, text="Remove Tenant", command=remT)
        tenantRemoveBtn.grid(column=2, row=0)

        # setup of rent table
        rentTable = ttk.Treeview(rentTab)
        rentTable['columns'] = ('apt_number', 'date_paid', 'amount_paid')
        rentTable['show'] = 'headings'
        rentTable.column('#0', width=0, stretch=YES)
        rentTable.column("apt_number", anchor=CENTER, width=80)
        rentTable.column("date_paid", anchor=CENTER, width=80)
        rentTable.column("amount_paid", anchor=CENTER, width=80)

        rentTable.heading('#0', text="", anchor=CENTER)
        rentTable.heading("apt_number", text='Apartment Number', anchor=CENTER)
        rentTable.heading("date_paid", text='Payment Date', anchor=CENTER)
        rentTable.heading("amount_paid", text='Payment Amount', anchor=CENTER)
        rentTable.grid(column=0, row=0, sticky='nsew')

        rb1 = tk.Frame(rentTab)
        rb1.grid(column=0, row=1)

        def subRent():
            addRWindow = tk.Tk()
            aptEntry = tk.Entry(addRWindow)
            aptEntry.grid(column=1, row=0)
            dateEntry = tk.Entry(addRWindow)
            dateEntry.grid(column=1, row=1)
            amountEntry = tk.Entry(addRWindow)
            amountEntry.grid(column=1, row=2)
            aptLabel = tk.Label(addRWindow, text="Apartment Number ").grid(column=0, row=0)
            dateLabel = tk.Label(addRWindow, text="Payment Date ").grid(column=0, row=1)
            amountLabel = tk.Label(addRWindow, text="Payment Amount ").grid(column=0, row=2)


            def checkIfAptExists(aptNumber):
                children = tenantTable.get_children('')
                for child in children:
                    values = tenantTable.item(child, 'values')
                    if aptNumber == values[1] and str(aptNumber) == str(values[1]):
                        return True
                return False

            def checkIfAlreadyPaid(aptNumber, datePaid):
                rentChildren = rentTable.get_children('')
                for child in rentChildren:
                    values = rentTable.item(child, 'values')
                    if aptNumber == values[0] and datePaid == values[1] and str(aptNumber) == str(values[0]) and str(datePaid) == str(values[1]):
                        return True
                return False

            def rentConf():
                r = rentRow.rentRow(aptEntry.get(), dateEntry.get(), amountEntry.get())
                if checkIfAptExists(r.getApt()) and not checkIfAlreadyPaid(r.getApt(), r.getDatePaid()):
                    rentTable.insert("",'end', values=(r.getApt(), r.getDatePaid(), r.getAmount()))
                    addRWindow.destroy()
                else:
                    errorLabel.config(text="ERROR: This apartment is not occupied or rent already paid this month!")

            tempFrameRent = tk.Frame(addRWindow)
            tempFrameRent.grid(column=0, row=4)
            errorLabel = tk.Label(tempFrameRent, text="", fg="RED")
            errorLabel.grid(column=0, row=1)
            confirmBtn = tk.Button(tempFrameRent, text='Confirm rent payment', command=rentConf)
            confirmBtn.grid(column=0, row=0)


        rentPayButton = tk.Button(rb1, text="Submit Rent", command=subRent)
        rentPayButton.grid(column = 0, row=0)
        def genAnnualReport():
            arWindow = tk.Tk()

            def getallpayments():
                children = rentTable.get_children('')
                paymentoutput = ''
                for index, child in enumerate(children):
                    values = rentTable.item(child, 'values')
                    paymentoutput += "\n\tMonth: " + values[1][0] + " | amount paid: " + values[2]

                return paymentoutput
                pass
            def getReport():
                children = rentTable.get_children('')
                totalSum = 0
                paymentoutput = ""
                tenantsShown = []
                for child in children:
                    values = rentTable.item(child, 'values')
                    totalSum = totalSum + int(values[2])
                    if values[0] in tenantsShown:
                        continue
                    else:
                        paymentoutput += "Appartment: " + values[0] + getallpayments() + "\n"
                        tenantsShown.append(str(values[0]))
                paymentoutput += '\nTotal Earned: '
                paymentoutput += str(totalSum) + '\n'
                return paymentoutput
                pass
            totalRent = getReport()
            totalRent += '\n'

            arEntry = tk.Label(arWindow, text=totalRent)
            # arEntry.config(textvariable=sampleText)
            # arScrollbar = tk.Scrollbar(arWindow, orient='vertical', command=arEntry.xview)
            # arEntry.config(xscrollcommand=arScrollbar.set)
            arEntry.grid(column=0, row=0)
            # arScrollbar.grid(column=2, row=0)
            def exitAR():
                arWindow.destroy()

            endARButton = tk.Button(arWindow, text='exit annual report', command=exitAR).grid(column=0,row=1)

        arLabel = tk.Label(reportTab, height=12, bg="WHITE", text="Here you can check your annual report. Press the button below.")
        arLabel.pack()
        arButton = tk.Button(reportTab, text="Generate Annual report", command=genAnnualReport).pack()



        window.title("Tenant Management System")
        window.geometry('700x550')

        windowFrames = []
        window.mainloop()

if __name__ == '__main__':
    RentApp().__int__()