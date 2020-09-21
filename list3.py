# Exercise Question 3: Given a Python list. Turn every item of a list into its square

# aList = [1, 2, 3, 4, 5, 6, 7]
# Expected output:[1, 4, 9, 16, 25, 36, 49]


alist = [1,2,3,4,5,6,7]
output =  [x * x for x in alist]
print(output)