import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)#create spider body
spider.penup()
spider.forward(30)
spider.pendown()
spider.circle(10)#Create spider Head

loop = 8 
length = 70#configure legs
angle = 360 / loop
spider.pensize(5)
i = 0 
while (i < loop):
  spider.goto(0,20)
  if(i % 4 == 0):
    spider.setheading(angle * i + 35)
  else:
    spider.setheading(angle * i - 35)
  spider.pendown()
  spider.circle(50, 90)#Draw legs
  spider.penup()
  i = i + 1

spider.pensize(2)
spider.penup()
spider.pencolor("purple")
spider.goto(30, 0)
spider.pendown()
spider.circle(4)
spider.pensize(2)

spider.penup()
spider.pencolor("purple")
spider.goto(35, 10)
spider.pendown()
spider.circle(4)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()