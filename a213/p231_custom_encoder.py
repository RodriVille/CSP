#   encode.py
#   Note this will not run in the code editor and must be downloaded
import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

#message = "dumb" # Change this to encode a different message. Length limit 20 characters.
global root
root = trtl.getcanvas().winfo_toplevel()
global bits_as_ints

bits_as_ints = []

master = tk.Tk()
tk.Label(master, text="what do you want to encode").grid(row=0)
msg = tk.Entry(master)
msg.grid(row=0, column=1)

encode_btn = tk.Button(master, text="encode", command=lambda:doTheThing(msg.get()))
encode_btn.grid(row=1)

screen = trtl.getscreen()
drawer = trtl.Turtle()

#message = input("what do you want to encode, 4head?")
def doTheThing(message):
  global root
  characters_as_ints = [] #initialize a array
  for cha in message:
    characters_as_ints.append(ord(cha)) #adds unicode of chars to array
  print(characters_as_ints)

  characters_as_bits = [] #another array
  for integ in characters_as_ints:
    characters_as_bits.append('{0:08b}'.format(integ)) #adds to array in bit format
  print(characters_as_bits)

  for index in range(0,len(characters_as_bits)):
    for bit in characters_as_bits[index]: #adds bits as ints
      bits_as_ints.append(bit)
  print(bits_as_ints)

  drawer.penup()
  drawer.goto(-200,221)
  drawer.shape("circle")
  drawer.color("black")

  message_length = len(bits_as_ints)
  index = 0
  i = 0
  while index < message_length:
    if index % 8 == 0:
      drawer.goto(-200, drawer.ycor()-21)
    if bits_as_ints[index]=='1':
      if( i == 0):
        drawer.color("blue")
        i = 1
      else:
        drawer.color("black")
        i = 0
      
      
      drawer.stamp()
    drawer.forward(21)
    index = index + 1

  screen = drawer.getscreen()
  root = trtl.getcanvas().winfo_toplevel()

  create_image(screen) #calls on this first

# draw the message instead of taking a screenshot for macOS users
def draw_message(im_size, x, y):
  im = Image.new("RGBA", im_size, (255,255,255,0))
  draw = ImageDraw.Draw(im)
  message_length = len(bits_as_ints)
  index = 0
  while index < message_length:
    if index % 8 == 0:
      x = im_size[0]/2-200-10.5
      y += 21
    if bits_as_ints[index]=='1':
      draw.rectangle([x,y,x+21,y+21], fill="blue") #stamp
    x += 21
    index = index + 1
  im.save("macOutput.gif")

def create_image(widget):
  global root
  x=root.winfo_rootx() #rando cord stuff (staring)
  y=root.winfo_rooty()
  x1=x+widget.window_width() #constraints
  y1=y+widget.window_height()
  im = ImageGrab.grab().crop((x,y,x1,y1))
  im.save("dumber.gif")
  print(im.size)

  # create an image for macOS users
  draw_message(im.size,im.size[0]/2-200-10.5,im.size[1]/2-221-10.5) # (149.5,98) in ImageDraw is equivalent to (205,275) in PIL 


screen.mainloop()