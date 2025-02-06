def roman1(romint):
    roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'I':1}
    resultinteger:0
    for i in range(0,len(romint)-1):
        if roman[romint[1]]<roman[romint[i+1]]:
            resultinteger-=roman[romint[i]]
        else:
            resultinteger+=roman[romint[i]]
    return resultinteger+roman[romint[-1]]  
roman=input("Enter a roman number") 
print("Answer: ",roman1(roman))       
  
