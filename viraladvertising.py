import math
def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for day in range(1,n+1):
        liked = math.floor(shared/2)
        shared = liked * 3
        cumulative += liked
        
    return cumulative

print(viralAdvertising(3))