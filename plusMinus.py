def plusMinus(arr):
  lengthArray = len(arr)
  countPositive = 0
  countNegative = 0
  countZeros = 0
  for num in arr:
    if num < 0 :
      countNegative += 1
    elif num > 0:
      countPositive += 1
    else:
      countZeros += 1
  print('%6f' % countPositive/lengthArray)
  print('%6f' % countNegative/lengthArray)
  print('%6f' % countZeros/lengthArray)