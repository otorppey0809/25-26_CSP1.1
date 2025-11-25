import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("green")

line = 4

while (line % 2 != 2):
  painter.goto(0,0)
  painter.right(50)
  painter.forward(90)
  painter.pendown()
  painter.circle(line)
  painter.penup()
  line = line + 1
  if (line % 18 == 0):
    painter.color('blue')
  if (line % 36 == 0):
    painter.color('red')
  if (line % 41 == 0):
    painter.color('green')
  if (line % 67 == 0):
    painter.color('gold')
wn = trtl.Screen()
wn.mainloop()
