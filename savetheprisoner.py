import math
def saveThePrisoner(n, m, s):
    #create the list of chairs that is going to be the same as prisoners there are
    remain = m % n
    end_chair = s + remain - 1
    if end_chair > n:
        end_chair = end_chair - n
    if remain == 0 and s == 1:
        end_chair =  n
    return end_chair  
  
inputs = []
solutions_given = []
with open('savetheprisonerdata.txt','r') as f, open('prisonersolution.txt','r') as s:
    for line in f:
      input = line.split()
      input = [int(number) for number in input]
      inputs.append(input)
    
    for line in s:
      solutions_given.append(int(s.readline()))
solutions = []
for input in inputs:
    solutions.append(saveThePrisoner(*input))
    
#compare solutions
i = 0
for f_solution, s_solution in zip(solutions,solutions_given):
    if f_solution != s_solution:
        print('This solution is wrong', f_solution, s_solution , inputs[i])
    i += 1
