#funtion that allow me to reject everything but numbers
def numtest(x):
  if (not x.isnumeric()):
    return(True)

#input the need info, and run the program numtest
while(True):
  testScoreStr = input('Pls, enter your test score: ')
  
  if numtest(testScoreStr) == True:
    print('Test score is not valid, try again')
  else:break

while(True):
  classRankStr = input('Pls, enter your class rank: ')

  if numtest(classRankStr) == True:
    print('Class rank is not valid, try again')
  else:break

#combert the values to int 
testScore = int(testScoreStr)
classRank = int(classRankStr)

#outputs
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
