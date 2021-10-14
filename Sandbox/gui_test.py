import tkinter as tk
from PIL import ImageTk, Image
import os
import math
import calendar
import datetime

START_MONTH = 10 # Month to begin
START_YEAR = 2021   # Associated year
END_MONTH = 4  # Month to end
END_YEAR = 2022     # Associated year

# Need to input the values to ensure the columns and canvas sizes are correct
_NUMCOLS = 8
_NUMROWS = 3
_MINSIZE = 100

BUILDS = ["SYSTEM", "EVT"]

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

class MainApplication:
    _NUMBER_OF_DAYS = []
    _NUMBER_OF_MONTHS = 0
    
    def __init__(self, parent):
        self.mainframe = tk.Frame(parent, width=1000, height=1000)
        self.mainframe.grid(column=0, row=0, rowspan=20, columnspan=20)

        # Configure size of the grid on root
        for i in range(_NUMCOLS):
            root.columnconfigure(i, minsize=_MINSIZE)
        for i in range(_NUMROWS):
            root.columnconfigure(i, minsize=_MINSIZE)

        # Create top row of months, get array of days, set column/rowspan
        self._NUMBER_OF_MONTHS = self.get_num_months()
        self._NUMBER_OF_DAYS = self.create_months()

        # # Try putting 2 timelines on -----FIX: need to create an array of Timelines
        firsttimeline = Timeline(self.mainframe, column=1, row=1, columnspan=_NUMCOLS-1, rowspan=1, \
            num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS)

        secondtimeline = Timeline(self.mainframe, column=1, row=2, columnspan=_NUMCOLS-1, rowspan=1, \
            num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS)


        # Builds going vertical on the left side
        self.build1 = tk.Label(self.mainframe, text="System")
        self.build1.grid(column=0, row=1, padx=10, pady=0)

        self.build1 = tk.Label(self.mainframe, text="EVT")
        self.build1.grid(column=0, row=2, padx=10, pady=0)

    # Function to count number of months based upon inputs
    def get_num_months(self):
        start_date = datetime.datetime(START_YEAR,START_MONTH,1)
        end_date = datetime.datetime(END_YEAR, END_MONTH, 1)
        return (end_date.year - start_date.year) * 12 \
            + (end_date.month - start_date.month) + 1

    # Function to get the months and create array of days
    def create_months(self):
        monthdays_arr = []
        num_months = self._NUMBER_OF_MONTHS

        # Create the month labels on the first row
        label_arr = []
        year = START_YEAR
        month = START_MONTH
        for i in range(num_months):
            # Account for months rollover at end of year
            if month==13:
                month = 1
                year += 1

            label_arr.append(tk.Label(self.mainframe, \
                text="  "+calendar.month_abbr[month]))
            label_arr[i].grid(column=i+1, row=0, padx=0, pady=0)
            monthdays_arr.append(calendar.monthrange(year,month)[1])
            month += 1

        return monthdays_arr

    def create_builds(self):
        a = 0
        return a


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    d = MainApplication(root)
    root.mainloop()