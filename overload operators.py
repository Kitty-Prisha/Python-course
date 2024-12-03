class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "Object 1 is less than object 2"
        else:
            return "Object 2 is less than Object 1"
    def __eq__(self,other):
        if(self.a==other.a):
            print("they both are equal")
        else:
            print("they are not equal")
ob1=A(8)
ob2=A(9)
print("Passed values",ob1.a,ob2.a)
print(ob1.a, "is less than",ob2.a)                
        
            

