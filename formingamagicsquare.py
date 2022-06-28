# Observing the problem we can try to solve it in the following way
# first generate all possible permutations that are a valid magic square
# then compare them to the given grid and find the minimun 'cost'

#We observe that the total sum of the numbers of the magic square is 45 which means every row or column amounts to 15

#then we notice that all the permutations are gonna be formed with the following sets which sum is 15 : {1,5,9} , {2,4,9} , {5,3,7} , {1,8,6}, {4,3,8}, {2,7,6}

##calculating the permutations every row or column has a total of 6 ways of ordering ie. {1,5,9},{5,1,9},{5,9,1},{9,5,1},{9,1,5},{1,9,5}

#and for every permutation there are just two ways to arrange the other rows (columns) ie.

# 9 5 1         9 5 1
# 4 3 8    and  2 7 6
# 2 7 6         4 3 8

#and finally there are six ways a set can be arranged in the magic square
#three of them correspond to row direction and the other three correspond to column direction

#the total of magic squares we have is 6 x 2 x 6 = 72

#preallocating the array  
from copy import copy

magicSquares = [[[0,0,0],[0,0,0],[0,0,0]]]*72
seed  = [[1,6,8],[9,2,4],[5,7,3]]
seedT = [[1,9,5],[6,2,7],[8,4,3]]

def permute(seed,array):
  #columns flag == 'col'
  for column in range(0,3):
    #for every column in the given seed we generate

def magicSqGen(result):
  # this is the base
  result[0] = [[1,6,8],[9,2,4],[5,7,3]]
  #now you create the other magic squares just through permutation
  