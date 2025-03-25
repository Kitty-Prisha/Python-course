def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(6) 
print(result)
print("The time compleity is O(n)") 
def printnumbers(n):
    if(n<=10):
        print(n)
        printnumbers(n+1)
    else:
        return
printnumbers(1)
print("The time complexity is O(n)")  