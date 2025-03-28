
# Declare and initialize variables here.
def numtest(input):
    if(not input.isnumeric()):
        return True
    else:
        return False





# Charge for this sign.
charge = 35.00
# Number of characters.
while(True):
    numChars = input('Pls enter the number of characters you want: ')
    if numtest(numChars) == True:
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
    if numtest(woodType) == False:
        print(f'{woodType} is not valid, pls try again')
    else:break


if woodType == 'oak':
    chargeWood = 20
else:
    chargeWood = 0


# Color of characters.
color = input('Pls enter the the color you want: ')

if color == 'gold':
    chargeColor = 15
else:
    chargeColor = 0

# Write assignment and if statements here as appropriate.

charge = charge + chargeChars + chargeColor + chargeWood

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
