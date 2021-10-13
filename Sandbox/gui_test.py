import tkinter as tk
import random

# Add the _create_circle function ot the Canvas function, makes it easier to create a circle
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle
class Timeline:

    array = [(50,50,70,70),(100,50,120,70),(150,50,170,70)]

    def __init__(self, parent):
        self.canvas = tk.Canvas(parent, width=400, height=400)
        self.canvas.grid(column=0, row=0)
        self.canvas.configure(width=100*5, height=100)

        # to keep all IDs and its start position
        self.ovals = {}

        for item in self.array:
            # create oval and get its ID
            item_id = self.canvas.create_oval(item, fill='brown', tags='id')
            # remember ID and its start position
            self.ovals[item_id] = item

        self.canvas.tag_bind('id', '<ButtonPress-1>', self.start_move)
        self.canvas.tag_bind('id', '<B1-Motion>', self.move)
        self.canvas.tag_bind('id', '<ButtonRelease-1>', self.stop_move)

        # to remember selected item
        self.selected = None

    def start_move(self, event):
        # find all clicked items
        self.selected = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        # get first selected item
        self.selected = self.selected[0]

    def move(self, event):
        circle_coords = self.canvas.coords(self.selected)
        x0 = circle_coords[0]   # currently unused, go off of the mouse position
        y0 = circle_coords[1]
        x1 = circle_coords[2]   # currently unused, go off of the mouse position
        y1 = circle_coords[3]

        # move selected item, hold y position
        self.canvas.coords(self.selected, event.x-10, y0, event.x+10,y1)

    def stop_move(self, event):
        print("stopped")


root = tk.Tk()
d = Timeline(root)
root.mainloop()