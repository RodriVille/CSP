import turtle as trtl
import random as rand
import time

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.bgpic("board.png")# Make the background of the scene
print("hello")

xcord = -120
ycord = 75

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

#Draws the circles inside the grid
i = 0
for spaces in spaceList:
    spaces.ht()
    spaces.penup()
    spaces.goto(xcord, ycord)
    spaces.circle(20)
    xcord += 50
    if (i == 2):
        ycord -= 50
        i = 0
        xcord = -120
    else:
        i += 1

#have to call this after every state change
def check_win():
    if(stateTL == stateTM && stateTM == stateTR)
      print(stateTL + " wins!")
    if(stateML == stateMM && stateMM == stateMR)
      print(stateML + " wins!")
    if(stateBL == stateBM && stateBM == stateBR)
      print(stateBL + " wins!")
    if(stateTL == stateML && stateML == stateBL)
      print(stateTL + " wins!")
    if(stateTM == stateMM && stateMM == stateBM)
      print(stateTM + " wins!")
    if(stateTR == stateMR && stateMR == stateBR)
      print(stateTR + " wins!")
    if(stateTL == stateMM && stateMM == stateBR)
      print(stateTL + " wins!")
    if(stateTR == stateMM && stateMM == stateBL)
      print(stateTR + " wins!")
#somehow we have to make this exit the program after, so maybe put click to exit

wn.listen()
# wn.exitonclick()
wn.mainloop()
