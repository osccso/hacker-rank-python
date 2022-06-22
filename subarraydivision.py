def birthday(s,d,m):
  matching = 0
  for index,number in enumerate(s):
    if sum(s[index:index+m]) == d:
      matching += 1
  return matching