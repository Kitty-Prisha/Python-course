def tail(a,n):
 
 while n:
    n=int(input("Enter a number"))
    if(a>n):
        return
    print(a)
    tail(a,n)


 tail(a,n)  