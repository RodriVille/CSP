import turtle as trtl 

painter = trtl.Turtle()
painter.speed(1000)
i = 0

<<<<<<< HEAD
i = 0
while (i < 19):
    painter.forward(20)
    painter.right(20)
    i = i + 1

=======
#Stem
painter.right(90)
painter.penup()
painter.goto(0, -150)
painter.pendown()
painter.color("green")
painter.pensize(10)
painter.forward(200)
painter.penup()
painter.goto(0,0)
painter.right(270)
painter.color("black")
painter.pensize(1)

painter.goto(0,0)
while (i < 18):
    painter.penup()
    painter.forward(20)
    painter.right(20)
    painter.pendown()
    painter.begin_fill()
    painter.circle(20)
    i = i + 1
    if (i % 2 == 0):
        painter.fillcolor("Yellow")
        painter.end_fill()
    else:
        painter.fillcolor("red")
        painter.end_fill()
painter.goto(0, -20)
s = 0
while (s < 10):
    painter.penup()
    painter.forward(20)
    painter.right(35)
    painter.pendown()
    painter.begin_fill()
    painter.circle(20)
    s = s + 1
    if (s % 2 == 0):
        painter.fillcolor("purple")
        painter.end_fill()
    else:
        painter.fillcolor("orange")
        painter.end_fill()
painter.goto(0, -45)
g = 0
while (g < 7):
    painter.penup()
    painter.forward(15)
    painter.right(60)
    painter.pendown()
    painter.begin_fill()
    painter.circle(20)
    g = g + 1
    if (g % 2 == 0):
        painter.fillcolor("green")
        painter.end_fill()
    else:
        painter.fillcolor("blue")
        painter.end_fill()
>>>>>>> b9b7eb46840677cdf1081621661400c3a50d2683

painter.penup()
painter.goto(0, -250)
painter.pensize(20)
painter.pencolor("green")
painter.pendown()
painter.circle(60, 40)

wn = trtl.Screen()
wn.mainloop()