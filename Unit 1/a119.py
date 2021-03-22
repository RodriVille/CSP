import turtle as trtl

painter = trtl.Turtle()
painter.speed(50)
painter.pensize(5)

loop = 0
spiral = 3
objectList = ["Background", "Mountains", "grass", "sun", "building", "roof", "door", "person", "turtle"]

for thing in objectList:
    if thing == "Background":
        painter.goto(0, -500)
        painter.color("cyan")
        painter.fillcolor("cyan")
        painter.begin_fill()
        painter.circle(1000)
        painter.end_fill()
    elif thing == "Mountains":
        painter.penup()
        xcord = -500
        ycord = 0
        painter.goto(xcord, ycord)
        painter.pensize(100)
        painter.color("brown")
        painter.fillcolor("brown")
        painter.pendown()
        painter.begin_fill()
        while xcord < 400:
            painter.goto(xcord, ycord)
            painter.goto(xcord + 100, ycord + 100)
            painter.goto(xcord + 200, ycord)
            xcord += 200
        
        painter.goto(-500, 0)
        painter.end_fill
    elif thing == "sun":
        painter.penup()
        painter.goto(-100, 300)
        painter.pendown()
        painter.pensize(40)
        painter.color("yellow")
        painter.circle(20)#create painter body
        loop = 10
        angle = 360 / loop
        i = 0
        painter.pensize(10)
        while (i < loop):
            painter.goto(-100, 315)
            if(i % 4 == 0):
                painter.setheading(angle * i)
            painter.pendown()
            painter.circle(50, 90)#Draw legs
            painter.penup()
            i = i + 1
    elif thing == "grass":
        painter.color("green")
        painter.goto(0, -2000)
        painter.fillcolor("green")
        painter.begin_fill()
        painter.circle(1000)
        painter.end_fill()
    elif thing == "building":
        painter.color("orange")
        painter.pensize(5)
        painter.penup()
        painter.goto(100, -100)
        painter.pendown()
        i = 0
        painter.begin_fill()
        painter.right(18)
        while (i < 4):
            painter.forward(300)
            painter.right(90)
            i += 1
        painter.end_fill()
    elif thing == "door":
        painter.color("brown")
        painter.penup()
        painter.goto(200, -50)
        painter.pendown()
        i = 0
        painter.begin_fill()
        while (i < 4):
            painter.forward(40)
            painter.right(90)
            if i% 2 == 1:
                painter.forward(40)
            i += 1
        painter.end_fill()
    elif thing == "roof":
        painter.color("maroon")
        painter.penup()
        painter.goto(100, 200)
        painter.pendown()
        painter.begin_fill()
        painter.goto(250, 300)
        painter.goto(400, 200)
        painter.goto(100, 200)
        painter.end_fill()
    elif thing == "person":
        painter.color("black")
        painter.penup()
        painter.goto(-300, -100)
        painter.pendown()
        painter.begin_fill()
        painter.circle(20)
        painter.end_fill()
        painter.left(90)
        painter.forward(20)
        painter.left(90)
        painter.forward(100)
        painter.right(180)
        painter.forward(50)
        painter.right(60)
        painter.forward(30)
        painter.right(180)
        painter.forward(30)
        painter.right(60)
        painter.forward(30)
        painter.right(180)
        painter.forward(30)
        painter.right(60)
        painter.forward(50)
        painter.right(60)
        painter.forward(50)
        painter.right(180)
        painter.forward(50)
        painter.right(60)
        painter.forward(50)
        painter.right(180)
        painter.forward(30)
        painter.right(60)
    elif thing == "turtle":
        painter.penup()
        painter.goto(100, -200)
        painter.pendown
        painter.color("cyan")
        painter.shape("turtle")
        painter.speed(1)
        painter.goto(-100, -200)
        

wn = trtl.Screen()
wn.mainloop()