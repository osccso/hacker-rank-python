with open('text2.txt','r') as f, open('comparethis2.txt','r') as f2:
  for line, line2 in zip(f, f2):
    if line != line2:
      print(line, line2)
      print('not equal')
      break