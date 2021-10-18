import tkinter as tk
import math

# Add the _create_circle function ot the Canvas function, makes it easier to create a circle
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle
class Timeline(tk.Frame):
    
    MARKER_RADIUS = 8 # All marker radii will be the same
    marker_ypos = _MINSIZE/2+MARKER_RADIUS/2
    array = [(25,marker_ypos),(50,marker_ypos),(75,marker_ypos)]

    def __init__(self, parent, **kwargs):
        self.num_days = kwargs['num_days']
        self.num_months = kwargs['num_months']

        self.canvas = tk.Canvas(parent)
        # self.canvas.pack()
        self.canvas.grid(column=kwargs['column'], row=kwargs['row'], rowspan=kwargs['rowspan'], \
            columnspan=kwargs['columnspan'])
        self.canvas.configure(width=_MINSIZE*(self.num_months), height=_MINSIZE, bg='green')

        # to keep all IDs and its start position
        self.ovals = {}
        self.texts = {}

        # Create markers for every item in the array
        for item in self.array:
            # create oval and get its ID
            item_id = self.canvas.create_circle(item[0], item[1], self.MARKER_RADIUS, \
                fill='blue', outline='white', tags='id')
            # remember ID and its start position
            self.ovals[item_id] = item

            # text_id = self.canvas.create_text(item[0], item[1]+2*self.MARKER_RADIUS, \
            #     text="hello", fill='white')
            self.texts[item_id] = self.canvas.create_text(item[0], item[1]+2*self.MARKER_RADIUS, \
                text="hello", fill='white')

        self.canvas.tag_bind('id', '<ButtonPress-1>', self.start_move)
        self.canvas.tag_bind('id', '<B1-Motion>', self.move)
        self.canvas.tag_bind('id', '<ButtonRelease-1>', self.stop_move)

        # # to remember selected item
        # self.selected = None

    def update_date(self, x):
        # Create the text that goes under the marker indicating the date
        # x is the position that the mouse moves the marker to
        # 1. Divide the pixel count by 100
        # 2. Round down to integer
        # 3. Map the integer to the month Start Month + integer

        month_iter = math.floor(x/100)
        month_num = START_MONTH+month_iter
        month_num = month_num if month_num <= 12 else month_num-12  # Rollover to January

        return str(month_num) + "/" + \
            str(math.ceil((x+1-100*month_iter)/100*self.num_days[month_iter]))
        # TODO: Set bounds so that the marker doesn't go out of bounds

    def start_move(self, event):
        # find all clicked items
        self.selected = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        # get first selected item
        self.selected = self.selected[0]

        # get selected text tag
        self.selected_text = self.canvas.find_withtag(self.texts[self.selected])

    def move(self, event):
        circle_coords = self.canvas.coords(self.selected)
        x0 = circle_coords[0]   # currently unused, go off of the mouse position
        y0 = circle_coords[1]
        x1 = circle_coords[2]   # currently unused, go off of the mouse position
        y1 = circle_coords[3]

        # move selected item, hold y position
        self.canvas.coords(self.selected, event.x-self.MARKER_RADIUS, \
            y0, event.x+self.MARKER_RADIUS,y1)

        # Also move the label position and date
        self.canvas.coords(self.selected_text, event.x, \
            self.marker_ypos+2*self.MARKER_RADIUS)
        self.canvas.tag_raise(self.selected_text)
        self.canvas.itemconfig(self.selected_text, text=str(self.update_date(event.x)))

    def stop_move(self, event):
        print("stopped")