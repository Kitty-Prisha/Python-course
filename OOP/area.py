class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print("The area of the square is ",self.side**2)
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("The area of circle is ",3.14*self.radius*self.radius)
objsquare=square(5)
objcircle=circle(3)
for i in (objsquare,objcircle):
    i.area()

                

        
        