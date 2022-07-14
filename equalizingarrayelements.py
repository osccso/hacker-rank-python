def minOperations(arr, threshold, d):
    # Write your code here
    length = len(arr)
    def n_length_combo(lst, n):
          if n == 0:
              return [[]]
          
          l =[]
          for i in range(0, len(lst)):
              
              m = lst[i]
              remLst = lst[i + 1:]
              
              remainlst_combo = n_length_combo(remLst, n-1)
              for p in remainlst_combo:
                  l.append([m, *p])
                
          return l
    n = 1
    condition = True
    while condition:
        list_combo = n_length_combo(arr,n)
        for element in list_combo:
            copy_element = element.copy()
            for index, num in enumerate(element):
                copy_element[index] = int(element[index]/d)
            
            for element in copy_element:
                if copy_element.count(element) == threshold:
                    condition = False
                    break
            
            if not condition:
                break
            else:
                n += 1
    return n
          
    

        