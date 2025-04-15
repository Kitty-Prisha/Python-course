import array as ar
def meanarray(arr,arraysize):
    totalsum=0
    for i in range(0,arraysize):
        totalsum+=i
    return(float(totalsum/arraysize))
def medianarray(arr,arraysize):
    sorted(arr)
    if arraysize%2!=0:
        return float(arr[int(arraysize/2)])
    return float((arr[int((arraysize-1)/2)] +

arr[int(arraysize/2)])/2.0)
arr=ar.array('i',[2,3,5,1,9])
arraysize=len(arr)
print(meanarray(arr,arraysize))
print(medianarray(arr,arraysize))