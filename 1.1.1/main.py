import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(2.5)
painter.pensize(5)
painter.pencolor('red')

painter.forward(200)
painter.right(90)
painter.pencolor('green')
painter.forward(200)
painter.right(90)
painter.speed(1)
painter.pencolor('blue')
painter.forward(200)
painter.right(90)
painter.pencolor('yellow')
painter.forward(200)
painter.speed(2)
painter.right(90)
painter.pencolor('cyan')
painter.forward(200)
painter.right(90)
painter.pencolor('magenta')
painter.forward(200)
painter.right(90)
painter.pencolor('orange')
painter.forward(200)
painter.right(90)
painter.pencolor('pink')
painter.forward(200)


wn = trtl.Screen()
wn.mainloop()

