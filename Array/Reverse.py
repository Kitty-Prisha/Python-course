def reverse(a,asize,n):
    temp=0
    while(temp<asize):
        start=temp
        end=min(temp+n-1,asize-1)
        while start<end:
            a[start],a[end]=a[end],a[start]
            start+=1
            end-=1
        temp+=n
a=[1,2,4,56,43,23]
n=2
asize=len(a)
reverse(a,asize,n)
for i in range(0,asize):
    print(a[i],end=' ')            
