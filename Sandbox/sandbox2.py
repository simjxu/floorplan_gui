
# Don't go off of pixels, first find the size of the window and then plaste the image based upon locatino
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

class Timeline:
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
		print("stopped")
        # # delete or release selected item
        # if 100 < event.x < 300 and 250 < event.y < 350:
        #     self.canvas.delete(self.selected)
        #     del self.ovals[self.selected]
        # else:
        #     self.canvas.coords(self.selected, self.ovals[self.selected])
        # # clear it so you can use it to check if you are draging item
        # self.selected = None
    
class Marker(tk.Canvas):
    MARKER_RADIUS = 6 # All marker radii will be the same
    def __init__(self):
        # Add the circle plus accompanying text
        global my_circle
        my_circle = self.create_circle(50, 50, self.MARKER_RADIUS, fill="blue", \
            outline="white", width=2)

        global my_text
        my_text = self.create_text(50, 50, text="hello", fill='white')

    def move_cb(self, e):
        # Callback when moving the marker
        circle_coords = self.coords(my_circle)      # Returns top left and bottom right corners
        x0 = circle_coords[0]   # currently unused, go off of the mouse position
        y0 = circle_coords[1]
        x1 = circle_coords[2]   # currently unused, go off of the mouse position
        y1 = circle_coords[3]
        self.coords(my_circle, e.x-self.MARKER_RADIUS, y0, e.x+self.MARKER_RADIUS, y1)

        # Update label position and date
        self.coords(my_text, e.x, 60)
        self.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
        self.itemconfig(my_text, text=str(self.update_date(e.x)))
    
    

class MainApplication(tk.Frame):
    _NUMBER_OF_DAYS = []
    _NUMBER_OF_MONTHS = 0
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Configure size of the grid on root
        for i in range(_NUMCOLS):
            root.columnconfigure(i, minsize=_MINSIZE)
        for i in range(_NUMROWS):
            root.columnconfigure(i, minsize=_MINSIZE)

        # Create top row of months, get array of days, set column/rowspan
        self._NUMBER_OF_MONTHS = self.get_num_months()
        self._NUMBER_OF_DAYS = self.create_months()

        # # Try putting 2 timelines on -----FIX: need to create an array of Timelines
        firsttimeline = Timeline(self)
        

        # secondtimeline = Timeline(self, column=1, row=2, columnspan=_NUMCOLS-1, rowspan=1, \
        #     num_days=self._NUMBER_OF_DAYS, num_months=self._NUMBER_OF_MONTHS)
        # # secondtimeline.bind('<B1-Motion>', secondtimeline.move_cb)

        # Builds going vertical on the left side
        self.build1 = tk.Label(parent, text="System")
        self.build1.grid(column=0, row=1, padx=10, pady=0)

        self.build1 = tk.Label(parent, text="EVT")
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

            label_arr.append(tk.Label(root, \
                text="  "+calendar.month_abbr[month]))
            label_arr[i].grid(column=i+1, row=0, padx=0, pady=0)
            monthdays_arr.append(calendar.monthrange(year,month)[1])
            month += 1

        return monthdays_arr

    def create_builds(self):
        a = 0
        return a

# class Legend(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    MainApplication(root)
    root.mainloop()
