def circularArrayRotation(a, k, queries):
    #first rotate the array according to the parameter k
    #findout startig index
    n = len(a)
    starting_index = k % n
    rotated_array = list([0 for i in range(n)])
    rotated_array[starting_index:] = a[0 : n - starting_index]
    rotated_array[:starting_index] = a[n - starting_index : ]
    results = []
    for query in queries:
        result = rotated_array[query]
        results.append(result)
    
    return results