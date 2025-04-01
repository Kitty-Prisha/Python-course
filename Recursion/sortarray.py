def sorted(a):
    length=len(a)
    if length==0 or length==1:
        return True
    return a[0]<=a[1] and sorted(a[1:])
a=[1,2,3,7,9]
if sorted(a):
    print("List is sorted")
else:
    print("List is not sorted")    
