import math
def powerset(set,setsize):
    powersubset=int (math.pow(2,setsize))
    outer=0
    inner=0
    for outer in range(0,powersubset):
        for inner in range(0,setsize):
            if((outer&(1<<inner))>0):
                print(set[inner],end=" ")
        print()        

n=int(input("Enter your array size"))
set=[]
for i in range(0,n):
    a=int(input("Enter your element"))
    set.append(a)
powerset(set,n)




