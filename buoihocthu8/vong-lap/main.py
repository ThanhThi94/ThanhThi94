import turtle
import math
n = turtle.Turtle()
n.speed(10)

def vehinh(bien1):
    for i in range(2):
        n.circle(bien1, 90)
        n.circle(bien1 // 2, 90)

vehinh(100)


n.forward(100)
vehinh(200)



turtle.done()





