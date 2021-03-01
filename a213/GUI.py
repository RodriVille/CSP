import tkinter as tk
import turtle as trtl
from PIL import ImageGrab, Image, ImageDraw
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
#import encode as e
#import encode

master = tk.Tk()
tk.Label(master, text="what do you want to encode").grid(row=0)
message = tk.Entry(master)
message.grid(row=0, column=1)

print (message)

master.mainloop()