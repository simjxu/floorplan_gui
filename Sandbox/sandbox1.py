import tkinter as tk

root = tk.Tk()
newframe = tk.Frame(root).pack()

newlabel = tk.Label(newframe, text='test' + '\n' + 'enter').pack()

root.mainloop()