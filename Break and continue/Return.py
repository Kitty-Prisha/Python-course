def money(a,b):
    return b-a
a=int(input("Enter the amount of money that the shopkeeper asked for"))
b=int(input("You didnt have change, enter the number of money you paid instead"))
print("The change the shopkeeper gives you is: ",money(a,b))