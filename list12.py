# Python | Count occurrences of an element in a list
#=================1st way ==========================
def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 
  
# Driver Code 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x))) 


#Method 2 (Using count())

def countX(lst, x): 
	return lst.count(x) 

# Driver Code 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x))) 

#Method 2 (Using Counter())
from collections import Counter 

# declaring the list 
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5] 

# driver program 
x = 3
d = Counter(l) 
print('{} has occurred {} times'.format(x, d[x])) 


