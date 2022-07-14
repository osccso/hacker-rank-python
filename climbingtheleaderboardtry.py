import math
import time
import math

def climbingLeaderboard(ranked,players):
  #using quicksort concept
  #Getting unique items and sorting list
  listRanked = list(set(ranked))
  listRanked.sort(reverse=True)
  #define variables
  ranks = []
  length = len(listRanked)
  factor = 1
  #define partitions
  if length >= 10:
    factor = math.log(length,1.1)
  chunk_size = math.ceil(length/factor)
  partitions = [([listRanked[i],listRanked[i:i+chunk_size][-1]],[i,i+chunk_size-1]) for i in range(0,length,chunk_size)]
  #getting ranges and indexes for partitions
  list_ranges = []
  list_indexes = []
  for part in partitions:
    list_ranges.extend(part[0])
    list_indexes.extend(part[1])
  length_range = len(list_ranges)
  #organizing players
  for player in players:
    for i in range(0,length_range):
      if player >= list_ranges[i] :
        if i == 0:
          ranks.append(1)
          break
        else:
          j = list_indexes[i-1]
          while player < listRanked[j]:
            j += 1
          ranks.append(j+1)
          break
      elif i != length_range-1:
        continue
      else:
        ranks.append(length+1)
        break
  return ranks
start = time.time()
rankedArray = [100, 100, 50, 40, 40, 20, 10]
playerArray = [5, 25, 50, 120, 0]
result = climbingLeaderboard(rankedArray,playerArray)
with open('text2.txt', 'w') as f:
  for rank in result:
    f.write(f'{str(rank)}\n')
end = time.time()
elapsedTime = end-start
print('The time elapsed is:',elapsedTime,' in seconds')
    