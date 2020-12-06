#   a116_ladybug.py
import turtle as trtl


ladybug = trtl.Turtle()

loop = 6 
length = 70#configure legs
angle = 360 / loop
ladybug.pensize(5)
i = 0 
while (i < loop):
  ladybug.goto(0,-10)
  ladybug.setheading(angle * i)
  ladybug.forward(length)#Draw legs
  i = i + 1

ladybug.pensize(40)
ladybug.penup()
ladybug.goto(0, 30)
ladybug.pendown()
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(-10, -35) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(5, 15)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -40
ladybug.pensize(10)




# draw two sets of dots
ladybug.pensize(10)
while (num_dots <= 2 ):
  ladybug.penup()
  if (num_dots == 1):
    ladybug.goto(xpos, ypos)
  else:
    ypos = ypos + 20
    xpos = xpos + 5
    ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()