
# Don't go off of pixels, first find the size of the window and then plaste the image based upon locatino
import tkinter as tk
from PIL import ImageTk, Image
import os

class Main(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        w = 600
        h = 400
        x = w/2
        y = h/2
        self.canvas = tk.Canvas.__init__(self, width=w, height=h, bg="white")
        self.pack(fill=tk.BOTH, expand=True)
        self.bind("<Configure>", self.resize_window_cb)
    
    def resize_window_cb(self, e):
        global layout, layout_resized, layout2
        layout = Image.open("./images/layout.png")
        layout_resized = layout.resize((e.width, e.height), Image.ANTIALIAS)
        layout2 = ImageTk.PhotoImage(layout_resized)
        self.create_image(0,0, image=layout2, anchor='nw')

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.main = Main(self)



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


# class Navbar(tk.Frame): ...
# class Toolbar(tk.Frame): ...
# class Statusbar(tk.Frame): ...
# class Main(tk.Frame): ...

# class MainApplication(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self.statusbar = Statusbar(self, ...)
#         self.toolbar = Toolbar(self, ...)
#         self.navbar = Navbar(self, ...)
#         self.main = Main(self, ...)

#         self.statusbar.pack(side="bottom", fill="x")
#         self.toolbar.pack(side="top", fill="x")
#         self.navbar.pack(side="left", fill="y")
#         self.main.pack(side="right", fill="both", expand=True)
