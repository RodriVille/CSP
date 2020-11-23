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
        xcord += 120
        if (i == 2):
            ycord -= 115
            i = 0
            xcord = -120
        else:
            i += 1



'''def start(win):
    turn = rand.randint(0, 1) #two random numbers to pick who goes first
    if (turn == 0):
        print("user one first")
        while (win == 2): #Keeps running turns while no one has one
            userOne() #allows user one to make a choice
            win = check_win() #checks win after turn
            userTwo()
            win = check_win()
    elif(turn == 1):
        print("user two first")
        while (win == 2):
            userTwo()
            win = check_win()
            userOne()
            win = check_win()'''






def pickTL(space):
    print("user chose TL")
    global user
    global stateTL
    if (user == 0 and stateTL == 2): #What user is the one picking the circle
        space.write("X", font = ("Arial", 20, "bold"))
        stateTL = 0 #sets the state of the tile for check win
        user = 1
        check_win()
    elif (user == 1 and stateTL == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTL = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateTM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTM = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateTR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTR = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateML == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateML = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateMM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMM = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateMR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMR = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateBL == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBL = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateBM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBM = 1
        user = 0
        check_win()
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
    elif (user == 1 and stateBR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBR = 1
        user = 0
        check_win()
    elif (user == 0 and stateBR != 2):#this is if the spot has already been taken
        user = 0
    elif (user == 1 and stateBR != 2):
        user = 1
    keyPress()
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
    else:
        print("No one has won")

def TL():
    global stateTL
    pickTL(spaceTL)
def TM():
    global stateTM
    pickTM(spaceTM)
def TR():
    global stateTR
    pickTR(spaceTR)
def ML():
    global stateML
    pickML(spaceML)
def MM():
    global stateMM
    pickMM(spaceMM)
def MR():
    global stateMR
    pickMR(spaceMR)
def BL():
    global stateBL
    pickBL(spaceBL)
def BM():
    global stateBM
    pickBM(spaceBM)
def BR():
    global stateBR
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
#wn.exitonclick()
wn.mainloop()
