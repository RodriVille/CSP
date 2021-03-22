import turtle as trtl
import random as rand

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.bgpic("board.png")# Make the background of the scene

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

global stateTL
global stateTM
global stateTR
global stateML
global stateMM
global stateMR
global stateBL
global stateBM
global stateBR

winner = trtl.Turtle()
winner.ht()
spaceTL = trtl.Turtle()
spaceTM = trtl.Turtle()
spaceTR = trtl.Turtle()
spaceML = trtl.Turtle()
spaceMM = trtl.Turtle()
spaceMR = trtl.Turtle()
spaceBL = trtl.Turtle()
spaceBM = trtl.Turtle()
spaceBR = trtl.Turtle()

# 0 for User One and 1 for user
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

global user
user = 0

#---Set each space postion---
spaceList = [spaceTL, spaceTM, spaceTR, spaceML, spaceMM, spaceMR, spaceBL, spaceBM, spaceBR]
userList = []

#print the circles in the grid
def draw_selection_areas(xcord, ycord):
    i=0
    for spaces in spaceList:
        spaces.speed(0)
        spaces.penup()
        spaces.goto(xcord, ycord)
        spaces.pendown()
        spaces.circle(40)
        spaces.setheading(90)
        xcord += 120
        if (i == 2):
            ycord -= 115
            i = 0
            xcord = -120
        else:
            i += 1


def pickTL(space):
    print("user chose TL")
    global user
    global stateTL
    if (user == 0 and stateTL == 2): #What user is the one picking the circle
        space.write("X", font = ("Arial", 20, "bold"))
        stateTL = 0 #sets the state of the tile for check win
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateTL == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTL = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateTL != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateTL != 2):
        user = 1
    keyPress()

def pickTM(space):
    global user
    global stateTM
    print("user chose TM")
    if (user == 0 and stateTM == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTM = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateTM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTM = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateTM != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateTM != 2):
        user = 1
    keyPress()

def pickTR(space):
    global user
    global stateTR
    print("user chose TR")
    if (user == 0 and stateTR == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTR = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateTR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTR = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateTR != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateTR != 2):
        user = 1
    keyPress()

def pickML(space):
    print("user chose ML")
    global user
    global stateML
    if (user == 0 and stateML == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateML = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateML == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateML = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateML != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateML != 2):
        user = 1
    keyPress()

def pickMM(space):
    print("user chose MM")
    global user
    global stateMM
    if (user == 0 and stateMM == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateMM = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateMM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMM = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateMM != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateMM != 2):
        user = 1
    keyPress()

def pickMR(space):
    print("user chose MR")
    global user
    global stateMR
    if (user == 0 and stateMR == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateMR = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateMR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMR = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateMR != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateMR != 2):
        user = 1
    keyPress()

def pickBL(space):
    print("user chose BL")
    global user
    global stateBL
    if (user == 0 and stateBL == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBL = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateBL == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBL = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateBL != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateBL != 2):
        user = 1
    keyPress()

def pickBM(space):
    print("user chose BM")
    global user
    global stateBM
    if (user == 0 and stateBM == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBM = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateBM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBM = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateBM != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateBM != 2):
        user = 1
    keyPress()

def pickBR(space):
    print("user chose BR")
    global user
    global stateBR
    if (user == 0 and stateBR == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBR = 0
        user = 1
        check_win()
        check_cats()
    elif (user == 1 and stateBR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBR = 1
        user = 0
        check_win()
        check_cats()
    elif (user == 0 and stateBR != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateBR != 2):
        user = 1
    keyPress()


#have to call this after every state change
def check_win():
    #User One win conditions
    if(stateTL == stateTM and stateTM == stateTR and stateTL == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateML == stateMM and stateMM == stateMR and stateML == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateBL == stateBM and stateBM == stateBR and stateBL == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateTL == stateML and stateML == stateBL and stateTL == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateTM == stateMM and stateMM == stateBM and stateTM == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateTR == stateMR and stateMR == stateBR and stateTR == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateTL == stateMM and stateMM == stateBR and stateTL == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    elif(stateTR == stateMM and stateMM == stateBL and stateTR == 0):
        print("User One wins!")
        oneWins()
        wn.exitonclick()
    #user win conditions
    elif(stateTL == stateTM and stateTM == stateTR and stateTL == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateML == stateMM and stateMM == stateMR and stateML == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateBL == stateBM and stateBM == stateBR and stateBL == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateTL == stateML and stateML == stateBL and stateTL == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateTM == stateMM and stateMM == stateBM and stateTM == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateTR == stateMR and stateMR == stateBR and stateTR == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateTL == stateMM and stateMM == stateBR and stateTL == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    elif(stateTR == stateMM and stateMM == stateBL and stateTR == 1):
        print("User two wins!")
        twoWins()
        wn.exitonclick()
    else:
        print("No one has won")

def check_cats():
    if((stateTL != 2) and (stateTM != 2) and (stateTR != 2) and (stateML != 2) and (stateMM != 2) and (stateMR != 2) and (stateBL != 2) and (stateBM != 2) and (stateBR != 2)):
        print("CATS GAME, REPLAY")
        wn.clear()
        winner.goto(-120,0)
        winner.write("NO ONE WINS, CAT GAME, PLAY AGAIN!", font = ("Arial", 20, "bold"))

def oneWins():
    wn.clear()
    winner.write("User One Wins!", font = ("Arial", 20, "bold"))
    winner.ht()

def twoWins():
    wn.clear()
    winner.write("User Two Wins!", font = ("Arial", 20, "bold"))
    winner.ht()

def TL(stateTL, num):
    pickTL(spaceTL)
def TM(stateTM, num):
    pickTM(spaceTM)
def TR(stateTR, num):
    pickTR(spaceTR)
def ML(stateML, num):
    pickML(spaceML)
def MM(stateMM, num):
    pickMM(spaceMM)
def MR(stateMR, num):
    pickMR(spaceMR)
def BL(stateBL, num):
    pickBL(spaceBL)
def BM(stateBM, num):
    pickBM(spaceBM)
def BR(stateBR, num):
    pickBR(spaceBR)

#---listens for space clicks---
def keyPress():
    spaceTL.onclick(TL) #code that runs after someone clicks on a circle
    spaceTM.onclick(TM)
    spaceTR.onclick(TR)
    spaceML.onclick(ML)
    spaceMM.onclick(MM)
    spaceMR.onclick(MR)
    spaceBL.onclick(BL)
    spaceBM.onclick(BM)
    spaceBR.onclick(BR)


#---function calls-----
draw_selection_areas(xcord, ycord)
keyPress()


wn.listen()
wn.mainloop()
