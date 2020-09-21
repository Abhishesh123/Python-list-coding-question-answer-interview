# Ways to remove duplicates from list
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i) 
 
print ("The list after removing duplicates : " + str(res)) 

 #==================2nd way======================================
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list))  
res = [] 
[res.append(x) for x in test_list if x not in res] 
print ("The list after removing duplicates : " + str(res)) 


#==============3rd way =========================================

test_list = [1, 5, 3, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(test_list)) 
test_list = list(set(test_list)) 

print ("The list after removing duplicates : " + str(test_list)) 