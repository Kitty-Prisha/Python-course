def arrlargest(a):
    length=len(a)
    if length==1:
        return a[0]
    return max(a[0],arrlargest(a[1:]))
a=[3,45,769,987,27]
print(arrlargest(a))