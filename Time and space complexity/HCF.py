largenumber=int(input("Enter a large number"))
smallnumber=int(input("Enter a small number"))
while(smallnumber):
    numberstore=smallnumber
    smallnumber=largenumber%smallnumber
    largenumber=numberstore
print(largenumber)    