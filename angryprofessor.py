def angryProfessor(k, a):
    students_ontime = list(filter(lambda x: x<=0, a))
    num_students_ontime = len(students_ontime)
    if num_students_ontime >= k:
      return 'NO'
    return 'YES'