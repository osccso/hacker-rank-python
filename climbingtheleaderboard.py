from audioop import reverse


def climbingLeaderboard(ranked,player):
  #check if the ranked leader board is valid
  comparingString = ranked.sort(reverse = True)
  if comparingString != ranked :
    return print('String not properly ranked')
  #this is where the positions for the array are going be stored
  ranks = []
  for score in player :
      for index,registered_score in enumerate(ranked) :
        if index == 0 :
          rank = 1
        else :
          if registered_score > ranked[index-1]:
            rank += 1
        if score > registered_score :
          ranks.append(rank)
          break
  return ranks
          

   
    