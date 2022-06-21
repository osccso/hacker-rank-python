import time
from climbingtheleaderboarddataheavy import *
#optimized using different for loops
#instead of using append using extend instead
def climbingLeaderboard(ranked,player):
  ranks = [0]*len(player)
  #convert list to dict and then back to list
  for i,given in enumerate(player):
    ranks[i] = sorted(list(dict.fromkeys([*ranked,given])),reverse=True).index(given)+1
  return ranks
start = time.time()
print(climbingLeaderboard(rankedArray,playerArray))
end = time.time()
elapsedTime = end-start
print('The time elapsed is:',elapsedTime,' in seconds')

    