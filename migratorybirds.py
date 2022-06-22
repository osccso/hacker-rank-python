def migratoryBirds(arr):
  #finding the most frequently sighted birds
  #transform the array to a set in order to get unique elements
  listUnique = list(dict.fromkeys(arr))
  #sorting the list
  listUnique.sort()
  id = 0 #there're just 1,2,3,4 and 5 types
  maxappearances = 0
  for bird in listUnique:
    #counting the amount of appearances
    appearances = sum([bird == i for i in arr])
    if appearances > maxappearances:
      maxappearances = appearances
      id = bird
  return id