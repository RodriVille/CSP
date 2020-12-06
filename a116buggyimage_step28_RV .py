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
  spider.setheading(angle * i)
  spider.forward(length)#Draw legs
  i = i + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()