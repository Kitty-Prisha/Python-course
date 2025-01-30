def printnumber(n):
    iteration=0
    print(n)
    iteration=iteration+1
    print(iteration)
printnumber(10)
#O(n)Time
def time(n):
    iteration=0
    for i in range(1,n+1):
        print(n)
        iteration=iteration+1
    print(iteration)
time(10) 
#O(n^2)
def time2(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
    
            print("*",end=" ")
            iteration=iteration+1
        print(" ")
    print(iteration)
time2(10)            


