def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("Please enter the letter of ur choice")
print("a.addition")
print("b.subtraction")
print("c.multiplication")
print("d.division")
choice=input("Enter the letter of your choice")
num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
if choice=="a":
    print(add(num1,num2))
elif choice=="b":
    print(subtract(num1,num2))
elif choice=="c":
    print(multiply(num1,num2))
else:
    print(divide(num1,num2))              