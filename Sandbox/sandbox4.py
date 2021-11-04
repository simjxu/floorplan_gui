from tkinter import *

startingWin = Tk()

canvas = Canvas(startingWin, height=600)
canvas.grid(row=0, column=0,sticky="nsew")
canvasFrame = Frame(canvas)
canvas.create_window(0, 0, window=canvasFrame, anchor='nw')

for i in range(70):
    element = Button(canvasFrame, text='Button %s ' % i)
    element.grid(row=i, column=0)

yscrollbar = Scrollbar(startingWin, orient=VERTICAL)
yscrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=yscrollbar.set)
yscrollbar.grid(row=0, column=1, sticky="ns")



canvasFrame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

# canvas.yview(END)
canvas.yview_moveto(float(1.0)/float(2.0))

startingWin.mainloop()