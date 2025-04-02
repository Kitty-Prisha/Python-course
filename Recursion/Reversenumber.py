def reversenum(num):
    if(num>=0):
        last=num%10
        if(num//10>0):
            currentnumber=reversenum((int)(num//10))
            return last*pow(10,len(str(currentnumber)))+currentnumber
        return num
n=int(input("Enter a number"))
print(reversenum(n))    
        