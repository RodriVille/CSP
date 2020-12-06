#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = ""
xcord = 0
ycord = 50
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple): #Step 1
  xcord = rand.randint(-100, 100)
  active_apple.goto(xcord, 50)
  active_apple.showturtle()
  active_apple.shape(apple_image)

def applFall(active_apple): #Step 6
  xcor = active_apple.xcor()
  ycor = active_apple.ycor()
  active_apple.penup()
  active_apple.goto(xcor, -150)
  active_apple.clear()
  active_apple.hideturtle()
  draw_apple(active_apple)

def new_letter(Appl): #Step 2
  letter = rand.choice(letter_list)
  #print str(letter)
  userI(Appl, letter)

def userI (active_apple, letter): #Step 3
  msg = str(letter)
  active_apple.color("blue")
  active_apple.write(msg, font=("Arial", 20, "bold"))
  keypress(active_apple, letter)
  
def dropAppl(): #Step 5
  applFall(apple)
  new_letter(apple)

def keypress (apple, letter): #Step 4
  given_letter = letter 
  wn.onkeypress(dropAppl, given_letter)
#-----function calls-----

draw_apple(apple)
wn.tracer(False)
new_letter(apple)
wn.tracer(True)

#wn.onkeypress(dropAppl, "a")





#   a123_apple_and_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. 

#TODO Create a function that draws a new letter from the letter list.

#TODO Create a function that takes a turtle (apple) as its parameter
# and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
# for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, retrieve a
# random turtle (apple) and causes the turtle (apple) to drop from the tree and the letter 
# to disappear. Call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop an apple at random.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.



wn.listen()

wn.update() 

wn.mainloop()