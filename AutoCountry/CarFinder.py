#funtions
def listCheck(input, list):
    #Happy path output
    if int(input) == 1:
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ')
        for i in list:
            print(i)

def inputCheck(input):
    if not input.isnumeric():
        return True
    if int(input) < 1 or int(input) > 2:
        return True

        


#list
AllowedVehiclesList = ['Ford f-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

#menu
while(True):
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')
    print('Please Enter the following number below from the following menu: ')
    print('')
    print('1. PRINT all Authorized Vehicles')
    print('2. Exit')
    print('')

    #input
    response = input('Your number is: ')
    print('')

    if inputCheck(response) == True:
        print('The enter value is not a valid number, please try again')
        continue

    listCheck(response, AllowedVehiclesList)
    if int(response) == 2:
        break
    

#Exit path
print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')