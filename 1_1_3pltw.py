import turtle as trtl 

painter = trtl.Turtle()

i = 0
while (i < 19):
    painter.forward(20)
    painter.right(20)
    i = i + 1



wn = trtl.Screen()
wn.mainloop()