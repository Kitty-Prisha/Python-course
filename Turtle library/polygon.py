import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsides=int(input("Enter the sides of the shape"))
length=int(input("Enter the length"))
angle=360/numsides
for i in range(numsides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()  

