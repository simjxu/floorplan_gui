
# Don't go off of pixels, first find the size of the window and then plaste the image based upon locatino
import tkinter as tk
from PIL import ImageTk, Image
import os

class Timeline(tk.Canvas):
    def __init__(self, parent, **kwargs):
        self.canvas = tk.Canvas.__init__(self)
        self.grid(column=kwargs['column'], row=kwargs['row'], \
            columnspan=kwargs['columnspan'], rowspan=kwargs['rowspan'])

        # Add the circle plus accompanying text
        # global blue_circle
        # blue_circle = tk.PhotoImage(file="./images/bluecircle.png")
        # blue_circle = blue_circle.subsample(30)
        # self.create_image(100,100,image=blue_circle)

        global my_text
        my_text = self.create_text(100,100, text="hello", fill='white')

    
    def move_cb(self, e):
        global blue_circle
        blue_circle = tk.PhotoImage(file="./images/bluecircle.png")
        blue_circle = blue_circle.subsample(30)     # Since we have to copy these lines so frequently, recommend we create a class or function
        blue_circle_img = self.create_image(e.x,100, image=blue_circle) # now locaked to the 100 pixel mark

        # Update label position and coordinates
        self.coords(my_text, e.x, 120)
        self.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
        self.itemconfig(my_text, text=str(e.x) + "," + str(e.y))

    def resize_window_cb(self, e):
        global layout, layout_resized, layout2
        layout = Image.open("./images/layout.png")
        layout_resized = layout.resize((e.width, e.height), Image.ANTIALIAS)
        layout2 = ImageTk.PhotoImage(layout_resized)
        self.create_image(0,0, image=layout2, anchor='nw')
    
    
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Configure size
        parent.grid_columnconfigure(0, minsize=100)
        parent.grid_columnconfigure(1, minsize=100)
        parent.grid_columnconfigure(2, minsize=100)
        parent.grid_columnconfigure(3, minsize=100)

        # Months going horizontal on top
        # Not sure why the labels have to be created with the parent,
        # maybe someday I can fix this.
        self.month1 = tk.Label(parent, text="  Jan")
        self.month1.grid(column=1, row=0, padx=0, pady=0)

        self.month2 = tk.Label(parent, text="  Feb")
        self.month2.grid(column=2, row=0, padx=0, pady=0)

        self.month3 = tk.Label(parent, text="  Mar")
        self.month3.grid(column=3, row=0, padx=0, pady=0)

        # # Try putting 2 timelines on
        firsttimeline = Timeline(self, column=1, row=1, columnspan=3, rowspan=1)
        firsttimeline.bind('<B1-Motion>', firsttimeline.move_cb)

        secondtimeline = Timeline(self, column=1, row=2, columnspan=3, rowspan=1)
        secondtimeline.bind('<B1-Motion>', secondtimeline.move_cb)

        # Builds going vertical on the left side
        self.build1 = tk.Label(parent, text="System")
        self.build1.grid(column=0, row=1, padx=10, pady=80)

        self.build1 = tk.Label(parent, text="EVT")
        self.build1.grid(column=0, row=2, padx=10, pady=80)


# class Legend(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
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
#         self.main = Main(self, ...)d

#         self.statusbar.pack(side="bottom", fill="x")
#         self.toolbar.pack(side="top", fill="x")
#         self.navbar.pack(side="left", fill="y")
#         self.main.pack(side="right", fill="both", expand=True)
