def countApplesAndOranges(s,t,a,b,apples,oranges):
  #define a count
  countApples = 0
  countOranges = 0
  for distance in apples:
    fallsAt = a + distance
    if fallsAt >= s and fallsAt <= t:
      countApples += 1
      
  for distance in oranges:
    fallsAt = b + distance
    if fallsAt >= s and fallsAt <= t:
      countOranges += 1
  
  return print("%d\n%d" % (countApples,countOranges))