def getTotalX(a,b):
  #get the maximun value of a
  maximum = max(a)
  #get the minimun value of b
  minimun = min(b)
  #find the numbers between the arrays
  count = 0
  for num in range(maximum,minimun+1):
    sumA = sum([num%i for i in a])
    sumB = sum([i%num for i in b])
    if sumA == 0 and sumB == 0:
      count += 1
  return count