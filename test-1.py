WOODS = ['oak', 'pine']

def count(start, end):
    while start:
        if input != woodType:  
            return True

woodType = input('Pls enter the wood type you want: ')

#for x in WOODS:
#    if count(x) != True:
#        print((f'{woodType} is not valid, pls try again'))

for x in WOODS: 
    if x == woodType:
        break
    elif x != woodType:
        continue
else:
    noValue = True
               
if noValue == True:
    print('no hay na')
else:
    print(woodType)
