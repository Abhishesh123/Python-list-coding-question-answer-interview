# # Python | Convert a nested list into a flat list
#      Input : l = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
#     Output : l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#     Input : l = [[[‘item1’, ‘item2’]], [[‘item3’, ‘item4’]]]
#     Output : l = [‘item1’, ‘item2’, ‘itm3, ‘item4”]


# Python code to flat a nested list with 
# multiple levels of nesting allowed. 

# input list 
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 

# output list 
output = [] 

# function used for removing nested 
# lists in python. 
def reemovNestings(l): 
	for i in l: 
		if type(i) == list: 
			reemovNestings(i) 
		else: 
			output.append(i) 

# Driver code 
print ('The original list: ', l) 
reemovNestings(l) 
print ('The list after removing nesting: ', output) 
