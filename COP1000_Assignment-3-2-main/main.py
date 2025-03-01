#Function: This program determines if a student will be admitted or rejected.

#Input:  Interactive

#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank

def numtest(x):
  if (not x.isnumeric()):
    return(True)

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

testScore = int(testScoreStr)
classRank = int(classRankStr)

# Test using admission requirements and print Accept or Reject

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
