def matchword(words):
    ctr=0
    lst=[]
    for word in words:
        if (len(word)>1 and word[0]==word[-1]):
            ctr=ctr+1
            lst.append(word)
    print("The list is now,",lst)
    return ctr
count=matchword(["abc","bcb","cfc"])  
print(count)  
