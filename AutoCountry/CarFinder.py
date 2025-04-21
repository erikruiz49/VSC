#funtions
def inputCheck(input):
    if not input.isnumeric():
        return True
    if int(input) < 1 or int(input) > 5:
        return True

def search(input, list):
    if input in list:
        print(f'{input} is an authorized vehicle''\n')
    else:
        print(f'{input} is not an authorized vehicle, if you received this in error please check the spelling and try again''\n')

#list

with open('AutoCountry/DataBase.txt', 'r') as db:
    AllowedVehiclesListdb = [line.strip() for line in db.readlines()]
#menu
while(True):
    #call the database 
    with open('AutoCountry/DataBase.txt', 'w') as db:
        for vehicule in AllowedVehiclesListdb:
            db.write(vehicule + '\n')


    #menu
    print('********************************''\n'
          'AutoCountry Vehicle Finder v0.4''\n'
          '********************************''\n'
          'Please Enter the following number below from the following menu: ''\n'
          ' ''\n'
          '1. PRINT all Authorized Vehicles''\n'
          '2. SEARCH for Authorized Vehicles''\n'
          '3. ADD Authorized Vehicle''\n'
          '4. DELETE Authorized Vehicle''\n'
          '5. Exit''\n'
          '********************************''\n'
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
        for vehicule in AllowedVehiclesListdb:
            print(vehicule)

    #obtion 2
    if response == 2:
        carPick = input('Please Enter the full Vehicle name: ')
        search(carPick, AllowedVehiclesListdb)

    #obtion 3
    if response == 3:
        addNewValue = input('Please Enter the full Vehicle name you would like to add: ')
        AllowedVehiclesListdb.append(addNewValue)
        print(f'You have added "{addNewValue}" as an authorized vehicle''\n')
        
    
    #obtion 4
    if response == 4:
        removeValue = input('Please Enter the full Vehicle name you would like to REMOVE: ')
        if removeValue not in AllowedVehiclesListdb:
            print(f'{removeValue} is not in the Authorized Vehicles, please try again')
            continue
        verification = input(f'Are you sure you want to remove "{removeValue}" from the Authorized Vehicles List?\n')
        if verification.lower() == 'yes':
            AllowedVehiclesListdb.remove(removeValue)
        else:
            continue


    #obtion 5
    if int(response) == 5:
        break
    

#Exit path
print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
