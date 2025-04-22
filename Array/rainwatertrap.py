def rainwater(arr,asize):
    
    lefttallest = [0] * asize
    righttallest = [0] * asize
    totalwater=0
    lefttallest[0]=arr[0]
    for i in range(1,asize):
        lefttallest[i]=max(lefttallest[i-1],arr[i])
    
    righttallest[asize-1] = arr[asize -1]

    for i in range(asize -2, -1, -1):

        righttallest[i] = max(righttallest[i +1], a[i])
        
    for i in range(0, asize):

      totalwater += min(lefttallest[i], righttallest[i]) - a[i]


    return totalwater

a = [0,1,0,2,1,0,1,3,2,1,2,1]

bars = len(a)

print("water : ", rainwater(a, bars))
