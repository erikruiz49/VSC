# taxes
# TAX_RATE

CALI_TAX_RATE = 0.13
RATE_OF_DEDUCTION = 2000

def calculate_tax(tax_rate):
     # calculate net income (gross_income * TAX_RATE)
    tax_bill = gross_income * tax_rate

    # calculate rate of deduction  
    dependent_deduction = RATE_OF_DEDUCTION * num_of_dependents 

    # calculate tax subtotal
    tax_subtotal = tax_bill - dependent_deduction

# get dependents
num_of_dependents = float(input('Please enter the number of dependents: '))

# get gross income 
gross_income = float(input('Please enter the gross income: '))

# get state
state_code = input('Please enter your two digit state code: ')

if(state_code == 'CA'):
    # print tax subtotal
    print(f'Your final tax bill is ${calculate_tax(0.13)}')
else:
    print(f'Your state does not have an income tax, time to plan a vacation')

# calculate tax home