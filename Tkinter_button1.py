# Tkinter Button script 1.

import tkinter
#import tkMessageBox # This is for python 2.X version
import tkinter.messagebox # This is for python 3.x version 

top = tkinter.Tk()

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

B1=tkinter.Button(top,text="Simple Button")
B2 = tkinter.Button(top, text ="Hello B", command = helloCallBack)
#B=tkinter.Button(top,text="Button")
exitbutton=tkinter.Button(top,text="EXIT",command=top.destroy)
B1.pack()
B2.pack()
exitbutton.pack()

top.mainloop()
