def numCells(grid):
  dominantCount = 0
  rows = len(grid)
  columns = len(grid[0])
  for i,row in enumerate(grid) :
    for j,value in enumerate(row):
      # left top corner
      if i == 0 and j == 0 :
        cond1 = value > grid[i+1][j]
        cond2 = value > grid[i+1][j+1]
        cond3 = value > grid[i][j+1]
        cond = cond1 and cond2 and cond3
      #right top corner
      elif i == 0 and j == columns-1:
        cond1 = value > grid[i+1][j]
        cond2 = value > grid[i+1][j-1]
        cond3 = value > grid[i][j-1]
        cond = cond1 and cond2 and cond3
      # left bottom corner
      elif j == 0 and i == rows -1:
        cond1 = value > grid[i-1][j]
        cond2 = value > grid[i-1][j+1]
        cond3 = value > grid[i][j+1]
        cond = cond1 and cond2 and cond3
      # right bottom corner
      elif i == rows -1 and j == columns -1 :
        cond1 = value > grid[i-1][j]
        cond2 = value > grid[i-1][j-1]
        cond3 = value > grid[i][j-1]
        cond = cond1 and cond2 and cond3
      # top border
      elif i == 0 :
        cond1 = value > grid[i][j-1]
        cond2 = value > grid[i+1][j-1]
        cond3 = value > grid[i+1][j]
        cond4 = value > grid[i+1][j+1]
        cond5 = value > grid[i][j+1]
        cond = cond1 and cond2 and cond3 and cond4 and cond5
      #left border
      elif j == 0 :
        cond1 = value > grid[i-1][j]
        cond2 = value > grid[i-1][j+1]
        cond3 = value > grid[i][j+1]
        cond4 = value > grid[i+1][j+1]
        cond5 = value > grid[i+1][j]
        cond = cond1 and cond2 and cond3 and cond4 and cond5
      #right border
      elif j == columns - 1 :
        cond1 = value > grid[i-1][j]
        cond2 = value > grid[i-1][j-1]
        cond3 = value > grid[i][j-1]
        cond4 = value > grid[i+1][j-1]
        cond5 = value > grid[i+1][j]
        cond = cond1 and cond2 and cond3 and cond4 and cond5
      #bottom border
      elif i == rows - 1 :
        cond1 = value > grid[i][j-1]
        cond2 = value > grid[i-1][j-1]
        cond3 = value > grid[i-1][j]
        cond4 = value > grid[i-1][j+1]
        cond5 = value > grid[i][j+1]
        cond = cond1 and cond2 and cond3 and cond4 and cond5
      #interior
      else :
        cond1 = value > grid[i][j-1]
        cond2 = value > grid[i-1][j-1]
        cond3 = value > grid[i-1][j]
        cond4 = value > grid[i-1][j+1]
        cond5 = value > grid[i][j+1]
        cond6 = value > grid[i+1][j+1]
        cond7 = value > grid[i+1][j]
        cond8 = value > grid[i+1][j-1]
        cond = cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8
      if cond :
        dominantCount += 1
        print(i,j)
    
  return dominantCount    