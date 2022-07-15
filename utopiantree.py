def utopianTree(n):
    if n == 0:
      return 1
    if n % 2 == 0:
      return utopianTree(n -1) + 1
    else:
      return utopianTree(n-1)*2