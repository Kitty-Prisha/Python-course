def sumofarray(a):
    length=len(a)
    if length==1:
        return a[0]
    return a[0]+ sumofarray(a[1:])
a=[1,2,3,5]
print(sumofarray(a))
