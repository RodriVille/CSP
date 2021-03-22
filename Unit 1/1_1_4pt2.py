import turtle as trtl

painter = trtl.Turtle()

painter.shape("circle")
painter.hideturtle()
painter.penup()

y = 200
x = -200
while (x < 200):
    x = x + 50
    y = 200
    painter.goto(x, y)
    painter.color("cyan")
    painter.stamp()
    while (y > 0):
        y = y - 50
        painter.goto(x, y)
        painter.color("blue")
        painter.stamp()

wn = trtl.Screen()
wn.mainloop()