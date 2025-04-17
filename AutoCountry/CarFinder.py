#funtions

def inputCheck(input):
    if not input.isnumeric():
        return True
    if int(input) < 1 or int(input) > 4:
        return True

def search(input, list):
    if list.__contains__(input):
        print(f'{input} is an authorized vehicle''\n')
    else:
        print(f'{input} is not an authorized vehicle, if you received this in error please check the spelling and try again''\n')

#menu
while(True):
    #call the database 
    with open('AutoCountry/DataBase.txt', 'r') as db:
        AllowedVehiclesList = db.read()
    #menu
    print('********************************''\n'
          'AutoCountry Vehicle Finder v0.2''\n'
          '********************************''\n'
          'Please Enter the following number below from the following menu: ''\n'
          ' ''\n'
          '1. PRINT all Authorized Vehicles''\n'
          '2. SEARCH for Authorized Vehicles''\n'
          '3. ADD Authorized Vehicle''\n'
          '4. Exit''\n'
          )
    #input
    response = input('Your number is: ')
    
    #check if the value is correct 
    if inputCheck(response) == True:
        print('The enter value is not a valid number, please try again')
        continue
        
    response = int(response)

    #obtion 1
    if response == 1:
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ')
        print(AllowedVehiclesList)

    #obtion 2
    if response == 2:
        carPick = input('Please Enter the full Vehicle name: ')
        search(carPick, AllowedVehiclesList)

    #obtion 3
    if response == 3:
        addNewValue = input('Please Enter the full Vehicle name you would like to add: ')
        with open('AutoCountry/DataBase.txt', 'a') as db: 
            db.write(f'{addNewValue}''\n')
        print(f'You have added "{addNewValue}" as an authorized vehicle''\n')

    if int(response) == 4:
        break
    

#Exit path
print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')