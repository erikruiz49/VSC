#funtion
def checkInput(x):
    if(not x.isnumeric()):
        return (f'{x} is not a numerical value')
    if(int(x) > 10 or int(x) < 1):
        return (f'{x} is not a valid number')
    return (f'The number is {x}')

#input
response = input('pls, enter a number between 1 and 10: ')

print(checkInput(response))
