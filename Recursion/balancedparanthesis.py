def paren(s,l,r,p,n):
    if p==2*n:
        for ss in s:
            print(ss,end=' ')
        print("\n")
        return
if l<n:
    s[p]=='('
    paren(s,l+1,r,p+1,n)
        
