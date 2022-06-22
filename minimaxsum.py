def miniMaxSum(arr):
  minSum = float('inf')
  maxSum = 0
  for num in arr:
    #copy the array
    ArrayCopy = [*arr]
    ArrayCopy.remove(num)
    sum(ArrayCopy)