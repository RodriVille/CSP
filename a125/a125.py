import turtle as trtl
import random as rand
import time

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.bgpic("board.png")# Make the background of the scene
print("hello")

xcord = 50
ycord = -50

spaceTL = trtl.Turtle()
spaceTM = trtl.Turtle()
spaceTR = trtl.Turtle()
spaceML = trtl.Turtle()
spaceMM = trtl.Turtle()
spaceMR = trtl.Turtle()
spaceBL = trtl.Turtle()
spaceBM = trtl.Turtle()
spaceBR = trtl.Turtle()

spaceList = [spaceTL, spaceTM, spaceTR, spaceML, spaceMM, spaceMR, spaceBL, spaceBM, spaceBR]

for spaces in spaceList:
    spaces.goto(xcord, ycord)
    spaces.square(20)
    xcord += 50
    i = 0
    if (i == 3):
        ycord -= 50
        i = 0
    i += 1


wn.listen()
# wn.exitonclick()
wn.mainloop()