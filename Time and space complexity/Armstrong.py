number=int(input("Enter a number"))
length=len(str(number))
temps=number
resultnumber=0
while temps>0:
    digits= temps%10
    resultnumber=resultnumber+digits**length
    temps//=10
if number==resultnumber:
    print("This is an armstrong number")
else:
    print("This is not an armstrong number")        

