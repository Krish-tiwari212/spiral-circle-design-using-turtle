import turtle
import random
from turtle import Turtle, Screen
clr = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
# tim1 = timmy.pos()
# print(tim1)
# a = 3
# while a!= 9:
#     timmy.forward(100)
#     timmy.right((360/a))
#     if abs(timmy.pos()) < 1:
#         d = random.randint(0, len(clr)-1)
#         timmy.color(clr[d])
#         a += 1
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c = (r, g, b)
    return c

# def draw_shape(sides):
#     angle = 360/sides
#     for i in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for a in range(3,11):
#     draw_shape(a)
#     timmy.color(random.choice(clr))
a = True
timmy.speed("fastest")


def spiro(size):
    for i in range(360 // size):
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size)
        timmy.color(rand_color())

spiro(5)






screen = Screen()
screen.exitonclick()
