#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.speed(0)
x = -200
y = 0
xCord = 1
yCord = 1
while (x < 200):
  while (y < 100):
    x = x + xCord
    y = y + yCord
    painter.goto(x,y)
  yCord = -1
  while (y > 0):
    x = x + xCord
    y = y + yCord
    painter.goto(x,y)
  yCord = 1
while(x>-200):
    while (y > -100):
        x = x - xCord
        y = y - yCord
        painter.goto(x,y)
    yCord = -1
    while (y < 0):
        x = x - xCord
        y = y - yCord
        painter.goto(x,y)
    yCord = 1

wn = trtl.Screen()
wn.mainloop()