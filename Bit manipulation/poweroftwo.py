def poweroftwo(number):
    if number<=0:
        return False
    return(number&(number-1))==0
number=int(input("Enter a number"))
if (poweroftwo(number)):
    print("Its a power of two")
else:
    print("Its not a power of two")    
