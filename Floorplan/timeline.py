import tkinter as tk


class Timeline(tk.Canvas):
    MARKER_RADIUS = 6 # All marker radii will be the same

    def __init__(self, parent, **kwargs):
        # Get number of days and months
        self.num_days = kwargs['num_days']
        self.num_months = kwargs['num_months']
        
        # Create canvas that covers the the entire row
        self.canvas = tk.Canvas.__init__(self)
        self.grid(column=kwargs['column'], row=kwargs['row'], \
            columnspan=kwargs['columnspan'], rowspan=kwargs['rowspan'])

        # TODO: Update the height to be shorter, and move the marker appropriately.
        self.configure(width=100*(self.num_months), height=100)
        
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