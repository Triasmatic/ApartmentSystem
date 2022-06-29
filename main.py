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

window = tk.Tk()
class loginWindow:
    def __int__(self):

        # window.geometry('400x200')
        window.title('RentApp login')
        wFrameL = ttk.Frame(window)
        wFrameL.grid(column=0, row = 0)
        userLabel = tk.Label(wFrameL, text='Username: ').grid(row=1, column=0)
        usernameEntry = tk.Entry(wFrameL)
        usernameEntry.grid(row=1, column=1)

        passLabel = tk.Label(wFrameL, text='Password: ').grid(row=2, column=0)
        passEntry = tk.Entry(wFrameL, show="*")
        passEntry.grid(row=2, column=1)

        def valLogin():
            print('username entered: ', usernameEntry.get())
            print('password enterd:', passEntry.get())
            if (usernameEntry.get() == 'admin' and passEntry.get() == 'pass'):
                wFrameL.destroy()
                RentApp.__int__(self)

            else:
                return False
            return False

        loginButton = tk.Button(wFrameL, text='Validate Login', command=valLogin).grid(row=3, column=1)
        window.mainloop()
        pass

    # def validate():
    #     if (valLogin(username, password)):
    #         self.quitLogin()
    def quitLogin(self):
        self.window.destroy()
        RentApp().__int__()


