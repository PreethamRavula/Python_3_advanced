from roster import student_roster
import itertools
from classroom_organizer import ClassroomOrganizer

num = 0
student_roster_iterator = iter(student_roster)
for i in range(10):
  print(next(student_roster_iterator), "\n")

# Student Roll call:
print("Student roll call:\n")
classroom = ClassroomOrganizer()
for students in classroom:
  print(students)

# comibations of 2 students in each table
combination_tuples_1 = classroom.table_organizer(student_roster)
for combination in combination_tuples_1:
  num += 1
  print("\n",combination)
print("\nThe total number of combinations with 2 students per table are", num)

# Math and science students:
print("\nAfter school program students:\n")
math_students = classroom.get_students_with_subject("Math")
science_students = classroom.get_students_with_subject("Science")
special_subjects = itertools.chain(math_students, science_students)
special_subjects_list = list(special_subjects)
special_subject_combinations = itertools.combinations(special_subjects_list, 4)
print(list(special_subject_combinations))
