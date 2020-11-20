import turtle as trtl

#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.bgpic("board.png")# Make the background of the scene

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

#---Set each space postion---
spaceList = [spaceTL, spaceTM, spaceTR, spaceML, spaceMM, spaceMR, spaceBL, spaceBM, spaceBR]

#print the circles in the grid
def draw_selection_areas():
    i=0
    for spaces in spaceList:
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
    if(stateTL == stateTM & stateTM == stateTR):
        print(" Andrew wins!")
    if(stateML == stateMM & stateMM == stateMR):
        print(" wins!")
    if(stateBL == stateBM & stateBM == stateBR):
        print(" wins!")
    if(stateTL == stateML & stateML == stateBL):
        print(" wins!")
    if(stateTM == stateMM & stateMM == stateBM):
        print(" wins!")
    if(stateTR == stateMR & stateMR == stateBR):
        print(" wins!")
    if(stateTL == stateMM & stateMM == stateBR):
        print(" wins!")
    if(stateTR == stateMM & stateMM == stateBL):
        print(" wins!")


#---function calls-----
draw_selection_areas()
check_win()



wn.listen()
wn.exitonclick()
wn.mainloop()
