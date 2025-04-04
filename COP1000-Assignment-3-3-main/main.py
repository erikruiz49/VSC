# Function:     This program determines if a date entered by the user is valid.  
def numtest(x):
    if(not x.isnumeric()):
        return True

# Input:        Interactive

while(True):
    month = input('Pls, enter a month: ')

    if numtest(month) == True:
        print(f'{month} is not valid')
    else:break

while(True):
    day = input('Pls, enter a day: ')

    if numtest(day) == True:
        print(f'{day} is not valid')
    else:break

while(True):
    year = input('Pls, enter a year: ')

    if numtest(year) == True:
        print(f'{year} is not valid')
    else:break


# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31


# Get the year, then the month, then the day
# housekeeping()

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(f'{month}/{day}/{year} is a valid date')
    # Output statement
if validDate == False:
    print(f'{month}/{day}/{year} is an invalid date')
    # Output statement
