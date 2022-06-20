def climbingLeaderboard(ranked,player):
  #check if the ranked leader board is valid
  comparingString = ranked.sort(reverse = True)
  length = len(ranked)
  if comparingString != ranked :
    return print('String not properly ranked')
  #this is where the positions for the array are going be stored
  ranks = []
  print('im here')
  for score in player :
      print(score)
      for index,registered_score in enumerate(ranked) :
        if index == 0 :
          rank = 1
        else :
          if registered_score > ranked[index-1]:
            rank += 1
        if score > registered_score :
          ranks.append(rank)
          break
        if score < registered_score and length == index+1:
          rank +=1
          ranks.append(rank)
  print(ranks+' - > this is ranks')
  return ranks
  
  climbingLeaderboard([100,100,50,40,40,20,10],[5,25,50,120])


   
    