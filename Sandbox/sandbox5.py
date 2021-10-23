import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Container contains the main canvas and the scrollbar
container = tk.Frame(root)

canvas = tk.Canvas(container)
scrollbar =  tk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)

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

canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    ttk.Label(scrollable_frame, text="Sample scrolling label").grid(row=i, column=0)

container.grid(row=0, column=0)
canvas.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

root.mainloop()