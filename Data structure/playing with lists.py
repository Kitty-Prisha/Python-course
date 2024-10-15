lists=[2,3,1,5,6,8]
print("The original list is",lists)
count=0
for i in lists:
    count+=i
avg=count/len(lists)
print("Sum = ",count)
print("average= ",avg)
lists.sort()
print("Smallest element is:",lists[0])
print("Largest element is:",lists[-1])