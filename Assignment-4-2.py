#Funtions
def bonusCalc(input):
    if input <= 30:
        return 50
    if input >= 31 and input <= 69:
        return 75
    if input >= 70 and input <= 199:
        return 100
    if input >= 200:
        return 200

def numTest(input):
    if(not input.isnumeric()):
        return True

#Inputs

#check if it is a name
while(True):
    employeeName = input('Pls enter your name: ')
    if numTest(employeeName) != True:
        print(f'{employeeName} is not a valid name, pls try again')
    else:break

#check if it is a number
while(True):
    numShifts = input('Pls enter the number of shift worked: ')
    if numTest(numShifts) == True:
        print(f'{numShifts} is not a number, pls try again')
    else:
        numShifts = int(numShifts)
        break
while(True):
    numTrans = input('Pls enter the number of transitions: ')
    if numTest(numTrans) == True:
        print(f'{numTrans} is not a number, pls try again')
    else:
        numTrans = int(numTrans)
        break
while(True):
    transDollarValue = input('Pls enter the transaction dollar value: ')
    if numTest(transDollarValue) == True:
        print(f'{transDollarValue} is not a number, pls try again')
    else:
        transDollarValue = float(transDollarValue)
        break




#Calculations
productivityScore = (transDollarValue / numTrans) / numShifts

bonus = float(bonusCalc(productivityScore))

#Outputs

print(f'Employee name: {employeeName}')
print(f'Employee bonus: ${bonus}')