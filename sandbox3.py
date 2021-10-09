import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os


# root window
root = tk.Tk()
root.geometry("1200x800")
root.title('Floor Plan')

NUMCOLS = 7
NUMROWS = 3
MINSIZE = 100
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# Configure the size of the Grid
for i in range(NUMCOLS):
    root.columnconfigure(i, minsize=MINSIZE)

for i in range(NUMROWS):
    root.rowconfigure(i, minsize=MINSIZE)

# Place Months on top row
label_arr = []
for i in range(NUMCOLS-1):
    label_arr.append(tk.Label(root, text=MONTHS[i]))
    label_arr[i].grid(column=i+1, row=0)

# Place Builds on left column
build1 = tk.Label(root, text="EVT")
build1.grid(column=0, row=1)

# Place a canvas underneath
my_canvas = tk.Canvas(root)
my_canvas.configure(bg='white', height=50, width=300)
my_canvas.grid(column=1, row=1, sticky='w', columnspan=3)



root.mainloop()