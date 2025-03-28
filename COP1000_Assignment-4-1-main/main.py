
# Declare and initialize variables here.
def numtest(input):
    if(not input.isnumeric()):
        return False

def listCheck(input, list):
    for x in list: 
        if x == input:
            return True
        elif x != input:
            continue



WOODS = ['oak', 'pine']
COLORS = ['black','whith','gold']


# Charge for this sign.
CHARGE = 35.00
# Number of characters.
while(True):
    numChars = input('Pls enter the number of characters you want: ')
    if numtest(numChars) == False:
        print(f'{numChars} is not a number, pls try again')
    else:break

numChars = int(numChars)

if numChars > 5:
    numChars = numChars - 5 
    chargeChars = numChars * 4
else:
    chargeChars = 0

# Type of wood.
while(True):
    woodType = input('Pls enter the wood type you want: ')
    if listCheck(woodType, WOODS) == True:
        break
    else:
        print(f'{woodType} is not valid, pls try again')

if woodType == 'oak':
    chargeWood = 20
elif woodType == 'pine':
    chargeWood = 0


# Color of characters.
while(True):
    color = input('Pls enter the the color you want: ')
    if listCheck(color, COLORS) == True:
        break
    else:
        print(f'{color} is not valid, pls try again')


if color == 'gold':
    chargeColor = 15
elif color == 'white' or color == 'black':
    chargeColor = 0

# Write assignment and if statements here as appropriate.

charge = CHARGE + chargeChars + chargeColor + chargeWood

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
