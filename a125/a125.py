import turtle as trtl
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

win = 0

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
        win = 1
    elif(stateML == stateMM & stateMM == stateMR & stateML == 0):
        print("Computer wins!")
        win = 1
    elif(stateBL == stateBM & stateBM == stateBR & stateBL == 0):
        print("Computer wins!")
        win = 1
    elif(stateTL == stateML & stateML == stateBL & stateTL == 0):
        print("Computer wins!")
        win = 1
    elif(stateTM == stateMM & stateMM == stateBM & stateTM == 0):
        print("Computer wins!")
        win = 1
    elif(stateTR == stateMR & stateMR == stateBR & stateTR == 0):
        print("Computer wins!")
        win = 1
    elif(stateTL == stateMM & stateMM == stateBR & stateTL == 0):
        print("Computer wins!")
        win = 1
    elif(stateTR == stateMM & stateMM == stateBL & stateTR == 0):
        print("Computer wins!")
        win = 1
    #user win conditions
    elif(stateTL == stateTM & stateTM == stateTR & stateTL == 1):
        print("User wins!")
        win = 1
    elif(stateML == stateMM & stateMM == stateMR & stateML == 1):
        print("User wins!")
        win = 1
    elif(stateBL == stateBM & stateBM == stateBR & stateBL == 1):
        print("User wins!")
        win = 1
    elif(stateTL == stateML & stateML == stateBL & stateTL == 1):
        print("User wins!")
        win = 1
    elif(stateTM == stateMM & stateMM == stateBM & stateTM == 1):
        print("User wins!")
        win = 1
    elif(stateTR == stateMR & stateMR == stateBR & stateTR == 1):
        print("User wins!")
        win = 1
    elif(stateTL == stateMM & stateMM == stateBR & stateTL == 1):
        print("User wins!")
        win = 1
    elif(stateTR == stateMM & stateMM == stateBL & stateTR == 1):
        print("User wins!")
        win = 1


def start():
    turn = rand.randint(0, 1) #two random numbers to pick who goes first
    if (turn == 0):
        userOne()
    elif(turn == 1):
        userTwo()


def userOne():
    print("user one goes first")
    user = 0
    personChoice(spaceList)
    spaceTL.onclick(pickTL, 0)
    spaceTM.onclick(pickTL, 0)
    spaceTR.onclick(pickTL, 0)
    spaceML.onclick(pickTL, 0)
    spaceMM.onclick(pickTL, 0)
    spaceMR.onclick(pickTL, 0)
    spaceBL.onclick(pickTL, 0)
    spaceBM.onclick(pickTL, 0)
    spaceBR.onclick(pickTL, 0)


def userTwo():
    print("user two goes first")
    personChoice(spaceList)
    spaceTL.onclick(pickTL, 1)
    spaceTM.onclick(pickTL, 1)
    spaceTR.onclick(pickTL, 1)
    spaceML.onclick(pickTL, 1)
    spaceMM.onclick(pickTL, 1)
    spaceMR.onclick(pickTL, 1)
    spaceBL.onclick(pickTL, 1)
    spaceBM.onclick(pickTL, 1)
    spaceBR.onclick(pickTL, 1)

def personChoice(spaceList):
    print("Choose from this list: ")
    print(spaceList)

def pickTL(space, user):
    print("user chose TL")
    space.write("X", font = ("Arial", 20, "bold"))

def pickTM(space, user):
    print("user chose TM")
    space.write("X", font = ("Arial", 20, "bold"))

def pickTR(space, user):
    print("user chose TR")
    space.write("X", font = ("Arial", 20, "bold"))

def pickML(space, user):
    print("user chose ML")
    space.write("X", font = ("Arial", 20, "bold"))

def pickMM(space, user):
    print("user chose MM")
    space.write("X", font = ("Arial", 20, "bold"))

def pickMR(space, user):
    print("user chose MR")
    space.write("X", font = ("Arial", 20, "bold"))

def pickBL(space, user):
    print("user chose BL")
    space.write("X", font = ("Arial", 20, "bold"))

def pickBM(space, user):
    print("user chose BM")
    space.write("X", font = ("Arial", 20, "bold"))

def pickBR(space, user):
    print("user chose BR")
    space.write("X", font = ("Arial", 20, "bold"))


#---function calls-----
draw_selection_areas(xcord, ycord)
start()
check_win()



wn.listen()
#wn.exitonclick()
wn.mainloop()
