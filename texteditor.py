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

#font helvetica
def FontHelvetica():
    global text
    text.config(font = "Helvetica")

#font courier
def FontCourier():
    global text
    text.config(font = "Courier")

#font menu button
font = Menubutton(root, text = "Font")
font.grid()
font.menu = Menu(font, tearoff = 0)
font["menu"]=font.menu
helvetica = IntVar()
courier = IntVar()

#font menu drop down
font.menu.add_checkbutton(label = "Courier", variable = courier, command = FontCourier)
font.menu.add_checkbutton(label = "Helvetica", variable = helvetica, command = FontHelvetica)

#mainloop
root.mainloop()

