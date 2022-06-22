import time
from climbingtheleaderboarddataheavy import *
#optimized using different for loops
#instead of using append using extend instead
#algorithm for climbing the leaderboard optimized for speed
#time complexity O(n)
#space complexity O(n)
def climbingLeaderboard(ranked,player):
  playerLength = len(player)
  #create dict from list and back to list (get rid of repeated items)
  listRanked = list(dict.fromkeys(ranked))
  rankedLength = len(listRanked)
  ranks = [0]*playerLength
  j = 0
  while j < playerLength:
    i = 0
    while i < rankedLength:
      if player[j] > ranked[i]:
        break
      i += 1
    ranks[j] = i+1
    j += 1
  return ranks
start = time.time()
print(climbingLeaderboard(rankedArray,playerArray))
end = time.time()
elapsedTime = end-start
print('The time elapsed is:',elapsedTime,' in seconds')
    