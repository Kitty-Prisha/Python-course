n=int(input("Enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
    #floyd's triangle
rows=int(input("Enter the number of rows"))
num=1  
for i in range(1,rows+1):
    for j in range(1,i+1):
         print(num,end=" ") 
         num=num+1
    print()     