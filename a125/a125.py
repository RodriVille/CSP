import turtle as trtl
import random as rand

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
#wn.bgpic("board.png")# Make the background of the scene

xcord = -120
ycord = 75

global stateTL
global stateTM
global stateTR
global stateML
global stateMM
global stateMR
global stateBL
global stateBM
global stateBR


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

global win
win = 2

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




def start(win):
    turn = rand.randint(0, 1) #two random numbers to pick who goes first
    if (turn == 0):
        print("user one first")
        while (win == 2):
            userOne()
            win = check_win()
            userTwo()
            win = check_win()
    elif(turn == 1):
        print("user two first")
        while (win == 2):
            userTwo()
            win = check_win()
            userOne()
            win = check_win()


def userOne():
    spaceTL.onclick(pickTL(spaceTL, 0), 1)
    spaceTM.onclick(pickTM(spaceTM, 0), 1)
    spaceTR.onclick(pickTR(spaceTR, 0), 1)
    spaceML.onclick(pickML(spaceML, 0), 1)
    spaceMM.onclick(pickMM(spaceMM, 0), 1)
    spaceMR.onclick(pickMR(spaceMR, 0), 1)
    spaceBL.onclick(pickBL(spaceBL, 0), 1)
    spaceBM.onclick(pickBM(spaceBM, 0), 1)
    spaceBR.onclick(pickBR(spaceBR, 0), 1)

    wn.listen()

def userTwo():
    spaceTL.onclick(pickTL(spaceTL, 1), 1)
    spaceTM.onclick(pickTM(spaceTM, 1), 1)
    spaceTR.onclick(pickTR(spaceTR, 1), 1)
    spaceML.onclick(pickML(spaceML, 1), 1)
    spaceMM.onclick(pickMM(spaceMM, 1), 1)
    spaceMR.onclick(pickMR(spaceMR, 1), 1)
    spaceBL.onclick(pickBL(spaceBL, 1), 1)
    spaceBM.onclick(pickBM(spaceBM, 1), 1)
    spaceBR.onclick(pickBR(spaceBR, 1), 1)


def pickTL(space, user):
    print("user chose TL")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTL = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTL = 1

def pickTM(space, user):
    print("user chose TM")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTM = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTM = 1

def pickTR(space, user):
    print("user chose TR")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTR = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTR = 1

def pickML(space, user):
    print("user chose ML")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateML = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateML = 1

def pickMM(space, user):
    print("user chose MM")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateMM = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMM = 1

def pickMR(space, user):
    print("user chose MR")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateMR = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMR = 1

def pickBL(space, user):
    print("user chose BL")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBL = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBL = 1

def pickBM(space, user):
    print("user chose BM")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBM = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBM = 1

def pickBR(space, user):
    print("user chose BR")
    if (user == 0):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBR = 0
    elif (user == 1):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBR = 1
#have to call this after every state change
def check_win():
    #Computer win conditions
    if(stateTL == stateTM & stateTM == stateTR & stateTL == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateML == stateMM & stateMM == stateMR & stateML == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateBL == stateBM & stateBM == stateBR & stateBL == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateTL == stateML & stateML == stateBL & stateTL == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateTM == stateMM & stateMM == stateBM & stateTM == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateTR == stateMR & stateMR == stateBR & stateTR == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateTL == stateMM & stateMM == stateBR & stateTL == 0):
        print("Computer wins!")
        win = 1
        return win
    elif(stateTR == stateMM & stateMM == stateBL & stateTR == 0):
        print("Computer wins!")
        win = 1
        return win
    #user win conditions
    elif(stateTL == stateTM & stateTM == stateTR & stateTL == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateML == stateMM & stateMM == stateMR & stateML == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateBL == stateBM & stateBM == stateBR & stateBL == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateTL == stateML & stateML == stateBL & stateTL == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateTM == stateMM & stateMM == stateBM & stateTM == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateTR == stateMR & stateMR == stateBR & stateTR == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateTL == stateMM & stateMM == stateBR & stateTL == 1):
        print("User wins!")
        win = 1
        return win
    elif(stateTR == stateMM & stateMM == stateBL & stateTR == 1):
        print("User wins!")
        win = 1
        return win
    else:
        win = 2

#---function calls-----
draw_selection_areas(xcord, ycord)
start(win)

wn.listen()
#wn.exitonclick()
wn.mainloop()
