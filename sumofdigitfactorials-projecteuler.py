import math
import fileinput
 
def f(n):
    numbers = [*str(n)]
    result = 0
    for number in numbers:
        result += math.factorial(int(number))
    return result
  
def sf(n):
    numbers = [*str(f(n))]
    result = 0
    for number in numbers:
        result += int(number)
    return result

def g(i):
    number = 1
    while True:
        if sf(number) == i:
            break
        number += 1
    return number

def sg(i):
    numbers = [*str(g(i))]
    result =  0
    for number in numbers:
        result += int(number)
    return result

def ssg(n, m):
    result = 0
    for i in range(1, n + 1):
        result += sg(i)
    return result % m
   
def main():
    input_list = []
    for index, line in enumerate(fileinput.input()):
        if index != 0:
            array_input = line.split(' ')
            input_list.append({"n": int(array_input[0]), "m": int(array_input[1])})
    for input in input_list:
        print(ssg(input['n'], input['m']))
    
print(ssg(50, 200))

