#!/usr/bin/python3
from tkinter import *

master = Tk()

w = Canvas(master, width=100, height=40)
w.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')

w.pack()
master.mainloop()