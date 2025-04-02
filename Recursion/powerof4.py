n=int(input("Enter a number")) 
def powerfour(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%4==0):
        return powerfour(n/4)
    return False

if(powerfour):
    print("This number is a power of four")  
else:
    print("This number is not a power of four")    