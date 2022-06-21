import time
import numpy as np
from climbingtheleaderboarddataheavy import *
#optimized using different for loops
#instead of using append using extend instead
def climbingLeaderboard(ranked,player):
  #preallocating data for speed
  length = len(ranked)
  lengthPlayer = len(player)
  ranks = [0]*lengthPlayer
  rankedMatrix = [0]*length
  track = float('inf')
  rank = 0
  for index,score in enumerate(ranked) :
    if score < track:
      rank +=1
      track = score
    rankedMatrix[index] = rank
  #this is where the positions for the array are going be stored
  for count,score in enumerate(player) :
      for index,registered_score in enumerate(ranked) :
        if score >= registered_score :
          ranks[count]=rankedMatrix[index]
          break
        if score < registered_score and length == index+1:
          ranks[count]=rankedMatrix[index]+1
  return ranks  
start = time.time()
print(climbingLeaderboard(rankedArray,playerArray))
end = time.time()
elapsedTime = end-start
print('The time elapsed is:',elapsedTime,' in seconds')

    