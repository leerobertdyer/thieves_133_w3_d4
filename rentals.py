class ROI():
    def __init__(self):
        self.expenses = {}
        self.others = {}
        self.laundry = ''
        self.storage = ''
        self.rent = ''
        self.otherAmount = ''
        self.totalIncome = 0
        self.totalExpense = 0
        self.annualCashFlow = 0
        self.downPay = 0
        self.closing = 0
        self.rehab = 0
        self.totalInvestment = 0
        
    def findIncome(self):
        while type(self.rent) != int:
            try:
                self.rent = int(input('How much do you make in rent each month?\n'))
            except:
                print("Please enter a number...")    
        while True:
            checkIncome = input("Do your tenants pay you for [L]aundry, [S]torage, or any [O]ther services? \n(If not, type [N]...)").lower()          
            if checkIncome == "l":
                while type(self.laundry) != int:
                    try:
                        self.laundry = int(input("How much do you make on your laundry?\n[0] to cancel..."))
                    except:
                        print('Please enter a number...')
            elif checkIncome == 's':
                while type(self.storage) != int:
                    try:
                        self.storage = int(input("How much do you make on your storage?\n[0] to cancel..."))
                    except:
                        print('Please enter a number...')
            elif checkIncome == 'o':
                other = input("What is the source of your other income?\n")
                while type(self.otherAmount) != int:
                    try:
                        self.otherAmount = int(input(f'How much do you make on your {other}?\n[0] to cancel...'))
                        self.others[other] = self.otherAmount
                    except:
                        print('Please enter a number...')
                self.otherAmount = ''
            elif checkIncome == 'n':
                self.totalIncome = self.rent
                print('\nGreat! According to our information, your income is:')
                if type(self.laundry) == int:
                    self.totalIncome += self.laundry
                    print(f'\tLaundry Services: ${self.laundry}\n')
                if type(self.storage) == int:
                    self.totalIncome += self.storage
                    print(f'\tStorage Facilities: ${self.storage}')
                for key,val in self.others.items():
                    if key:
                        self.totalIncome += val
                        print(f'\t{key}: ${val}')
                
                print(f'\t\t\tTotal Income = ${self.totalIncome}')
                break
            
    def findExpenses(self):
        while True:
            try:
                print("For the following enter 0 on those you don't pay for: \n")
                mort = int(input("\tWhat is your Mortgage? "))
                tax = int(input("\tWhat do you pay for Housing Tax? "))
                insurance = int(input("\tWhat do you pay for insurance? "))
                HOA = int(input("\tWhat do you pay for Home Owners Association? "))
                lawn = int(input("\tWhat do you pay for lawn/snow care? "))
                
                self.expenses["Mortgage"] = mort
                self.expenses["Tax"] = tax
                self.expenses['Insurance'] = insurance
                self.expenses["Home Owners Association Fees"] = HOA
                self.expenses["Lawn Care"] = lawn
                
                checkUtil = ''
                while checkUtil !='y' and checkUtil != 'n' and checkUtil != 'yes' and checkUtil != 'no':
                    checkUtil = input("Do you pay for utilities? (y/n)\n").lower()
                if checkUtil == 'y' or checkUtil == 'yes':
                    electric = int(input("\tWhat do you pay for Electric? "))
                    water = int(input("\tWhat do you pay for Water? "))
                    sewer = int(input("\tWhat do you pay for Sewer? "))
                    garbage = int(input("\tWhat do you pay for Garbage? "))
                    gas = int(input("\tWhat do you pay for Gas? "))
                    self.expenses["Electric"] = electric
                    self.expenses["Water"] = water
                    self.expenses["Sewer"] = sewer
                    self.expenses["Garbage"] = garbage
                    self.expenses["Gas"] = gas
                print("\nLooking at your inputs, your expenses are:")
                for k,v in self.expenses.items():
                    if v > 0:
                        print('\t', k, v)
                        self.totalExpense += v
                cut = self.totalIncome * .05
                print(f'We\'ve included a 5% vacancy fund of {cut}')
                print(f'As well as a repair fund of {cut}')
                print(f'A CapEx of {cut} for when that Heater blows...')
                print(f'And we had to pay your Prop MGMT team {cut*2}\n')
                self.totalExpense += (cut*5)
                print('So in summary:')
                print(f'\t\tTotal Income = {self.totalIncome}')
                print(f'\t\tTotal Expenses = {self.totalExpense}')
                cashFlow = self.totalIncome - self.totalExpense
                self.annualCashFlow = cashFlow * 12
                print(f'\t\tMonthly cash flow = ${cashFlow}') 
                break   
            except:
                print("Please only enter numbers...")
    
    def findROI(self):
        own = ''
        while True:
            try:
                self.downPay = int(input("How much is your downpayment? "))
                self.closing = int(input("How much were closing costs? "))
                self.rehab = int(input("How much did you spend rehabilitating the property? "))
                self.otherInitial = int(input("How much did you spend on other initial investments? (0 for none) "))
                self.totalInvestment = self.downPay + self.closing + self.rehab + self.otherInitial
                print(f"\t\tInitial Investment: ${self.totalInvestment}")
                print(f"\t\tAnnual Cashflow: ${self.annualCashFlow}")
                print(f"\t\tTotal ROI: %{self.annualCashFlow/self.totalInvestment*100}")
                break
            except:
                print("Please enter a number...")
                        
                
    def runner(self):
        print("\n\n\n\n\n\n\n\n\n\n********ROI_Calculator***********\n\nWelcome to Lee's Wacky ROI calculator! Let's Calculate!\n")
        self.findIncome()
        print("\nNow let's focus on expenses...\n")
        self.findExpenses()
        print("\nAnd finally, let's consider your Initial Investment, to find your ROI:")
        self.findROI()
                        
# Given:
# rent 2000, tax 150, insur 100, util 0, hoa 0, lawn 0, vac 100, rep 100, capEx 100, MGMT 200, MORT 860, 40000 down, 3000 closing, 7000 rehab, yields 9.36 percent
# My main gripe is with UX. I tried using a try block for every single input, but that is both annoying to read through, but also
# didn't work how I wanted, as it would skip over the input if it wasn't an int. So I'd have to wrap each input in a while loop AND a try block
# Which just seems too ridiculous. Wonder if there's a good solution for this... Time to sleep
run = ROI()
run.runner()