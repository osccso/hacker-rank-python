def kangaroo(x1,v1,x2,v2):
  condition = 1
  #the second kangaroo will always be ahead of kangaroo 1 x2 > x1
  positionKangaroo1 = x1
  positionKangaroo2 = x2
  answer = 'NO'
  if v1 > v2:
    while positionKangaroo1 <= positionKangaroo2:
      if positionKangaroo1 == positionKangaroo2:
        answer = 'YES'
      positionKangaroo1 += v1
      positionKangaroo2 += v2 
  return answer