def combinatorics(k, n):
    """_summary_

    Args:
        k (_int_): size of the combining group
        n (_list_): amount of element to be combined
    """
    # available positions
    free_positions = len(n) - k
    counters = [0]*k
    indexes = [i for i in range(k)]
    list_combinations = [list(map(n.__getitem__,indexes))]
    temp_positions = free_positions
    # -------------------------------------------------
    while counters[-1] < free_positions:
        add = 1
        for index, counter in enumerate(counters):
            #calculating the amount of free positions
            if index != k -1:
                temp_positions = free_positions - sum(counters[index + 1 : ])
            else:
                tem_positions = free_positions - counters[-1]
            
            if counter < temp_positions:
                counters[index] += add
                add = 0
            elif counter == temp_positions and index != k - 1 and temp_positions != 0:
                counters[index] = 0
                counters[index + 1] += add
                add = 0
            
            if add == 0:
              break
        #calculating the indexes

        counter_copy = counters.copy()
        counter_copy.reverse()
        accumulate = 0
        for i, (count, index)  in enumerate(zip(counter_copy, indexes)):
            accumulate += count
            indexes[i] = i + accumulate
        #append the elements to the combinatorics
        list_combinations.append(list(map(n.__getitem__,indexes)))
    # -------------------------------------------------
    return list_combinations
result = combinatorics(7,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])