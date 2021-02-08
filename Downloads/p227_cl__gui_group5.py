# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry
    # If url_entry is blank, use localhost IP address
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
        print(url_val)
    # use url_val 
    print(url_val)
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    p = subprocess.Popen(command + " " + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()


root = tk.Tk()
frame = tk.Frame(root)
root.geometry("500x500")
frame.pack()

# set up button to run the do_command function

frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"), compound = "left", font = ("Arial", 18), bd=0, relief = "flat", cursor = "heart", bg="yellow")
ping_btn.pack()

tracert_btn = tk.Button(frame, text="trace route", command=lambda:do_command("tracert"), compound = "left", font = ("Arial", 18), bd=0, relief = "flat", cursor = "cross", bg="red")
tracert_btn.pack()

ns_btn = tk.Button(frame, text="ns lookup", command=lambda:do_command("nslookup"), compound = "left", font = ("Arial", 18), bd=0, relief = "flat", cursor = "star", bg="green")
ns_btn.pack()

save_btn = tk.Button(frame, text="save", command=lambda:mSave(), compound = "left", font = ("Arial", 18), bd=0, relief = "flat", cursor = "circle", bg="blue")
save_btn.pack()

#add extra commands


root.mainloop()
