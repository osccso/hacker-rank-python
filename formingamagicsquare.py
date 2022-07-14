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


                

def formingMagicSquare(s):
  
  def magic_squares_generator(seed):
    #you take a row and column with a common element as reference an from there you start generating all the different magic squares
    
    def column_permutation(array_2d):
        permutations = []
        for index in range(0,3):
            generated_array = []
            generated_array_reversed = []
            for row in array_2d:
                copy_row = row[index:] + row[:index]
                generated_array.append(copy_row)
            
            permutations.append(generated_array)
            for row in generated_array:
                copy_row = [num for num in reversed(row)]
                generated_array_reversed.append(copy_row)
            permutations.append(generated_array_reversed)
        
        return permutations
      
    def row_permutation(array_2d):
        permutations = []
        for index in range(0,3):
            generated_array = array_2d[index:] + array_2d[:index]
            permutations.append(generated_array)
            generated_array = [row for row in reversed(generated_array)]
            permutations.append(generated_array)
        return permutations
    
    def transpose(args):
      transpose_array = []
      for array in args:
          new_array = [[0,0,0] for i in range(0,3)]
          for i in range(0,3):
              for j in range(0,3):
                  new_array[i][j] = array[j][i]
          transpose_array.append(new_array)
      return transpose_array
    
        
    column_permutations = column_permutation(seed)
    all_magic_squares = []
    for array in column_permutations:
        all_magic_squares.extend(row_permutation(array))
    
    all_magic_squares_transposed = transpose(all_magic_squares)
   
    all_magic_squares += all_magic_squares_transposed
    
    return all_magic_squares
  
  def cost(square, magic_square):
      cost = 0
      for row_square,row_magic in zip(square,magic_square):
          for num_square, num_magic in zip(row_square,row_magic):
              cost += abs(num_magic - num_square)    
      return cost
  
  seed_given  = [[1,6,8],[9,2,4],[5,7,3]]
  magic_squares= magic_squares_generator(seed_given)
  
  cost_list = []
  for square in magic_squares:
      cost_list.append(cost(s, square))
  
  minimun_cost = min(cost_list)
  index_magic = cost_list.index(minimun_cost)
  print(index_magic)
  print(magic_squares[index_magic])
  return minimun_cost
  
  #now you create the other magic squares just through permutation

min_cost = formingMagicSquare([[4, 4, 7], [3, 1, 5], [1, 7, 9]])

print(min_cost)