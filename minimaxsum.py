def miniMaxSum(arr):
  minSum = float('inf')
  maxSum = 0
  for num in arr:
    #copy the array
    ArrayCopy = [*arr]
    #removing the element
    ArrayCopy.remove(num)
    #calculating sum
    sumValue = sum(ArrayCopy)
    #evaluating conditions
    if sumValue < minSum :
      minSum = sumValue
    if sumValue > maxSum :
      maxSum = sumValue
  print(minSum,maxSum)
  return