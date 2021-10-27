from tkinter import *   
from tkinter import ttk
master = Tk()
player1 = "A"
player2 = "B"
from tkinter import *
Label(master, text="NAME", font=30).grid(row=0)
Label(master, text=player1, font=30).grid(row=1)
Label(master, text=player2, font=30).grid(row=2)
Label(master, text="SCORE", font=30).grid(column=2, row=0)

ttk.Separator(master, orient=VERTICAL).grid(column=1, row=0, rowspan=3, sticky='ns')

master.mainloop()