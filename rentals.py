## Write a program that calculates Rental Property ROI
# Using Object Oriented Programming 

#four square method:

#INCOME:
    #top left box
    #Rental income
    #laundry machine
    #storage
    #misc
        #xample: DUPLEX $1000/each/month
                           #total monthly income = $200

#XPENSES:
    #Bottom Left Box
    #Tax - 150
    #Insurance - 100
    #Utilities - 0
        #electric 
        #water
        #sewer
        #garbage
        #gas
    #HOA FEES - 0
    #Lawn/snow care - 0
    #Vacancy  - 5% / (100)
    #repairs - 100
    #CapEx (new roof/heater/etc...) 100 
    #Prop MGMT - 10% / 200/month
    #Mortgage: 860
                          #TOTAL MONTHLY XPENSES = $1610
        
#Cash Flow
    #Top Right Box
    #Income - Xpenses
        #2000-1610
        # MONTHLY CASH FLOW: 390 * 12 = YEARLY CASH FLOW 4680

#Cash On Cash ROI
    #is your money earning a good percent?
    #Downpayment - 40,000
    #closing costs - 3000
    #rehab budget - 7000
    #misc other - 0
        #total investment:  - 50k
        #yearly cashflow = 4680
        #Yearly cashflow divided by total investment:
                             # 4690/50000  ROI = 9.36%
    

class ROI():
    def __init__(self):
        self.houseCost = 0
        self.income = 0
        self.expenses = 0

    def income(self):
        rent = ''
        others = {}
        while type(rent) != int:
            try:
                int(input('How much do you make in rent each month?\n'))
            except:
                print("Please enter a number...")    
        while True:
            checkIncome = input("Do your tenants pay for [L]aundry, [S]torage, or any [O]ther services? \n(If not, type [N]...)").lower()
            if checkIncome == "l":
                laundry = ''
                while type(laundry) != int:
                    try:
                        laundry = int(input("How much do you make on your laundry?\n[0] to cancel..."))
                    except:
                        print('Please enter a number...')
            elif checkIncome == 's':
                storage = ''
                while type(storage) != int:
                    try:
                        storage = int(input("How much do you make on your storage?\n[0] to cancel..."))
                    except:
                        print('Please enter a number...')
            elif checkIncome == 'o':
                other = input("What is the source of your other income?\n")
                otherAmount = ''
                while type(otherAmount) != int:
                    try:
                        otherAmount = int(input(f'How much do you make on your {other}?\n[0] to cancel...'))
                        others[{other}] = otherAmount
                    except:
                        print('Please enter a number...')
            elif checkIncome == 'n':
                totalIncome = 0
                if laundry:
                    totalIncome += laundry
                if storage:
                    totalIncome += storage
                for key,val in others.items():
                    if key:
                        totalIncome += val
                print(f'Based on your input, your Total Income = {totalIncome}')
                break

