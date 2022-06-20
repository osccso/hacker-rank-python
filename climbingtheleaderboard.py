import time
# from climbingtheleaderboarddata import *
from climbingtheleaderboarddataheavy import *

def climbingLeaderboard(ranked,player):
  #check if the ranked leader board is valid
  comparingString = ranked.copy()
  comparingString.sort(reverse = True)
  length = len(ranked)
  if comparingString != ranked :
    return print('String not properly ranked')
  #creates the ranks for the ranked matrix
  rankedMatrix = []
  track = float('inf')
  rank = 0
  for score in ranked :
    if score < track:
      rank +=1
      track = score
    rankedMatrix.append(rank)
  #this is where the positions for the array are going be stored
  ranks = []
  for score in player :
      for index,registered_score in enumerate(ranked) :
        if score >= registered_score :
          ranks.append(rankedMatrix[index])
          break
        if score < registered_score and length == index+1:
          ranks.append(rankedMatrix[index]+1)
      
  return ranks
start = time.time()
print(climbingLeaderboard(rankedArray,playerArray))
end = time.time()
elapsedTime = end-start
print('The time elapsed is:',elapsedTime,' in seconds')
#not optimized some test did fail

   
    