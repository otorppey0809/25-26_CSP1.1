# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

#spider body
spider.pensize(40)
spider.circle(20)

#spider legs
num_of_legs = 8
length_of_legs = 90
z = 360 / num_of_legs
spider.pensize(5)
n = 0
while (n < num_of_legs):
  spider.goto(-2, 10)
  spider.setheading(z * n)
  spider.forward(length_of_legs)
  n = n + 1
spider.penup()

spider.goto(0, 10)
spider.pendown()
spider.pencolor('red')
spider.pensize(5)
spider.circle(1)
spider.penup()
spider.goto(-25, 10)
spider.pendown()
spider.pencolor('red')
spider.pensize(5)
spider.circle(2)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()