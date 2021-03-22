import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
loop = 6 
length = 70
angle = 380 / loop
spider.pensize(5)
i = 0 
while (i < loop):
  spider.goto(0,0)
  spider.setheading(angle * i)
  spider.forward(length)
  i = i + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()