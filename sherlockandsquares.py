import math
def squares(a, b):
    n = 0
    #figure out the range of integer with corresponding squares in that range
    lower_bound = math.ceil(math.sqrt(a))
    upper_bound = math.floor(math.sqrt(b))
    
    if upper_bound < lower_bound:
        return n
    n = upper_bound -lower_bound + 1
    return n