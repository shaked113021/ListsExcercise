
number_of_students = 25
grades_list = []

# input
for i in range(number_of_students):
    grade = int(input("Please Enter a grade for student No." + str(i + 1) + ": "))
    grades_list.append(grade)

# max, failure, and average calculation
grades_sum = 0
failure_counter = 0
max_grade = 0
max_counter = 0

for grade in grades_list:
    grades_sum += grade
    if grade > max_grade:
        max_grade = grade
        max_counter = 1
    elif grade == max_grade:
        max_counter += 1
    if grade < 55:
        failure_counter += 1

average_grade = grades_sum / number_of_students

# Printing results
print("Average grade: ", average_grade)
print("Number of failed students: ", failure_counter)
print("Max grade:", str(max_grade) + ".", max_counter, "students got it.")