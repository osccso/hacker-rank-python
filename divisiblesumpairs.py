def divisibleSumPairs(n,k,ar):
  i = 0
  count = 0
  while i < n-1:
    j = i
    while j < n:
      if j != i:
        if (ar[i]+ar[j])%k == 0:
          count += 1
      j +=1
    i +=1
  return count
    
  