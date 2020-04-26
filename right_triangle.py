import turtle
import math
a = float(input("Enter base length: "))
b = float(input("Enter Height length: "))
c = ((a*a)+(b*b)) ** 0.5
radians = math.atan(a/b)
degrees = math.degrees(radians)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(180 - (degrees))
turtle.forward(c)
turtle.hideturtle()
turtle.done()