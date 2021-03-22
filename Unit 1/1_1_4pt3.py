import turtle as trtl

painter = trtl.Turtle()

painter.shape("circle")
painter.hideturtle()
painter.penup()
#ok
y = 200
x = -200
while (x < 200):
    x = x + 50
    y = 200
    painter.goto(x, y)
    if (x == - 150):
        painter.color("cyan")
    else:
        painter.color("magenta")
    painter.stamp()
    while (y > 0):
        y = y - 50
        painter.goto(x, y)
        painter.stamp()

wn = trtl.Screen()
wn.mainloop()