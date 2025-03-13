#This is Arithmetic operator
a=int(input("Enter a number"))
b=int(input("Enter another number"))
print("Your number:", a, b)
a=a+b
b=a-b
a=a-b
print("Swaped numbers:", a, b)
#Binary operaor
def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("Swaped numbers",a, b)
a=int(input("Enter your number"))
b=int(input("Enter another number"))
print(bin(a))
print(bin(b))
swap(a,b)    