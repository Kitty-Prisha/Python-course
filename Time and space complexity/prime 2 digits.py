from math import sqrt
num=int(input("Enter a number"))
if num>10:
    for i in range(10,int(sqrt(num))+1):
        if num%i==0:
            print(num, "is not a prime number" )
            break
    else:
        print(num,"is a prime number")
else:            
    print("Please enter a number greater than 10")    