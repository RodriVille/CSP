import turtle as trtl

painter = trtl.Turtle()

painter.pensize(5)


#QUESTION 16
#painter.penup()
#painter.goto(200, 200)
#painter.pendown()
#painter.circle(100)

#painter.penup()
#painter.goto(-200, 200)
#painter.pendown()
#painter.circle(100, 30)

#painter.penup()
#painter.goto(-200, -200)
#painter.pendown()
#painter.circle(100, 360, 7)

#painter.penup()
#painter.goto(200, -200)
#painter.pendown()
#painter.circle(100, 270)

#QUESTOIN 18
#painter.fillcolor("Blue")
#painter.pencolor("Green")

#painter.begin_fill()
#painter.circle(20)
#painter.end_fill()

#painter.penup()
#painter.goto(200, 200)
#painter.pendown()
#painter.pencolor("red")
#painter.fillcolor("Yellow")
#painter.begin_fill()
#painter.circle(100, 360, 10)
#painter.end_fill()

#QUESTION 21
headSize = int(input("What size noggin do you want? "))

painter.fillcolor("Blue")

painter.begin_fill()
painter.circle(headSize)
painter.end_fill()

bodySize = int(input("how tall you want this homie to be? "))

painter.penup()
painter.goto(0, 0)
painter.right(90)
painter.pendown()
painter.forward(bodySize)

painter.penup()
painter.goto(0, 0)
painter.right(90)
painter.pendown()
painter.forward(bodySize)

painter.penup()
painter.goto(0, 0)
painter.right(180)
painter.pendown()
painter.forward(bodySize)

painter.penup()
painter.goto(0, -bodySize)
painter.right(45)
painter.pendown()
painter.forward(bodySize)

painter.penup()
painter.goto(0, -bodySize)
painter.right(90)
painter.pendown()
painter.forward(bodySize)

wn = trtl.Screen()
wn.mainloop()