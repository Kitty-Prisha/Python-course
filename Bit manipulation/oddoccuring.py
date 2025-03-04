def oddoccuring(arr):
    res=0
    for element in arr:
     res=res^element
    return res
arr=[2,2,4,4,1]
print(oddoccuring(arr))
