# Tkinter Entry script 1.

'''
from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()
'''


from tkinter import *

top=Tk()
l1=Label(top,text="Enter User name:")
l1.grid(row=0,column=0)
e1=Entry(top,bd=5)
e1.grid(row=0,column=1)
top.mainloop()
