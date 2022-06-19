def designerPdfViewer(h, word):
    #cheks if the length of h is right
    if len(h) != 26 :
      return print('wrong list length it should be 26')
    wordLength =  len(word)
    highest = 0
    for i in word :
      index = ord(i)-97
      if index < 0 and ord(i) > 25:
        return print('only lower case letters')
      if  h[index] > highest :
        highest = h[index]
      
    return highest*wordLength
      

print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],'abc'))