
# Don't go off of pixels, first find the size of the window and then plaste the image based upon locatino
import tkinter as tk
from PIL import ImageTk, Image
import os
import math
import calendar
import datetime

START_MONTH = 1 # Month to begin
START_YEAR = 2021   # Associated year
END_MONTH = 3  # Month to end
END_YEAR = 2021     # Associated year

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

        # Add the circle plus accompanying text
        global my_circle
        my_circle = self.create_circle(100, 100, self.MARKER_RADIUS, fill="blue", \
            outline="white", width=2)

        global my_text
        my_text = self.create_text(100,100, text="hello", fill='white')
    
    def update_date(self, x):
        # Create the text that goes under the marker indicating the date
        # x is the position that the mouse moves the marker to
        if x < 100:
            return str(START_MONTH) + "/" + \
                str(math.ceil((x+1)/100*MainApplication.NUMBER_OF_DAYS[0]))
        elif x < 200:
            return str(START_MONTH+1) + "/" + \
                str(math.ceil((x-99)/100*MainApplication.NUMBER_OF_DAYS[1]))
        elif x < 300:
            return str(START_MONTH+2) + "/" + \
                str(math.ceil((x-199)/100*MainApplication.NUMBER_OF_DAYS[2]))
        else:
            print("Error: pixels out of bounds")

    
    def move_cb(self, e):
        # Callback when moving the marker
        circle_coords = self.coords(my_circle)      # Returns top left and bottom right corners
        x0 = circle_coords[0]   # currently unused, go off of the mouse position
        y0 = circle_coords[1]
        x1 = circle_coords[2]   # currently unused, go off of the mouse position
        y1 = circle_coords[3]
        self.coords(my_circle, e.x-self.MARKER_RADIUS, y0, e.x+self.MARKER_RADIUS, y1)

        # Update label position and date
        self.coords(my_text, e.x, 120)
        self.tag_raise(my_text)            # Bring the text to the front, otherwise it is behind the circle.
        # self.itemconfig(my_text, text=str(e.x) + "," + str(e.y))
        self.itemconfig(my_text, text=str(self.update_date(e.x)))

    # BELOW ITEMS ARE NOT COMPLETE
    def resize_window_cb(self, e):
        global layout, layout_resized, layout2
        layout = Image.open("./images/layout.png")
        layout_resized = layout.resize((e.width, e.height), Image.ANTIALIAS)
        layout2 = ImageTk.PhotoImage(layout_resized)
        self.create_image(0,0, image=layout2, anchor='nw')
    
    
class MainApplication(tk.Frame):
    NUMBER_OF_DAYS = [31, 28, 31]

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Handle months
        # Abbreviated names of month
        print(calendar.month_abbr[START_MONTH])
        # Number of days in each month
        print(calendar.monthrange(START_YEAR,START_MONTH)[1])

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
