def rotate1(a,asize,n):
    for i in range(n):
        rotate(a,asize)
def rotate(a,asize):
    temp=[0]
    for i in range(asize-1):
        a[i]=a[i+1]
    a[asize-1]=temp
def printarray(a,asize):
    for i in range(asize):
        print("%d"%a[i],end=" ")
    print("\n")
a=[23,42,67,89,12]
printarray(a,len(a))
rotate1(a,2,len(a))
printarray(a,len(a))