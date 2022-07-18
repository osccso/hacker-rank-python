
import math
import time


def jumpingOnClouds(c, k):
    #calculate the length of the sequence
    n = len(c)
    #generates the sequence until landing in cloud 0
    energy_level = 100
    sequence = []
    if k != n:
        sequence.append(c[k])
        i = k
    else: 
        sequence.append(c[0])
        i = 0
    print(i)
    while i != 0:
        i = (i + k) % n
        print(i)
        # time.sleep(3)
        sequence.append(c[i])
    print(sequence)
    for cloud in sequence:
        #now check the sequence and keep track of energy level
        energy_level -= 1
        if cloud == 1:
            energy_level -= 2
    return energy_level

result = jumpingOnClouds([1,1,1,0,1,1,0,0,0,0], 3)
print(result)