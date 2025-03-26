def tail(a,num):
    if(a>num):
        return
    print(a)
    tail(a+1,num)
n=int(input("Enter a number"))
tail(1,n)   
