from tkinter import *
import os


root = Tk()
root.title('Test Coordinates')
root.geometry("800x600")

tk_legend = Tk()
tk_legend.title('Selector')
tk_legend.geometry("150x400")

var1 = IntVar()
Checkbutton(tk_legend, text="male", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(tk_legend, text="female", variable=var2).grid(row=1, sticky=W)
mainloop()