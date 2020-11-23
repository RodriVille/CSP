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



spaceTL.onclick(pickTL(spaceTL, 0, stateTL), 1) #code that runs after someone clicks on a circle
spaceTM.onclick(pickTM(spaceTM, 0, stateTM), 1)
spaceTR.onclick(pickTR(spaceTR, 0, stateTR), 1)
spaceML.onclick(pickML(spaceML, 0, stateML), 1)
spaceMM.onclick(pickMM(spaceMM, 0, stateMM), 1)
spaceMR.onclick(pickMR(spaceMR, 0, stateMR), 1)
spaceBL.onclick(pickBL(spaceBL, 0, stateBL), 1)
spaceBM.onclick(pickBM(spaceBM, 0, stateBM), 1)
spaceBR.onclick(pickBR(spaceBR, 0, stateBR), 1)



def pickTL(space, user, stateTL):
    print("user chose TL")
    if (user == 0 and stateTL == 2): #What user is the one picking the circle
        space.write("X", font = ("Arial", 20, "bold"))
        stateTL = 0 #sets the state of the tile for check win
    elif (user == 1 and stateTL == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTL = 1
    elif (user == 0 and stateTL != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateTL != 2):
        userTwo()

def pickTM(space, user, stateTM):
    print("user chose TM")
    if (user == 0 and stateTM == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTM = 0
    elif (user == 1 and stateTM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTM = 1
    elif (user == 0 and stateTM != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateTM != 2):
        userTwo()

def pickTR(space, user, stateTR):
    print("user chose TR")
    if (user == 0 and stateTR == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateTR = 0
    elif (user == 1 and stateTR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateTR = 1
    elif (user == 0 and stateTR != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateTR != 2):
        userTwo()

def pickML(space, user, stateML):
    print("user chose ML")
    if (user == 0 and stateML == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateML = 0
    elif (user == 1 and stateML == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateML = 1
    elif (user == 0 and stateML != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateML != 2):
        userTwo()

def pickMM(space, user, stateMM):
    print("user chose MM")
    if (user == 0 and stateMM == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateMM = 0
    elif (user == 1 and stateMM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMM = 1
    elif (user == 0 and stateMM != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateMM != 2):
        userTwo()

def pickMR(space, user, stateMR):
    print("user chose MR")
    if (user == 0 and stateMR == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateMR = 0
    elif (user == 1 and stateMR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateMR = 1
    elif (user == 0 and stateMR != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateMR != 2):
        userTwo()

def pickBL(space, user, stateBL):
    print("user chose BL")
    if (user == 0 and stateBL == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBL = 0
    elif (user == 1 and stateBL == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBL = 1
    elif (user == 0 and stateBL != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateBL != 2):
        userTwo()

def pickBM(space, user, stateBM):
    print("user chose BM")
    if (user == 0 and stateBM == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBM = 0
    elif (user == 1 and stateBM == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBM = 1
    elif (user == 0 and stateBM != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateBM != 2):
        userTwo()

def pickBR(space, user, stateBR):
    print("user chose BR")
    if (user == 0 and stateBR == 2):
        space.write("X", font = ("Arial", 20, "bold"))
        stateBR = 0
    elif (user == 1 and stateBR == 2):
        space.write("O", font = ("Arial", 20, "bold"))
        stateBR = 1
    elif (user == 0 and stateBR != 2):#this is if the spot has already been taken
        userOne()
    elif (user == 1 and stateBR != 2):
        userTwo()
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
