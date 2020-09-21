# Exercise Question 4: Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resList = [x+y for x in list1 for y in list2]
print(resList)