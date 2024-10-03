try:
    num,num1=eval(input("Enter two numbers seperated by commas"))
    result=num/num1
    print("The result is ",result)
except ZeroDivisionError:
    print("You divided the number by zero") 
except SyntaxError:
    print("Wrong syntax")
finally:
    print("This is the final output")           