class RentApp:
    def __int__(self):
        # basic window setup
        # window = tk.Tk()
        window.configure(bg="#01014a")
        window.title("Rent Application")
        noteStyle = ttk.Style(window)
        noteStyle.theme_use('clam')
        noteStyle.configure("TNotebook", tabposition='n', background='white')
        wFrame = ttk.Frame(window)
        wFrame.pack()
        # window.geometry('400x200')
        tabControl = ttk.Notebook(wFrame)

        print(noteStyle.theme_names())

        # Setup of tkinter Notebooks (Tabs)
        mainTab = ttk.Frame(tabControl)
        tenantTab = ttk.Frame(tabControl)
        rentTab = ttk.Frame(tabControl)
        reportTab = ttk.Frame(tabControl, style="TNotebook")
        expenseTab = ttk.Frame(tabControl)

        tabControl.add(mainTab, text="Home Page")
        tabControl.add(tenantTab, text="Tenant Management")
        tabControl.add(rentTab, text="Rent Management")
        tabControl.add(expenseTab, text="Expense Management")
        tabControl.add(reportTab, text="Annual Report")
        tabControl.pack(expand=1, fill='both')
        PhotoImage(master = window)
        img = ImageTk.PhotoImage(Image.open("RentAppShark.png"))
        imgLabel = tk.Label(mainTab, image=img)
        imgLabel.pack()

        tenantTab.grid_rowconfigure(0, weight=1)
        tenantTab.grid_columnconfigure(0, weight=1)
        rentTab.grid_rowconfigure(0, weight=1)
        rentTab.grid_columnconfigure(0, weight=1)
        expenseTab.grid_rowconfigure(0, weight=1)
        expenseTab.grid_columnconfigure(0, weight=1)

        # setup of tables for tenant
        tenantTable = ttk.Treeview(tenantTab)
        tenantTable['columns'] = ('tenant_name', 'tenant_apt_number', 'tenant_phone_number')
        tenantTable['show'] = 'headings'
        tenantTable.column('#0', width=0, stretch=YES)
        tenantTable.column("tenant_name", anchor=CENTER, width=80)
        tenantTable.column("tenant_apt_number", anchor=CENTER, width=80)
        tenantTable.column("tenant_phone_number", anchor=CENTER, width=80)

        tenantTable.heading('#0', text="", anchor=CENTER)
        tenantTable.heading("tenant_name", text="Tenent Name", anchor=CENTER)
        tenantTable.heading("tenant_apt_number", text="Apartment Number", anchor=CENTER)
        tenantTable.heading("tenant_phone_number", text="Phone Number", anchor=CENTER)

        tenantTable.grid(column=0, row=0, sticky="nsew")

        # add tenant window
        def addT():
            addTWindow = tk.Tk()
            nameText = tk.Entry(addTWindow)
            nameText.grid(column=1, row=0)
            aptText = tk.Entry(addTWindow)
            aptText.grid(column=1, row=1)
            phoneText = tk.Entry(addTWindow)
            phoneText.grid(column=1, row=2)
            nameLabel = tk.Label(addTWindow, text="Name ").grid(column=0, row=0)
            aptLabel = tk.Label(addTWindow, text="Apt ").grid(column=0, row=1)
            phoneLabel = tk.Label(addTWindow, text="Phone ").grid(column=0, row=2)

            btnPlusLabFrame = tk.Frame(addTWindow)
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
                tenantTable.insert("", 'end', values=(t.getName(), t.getAptNumber(), t.getPhoneNumber()))
                addTWindow.destroy()

            tAddBtn = tk.Button(btnPlusLabFrame, text="Add this tenant", command=tempAddT).grid(column=0, row=0)
            btnPlusLabFrame.grid(column=0, row=4)

        # remove selected tenant
        def remT():
            selectedItem = tenantTable.selection()[0]
            tenantTable.delete(selectedItem)

        tb1 = tk.Frame(tenantTab)
        tb1.grid(column=0, row=1)

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
                    if aptNumber == values[0] and datePaid == values[1] and str(aptNumber) == str(values[0]) and str(
                            datePaid) == str(values[1]):
                        return True
                return False

            def rentConf():
                r = rentRow.rentRow(aptEntry.get(), dateEntry.get(), amountEntry.get())
                if checkIfAptExists(r.getApt()) and not checkIfAlreadyPaid(r.getApt(), r.getDatePaid()):
                    rentTable.insert("", 'end', values=(r.getApt(), r.getDatePaid(), r.getAmount()))
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
        rentPayButton.grid(column=0, row=0)

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
                expChildren = expTable.get_children('')
                totalExpense = 0
                for child in expChildren:
                    values = expTable.item(child, 'values')
                    totalExpense += int(values[4])
                paymentoutput += "Earning: " + str(totalSum) + '\n'
                paymentoutput += "Expenses: " + str(totalExpense) + '\n'
                totalMoney = totalSum - totalExpense
                paymentoutput += '\nTotal Money Owned(negative implies in debt): '
                paymentoutput += str(totalMoney) + '\n'
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

            endARButton = tk.Button(arWindow, text='exit annual report', command=exitAR).grid(column=0, row=1)

        arLabel = tk.Label(reportTab, height=12, bg="WHITE",
                           text="Here you can check your annual report. Press the button below.")
        arLabel.pack()
        arButton = tk.Button(reportTab, text="Generate Annual report", command=genAnnualReport).pack()

        expTable = ttk.Treeview(expenseTab)
        expTable['columns'] = ('month', 'day', 'category', 'payee', 'amount')
        expTable['show'] = 'headings'
        expTable.column('#0', width=0, stretch=YES)
        expTable.column("month", anchor=CENTER, width=30)
        expTable.column("day", anchor=CENTER, width=20)
        expTable.column("category", anchor=CENTER, width=120)
        expTable.column("payee", anchor=CENTER, width=120)
        expTable.column("amount", anchor=CENTER, width=40)

        expTable.heading('#0', text="", anchor=CENTER)
        expTable.heading("month", text="Month", anchor=CENTER)
        expTable.heading("day", text="Day", anchor=CENTER)
        expTable.heading("category", text="Category", anchor=CENTER)
        expTable.heading("payee", text="Payee", anchor=CENTER)
        expTable.heading("amount", text="Amount", anchor=CENTER)

        expTable.grid(column=0, row=0, sticky='nsew')

        expBtnFrame = tk.Frame(expenseTab)
        expBtnFrame.grid(column=0, row=1)

        def addExp():
            addWindow = tk.Tk()
            monthText = tk.Entry(addWindow)
            monthText.grid(column=1, row=0)
            dayText = tk.Entry(addWindow)
            dayText.grid(column=1, row=1)
            categoryText = tk.Entry(addWindow)
            categoryText.grid(column=1, row=2)
            payeeText = tk.Entry(addWindow)
            payeeText.grid(column=1, row=3)
            amountText = tk.Entry(addWindow)
            amountText.grid(column=1, row=4)
            monthLabel = tk.Label(addWindow, text="Month ").grid(column=0, row=0)
            dayLabel = tk.Label(addWindow, text="Day ").grid(column=0, row=1)
            categoryLabel = tk.Label(addWindow, text="Category ").grid(column=0, row=2)
            payeeLabel = tk.Label(addWindow, text="Payee ").grid(column=0, row=3)
            amountLabel = tk.Label(addWindow, text="Amount ").grid(column=0, row=4)

            def addExpHelper():
                e = expense.expense(monthText.get(), dayText.get(), categoryText.get(), payeeText.get(),
                                    amountText.get())
                expTable.insert('', 'end',
                                values=(e.getMonth(), e.getDay(), e.getCategory(), e.getPayee(), e.getAmount()))
                addWindow.destroy()

            tempAddExpBtn = tk.Button(addWindow, text="confirm adding expense", command=addExpHelper).grid(column=0,
                                                                                                           row=5)
            pass

        pass

        def removeExpRow():
            selectedItem = expTable.selection()[0]
            expTable.delete(selectedItem)

        def calcExpense():
            calcExpWindow = tk.Tk()

            def getExpReport():
                children = expTable.get_children('')
                totalExpense = 0
                expoutput = ''
                for child in children:
                    values = expTable.item(child, 'values')
                    totalExpense = totalExpense + int(values[4])
                    expoutput += values[1] + "-" + values[0] + ":\n\t " + values[3] + " was paid for " + values[
                        2] + " and was paid $" + values[4] + "\n"
                expoutput += "Total Expense: $" + str(totalExpense)
                return expoutput

            expReport = getExpReport()

            totalExpLabel = tk.Label(calcExpWindow, text=expReport)
            totalExpLabel.grid(column=0, row=0)
            exitExpBtn = tk.Button(calcExpWindow, text="Return to main program",
                                   command=lambda: calcExpWindow.destroy()).grid(column=0, row=1)

        pass

        addExpenseBtn = tk.Button(expBtnFrame, text="Add Expense", command=addExp).grid(column=0, row=0)
        removeExpenseBtn = tk.Button(expBtnFrame, text="Remove Expense", command=removeExpRow).grid(column=1, row=0)
        calcExpenseBtn = tk.Button(expBtnFrame, text="Calculate Expenses", command=calcExpense).grid(column=2, row=0)

        window.title("Tenant Management System Version 1.0")
        window.geometry('700x550')

        windowFrames = []
        window.mainloop()


if __name__ == '__main__':
    loginWindow().__int__()
