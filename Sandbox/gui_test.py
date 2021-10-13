import tkinter as tk
import random

class Desktop:

    array = [(50,50,70,70),(100,50,120,70),(150,50,170,70),(150,100,170,120),
            (150,150,170,170),(100,150,120,170),(50,150,70,170),(50,100,70,120)]

    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.canvas.create_rectangle(100, 250, 300, 350)

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
        # move selected item
        self.canvas.coords(self.selected, event.x-10, event.y-10, event.x+10,event.y+10)

    def stop_move(self, event):
        # delete or release selected item
        if 100 < event.x < 300 and 250 < event.y < 350:
            self.canvas.delete(self.selected)
            del self.ovals[self.selected]
        else:
            self.canvas.coords(self.selected, self.ovals[self.selected])
        # clear it so you can use it to check if you are draging item
        self.selected = None

root = tk.Tk()
d = Desktop(root)
root.mainloop()