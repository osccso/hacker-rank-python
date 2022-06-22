def breakingRecords(scores):
  #define minimun and maximun
  minimun = float('inf')
  maximun = 0
  maxBroken = -1
  minBroken = -1
  for score in scores:
    if score < minimun:
      minimun = score
      minBroken += 1
    if score > maximun or score == 0:
      maximun = score
      maxBroken +=1
      
  return [maxBroken,minBroken]