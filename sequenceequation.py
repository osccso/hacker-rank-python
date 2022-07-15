def permutationEquation(p):
    #first create a copy of the array
    p_copy = p.copy()
    #sort the items (ascending)
    p_copy.sort()
    #for every item sorted find x = p(p(y)) or index(index(x)+1)+1
    y_list = []
    for p_element in p_copy:
        index_of_x =p.index(p_element)+1 
        y = p.index(index_of_x) + 1
        y_list.append(y)
    return y_list
    