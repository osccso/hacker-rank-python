def diagonalDifference(arr):
  #find row length
  rows = len(arr)
  #find column length
  columns = len(arr[0])
  #checks if it is an squared matrix
  if rows != columns:
    print('It is not a squared matrix')
    return
  #left to right diagonal
  leftToRight = []
  for i,row in enumerate(arr):
    for j,num in enumerate(row):
      if i == j:
        leftToRight.append(num)        
  sumLeftToRight = sum(leftToRight)
  #right to left diagonal
  rightToLeft = []
  for i,row in enumerate(arr):
    for j,num in enumerate(row):
      if i == rows-j-1:
        rightToLeft.append(num)        
  sumRightToLeft = sum(rightToLeft)
  print(sumLeftToRight)
  print(sumRightToLeft)
  result = abs(sumLeftToRight-sumRightToLeft)
  return result

diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]])