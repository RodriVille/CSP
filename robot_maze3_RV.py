#   a114_robot_maze.py
import turtle as trtl

#------ robot algorithms
def move():
  robot.dot(10)
  robot.forward(50)

def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)
  
#----- roboto starting location
startx = -100
starty = -100

#----- init screen
wn = trtl.Screen()
wn.setup(width=400, height=420)

#----- init robot
robot_image = "robot.gif"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO 1: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO 2: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
i = 1
while (i < 2):
  j = 0
  i = i + 1
  move()
  turn_left()
  while(j < 2):
    j = j + 1
    turn_left()
  l = 0
  while(l<2):
    move()
    l = l +1
  turn_left()
  m = 0
  while( m < 2):
    move()
    m = m + 1
    if(m == 1):
      robot.pencolor("cyan")
  h = 0
  while (h < 3):
    turn_left()
    h = h + 1
  t = 0
  while (t < 2):
    move()
    t = t + 1
  turn_left()
  move()
'''
i = 0
while (i < 3): # forward 3
  i += 1
  move()
'''

#---- end robot movement 

wn.mainloop()
