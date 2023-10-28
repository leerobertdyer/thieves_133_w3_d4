import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfilename
import os

currentFile = None


#converting from txt editor to calculator...
#May not need txtEdit at all...
#

def newFile(txtEdit, window):
    global currentFile
    txtEdit.delete(1.0, tk.END) #tk function (delete)
    currentFile = None
    window.title("Textual Healing - New File")
    
def saveAs(txtEdit, window):
    global currentFile
    file= asksaveasfile(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not file:
        return
    
    filepath = file.name 
    
    with open(filepath, 'w') as outputFile:
        text = txtEdit.get(1.0, tk.END)
        outputFile.write(text)
        
    window.title(f'Texual Healing - {filepath}')
    currentFile = filepath

def saveFile(txtEdit, window):
    global currentFile
    if currentFile is not None and os.path.exists(currentFile):
        with open(currentFile, 'w') as outputFile:
            text = txtEdit.get(1.0, tk.END)
            outputFile.write(text)
    else:
        saveAs(txtEdit, window)

def openFile(txtEdit, window):
    global currentFile
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    
    with open(filepath, 'r') as inputFile:
        text = inputFile.read()
    
    txtEdit.delete(1.0, tk.END)
    txtEdit.insert(tk.END, text)
        
    window.title(f'Texual Healing - {filepath}')
    currentFile = filepath
        
    
    
def main():
    window = tk.Tk()
    window.title("ROI Calculator")
    
    window.columnconfigure(0, minsize=80, weight=1) #One column for entire window
    window.rowconfigure(0, minsize=20, weight=0) #Menu
    window.rowconfigure(1, minsize=40, weight=1) #Label (Income)
    window.rowconfigure(2, minsize=220, weight=1) #income form
    window.rowconfigure(3, minsize=40, weight=1) #Label (Xpenses)
    window.rowconfigure(4, minsize=250, weight=1) #Expenses Form
    window.rowconfigure(5, minsize=40, weight=1)    #label (ROI)
    window.rowconfigure(6, minsize=200, weight=1) #ROI FORM
    window.rowconfigure(7, minsize=40, weight=1) #Label (OUTCOME) --> use variable in text paramater
    window.rowconfigure(8, minsize=40, weight=1) #Label (NOTES)
    window.rowconfigure(9, minsize=200) #TXT note pad
    
    menuButtons = tk.Frame(window, relief=tk.RIDGE, bd=10)
    income = tk.Label(window, text="Income")
    incomeForm = tk.Frame(window, relief=tk.SUNKEN, bd=4, background='beige')
    expenses = tk.Label(window, text="Expenses")
    expensesForm = tk.Frame(window, relief=tk.SUNKEN, bd=4, background='beige')
    roi = tk.Label(window, text='ROI')
    roiForm = tk.Frame(window, relief=tk.SUNKEN, bd=4, background="beige")
    outcome = tk.Label(window, text="OUTCOME:") # will need to define a function that updates this value...
    notes = tk.Label(window, text="NOTES")
    txtEdit = tk.Text(window) 
    
    incomeForm.columnconfigure(1, minsize=300, weight=1)
    expensesForm.columnconfigure(1, minsize=300, weight=1)
    roiForm.columnconfigure(1, minsize=300, weight=1)
    
    
    
    style = ttk.Style()
    style.configure("myBtn.TButton",
                    relief="ridge",
                    foreground="yellow",
                    padding=(10, 5))

#Menu Buttons
    btnOpen = ttk.Button(menuButtons, text="Open", style="myBtn.TButton", command=lambda: openFile(txtEdit, window))
    btnSave = ttk.Button(menuButtons, text="Save", style="myBtn.TButton", command=lambda: saveFile(txtEdit, window))
    btnSaveAs = ttk.Button(menuButtons, text="Save As", style="myBtn.TButton", command=lambda: saveAs(txtEdit, window))
    btnNew = ttk.Button(menuButtons, text="New", style="myBtn.TButton", command=lambda: newFile(txtEdit, window))

    btnNew.pack(side='left',fill="both", expand=True, padx=15, pady=18)
    btnOpen.pack(side='left',fill="both", expand=True, padx=15, pady=18)
    btnSave.pack(side='left',fill="both", expand=True, padx=15, pady=18)
    btnSaveAs.pack(side='left',fill="both", expand=True, padx=15, pady=18)

#Input Variables and Entries
    rent = tk.Label(incomeForm, text="Rent: ")
    rent.config(bg="beige", fg='black')
    rentVar = tk.IntVar()
    rentEntry = tk.Entry(incomeForm, textvariable=rentVar)
    
    laundry = tk.Label(incomeForm, text="Laundry: ")
    laundry.config(bg="beige", fg='black')
    laundryVar = tk.IntVar()
    laundryEntry = tk.Entry(incomeForm, textvariable=laundryVar)
    
    storage = tk.Label(incomeForm, text="Storage: ")
    storage.config(bg="beige", fg='black')
    storageVar = tk.IntVar()
    storageEntry = tk.Entry(incomeForm, textvariable=storageVar)
    
    other = tk.Label(incomeForm, text="Other (Type/Amount): ")
    other.config(bg="beige", fg='black')
    otherVar = tk.IntVar()
    otherType = tk.StringVar()
    otherTypeEntry = tk.Entry(incomeForm, textvariable=otherType)
    otherEntry = tk.Entry(incomeForm, textvariable=otherVar)
    
    def incomeSubmit():
        total = rentVar.get() + laundryVar.get() + storageVar.get() + otherVar.get()
        incomeTotalVar.set(total)
        incomeTotal.config(text=f'Total Income: _________{incomeTotalVar.get()}___________')
    incomeTotalVar = tk.IntVar()
    inputSubmitBtn = ttk.Button(incomeForm, text="Submit Income", style="myBtn.TButton", command=incomeSubmit)
    incomeTotal = tk.Label(incomeForm, text=f'Total Income: _________0___________') 


    
    
#Expenses Variables:
    mort = tk.Label(expensesForm, text="Mortgage: ")
    mort.config(bg="beige", fg='black')
    mortVar = tk.IntVar()
    mortEntry = tk.Entry(expensesForm, textvariable=mortVar) 
    
    tax = tk.Label(expensesForm, text="Tax: ")
    tax.config(bg="beige", fg='black')
    taxVar = tk.IntVar()
    taxEntry = tk.Entry(expensesForm, textvariable=taxVar)
    
    insurance = tk.Label(expensesForm, text="Insurance: ")
    insurance.config(bg="beige", fg='black')
    insuranceVar = tk.IntVar()
    insuranceEntry = tk.Entry(expensesForm, textvariable=insuranceVar)
    
    HOA = tk.Label(expensesForm, text="HOA Fees: ")
    HOA.config(bg="beige", fg='black')
    HOAVar = tk.IntVar()
    HOAEntry = tk.Entry(expensesForm, textvariable=HOAVar)
    
    lawn = tk.Label(expensesForm, text="Lawn Care: ")
    lawn.config(bg="beige", fg='black')
    lawnVar = tk.IntVar()
    lawnEntry = tk.Entry(expensesForm, textvariable=lawnVar)    
    
    electric = tk.Label(expensesForm, text="Electric: ")
    electric.config(bg="beige", fg='black')
    electricVar = tk.IntVar()
    electricEntry = tk.Entry(expensesForm, textvariable=electricVar)
    
    water = tk.Label(expensesForm, text="Water: ")
    water.config(bg="beige", fg='black')
    waterVar = tk.IntVar()
    waterEntry = tk.Entry(expensesForm, textvariable=waterVar)
    
    sewer = tk.Label(expensesForm, text="Sewer: ")
    sewer.config(bg="beige", fg='black')
    sewerVar = tk.IntVar()
    sewerEntry = tk.Entry(expensesForm, textvariable=sewerVar)
    
    garbage = tk.Label(expensesForm, text="Garbage: ")
    garbage.config(bg="beige", fg='black')
    garbageVar = tk.IntVar()
    garbageEntry = tk.Entry(expensesForm, textvariable=garbageVar)  
    
    gas = tk.Label(expensesForm, text="Gas: ")
    gas.config(bg="beige", fg='black')
    gasVar = tk.IntVar()
    gasEntry = tk.Entry(expensesForm, textvariable=gasVar)
    
    vacancy = tk.Label(expensesForm, text="Vacancy Fund: ") ###update with cut() function (5% of income total)
    vacancy.config(bg="beige", fg='black')
    vacancyVar = tk.IntVar()
    
    repair = tk.Label(expensesForm, text="Repair Fund: ") ###update with cut() function (5% of income total)
    repair.config(bg="beige", fg='black')
    repairVar = tk.IntVar()
    
    capEx = tk.Label(expensesForm, text="Capital Expense Fund: ") ###update with cut() function (5% of income total)
    capEx.config(bg="beige", fg='black')
    capExVar = tk.IntVar()
    
    mgmt = tk.Label(expensesForm, text="Management: ") ###update with cut() function (5% of income total)
    mgmt.config(bg="beige", fg='black')
    mgmtVar = tk.IntVar()
    
    def expenseSubmit(): # don't forget to add in vacancy cap ex mgmt and repair fund....
        vacancyVar.set(incomeTotalVar.get()*.05)
        repairVar.set(incomeTotalVar.get()*.05)
        capExVar.set(incomeTotalVar.get()*.05)
        mgmtVar.set(incomeTotalVar.get()*.1)
        total =  vacancyVar.get() + repairVar.get() + capExVar.get() + mgmtVar.get() + mortVar.get() + taxVar.get() + insuranceVar.get() + HOAVar.get() + lawnVar.get() + electricVar.get() + waterVar.get() + sewerVar.get() + garbageVar.get() + gasVar.get()
        expenseTotalVar.set(total)
        expensesTotal.config(text=f'Total Expenses: {expenseTotalVar.get()} includes {vacancyVar.get()} each for vacancy, repair, and capex funds, and {vacancyVar.get()*2} for MGMT')
    expenseTotalVar = tk.IntVar()
    expenseSubmitBtn = ttk.Button(expensesForm, text="Submit Expense", style="myBtn.TButton", command=expenseSubmit)
    expensesTotal = tk.Label(expensesForm, text=f'Total expense: 0') 

#ROI Variables:
    downPayment = tk.Label(roiForm, text="Down Payment: ")
    downPayment.config(bg="beige", fg='black')
    downPaymentVar = tk.IntVar()
    downPaymentEntry = tk.Entry(roiForm, textvariable=downPaymentVar)
    
    closing = tk.Label(roiForm, text="Closing Costs: ")
    closing.config(bg="beige", fg='black')
    closingVar = tk.IntVar()
    closingEntry = tk.Entry(roiForm, textvariable=closingVar)
    
    rehab = tk.Label(roiForm, text="Rehabilitation: ")
    rehab.config(bg="beige", fg='black')
    rehabVar = tk.IntVar()
    rehabEntry = tk.Entry(roiForm, textvariable=rehabVar)
    
    otherInvest = tk.Label(roiForm, text="Other Investment Costs: ")
    otherInvest.config(bg="beige", fg='black')
    otherInvestVar = tk.IntVar()
    otherInvestType = tk.StringVar()
    otherInvestTypeEntry = tk.Entry(roiForm, textvariable=otherInvestType)
    otherInvestEntry = tk.Entry(roiForm, textvariable=otherInvestVar)
    
    def roiSubmit(): # don't forget to add in vacancy cap ex mgmt and repair fund....
        incomeSubmit()
        expenseSubmit()
        total = downPaymentVar.get() + closingVar.get() + rehabVar.get() + otherInvestVar.get()
        initialInvestVar.set(total)
        initialInvestTotal.config(text=f'Initial Investment: {initialInvestVar.get()} ')
        cash = ((incomeTotalVar.get() - expenseTotalVar.get() ) * 12)
        roiTotalVar.set(cash / initialInvestVar.get())
        roiTotal.config(text=f'Total ROI: {roiTotalVar.get()}')
        outcome.config(text=f'Total ROI: {roiTotalVar.get()}')
    roiTotalVar = tk.DoubleVar()
    initialInvestVar = tk.IntVar()
    roiSubmitBtn = ttk.Button(roiForm, text="Submit ROI", style="myBtn.TButton", command=roiSubmit)
    initialInvestTotal = tk.Label(roiForm, text=f'Initial Investment: 0') 
    roiTotal = tk.Label(roiForm, text=f'Total ROI: 0') 
    
      
    
#Main Grid
    menuButtons.grid(row=0, column=0, sticky='nsew')
    income.grid(row=1, column=0, sticky='nsew')
    incomeForm.grid(row=2, column=0, sticky="nsew")
    expenses.grid(row=3, column=0, sticky='nsew')
    expensesForm.grid(row=4, column=0, sticky='nsew')
    roi.grid(row=5, column=0, sticky='nsew')
    roiForm.grid(row=6, column=0, sticky='nsew')
    outcome.grid(row=7, column=0, sticky='nsew')
    notes.grid(row=8, column=0, sticky='nsew')
    txtEdit.grid(row=9, column=0, sticky='nsew')

#Income Form Grid
    rent.grid(row=0, column=0, sticky='w', padx=5)
    rentEntry.grid(row=0, column=2, sticky='ew', padx=2, pady=1)
    laundry.grid(row=1, column=0, sticky='w', padx=5)
    laundryEntry.grid(row=1, column=2, sticky='ew', padx=2, pady=1)
    storage.grid(row=2, column=0, sticky='w', padx=5)
    storageEntry.grid(row=2, column=2, sticky='ew', padx=2, pady=1)
    other.grid(row=3, column=0, sticky='w', padx=5)
    otherTypeEntry.grid(row=3, column=1, sticky='ew', padx=2, pady=1)
    otherEntry.grid(row=3, column=2, sticky='ew', padx=2, pady=1)
    incomeTotal.grid(row=5, column=0, sticky='ew', pady=5)
    inputSubmitBtn.grid(row=6, columnspan=3, sticky='ew', padx=105, pady=5)
    
#expense grid:
    #   lawn electric water sewer garbage gas
    mort.grid(row=0, column=0, sticky='w', padx=5)
    mortEntry.grid(row=0, column=1, sticky='ew', padx=2, pady=1)
    tax.grid(row=1, column=0, sticky='w', padx=5)
    taxEntry.grid(row=1, column=1, sticky='ew', padx=2, pady=1)
    insurance.grid(row=2, column=0, sticky='w', padx=5)
    insuranceEntry.grid(row=2, column=1, sticky='ew', padx=2, pady=1)
    HOA.grid(row=3, column=0, sticky='w', padx=5)
    HOAEntry.grid(row=3, column=1, sticky='ew', padx=2, pady=1)
    lawn.grid(row=4, column=0, sticky='w', padx=5)
    lawnEntry.grid(row=4, column=1, sticky='ew', padx=2, pady=1)
    electric.grid(row=0, column=2, sticky='w', padx=5)
    electricEntry.grid(row=0, column=3, sticky='ew', padx=2, pady=1)
    water.grid(row=1, column=2, sticky='w', padx=5)
    waterEntry.grid(row=1, column=3, sticky='ew', padx=2, pady=1)
    sewer.grid(row=2, column=2, sticky='w', padx=5)
    sewerEntry.grid(row=2, column=3, sticky='ew', padx=2, pady=1)
    garbage.grid(row=3, column=2, sticky='w', padx=5)
    garbageEntry.grid(row=3, column=3, sticky='ew', padx=2, pady=1)
    gas.grid(row=4, column=2, sticky='w', padx=5)
    gasEntry.grid(row=4, column=3, sticky='ew', padx=2, pady=1)
    expensesTotal.grid(row=5, column=0, sticky='ew', pady=5)
    expenseSubmitBtn.grid(row=6, columnspan=4, sticky='ew', padx=95)
    
#ROI GRID:
    downPayment.grid(row=0, column=0, sticky='w', padx=5)
    downPaymentEntry.grid(row=0, column=1, sticky='ew', padx=2, pady=1)
    closing.grid(row=1, column=0, sticky='w', padx=5)
    closingEntry.grid(row=1, column=1, sticky='ew', padx=2, pady=1)
    rehab.grid(row=2, column=0, sticky='w', padx=5)
    rehabEntry.grid(row=2, column=1, sticky='ew', padx=2, pady=1)
    otherInvest.grid(row=3, column=0, sticky='w', padx=5)
    otherInvestTypeEntry.grid(row=3, column=1, sticky='ew', padx=2, pady=1)
    otherInvestEntry.grid(row=3, column=2, sticky='ew', padx=2, pady=1)
    initialInvestTotal.grid(row=4, column=0, sticky='ew', pady=5)
    roiSubmitBtn.grid(row=5, columnspan=3, sticky='ew', padx=95)
    
    window.mainloop()



if __name__ == '__main__':
    main()


