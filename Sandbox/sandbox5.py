# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# # Container contains the main canvas and the scrollbar
# container = tk.Frame(root)

# canvas = tk.Canvas(container)
# scrollbar =  tk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)

# # Frame inside the main canvas that has the scrollable area
# scrollable_frame = tk.Frame(canvas)
# # scrollable_frame.grid(row=0, column=0)

# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# canvas.configure(yscrollcommand=scrollbar.set)

# for i in range(50):
#     ttk.Label(scrollable_frame, text="Sample scrolling label").grid(row=i, column=0)

# container.grid(row=0, column=0)
# canvas.grid(row=0, column=0)
# scrollbar.grid(row=0, column=1, sticky=tk.NS)

# root.mainloop()


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# root.geometry("400x400")

ROWS=10
ROWS_DISP=7

# Right container contains the labels
right_container = tk.Frame(root)
right_container.grid(row=0, column=1)

right_canvas = tk.Canvas(right_container)
right_canvas.grid(row=0, column=0)

right_frame = tk.Frame(right_canvas)
right_frame.grid(row=0, column=0)

for i in range(ROWS_DISP):
    right_frame.rowconfigure(i, minsize=50)
    tk.Label(right_frame, text='TESTER').grid(row=i, column=0, sticky=tk.N, pady=(0,20))




# Container contains the main canvas and the scrollbar
container = tk.Frame(root)
container.grid(row=0, column=0)

canvas = tk.Canvas(container, height=ROWS_DISP*50)
canvas.grid(row=0, column=0)

scrollbar =  tk.Scrollbar(container, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar.grid(row=1, column=0, sticky=tk.EW)

# Frame inside the main canvas that has the scrollable area
scrollable_frame = tk.Frame(canvas)
# scrollable_frame.grid(row=0, column=0)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(xscrollcommand=scrollbar.set)

for i in range(ROWS):
    scrollable_frame.rowconfigure(i, minsize=50)
    tk.Canvas(scrollable_frame, bg='red', height=25, width=500).grid(row=i, column=0, columnspan=50, sticky=tk.N)


root.mainloop()