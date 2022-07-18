def appendAndDelete(s, t, k):
    #calculate amount of moves required to change s into t
    #chek till what point s ant t are equal or if they are not
    answer = 'Yes'
    s_length = len(s)
    t_length = len(t)
    minor_length = min(s_length, t_length)
    first_difference = minor_length
    for index in range(minor_length):
        if s[index] != t[index]:
          first_difference = index
          break
    #calculate  minimun amount of moves
    n_to_remove = s_length - first_difference
    n_to_add = t_length - first_difference
    #total minimun number of moves
    total = n_to_remove + n_to_add
    if total > k:
        answer = 'No'
        return answer
    #generate possibles sequences in case you have to delete the first string beyond the difference
    start_sequence = s_length - first_difference
    end_sequence = (s_length - start_sequence) * 2 + t_length - first_difference
    sequence = [i + t_length - first_difference for i in range(start_sequence, end_sequence+1, 2)]
    if k <= end_sequence and k not in sequence:
        answer = 'No'
        return answer
    return answer
  
result = appendAndDelete('abcd','abcdert',10)
print(result)
