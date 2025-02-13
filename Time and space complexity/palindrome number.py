number=int(input("Enter a number"))
originalnumber=number
reversednumber=0
while originalnumber>0:
    digits=originalnumber%10
    reversednumber=reversednumber*10+digits
    originalnumber//=10
if number==reversednumber:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")        
