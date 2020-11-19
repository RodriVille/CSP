import turtle as trtl
import random as rand
import time

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.bgpic("board.png")# Make the background of the scene
print("hello")

xcord = -50
ycord = 50

spaceTL = trtl.Turtle()
spaceTM = trtl.Turtle()
spaceTR = trtl.Turtle()
spaceML = trtl.Turtle()
spaceMM = trtl.Turtle()
spaceMR = trtl.Turtle()
spaceBL = trtl.Turtle()
spaceBM = trtl.Turtle()
spaceBR = trtl.Turtle()

stateTL = 0
stateTM = 0
stateTR = 0
stateML = 0
stateMM = 0
stateMR = 0
stateBL = 0
stateBM = 0
stateBR = 0

spaceList = [spaceTL, spaceTM, spaceTR, spaceML, spaceMM, spaceMR, spaceBL, spaceBM, spaceBR]

i = 0
for spaces in spaceList:
    spaces.goto(xcord, ycord)
    spaces.circle(20)
    xcord += 50
    if (i == 2):
        ycord -= 50
        i = 0
        xcord = -50

wn.listen()
# wn.exitonclick()
wn.mainloop()