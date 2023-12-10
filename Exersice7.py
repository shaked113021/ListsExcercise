
salaries = []

# salary inputs
for i in range(8):
    salary = int(input("Enter the salary for employee " + str(i + 1) + ":"))
    salaries.append(salary)

# average, min, and max calculation
salaries_sum = 0

min_salary = -1
min_counter = 0

max_salary = -1
max_counter = 0

for salary in salaries:
    salaries_sum += salary
    # checking if salary is smaller than min or at starting value
    if salary < min_salary or min_salary == -1:
        min_salary = salary
        min_counter = 1
    # append counter if needed
    elif min_salary == salary:
        min_counter += 1
    # checking if salary is larger than max_salary
    if salary > max_salary:
        max_salary = salary
        max_counter = 1
    # append counter if needed
    elif max_salary == salary:
        max_counter += 1

average_salary = salaries_sum / 8

# printing average, min, and max
print("average: ", average_salary)

print('min: ', min_salary, end=', ')
if min_counter > 1:
    print("appeared multiple times.")
else:
    print("appeared once.")

print('max: ', max_salary, end=', ')
if max_counter > 1:
    print("appeared multiple times.")
else:
    print("appeared once.")