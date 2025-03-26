def head(a,num):
    if(a>num):
        return
    print(a)
    head(a+1,num)
    print(a)
n=int(input("Enter a number"))
head(1,n)