# Exercise Question 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

# list1 = [5, 10, 15, 20, 25, 50, 20]

# Expected output:

# list1 = [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)