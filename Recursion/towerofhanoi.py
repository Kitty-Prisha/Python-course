def Hanoi(n,a,b,c):
    if(n==1):
        print("Move this from rod",a,"To rod",b)
        return
    Hanoi(n-1,a,c,b)
    print("Move this from rod",a,"To rod",c)
    Hanoi(n-1,c,b,a)
n=4
Hanoi(n,'a','c','b')    