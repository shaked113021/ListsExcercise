
list_1 = []
list_2 = []

# input for list_1

print("Enter 5 values for first list:")
for i in range(5):
    user_in = int(input("Enter a number: "))
    list_1.append(user_in)

# input for list_2

print("Enter 5 values for second list:")
for i in range(5):
    user_in = int(input("Enter a number: "))
    list_2.append(user_in)

# printing before swap
print("list_1: ", list_1)
print("list_2: ", list_2)

# swapping

for i in range(5):
    tmp = list_2[i]
    list_2[i] = list_1[i]
    list_1[i] = tmp

print("swapped")

# printing after swap
print("list_1: ", list_1)
print("list_2: ", list_2)

