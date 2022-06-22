def staircase(n):
  i = 1
  while i <= n:
    space = ' '*(n-i)
    step = '#'*i
    print(space+step) 
    i += 1