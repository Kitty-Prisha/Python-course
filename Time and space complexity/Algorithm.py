#first method
def func1(n):
    return n*(n+1)/2
print(func1(4))
#second method
def func2(j):
    sum=0
    for i in range(1,j+1):
        sum=sum+i
    return sum
print(func2(4))
#third method
def func3(k):
    sum=0
    for i in range(1,1+k):
        for j in range(1,i+1):
            sum=sum+1
    return sum
print(func3(4))
