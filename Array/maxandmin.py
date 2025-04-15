import array as arr
def mini(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=min(temp,a[i])
    return temp
def maxi(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=max(temp,a[i])
    return temp
a=[1,3,45,76,543,9]
size=len(a)
print("Maximum array is ",maxi(a,size))
print("Minimum array is ",mini(a,size))
    