def numberofbit(n):
    zeros=0
    ones=0
    while(n):
        if(n&1==1):
            ones=ones+1
        else:
            zeros=zeros+1
        n>>=1
    print("There are ",zeros," zeros and ",ones, "Ones")
number=int(input("Enter a number"))
print(bin(number))
numberofbit(number)    