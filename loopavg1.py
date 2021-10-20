student_heights = input("Input a list of students heights").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  # print(student_heights)
total_height=0
for height in student_heights:
    total_height += height
#print(total_height)

# number_of_students = len(student_heights)
# avg_height = round(total_height/number_of_students)
# print(avg_height)

# the commented code (10-12 lines)is using without for loop now the code is implemented by for loop

no_of_student = 0
for student in student_heights:
    no_of_student += 1
   # print(no_of_student)
    avg_height = round(total_height / no_of_student)
print(avg_height)

highest_height= 0
for height in student_heights:
    if height > highest_height:
        highest_height = height
print(f" the heihtest height is {highest_height}")