import sys
from tkinter import *
import tkinter.filedialog

#initalizing a window
root =Tk("Text Editor")

#Adding a textbox
text = Text(root)
text.grid()

#adding save functionality
def saveas():
    global text
    t = text.get("1.0","end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text = "Save", command = saveas)
button.grid()

#mainloop
root.mainloop()

