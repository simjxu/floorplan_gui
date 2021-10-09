
# Don't go off of pixels, first find the size of the window and then plaste the image based upon locatino
import tkinter as tk
from PIL import ImageTk, Image
import os
import math
import calendar
import datetime

START_MONTH = 12 # Month to begin
START_YEAR = 2021   # Associated year
END_MONTH = 5  # Month to end
END_YEAR = 2022     # Associated year

_NUMCOLS = 7
_NUMROWS = 3
_MINSIZE = 100

BUILDS = ["SYSTEM", "EVT"]

# Add the _create_circle function ot the Canvas function, makes it easier to create a circle
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

class Timeline(tk.Canvas):
    MARKER_RADIUS = 6 # All marker radii will be the same

    def __init__(self, parent, **kwargs):
        # Create canvas that covers the the entire row
        self.canvas = tk.Canvas.__init__(self)
        self.grid(column=kwargs['column'], row=kwargs['row'], \
            columnspan=kwargs['columnspan'], rowspan=kwargs['rowspan'])
        self.configure(width=100*(_NUMCOLS-1), height=100)
        
        # Get number of days
        self.num_days = kwargs['num_days']

        # Add the circle plus accompanying text
        global my_circle
        my_circle = self.create_circle(50, 50, self.MARKER_RADIUS, fill="blue", \
            outline="white", width=2)

        global my_text
        my_text = self.create_text(50, 50, text="hello", fill='white')
    
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

    # BELOW ITEMS ARE NOT COMPLETE
    def resize_window_cb(self, e):
        global layout, layout_resized, layout2
        layout = Image.open("./images/layout.png")
        layout_resized = layout.resize((e.width, e.height), Image.ANTIALIAS)
        layout2 = ImageTk.PhotoImage(layout_resized)
        self.create_image(0,0, image=layout2, anchor='nw')
    
    
class MainApplication(tk.Frame):
    _NUMBER_OF_DAYS = []
    

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Configure size of the grid on root
        for i in range(_NUMCOLS):
            root.columnconfigure(i, minsize=_MINSIZE)
        for i in range(_NUMROWS):
            root.columnconfigure(i, minsize=_MINSIZE)

        # Create top row of months, get array of days, set column/rowspan
        self._NUMBER_OF_DAYS = self.create_months()

        # # Try putting 2 timelines on
        firsttimeline = Timeline(self, column=1, row=1, columnspan=_NUMCOLS-1, rowspan=1, \
            num_days=self._NUMBER_OF_DAYS)
        firsttimeline.bind('<B1-Motion>', firsttimeline.move_cb)

        secondtimeline = Timeline(self, column=1, row=2, columnspan=_NUMCOLS-1, rowspan=1, \
            num_days=self._NUMBER_OF_DAYS)
        secondtimeline.bind('<B1-Motion>', secondtimeline.move_cb)

        # Builds going vertical on the left side
        self.build1 = tk.Label(parent, text="System")
        self.build1.grid(column=0, row=1, padx=10, pady=80)

        self.build1 = tk.Label(parent, text="EVT")
        self.build1.grid(column=0, row=2, padx=10, pady=80)

    # Function to get the months and create array of days
    def create_months(self):
        monthdays_arr = []

        # Calculate the number of months between the date ranges
        start_date = datetime.datetime(START_YEAR,START_MONTH,1)
        end_date = datetime.datetime(END_YEAR, END_MONTH, 1)
        num_months = (end_date.year - start_date.year) * 12 \
            + (end_date.month - start_date.month) + 1

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
