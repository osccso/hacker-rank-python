def numCells(grid):
  def validate(g,x,y,r,c):
    condition = True
    combinations = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for combination in combinations:
      if x + combination[0] < 0 or x + combination[0] > r -1 or y + combination[1] < 0 or y + combination[1] > c -1:
        continue
      if g[x][y] <= g[x + combination[0]][y + combination[1]] :
        condition = condition and False
        break
    return condition
  
  dominantCount = 0
  rows = len(grid)
  columns = len(grid[0])
  for i,row in enumerate(grid) :
    for j,value in enumerate(row):
      # left top corner
      cond = validate(grid,i,j,rows,columns)
      if cond :
        dominantCount += 1
  
  
  return dominantCount

