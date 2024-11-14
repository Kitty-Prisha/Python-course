class circle:
    def __init_subclass__(self):
       radius=" "
       answer=" "
    def Radius(self):
        radius=int(input("Enter the radius"))
    def Answer(self):
        answer=radius*radius*3.14  
    def printresult(self):
        print("The area of the circle is ",self.answer)
radius=circle()     
radius.Radius()
radius.Answer()
radius.printresult    

