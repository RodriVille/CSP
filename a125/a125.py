import turtle as trtl
import random as rand
import time
import os


dir = os.path.dirname(os.path.abspath(__file__))
board = os.path.join(dir, "C:\Users\ethan\OneDrive\Desktop\Rod\CSP\a125\board.png")
#-----setup-----
wn = trtl.Screen()
wn.setup(width=.5, height=.5)
wn.bgpic("board.png")# Make the background of the scene
print("hello")

wn.listen()
# wn.exitonclick()
wn.mainloop()