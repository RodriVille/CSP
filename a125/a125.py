import turtle as trtl
import ComputerAI as AI
import random as rand

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
#wn.bgpic("board.png")# Make the background of the scene

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

# 0 for computer and 1 for user
stateTL = 2
stateTM = 2
stateTR = 2
stateML = 2
stateMM = 2
stateMR = 2
stateBL = 2
stateBM = 2
stateBR = 2

#---Set each space postion---
spaceList = [spaceTL, spaceTM, spaceTR, spaceML, spaceMM, spaceMR, spaceBL, spaceBM, spaceBR]
userList = []

#print the circles in the grid
def draw_selection_areas(xcord, ycord):
    i=0
    for spaces in spaceList:
        spaces.speed(0)
        spaces.ht()
        spaces.penup()
        spaces.goto(xcord, ycord)
        spaces.pendown()
        spaces.circle(40)
        xcord += 120
        if (i == 2):
            ycord -= 115
            i = 0
            xcord = -120
        else:
            i += 1

#have to call this after every state change
def check_win():
    #Computer win conditions
    if(stateTL == stateTM & stateTM == stateTR & stateTL == 0):
        print("Computer wins!")
    elif(stateML == stateMM & stateMM == stateMR & stateML == 0):
        print("Computer wins!")
    elif(stateBL == stateBM & stateBM == stateBR & stateBL == 0):
        print("Computer wins!")
    elif(stateTL == stateML & stateML == stateBL & stateTL == 0):
        print("Computer wins!")
    elif(stateTM == stateMM & stateMM == stateBM & stateTM == 0):
        print("Computer wins!")
    elif(stateTR == stateMR & stateMR == stateBR & stateTR == 0):
        print("Computer wins!")
    elif(stateTL == stateMM & stateMM == stateBR & stateTL == 0):
        print("Computer wins!")
    elif(stateTR == stateMM & stateMM == stateBL & stateTR == 0):
        print("Computer wins!")
    #user win conditions
    elif(stateTL == stateTM & stateTM == stateTR & stateTL == 1):
        print("User wins!")
    elif(stateML == stateMM & stateMM == stateMR & stateML == 1):
        print("User wins!")
    elif(stateBL == stateBM & stateBM == stateBR & stateBL == 1):
        print("User wins!")
    elif(stateTL == stateML & stateML == stateBL & stateTL == 1):
        print("User wins!")
    elif(stateTM == stateMM & stateMM == stateBM & stateTM == 1):
        print("User wins!")
    elif(stateTR == stateMR & stateMR == stateBR & stateTR == 1):
        print("User wins!")
    elif(stateTL == stateMM & stateMM == stateBR & stateTL == 1):
        print("User wins!")
    elif(stateTR == stateMM & stateMM == stateBL & stateTR == 1):
        print("User wins!")


def start():
    turn = rand.randint(0, 1) #two random numbers to pick who goes first
    if (turn == 0):
        personFirst()
    elif(turn == 1):
        computerFirst()


def userOneFirst():
    print("user one goes first")
    AI.pickSpace(spaceList, userList)


def userTwoFirst():
    print("user two goes first")

def personChoice(spaceList):
    print("Choose from this list: ")
    print(spaceList)


#---function calls-----
draw_selection_areas(xcord, ycord)
start()
check_win()



wn.listen()
#wn.exitonclick()
wn.mainloop()
