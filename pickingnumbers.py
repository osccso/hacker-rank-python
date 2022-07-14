

def pickingNumbers(a):

    list_transformed = [*a]
    list_transformed.sort()
    #get distinct elements
    list_distinct = set(list_transformed)
    register = []
    for num in list_distinct:
        diff = 0
        i = list_transformed.index(num)
        count = 0
        while diff <= 1:
            count += 1
            if not i <= len(list_transformed)-2:
              break
            i+=1
            diff = abs(num - list_transformed[i])
            
        register.append(count)
    return max(register)
  
input=[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66]

print(pickingNumbers(input))