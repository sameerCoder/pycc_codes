# Tkinter canvas script 1


import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 1, 5, 240, 210
arc = C.create_arc(coord, start=0, extent=90, fill="red")
#rectangle=C.create_rectangle(coord,fill="red")

C.pack()
top.mainloop()
