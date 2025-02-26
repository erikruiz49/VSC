# tax
STATE_TAX = 0.065
FEDERAL_TAX = 0.28
EMP_SALARY = 0.025

# input statements
salary = float(input('Pls, enter your salary: '))
numDependents = float(input('Pls, enter num of dependents: '))

# calculate taxes here

stateTaxNum = STATE_TAX * salary
federalTaxNum = FEDERAL_TAX * salary
dependentDeduction = (EMP_SALARY * numDependents) * salary
totalWithholding = stateTaxNum + federalTaxNum + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
