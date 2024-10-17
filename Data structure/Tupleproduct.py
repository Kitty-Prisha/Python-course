def prod(val) : 
    res = 1
    for ele in val: 
        res *= ele 
    return res  
 

print("The original tuple is : " + str(test_tup)) 
 

res = prod(list(test_tup)) 
 
 
print("The product of tuple elements are : " + str(res)) 