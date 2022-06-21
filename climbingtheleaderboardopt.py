import time
from climbingtheleaderboarddata import *
#optimized using different for loops
#instead of using append using extend instead
def climbingLeaderboard(ranked,player):
  #convert list to set
  #and convert back to list
  listRanked = list(dict.fromkeys(ranked))
  #preallocate for speed
  rankedLength = len(listRanked)
  playerLength = len(player)
  ranks = [0]*playerLength
  count = 0
  for score in player:
    countinner = 1
    if score < listRanked[-1]:
      ranks[count] = rankedLength+1
      count += 1
      continue
    for data in listRanked:
      if score >= data:
        ranks[count] = countinner
        break
      countinner += 1
    count += 1  
  return ranks
start = time.time()
print(climbingLeaderboard(rankedArray,playerArray))
end = time.time()
elapsedTime = end-start
print('The time elapsed is:',elapsedTime,' in seconds')

    