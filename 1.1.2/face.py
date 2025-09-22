# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

painter.pensize(3)
painter.penup()
painter.goto(150,-200)
painter.pendown()
painter.circle(250)
painter.penup()
painter.goto(0,0)
painter.pendown()
painter.circle(50)
painter.circle(25)
painter.penup()
painter.forward(150)
painter.pendown()
painter.circle(50)
painter.circle(25)
painter.penup()
painter.goto(0,-50)
painter.right(90)
painter.pendown()
painter.circle(100,180)
# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()