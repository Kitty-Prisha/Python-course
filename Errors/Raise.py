age=int(input("Enter your age"))
if not type(age):
    raise TypeError("Sorry you had a type error")
try:
    age1=int(input("Enter your age again"))
except SyntaxError:
    print("You have a Syntax error")
except ValueError:
    print("You have a Value error")    
finally:
    print("Your age is ",age)        

