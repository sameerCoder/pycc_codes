# Tkinter Label script 1 .

from tkinter import *

root = Tk()
root.geometry("500x500")
var = StringVar()

#intvar=IntVar()

label = Label( root, textvariable=var, relief=FLAT )#RAISED

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
