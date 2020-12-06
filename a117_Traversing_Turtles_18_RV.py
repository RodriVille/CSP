#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "turtle", "arrow", "square", "triangle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "cyan", "Magenta", "pink", "black"]

for s in turtle_shapes:
  newColor = turtle_colors.pop()
  t = trtl.Turtle(shape=s) 
  t.color(newColor)
  my_turtles.append(t)
  t.penup()
  

#The x and y coordinates where the shapes will be drawn from
startx = 0
starty = 0
heading = 90
#for each loop that goes through the my_turtles list
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(heading)
  t.pendown()
  t.right(35) 
  t.forward(50)

#change in coordinates after each iteration
  startx = t.xcor()
  starty = t.ycor()
  heading = t.heading()

wn = trtl.Screen()
wn.mainloop()