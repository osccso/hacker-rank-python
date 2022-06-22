from math import remainder


def gradingStudents(grades):
  #according to rules you round the grades
  #preallocating grades
  roundedGrades = [0]*len(grades)
  for index,grade in enumerate(grades):
    if grade >= 38:
      remainder = grade % 5
      if remainder > 2:
        roundedGrades[index] = grade + (5-remainder)
        continue
    roundedGrades[index] = grade
  return roundedGrades  