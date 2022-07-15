def beautifulDays(i, j, k):
    reverse = lambda num : int(str(num)[::-1]) #reversing string and casting it back to integer
    count = 0
    
    for day in range(i,j+1):
        reversed_day = reverse(day)
        difference = abs(day - reversed_day)
        if difference % k == 0:
            count += 1
    
    return count
    