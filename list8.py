# Exercise Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list

# Given List:

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# Sub List to be added = ["h", "i", "j"]

# Expected output:

# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

res=list1[2][1][2].extend(subList)
print(res)