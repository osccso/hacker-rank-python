import time
#defining combinations with a while
def combinations(k, n):
    '''
    combinations(k, n), k number of elements to combine from n elements
    using while and the following logic.
    selected: *
    not selected: x
    The items are at a fixed position
    ***...**xxx...xx
    the idea is to move the items from the position above to the next position
    xxx...xx***...**
    move one at a time from left to right starting from the right-most element and once it reaches the right move the next element to the left, repeat the process until all items can't move
    '''
    #function that will do all the actions needed every iteration
    # FUNC BLOCK #
    def next_iteration():
        #tick count
        add = 1
        #number of positions
        k = len(counters)
        for index, (counter, state, cycle) in enumerate(zip(counters, status, cycle_status)):
            if state == 0 and cycle != 0:
                #reset the status of the counter
                cycle_status[index] -= 1
                status[index] = number_positions - (cycles[index] - cycle_status[index])
            if counter < state:
                counters[index] += add
                add = 0
            elif counter == state and index == k - 1:
                counters[index] = 0
                status[index] = 0
                add = 0
            elif counter == state and state != 0:
                counters[index] = 0
                counters[index + 1] += add
                status[index] -= 1
                add = 0
            if add == 0:
                break
        reverse_counters = [*counters]
        reverse_counters.reverse()
        accumulate = 0
        for i, (count, index)  in enumerate(zip(reverse_counters, indexes)):
            accumulate += count
            indexes[i] = i + accumulate
    #  END FUNC BLOCK #
    #create a copy of the elements
    n_copy = n.copy()
    #sort the elements in ascending order
    n_copy.sort()
    #get the length of the array of all elements
    length = len(n)
    #every element has the same number of positions available to move
    number_positions = length - k
    #start the counter from zero because the counter will be used to reference the index for each element
    counters = [0]*k
    #conter status
    status = [number_positions]*k
    print(status)
    #cicles
    cycles = [sum([j for j in range(1,i+1)]) for i in reversed(range(1,k+1))]
    #cicle status
    cycle_status = [*cycles]
    #indexes to be accessed every iteration
    indexes = [i for i in range(k)]
    #combination's list 
    list_combinations= []
    #generate all combinations
    while any(status) or list_combinations[-1] != [4, 5, 6, 7]:
        list_combinations.append(list(map(n.__getitem__,indexes)))
        next_iteration()
        # time.sleep(3)
        print(cycle_status , status , counters,list(map(n.__getitem__,indexes)))
    
    return list_combinations
result = combinations(4, [1,2,3,4,5,6,7])
print(result)
print(len(result))